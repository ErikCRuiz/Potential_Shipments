# Potential_Shipments

Objective:
Get all the orders are ready to ship, to share with planning department

Input:

 * Daily Master base and Ship status
 * 860 Holds
 * Hold tool report
 * Previous day PO Viewer

Output:

  * Current ship orders and complete orders ready to ship, excluding HPE restrictions and internal holds

Updates and Releases:

  * 08/15/2022: Report shared to the team
  * 08/25/2022: hold_tool_format method do fixed miss match in work orders merge
  * 09/07/2022: HOLD_PARTNO validation
  * 09/30/2022: Shippeable complete with case assigment created
  * 10/20/2022: Changed pivot table columns(Pending PGI and Shipped PGI) and also schedule was changed by SAB's reason.
  * 10/21/2022: Shippeable_complete edited, CD_FLAG_BUCKET, NET_VALUE columns added.
  * 12/02/2022: Added sleep time to files waiting to be updated with current date.  