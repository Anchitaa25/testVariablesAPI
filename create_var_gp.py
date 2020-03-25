import json
import sys
import requests

variableGroupName = sys.argv[1]
variableName = sys.argv[2]
variableValue = sys.argv[3]
id_content = {
  "variables": {
    variableName: {
      "value": variableValue
    }
  },
  "type": "Vsts",
  "name": variableGroupName
}
header = {"Content-type": "application/json"}
def deleteRepository():
  get_URL = 'https://dev.azure.com/guptashreya21/deleteRepo/_apis/distributedtask/variablegroups?api-version=5.0-preview.1'
  get_ID_request = requests.post(url = get_URL , auth = ('guptashreya21','o6vnjl3lehhcv6brzatndur7u2jhcu6o5mbmsm2ia3put46vdy3q'), data=json.dumps(id_content),headers =header)
  data = get_ID_request.json()
  print(data)

try:

  deleteRepository()
except KeyError:
  print("URL Incorrect. Check values for Repository/Organization/Project Name")
except ValueError:
  print("Incorrect Credentials")
except Exception as error:
  print(error)
