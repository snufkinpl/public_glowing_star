import requests
from bs4 import BeautifulSoup
from requests import get


def scrap_book_data(URL):
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    for book_offer in bs.find_all("div", class_="search-content js-search-content"):
        book_author = book_offer.find("div", class_="smartAuthorWrapper ta-product-smartauthor").get_text().strip()
        book_name = book_offer.find("strong", class_="ta-product-title").get_text().strip()
        book_price = book_offer.find("div", class_="price ta-price-tile").get_text().strip().splitlines()[0]
        print(book_author, book_name, book_price)


def construct_URL(book_name):
    #book_name = 'rok 1984'
    payload = {'q': [book_name], 'type': 'basicForm', 'ac': 'true'}

    r = requests.get('https://www.empik.com/szukaj/produkt', params=payload)
    print(r.url)
    # https://httpbin.org/get?key1=value1&key2=value2

    return r.url


book_name = input("Podaj nazwę książki, dla której ma być wykonane szukanie na stronie empik.com: ")
scrap_book_data(construct_URL(book_name))
