# Web scraping with pandas
import pandas as pd
import requests

url = 'https://apexranked.com/'

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(url, header)


def read():
    ranked_leaderboard = pd.read_html(r.text)
    print(ranked_leaderboard)

read()



