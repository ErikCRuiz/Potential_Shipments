curl -b bash_scripts/cookie.txt 'http://10.19.17.100/CyGNUS/srvcygnus' \
  -H 'Connection: close' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"' \
  -H 'Accept: */*' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'Origin: http://10.19.17.100' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: http://10.19.17.100/CyGNUS/cygnus.jsp?page=HoldToolReport&platform=arpt' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  --data-raw 'data=%5B%7B%22param%22%3A%22strHoldType%22%2C%22val%22%3A%22ALL%22%7D%2C%7B%22param%22%3A%22strHoldStatus%22%2C%22val%22%3A%221%22%7D%2C%7B%22param%22%3A%22dtini%22%2C%22val%22%3A%22'$1'%22%7D%2C%7B%22param%22%3A%22dtfin%22%2C%22val%22%3A%22'$2'%22%7D%2C%7B%22param%22%3A%22strMasterTrantype%22%2C%22val%22%3A%22cygnusHold_Tool_sp%22%7D%2C%7B%22param%22%3A%22strTrantype%22%2C%22val%22%3A%22HoldToolReport%22%7D%2C%7B%22param%22%3A%22environment%22%2C%22val%22%3A%22CyGNUS%22%7D%2C%7B%22param%22%3A%22strClient%22%2C%22val%22%3A%22HPE%22%7D%2C%7B%22param%22%3A%22strUserName%22%2C%22val%22%3A%22erikruiz%22%7D%5D' \
  --compressed