'''page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')

for book_offer in bs.find_all("div", class_="search-content js-search-content"):
    book_author = book_offer.find("div", class_="smartAuthorWrapper ta-product-smartauthor").get_text().strip()
    book_name = book_offer.find("strong", class_="ta-product-title").get_text().strip()
    book_price = book_offer.find("div", class_="price ta-price-tile").get_text().strip().splitlines()[0]
    print(book_author, book_name, book_price)'''