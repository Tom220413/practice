import codecs
import requests
from bs4 import BeautifulSoup

def load_compass():
    print('登録したいCompassのイベント参加者・申込者一覧ページのURLを入力して')
    page = input('>> ')
    res = requests.get(page)
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    result = []
    twitter = []
    github = []
    username = []
    userpage = []
    for p_tag in soup.find_all('p', class_='display_name'):
        if p_tag == '\n':
            continue
        username.append(p_tag.text)
        userpage.append(p_tag.contents)
        
    for td in soup.find_all('td', class_='social text_center'):
        for i in td.contents:
            if i == '\n':
                continue
            if 'Twitter' in i.attrs.get('title', ''):
                twitter.append(i.attrs.get('href', ''))
            elif 'GitHub' in i.attrs.get('title', ''):
                github.append(i.attrs.get('href', ''))
    index = 0
    for n in username:
        userdata = {
                'username' : n,
                'userpage' : userpage[index],
                'usertwitter' : twitter[index],                
                'usergithub' : github[index]
            }
        result.append(userdata)
        index += 1
    print('compassのデータ取れた')

def put_spredsheet():
    result = load_compass()
    
    
    print('スプレッドに記入できた')

def send_slack():
    print('Slackにも通知したよ')
    

   

put_spredsheet()