import requests
import json

print('Please enter your zip code: ')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s&appid=4de199b54b93ce29738ba89d225d5b03' % zip)
data=r.json()

ktemp = data['main']['temp']
ftemp = (ktemp - 273.15) * 1.8 + 32
rtemp = round(ftemp, 2)

print("The weather in %s is %s. It is %s degrees Fahrenheit." %(data['name'], data['weather'][0]['description'], rtemp))