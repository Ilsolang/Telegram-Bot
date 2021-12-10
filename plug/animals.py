import requests
from config import bot
from bs4 import BeautifulSoup

def cats(m):
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    search = "https://theoldreader.com/kittens/1366/768/js"
    url = requests.get(search, headers=user_agent) 
    soup = BeautifulSoup(url.text, features="lxml")
    result = soup.find("img").get("src")
    result = "https://theoldreader.com" + result
    bot.send_photo(m.chat.id, photo=result, parse_mode= "Markdown")
    bot.delete_message(m.chat.id, m.message_id)

def get_dogurl():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def dogs(m):
    url = get_dogurl()
    bot.delete_message(m.chat.id, m.message_id)
    bot.send_photo(m.chat.id, photo=url)