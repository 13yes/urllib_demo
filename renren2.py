import requests
url = 'http://www.renren.com/PLogin.do'
data = {
    'email': '15613852806',
    'password': '15175608090'
}
headers ={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
session = requests.Session()
session.post(url, data=data, headers=headers)
response = session.get('http://www.renren.com/426203590/profile')
with open('renren2.html', 'w', encoding='utf-8')as fp:
    fp.write(response.text)
