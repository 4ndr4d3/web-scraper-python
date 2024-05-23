import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

def fetch_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to load page {url}")
    page_content = response.content
    soup = BeautifulSoup(page_content, 'html.parser')
    return soup

def parse_books(soup):
    books = []
    for article in soup.find_all('article', class_='product_pod'):
        title = article.h3.a['title']
        price = article.find('p', class_='price_color').text
        books.append({
            'title': title,
            'price': price
        })
    return books

def main():
    base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
    all_books = []
    for page_num in range(1, 51):  # Assumindo que há 50 páginas
        url = base_url.format(page_num)
        soup = fetch_books(url)
        books = parse_books(soup)
        all_books.extend(books)
        print(f"Processed page {page_num}")
    
    # Armazenar os dados em um DataFrame do Pandas
    df = pd.DataFrame(all_books)
    df.to_csv('books.csv', index=False)
    print("Data saved to books.csv")

    # Opcional: Armazenar em um banco de dados SQLite
    conn = sqlite3.connect('books.db')
    df.to_sql('books', conn, if_exists='replace', index=False)
    conn.close()
    print("Data saved to books.db")

if __name__ == "__main__":
    main()
