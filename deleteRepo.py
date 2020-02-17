import json
import requests

r = requests.get('https://dev.azure.com/anchitaa95/deleteRepositoryPipeline/_apis/git/repositories/deleteRepo?api-version=5.1', auth = (username,private_token))
data=r.json()

json_string = json.dumps(data)
x = json.loads(json_string)
id1 = x["id"]
URL = "https://dev.azure.com/anchitaa95/deleteRepositoryPipeline/_apis/git/repositories/"+id1+"?api-version=5.1"

id_content = {  "name": "deleteRepo",
                "project": {
                  "id": id1
                }
}
header = {"Content-type": "application/json"}
a = requests.delete(url = URL,auth =  ('anchitaa95','vqluceje46tbuwz5xnjqhecpgebcg7cjakvbzfe43vg7m2e2zynq'),data = json.dumps(id_content), headers =header)
