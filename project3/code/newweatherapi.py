import requests
import json

#gets zip code input from the user
print('Please enter your zip code: ')
zip = input()

#aquires weather information as json data from api.openweathermap.org based on the zip code the user entered
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s&appid=4de199b54b93ce29738ba89d225d5b03' % zip)
data=r.json() 

#converts the temperature from kelvin to fahrenheit and rounds to one decimal place.
ktemp = data['main']['temp']
ftemp = (ktemp - 273.15) * 1.8 + 32
rtemp = round(ftemp, 2)

#prints specific, formated data.
print("The weather in %s is %s. It is %s degrees Fahrenheit." %(data['name'], data['weather'][0]['description'], rtemp))