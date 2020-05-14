import requests
proxy = {
    'http': 'http://110.243.2.201:9999'
}
response = requests.get('http://httpbin.org/ip')
print(response.text)
response = requests.get('http://httpbin.org/ip', proxies=proxy)
print(response.text)

