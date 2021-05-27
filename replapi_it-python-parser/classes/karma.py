import json
def getKarma(jsondata):
  if (jsondata == None or jsondata == ''):
    print("No JSON found.")
    exit(0)
  try:
    jsondata = json.dumps(jsondata)
    jsondata = json.loads(jsondata)  
    returnData = jsondata["data"]["userByUsername"]["karma"]
    return returnData
  except:
    print("We encountered an eror trying to parse this, please check the JSON you are giving us.\nIf this is a mistake, please contact us in out repo, which can e found here:\nhttps://github.com/darkdarcool/ReplAPI-Python-Parser")
    exit(0)