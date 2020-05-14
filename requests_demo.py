import requests

# response = requests.get('https://baidu.com/')
# print((type(response.content)))
# print(response.content.decode('utf-8'))
# print(response.text)
# print(response.url)
# print(response.encoding)
# print(response.status_code)
kw = {'query': '中国'}
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
response = requests.get('https://www.sogou.com/web?', params=kw, headers=headers)
with open('baidu2.html', 'w', encoding='utf-8')as fp:
    fp.write(response.content.decode('utf-8'))
    print(response.url)
    print(response.status_code)
