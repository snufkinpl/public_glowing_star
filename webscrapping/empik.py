from bs4 import BeautifulSoup
from requests import get
import sqlite3
from sys import argv
import datetime


#URL = "https://www.empik.com/szukaj/produkt?q=blask%20ostatecznego%20kresu&qtype=basicForm&ac=true"
URL = "https://www.empik.com/ksiazki/fantasy"

db = sqlite3.connect("dane.db")
cursor = db.cursor()

#python empik.py setup
if len(argv) > 1 and argv[1] == "setup":
    cursor.execute('''CREATE TABLE book_offer (author Text, name Text, price Real, book_type Text, date Date, linku TEXT)''')
    quit()

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')

#for book_offer in bs.find_all("div", class_="product details product-item-details"):
#    print(book_offer)
for book_offer in bs.find_all("div", class_="search-list-item js-reco-product js-energyclass-product ta-product-tile"):
    book_author = book_offer.find("div", class_="smartAuthorWrapper ta-product-smartauthor").get_text().strip()
    book_name = book_offer.find("strong", class_="ta-product-title").get_text().strip()
    book_price = book_offer.find("div", class_="price ta-price-tile").get_text().strip().splitlines()[0].replace('\xa0', ' ')
    book_type = book_offer.find("span", class_="productMainInfoSuffix ta-product-category").get_text().strip()
    link = book_offer.find("a")
    linku = "https://www.empik.com/" + link["href"]
    # print(link)
    # print(book_name, book_price, linku)
    date = datetime.date.today()

    cursor.execute("INSERT INTO book_offer VALUES (?, ?, ?, ?, ?, ?)", (book_author, book_name, book_price, book_type, date, linku,))
    #db.commit()

# db.close()

for row in db.execute('SELECT * FROM book_offer ORDER BY date'):
    print(row)


cursor.execute('SELECT count(*) FROM book_offer')
how_many = cursor.fetchone()
print(f"W bazie danych jest tyle rekordów: {how_many[0]}")

'''cursor.execute('DELETE FROM book_offer WHERE date = "2022-04-30"')
print(f"Usunięto: {cursor.rowcount} rekordów.")

cursor.execute('SELECT count(*) FROM book_offer')
how_many = cursor.fetchone()
print(f"W bazie danych jest tyle rekordów: {how_many[0]}")'''

db.commit()
db.close()

