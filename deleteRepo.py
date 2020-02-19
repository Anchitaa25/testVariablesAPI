import json
import sys
import requests
URL = 'https://dev.azure.com/'+sys.argv[2]+'/'+sys.argv[3]+'/_apis/git/repositories/'+sys.argv[1]+'?api-version=5.1'
r = requests.get(url = URL, auth = ('anchitaa95','vqluceje46tbuwz5xnjqhecpgebcg7cjakvbzfe43vg7m2e2zynq'))
data=r.json()
print(data)
json_string = json.dumps(data)
x = json.loads(json_string)
id1 = x["id"]
URL = "https://dev.azure.com/anchitaa95/deleteRepositoryPipeline/_apis/git/repositories/"+id1+"?api-version=5.1"

id_content = {  "name": sys.argv[1],
                "project": {
                  "id": id1
                }
}
header = {"Content-type": "application/json"}
a = requests.delete(url = URL,auth =  ('anchitaa95','vqluceje46tbuwz5xnjqhecpgebcg7cjakvbzfe43vg7m2e2zynq'),data = json.dumps(id_content), headers =header)
