from bs4 import BeautifulSoup

with open("index.html", encoding = "utf-8") as html:
    soup = BeautifulSoup(html, "html.parser")

tbody = soup.find("tbody", {"id": "info-produtos"})

print(list(filter(lambda x: x != "\n", tbody.children)))
