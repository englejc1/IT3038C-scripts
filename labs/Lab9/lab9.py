import requests
import json

r = requests.get('http://localhost:3000')
data = r.json()

print("Widget1 is %s." % (data[0]['color']))
print("Widget2 is %s." % (data[1]['color']))
print("Widget3 is %s." % (data[2]['color']))
print("Widget4 is %s." % (data[3]['color']))