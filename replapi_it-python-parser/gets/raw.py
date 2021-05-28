import json
import requests
def getRawCount(username):
  getCyclesQuery = """
    karma
  """
  headers = {
    "X-Requested-With": "ReplAPI-IT Team",
    "Referrer": "https://staging.replit.com/",
  }
  url = "https://staging.replit.com/graphql"
  body = {
      "query": 'query UserData { userByUsername(username: "'
      + username
      + '") { '
      + getCyclesQuery
      + " } }"
  }
    # Get Data from graphql
  ourdata = json.loads(requests.post(url, body, headers=headers).text)
  returnData = ourdata
    # Check if user exists
  f = returnData
  f = f["data"]["userByUsername"]
  if f is None:
    # Error if user doesn't exist
    print("We couldn't fine the user that you were looking for! ")
    print("The username we revieved was: " + username)
    exit(0)
  returnDatam = returnData # ["data"]["userByUsername"]["karma"]  # Make data
  return returnDatam