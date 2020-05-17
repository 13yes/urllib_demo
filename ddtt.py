import requests
from lxml import etree

BASE_DOMIN= 'https://dytt8.net'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Cookie': 'XLA_CI=ae81c1bfe83e706c774df3385c3bfd57'
}
# movie = []
def get_detail_urls(url):
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('GBK', errors='ignore')
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    # for detail_url in detail_urls:
        # print(BASE_DOMIN+detail_url)
    detail_urls = map(lambda url: BASE_DOMIN+url, detail_urls)
    return detail_urls
def parse_detail_page(url):
    movie = {}
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('GBK', errors='ignore')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    # for x in title:
    #     print(etree.tostring(x, encoding='utf-8').decode('utf-8'))
    # print(title)
    # print(type(title))
    movie['title'] = title
    zoomE = html.xpath("//div[@id='Zoom']")[0]
    cover = zoomE.xpath(".//img/@src")[0]
    movie['cover'] = cover

    def parse_info(info, rule):
        return info.replace(rule, "").strip()
    infos = zoomE.xpath(".//text()")
    # print(infos)
    for index, info in enumerate(infos):
        # print(info)
        # print(index)
        if info.startswith("◎年　　代"):
            # info = info.replace("◎年　　代", "").strip()
            # print(info)
            info = parse_info(info, "◎年　　代")
            movie['year'] = info
            # print(info)
        elif info.startswith("◎产　　地"):
            info = parse_info(info, "◎产　　地")
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info, "◎类　　别")
            movie['category'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info, "◎导　　演")
            movie['dirctor'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info, "◎片　　长")
            movie['duration'] = info
        elif info.startswith("◎主　　演"):
            info = parse_info(info, "◎主　　演")
            actors = [info]
            # print(actors)
            for x in range(index+1, len(infos)):
                # print(infos[x]
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            # print(actors)
            movie['actors'] = actors
    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download_url'] = download_url
    # print(download_url)
    return movie

    # movie = {
    #     'title': title,
    #     'cover': cover,
    #     'year': info
    # }
    # movies.append(movie)
def spider():
    base_url = 'https://dytt8.net/html/gndy/dyzz/list_23_{}.html'
    movies = []
    for x in range(1, 3):
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            # print(detail_url)
            movie = parse_detail_page(detail_url)
            movies.append(movie)
        print(movies)
            # break
        # break
if __name__ == '__main__':
    spider()
