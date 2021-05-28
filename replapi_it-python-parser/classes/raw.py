import json 

def getRaw(jsondata):
  if (jsondata == None or jsondata == ''):
    print("No json found")
    exit(0)
  try:
    jsondata = json.dumps(jsondata)
    jsondata = json.loads(jsondata)  
    returnData = jsondata["data"]["userByUsername"]
  except:
    print("We encountered an error trying to parse this, please check the JSON you are giving us.\nIf this is a mistake, please contact us in our repo, which can be found here:\nhttps://github.com/darkdarcool/ReplAPI-Python-Parser")
  return returnData
