import requests
import time
import json
from bs4 import BeautifulSoup


def getVideoLink(url):
    href = []
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'__cfduid=d3cfe89e95fce452bd3ba611e637423d21491657054; PHPSESSID=77a35d2c06874bc4d03f34e8a87c6fda; _gat=1; _ga=GA1.2.1810241444.1491657058; _gid=GA1.2.1363690942.1494072488',
        'Host':'www.123kubo.com',
        'Referer':'http://www.123kubo.com/vod-play-id-92197-sid-2-pid-1.html',
        'Upgrade - Insecure - Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }

    resp = requests.get(url,headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    print(soup.prettify())

if __name__ == '__main__':
    getVideoLink('http://www.123kubo.com/vod-play-id-92197-sid-2-pid-1.html')