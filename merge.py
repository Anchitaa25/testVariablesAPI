import json
import sys
import requests

variableGroupName = sys.argv[1]
variableName = sys.argv[2]
variableValue = sys.argv[3]

def updateVariableValue():
  get_URL = 'https://dev.azure.com/guptashreya21/deleteRepo/_apis/distributedtask/variablegroups?groupName='+variableGroupName+'&api-version=5.0-preview.1'
  get_ID_request = requests.get(url = get_URL , auth = ('guptashreya21','o6vnjl3lehhcv6brzatndur7u2jhcu6o5mbmsm2ia3put46vdy3q'))
  data = get_ID_request.json()
  print(data)
  variableGroupID = str(data["value"][0]["id"])
  variables_json = data["value"][0]["variables"]
  variables_json[variableName]["value"]= variableValue
  del data["value"][0]["variables"]
  data["value"][0]["variables"]= variables_json
  id_content = {"id":variableGroupID,"type":"Vsts","name":variableGroupName,"variables":variables_json}
  header = {"Content-type": "application/json"}
  put_URL = 'https://dev.azure.com/guptashreya21/deleteRepo/_apis/distributedtask/variablegroups/'+variableGroupID+'?api-version=5.0-preview.1'
  get_ID_request = requests.put(url = put_URL , auth = ('guptashreya21','o6vnjl3lehhcv6brzatndur7u2jhcu6o5mbmsm2ia3put46vdy3q'), data=json.dumps(id_content),headers =header)
  data = get_ID_request.json()
  print(data)

try:
  updateVariableValue()
except KeyError:
  print("URL Incorrect. Check values for Repository/Organization/Project Name")
except ValueError:
  print("Incorrect Credentials")
except Exception as error:
  print(error)
