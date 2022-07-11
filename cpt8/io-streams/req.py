from codecs import IncrementalDecoder
import requests
from pprint import pprint

urls = {
    "get": "https://httpbin.org/get?t=learn+python+programming",
    "headers": "https://httpbin.org/headers",
    "ip": "https://httpbin.org/ip",
    "user-agent": "https://httpbin.org/user-agent",
    "UUID": "https://httpbin.org/uuid",
    "JSON": "https://httpbin.org/json",
}

def get_data(title,url):
    resp = requests.get(url)
    print(f"Response for {title}")
    pprint(resp.json())
    
for title, url in urls.items():
    get_data(title,url)
    print('_' * 10)
