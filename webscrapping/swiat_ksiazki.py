from bs4 import BeautifulSoup
from requests import get
import sqlite3
from sys import argv

URL = "https://www.swiatksiazki.pl/catalogsearch/result/?q=blask+ostatecznego+kresu"

db = sqlite3.connect("dane2.db")
cursor = db.cursor()

#python empik.py setup
if len(argv) > 1 and argv[1] == "setup":
    cursor.execute('''CREATE TABLE book_offer (name Text, price Real, link TEXT)''')
    quit()

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')

#for book_offer in bs.find_all("div", class_="product details product-item-details"):
#    print(book_offer)
for book_offer in bs.find_all("li", class_="item product product-item"):
    book_name = book_offer.find("strong", class_="product name product-item-name").get_text()
    #single_book_price = book_offer.find("span", class_="price").get_text()
    book_price = book_offer.find("div", class_="price-box price-final_price").get_text().strip()
    link = str(book_offer.find("a"))
    #print(name, price, link["href"])

    cursor.execute("INSERT INTO book_offer VALUES (?, ?, ?)", (book_name, book_price, link))
    db.commit()

db.close()
