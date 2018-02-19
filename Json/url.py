import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice"
             "/v1/symbols/allcurrencies/quote?format=json") as request:
    source = request.read().decode('utf-8')

#print(source)
data=json.loads(source)

#print(json.dumps(data,indent=2))
print(len(data['list']['resources']))

usd_rates=dict() #empty dict
for item in data['list']['resources']:
    name=item['resource']['fields']['name']
    price=item['resource']['fields']['price']
    print(name,price)
    usd_rates[name]=price
print(usd_rates['USD/EUR'])
