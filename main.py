import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Titre", "Prix"])

    titles = soup.findAll("h3")
    prices = soup.find_all("p", class_="price_color")

    for title, price in zip(titles, prices):
        writer.writerow([title.text, price.text])

