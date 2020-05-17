import requests
from lxml import etree
headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
'Referer':'https://movie.douban.com/'
}
url = 'https://movie.douban.com/cinema/nowplaying/tangshan/'
response = requests.get(url, headers=headers)
text = response.text
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[1]
# print(etree.tostring(ul, encoding='utf-8').decode('utf-8'))
lis = ul.xpath('./li')
movies = []
for li in lis:
    title = li.xpath('@data-title')[0]
    score = li.xpath('@data-score')[0]
    duration = li.xpath('@data-duration')[0]
    region = li.xpath('@data-region')[0]
    director = li.xpath('@data-director')[0]
    actors = li.xpath('@data-actors')[0]
    thumbnail = li.xpath('.//img/@src')[0]
    # print(title, score, duration, region, director, actors, thumbnail)
    movie = {
        'title': title,
        'score': score,
        'duration': duration,
        'region': region,
        'director': director,
        'actors': actors,
        'thumbnail': thumbnail
    }
    movies.append(movie)
print(movies)
