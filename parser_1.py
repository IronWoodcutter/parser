import requests
from bs4 import BeautifulSoup

URL = "https://auto.ria.com/uk/newauto/marka-jeep/"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 'accept': '*/*'}
HOST = "https://auto.ria.com"

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('section', class_='proposition')
    #print(items)
    cars = []

    for item in items:
                    cars.append({
                'title': item.find('span', class_='link').get_text(strip=True),
                'link': HOST + item.find('a', class_='proposition_link').get('href'),
                'usd_price': item.find('span', class_='green').get_text(),
                
                
            })

        


    print(cars)
    print(len(cars))



def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
        
    else:
        print('Error')


parse()