import requests
import json

print('Please enter your zip code: ')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s&appid=4de199b54b93ce29738ba89d225d5b03' % zip)
data=r.json()

#print(type(data['weather'][0]['description']))
print("The weather in %s is %s" %(zip, data['weather'][0]['description']))