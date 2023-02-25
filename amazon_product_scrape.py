from bs4 import BeautifulSoup
import requests

import csv
import datetime
#connecting to the wesbite
url = "https://www.amazon.in/dp/B08W8DGK3X"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0"}
page = requests.get(url,headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
#searching for the title
title = soup.find(id = "productTitle")
if title:
    title = title.get_text()
else:
    title = "default_title"
#searching for the price
price = soup.find(class_="a-price-whole")
if price:
    price = price.get_text()
else:
    price = "default_title"
#searching for review stars
review_star = soup.find(class_="a-icon-alt")
if review_star:
    review_star = review_star.get_text()
else:
    review_star = "default_title"
#sysdate
today = datetime.date.today()
#converting the output into a csv file
header = ['Title', 'Price', 'review_star','Date']
data = [title, price, review_star, today]
with open('C:/Users/amine/Downloads/me.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
with open('C:/Users/amine/Downloads/me.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)
