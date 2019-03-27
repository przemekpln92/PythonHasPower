import sys
import requests

if len(sys.argv) < 2: 
	print("Please provide city")
	exit()

city = sys.argv[1]
link = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=f4c03d1f0c13165fe150ba3a8ef91bb5'
json = requests.get(link).json()

if json["cod"] == 200:
	temp = int((json["main"]["temp"]))
	print(f'{temp}\N{DEGREE SIGN}C')
else:
	print(json["message"])