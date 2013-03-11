import requests
import json

auth_key = '9de2f5f2-babe-4ead-9ff5-43bb705ea614'

url = 'http://f7odwebqab2.statcan.gc.ca/data/api/3/action/'

resource_id = 'a36ea99b-9517-4845-adbb-80fd7f4c636a'

datastore_structure = {
                        'resource_id': resource_id,
                        'fields': [ {"id": "a"}, {"id": "b"} ],
                        "records": [ { "a": 1, "b": "gasoline"}, {"a": 2, "b": "coal"} ]
                      }
headers = {'content-type': 'application/json', 'Authorization': auth_key}
r = requests.post(url + 'datastore_create', data=json.dumps(datastore_structure), headers=headers)
print "Request Status Code: " + str(r.status_code)
print "done, and now for a quick search\n"

datastore_structure = {
                        'resource_id': resource_id
                      }
headers = {'content-type': 'application/json', 'Authorization': auth_key}
r = requests.post(url + 'datastore_search', data=json.dumps(datastore_structure), headers=headers)

print r.text

print "done\n"