import requests
import json

city=  "Bucheon-si"
key = "e33c4b0df933a3817b2f029b526b80a5"
lang = "kr"
units = "metric"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang={lang}&units={units}"

response = requests.get(url)

result = json.loads(response.text)

print(f"부천은 현재 {result['weather'][0]['description']}, {result['main']['temp']}도")