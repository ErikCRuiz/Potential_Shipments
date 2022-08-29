import subprocess
import pandas as pd
import json as json
from My_Book import *
from io import StringIO
from datetime import date 
from dateutil.relativedelta import relativedelta
from code_holds import code_holds
from Hold_tool import po_validation,Hold_type_column


def hold_tool():

    cookie_cygnus()
  
    initial_date = (date.today() + relativedelta(months=-6)).strftime("%Y-%m-%d")

    final_date = (date.today()).strftime("%Y-%m-%d")

    subprocess.call('sh bash_scripts/request.sh ' + initial_date + ' ' + final_date + ' HOLD_TOOL')   

    data = open(path()+'\Json_Files\\cygnus_files.json','r') #read json file downloaded
    json_array = json.load(data)
    jsonf = json.dumps(json_array[1]) #get inormation to dataframe  
    df = pd.read_json(StringIO(jsonf))

    df.reset_index(drop=True,inplace=True)
    
    df = drop_list_of_columns(['change','row_action','objID'],df)
    df.columns = txt_array('default_Hold_tool_report.txt')

    df = df[txt_array('hold_tool_columns.txt')]
    df = hold_tool_format(df)

    #-------------------------------------------------------------------------------
   
    df_master = pd.read_excel(share_path()+'\Master Template\\master_base.xlsx')

    for i in range(0,len(df.index)):

        id = df['ID'][i]
        type_c = df['Type'][i]

        if '52C' in str(id):

            df.loc[i,'HOLD LEVEL'] = 'PO'

        elif type(id) == int and (len(str(id)) == 8 or len(str(id)) == 9):

            df.loc[i,'HOLD LEVEL'] = 'WO'

        elif ('SKU' in type_c) or ('PARTNO' in type_c):

            df.loc[i,'HOLD LEVEL'] = 'BASE SKU'

        else:

            df.loc[i,'HOLD LEVEL'] = 'OTHERS / HOLD_SSN'

    df = Hold_type_column(df)
    df_po = df[df['HOLD LEVEL'].str.contains('PO') == True].reset_index(drop= True)
    df_po = df_po.rename(columns = {'ID':'PO'})
    df_po = pd.merge(df_po,df_master['PO'], on= ['PO'], how= 'inner')
    df_po = df_po.rename(columns = {'PO':'ID'})

    df_wo = df[df['HOLD LEVEL'].str.contains('WO') == True].reset_index(drop= True)
    df_wo = df_wo.rename(columns = {'ID':'WORK ORDER'})
    df_wo = pd.merge(df_wo,df_master['WORK ORDER'], on= ['WORK ORDER'], how= 'inner')
    df_wo = df_wo.rename(columns = {'WORK ORDER':'ID'})

    df_sku = df[df['HOLD LEVEL'].str.contains('BASE SKU') == True].reset_index(drop= True)
    df_sku = df_sku.rename(columns = {'ID':'BASE SKU'})
    df_sku = pd.merge(df_sku,df_master['BASE SKU'], on= ['BASE SKU'], how= 'inner')
    df_sku = pd.merge(df_sku, df_master[['BASE SKU','WORK ORDER']], on = 'BASE SKU', how = "left")
    #df_sku['WORK ORDER'] = df_sku['WORK ORDER'].astype(int)
    df_sku.pop('BASE SKU')
    df_sku.insert(0, 'WORK ORDER', (df_sku.pop('WORK ORDER')))
    df_sku = df_sku.rename(columns = {'WORK ORDER':'ID'})

    df_final = pd.concat([df_po,df_wo,df_sku])
    df_final.to_excel(path()+'\Files\hold_tool_report.xlsx',index= False)

    po_priority_code = po_validation(df_po)
    code_holds(po_priority_code)

#hold_tool()