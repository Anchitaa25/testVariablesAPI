import json
import sys
import requests
try:
  get_URL = 'https://dev.azure.com/'+sys.argv[2]+'/'+sys.argv[3]+'/_apis/git/repositories/'+sys.argv[1]+'?api-version=5.1'
  r = requests.get(url = get_URL , auth = (sys.argv[4],sys.argv[5]))
  data=r.json()
  json_string = json.dumps(data)
  x = json.loads(json_string)
  repository_id = x["id"]
  delete_URL = "https://dev.azure.com/"+sys.argv[2]+"/"+sys.argv[3]+"/_apis/git/repositories/"+repository_id+"?api-version=5.1"
  a = requests.delete(url = delete_URL,auth =  (sys.argv[4],sys.argv[5]))
except KeyError:
  print("URL Incorrect. Check values for Repository/Organization/Project Name")
except ValueError:
  print("Incorrect Credentials")
