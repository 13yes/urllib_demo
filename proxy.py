from urllib import request
url = 'http://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())
handler = request.ProxyHandler({'HTTP': '116.0.54.30:8080'})
opener = request.build_opener(handler)
resp = opener.open(url)
print(resp.read())
