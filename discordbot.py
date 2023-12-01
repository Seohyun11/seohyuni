import discord
TOKEN='MTE3ODU5NDk0NDEzNTQ4MzQzMg.G136uH.E89iYplHbBveJaR00qNdz8hUrT3Zh1a3YNPxy4'
CHANNEL_ID='1178601645672759317'

""" class MyClient(discord.Client):
    async def on_ready(self):
        channel=self.get_channel(int(CHANNEL_ID))
        await channel.send('Hello World')
        
intents=discord.Intents.default()
intents.message_content=True
client=MyClient(intents=intents)
client.run(TOKEN) """

""" class info(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.change_presence(status=discord.Status.online,
activity=discord.Game("날씨 입력 "))
        
intents=discord.Intents.default()
intents.message_content=True
client=info(intents=intents)
client.run(TOKEN) """

#날씨
import requests
import json
city=  "Bucheon-si"
key = "e33c4b0df933a3817b2f029b526b80a5"
lang = "kr"
units = "metric"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang={lang}&units={units}"
response = requests.get(url)
result = json.loads(response.text)



#디스코드 봇 관련
class reply(discord.Client):
    async def on_message(self,message):
        if message.author==self.message:
            return
        if message.content=='날씨':
            awati message.channel.send(f"부천은 현재 {result['weather'][0]['description']}, {result['main']['temp']}도"))