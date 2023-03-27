from bs4 import BeautifulSoup
import requests


def parse():
    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")

    tdict = {}
    for row in soup.find_all('tr'):
        title = row.find_next(class_='titleColumn').find_next('a').text
        rating = row.find_next(class_='ratingColumn imdbRating').find_next('strong').text
        tdict[title] = rating

    return tdict
