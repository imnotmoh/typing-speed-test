from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.ef.com/wwen/english-resources/english-vocabulary/top-1000-words/")
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")


p = soup.select_one("#node-7908 > div > div > div > div > p:nth-child(3)")
words = p.getText()

words_list = words.split("\n\t")
print(words_list)
a
