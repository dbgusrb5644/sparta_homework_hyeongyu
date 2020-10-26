import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


my_url = "https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
res = requests.get(my_url,headers=headers) #HTML,CSS,JS
soup=BeautifulSoup(res.text,'html.parser') #크롤링 기본줄
client = MongoClient('localhost', 27017)/#db 주소
db = client.myData

musics = soup.select("#body-content > div.newest-list > div > table > tbody > tr") # >안에있는
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#반복되는 기준으로 넣는다
for music in musics :
    title = music.select_one('td.info > a.title.ellipsis').text.strip()
    artist = music.select_one('td.info > a.artist.ellipsis').text
    # body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
    rank1 = music.select_one('td.number').text
    rank= rank1[0:2].strip()
    print(rank,title,artist)
    music_dict = {
        'rank': rank,
        'title': title,
        'artist': artist,

    }
    db.music.insert_one(music_dict)
#수정






        #pymongo를사용해서 데이터 저장하기
        # navernmovie
        # 저장되는 데이터의 형태는 dictionarty
        #dict()함수 찾아보기



