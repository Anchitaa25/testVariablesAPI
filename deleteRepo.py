import json
import requests

r = requests.get('https://dev.azure.com/anchitaa95/deleteRepositoryPipeline/_apis/git/repositories/deleteRepo?api-version=5.1', auth = ('anchitaa95','vqluceje46tbuwz5xnjqhecpgebcg7cjakvbzfe43vg7m2e2zynq'))
data=r.json()

json_string = json.dumps(data)
x = json.loads(json_string)
id = x["id"]
URL = "https://dev.azure.com/anchitaa95/deleteRepositoryPipeline/_apis/git/repositories/"+id+"?api-version=5.1"

id_content = {  "name": "deleteRepo",
                "project": {
                  "id": id
                }
}
header = {"Content-type": "application/json"}
a = requests.delete(url = URL,auth =  ('anchitaa95','vqluceje46tbuwz5xnjqhecpgebcg7cjakvbzfe43vg7m2e2zynq'),data = json.dumps(id_content), headers =header)
