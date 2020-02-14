import json
import requests

r = requests.get('https://dev.azure.com/anchitaa25/check1/_apis/git/repositories/deleteRepo?api-version=5.1', auth = ('anchitaa25','4fzcufr6inmc4yltqsp4pg5ouye7n57mvczxhg5n656jq4j5t4hq'))
data=r.json()

json_string = json.dumps(data)
x = json.loads(json_string)
id = x["id"]
URL = "https://dev.azure.com/anchitaa25/check1/_apis/git/repositories/"+id+"?api-version=5.1"

id_content = {  "name": "deleteRepo",
                "project": {
                  "id": "0bd38e45-4237-449c-b8a2-9e96e71b3a53"
                }
}
header = {"Content-type": "application/json"}
a = requests.delete(url = URL,auth =  ('anchitaa25','4fzcufr6inmc4yltqsp4pg5ouye7n57mvczxhg5n656jq4j5t4hq'),data = json.dumps(id_content), headers =header)
