import json
import sys
import requests
Organization_Name = sys.argv[2]
Project_Name = sys.argv[3]
Repository_Name = sys.argv[1]
User_Name = sys.argv[4]
Personal_Token = sys.argv[5]
def deleteRepository():
  get_URL = 'https://dev.azure.com/'+Organization_Name+'/'+Project_Name+'/_apis/git/repositories/'+Repository_Name+'?api-version=5.1'
  get_ID_request = requests.get(url = get_URL , auth = (User_Name,Personal_Token))
  data = get_ID_request.json()
  Repository_ID = data["id"]
  delete_URL = "https://dev.azure.com/"+Organization_Name+"/"+Project_Name+"/_apis/git/repositories/"+Repository_ID+"?api-version=5.1"
  delete_repo_request = requests.delete(url = delete_URL, auth =  (User_Name,Personal_Token))

try:
  deleteRepository()
except KeyError:
  print("URL Incorrect. Check values for Repository/Organization/Project Name")
except ValueError:
  print("Incorrect Credentials")
except Exception as error:
  print(error)
