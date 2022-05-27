import requests
from pprint import pprint
import json

# pc_req = requests.get("https://api.postcodes.io/postcodes/SK5 8BL")
# print(pc_req.status_code)
#
# if pc_req.status_code == 200:
#     #pprint(dict(pc_req.headers), sort_dicts=False)
#     print(type(pc_req.content))
#     print(pc_req.content)
#     postcode = json.loads(pc_req.content)
#     postcode2 = pc_req.json() # turn the byte into json
#     #pprint(postcode)
#     pprint(postcode2)
#     pprint("------------------------")
#     # print admin_district, the eastings and northings, nuts code
#     pprint(postcode2["result"]["codes"]["nuts"])
#     pprint(postcode2["result"]["admin_district"])
#     pprint(postcode2["result"]["eastings"])
#     pprint(postcode2["result"]["northings"])
pprint("------------------------")
headers = {'Content-Type': 'application/json'}
body = {'postcodes': ['SK5 8BL', 'SK5 8LG', 'M45 6GN']}

pc_req = requests.post(
    "https://api.postcodes.io/postcodes/",
    headers=headers,
    data=json.dumps(body)
)
print(pc_req)
pcs = pc_req.json()["result"]
pprint(pcs)

for x in pcs:  # turn into dictionary, so I can get the key,values
    result = x["result"]
    print(result['postcode'])
    print(result['admin_ward'])
    print(result['eastings'], result['northings'])
    print(result['codes']['nuts'])



pprint("------------- GET admin_word, eastings, northings, nutds code -----------")
