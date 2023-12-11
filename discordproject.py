import discord
from datetime import datetime
import requests
import json

TOKEN='토큰 해킹으로 인한 비공개'


#날씨

#디스코드 봇 관련

class discordbot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
       
    async def on_message(self, message):
        if message.author == self.user:
            return
 
        if message.content == '안녕':
            await message.channel.send('안녕하세요{0.author.mention}님'.format(message))
            
        elif message.content=='명령어':
            await message.channel.send('현재 이 봇에서 이용할 수 있는 명령어는 ||안녕,날씨,요일,시간||입니다.')
        else:
            answer = self.answer(message.content)
            await message.channel.send(answer)
            
    def weather(self):
        city=  "Bucheon-si"
        key = "e33c4b0df933a3817b2f029b526b80a5"
        lang = "kr"
        units = "metric"

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang={lang}&units={units}"

        response = requests.get(url)

        result = json.loads(response.text)

        return (f"부천의 현재 날씨는{result['weather'][0]['description']}, {result['main']['temp']}도 입니다.")
               
 
    def week(self):
        list = ['월', '화', '수', '목', '금', '토', '일']
 
        weeks = list[datetime.today().weekday()]
        date = datetime.today().strftime("%Y년 %m월 %d일")
        result = f'{date}({weeks})'        
        return result
 
    def time(self):
        return datetime.today().strftime("%H시%M분%S초")
 
    def answer(self, text):
        response =text.replace(" ", "")
 
        dictionary = {
            '날씨': f'{self.weather()}',
            '요일': f'오늘은 {self.week()}요일 입니다',
            '시간': f' {self.time()}입니다.',
        }
 
        if response == '' or None:  #만약 ' '또는 아무거나 입력하지 않았을 때 패스함.
            pass
        elif response in dictionary.keys(): #만약 answer에 있는 key들을 입력했을 때 답변함.
            return dictionary[text]
        else:
            pass



    
intents=discord.Intents.default()
intents.message_content=True
client=discordbot(intents=intents)
client.run(TOKEN)
