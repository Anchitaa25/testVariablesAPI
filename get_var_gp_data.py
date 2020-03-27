import json
import sys
import requests

variableGroupName = sys.argv[1]
user_name = sys.argv[2]
auth_token = sys.argv[3]
organisation_name = sys.argv[4]
project_name = sys.argv[5]

def getVariables():
  get_URL = 'https://dev.azure.com/'+organisation_name+'/'+project_name+'/_apis/distributedtask/variablegroups?groupName='+variableGroupName+'&api-version=5.0-preview.1'
  get_ID_request = requests.get(url = get_URL , auth = (user_name,auth_token))
  data = get_ID_request.json()
  variables = data["value"][0]["variables"]
  print(variables)

try:
  getVariables()
except KeyError:
  print("URL Incorrect. Check values for Repository/Organization/Project Name")
except ValueError:
  print("Incorrect Credentials")
except Exception as error:
  print(error)
