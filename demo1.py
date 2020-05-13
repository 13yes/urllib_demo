from urllib import request
from  urllib import parse
# resp = request.urlopen('http://www.baidu.com')
# print(resp.getcode())
# read()\readline()\readlines()
headers = {'User-Agent':'User-Agent:Mozilla/5.0'}
# download
# request.urlretrieve('https://wimg.ruan8.com/uploadimg/image/20190613/20190613091540_80642.jpg', 'luban.jpg')
# request.urlretrieve('https://baidu.com/', 'baidu.html')
# encode
# params = {'name': 'Alvin', 'age': 18, 'greet': 'hello world'}
# result = parse.urlencode(params)
# print(result)
# url = 'https://www.baidu.com/s?wd=周杰伦'
# url = 'https://www.baidu.com/s'
# params = {'wd': "周杰伦"}
# qs = parse.urlencode(params)
# url = url + '?' + qs
# print(url)
# resp = request.urlopen(url)
# print(resp.read())
# parse_qs
params = {'name': '周杰伦', 'age': 18, 'greet': 'hello world'}
result = parse.urlencode(params)
print(result)
qs = parse.parse_qs(result)
print(qs)
