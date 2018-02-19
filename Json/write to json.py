import json

with open ('state.json') as f:
    data=json.load(f)      #transform json to python
for eachstate in data['states']:
    print(eachstate['name'])
    del eachstate['area_codes']

with open ('new_states.json','w') as f:
    json.dump(data,f,indent=2)

