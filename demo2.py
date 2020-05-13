from urllib import parse

url = 'https://www.baidu.com/s?wd=python'
result = parse.urlparse(url)
print(result)
result = parse.urlsplit(url)
print(result)
