import json
def getKarma(jsondata):
  jsondata = json.dumps(jsondata)
  jsondata = json.loads(jsondata)  
  returnData = jsondata["data"]["userByUsername"]["karma"]
  return returnData