import requests
from bs4 import BeautifulSoup

#임의의 회차 번호
draw_no = 1150

url=f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={draw_no}"

headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/124.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")
# print(soup)


# 추첨일자


# 당첨번호