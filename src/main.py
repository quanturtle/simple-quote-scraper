import requests as r
from bs4 import BeautifulSoup
import sqlmodel as sql
from models import init_sql, Quotes

def main():
    engine = init_sql()
    result = r.get('https://quotes.toscrape.com/')

    soup = BeautifulSoup(result.text, 'html.parser')
    quotes = soup.find_all('span', attrs={'class': 'text', 'itemprop':'text'})
    authors = soup.find_all('small', attrs={'class':'author', 'itemprop':'author'}) 
    
    quotes_authors = zip(quotes, authors)

    with sql.Session(engine) as session:
        for elem in quotes_authors:
            quote_to_add = Quotes(quote=elem[0].text, author=elem[1].text)
            session.add(quote_to_add)
            session.commit()

main()
