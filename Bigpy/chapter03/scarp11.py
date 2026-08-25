import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

res=requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# 첫 번쨰 책 하나만 찾기
book = soup.find("article", class_="product_pod")
# book = soup.select("article.product_pod")
# book = soup.find("article.product_pod") # (X)첫번째 인자값을 태그로 인지

for bood in book:
    title = book.select_one("h3 a")["title"]
    price = book.select_one("p.price_color").text
    rating = book.select_one("p.star-rating")["class"][1] # 두번째 class가 별점(One, Two, Three...)

    print(f"{title} | {price} | 별점: {rating}")