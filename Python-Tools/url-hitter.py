import requests
import time

HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/45.0.2454.101 Safari/537.36'),
           'referer': 'https://github.com/abhisheksarkar30/abhisheksarkar30'}

url = 'https://camo.githubusercontent.com/b964c6ed910315cfca5e4e42d2b5ec02acb3289e/68747470733a2f2f677076632e6172747572696f2e6465762f616268697368656b7361726b61723330'

while True:
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        time.sleep(1)
    else:
        time.sleep(10)
