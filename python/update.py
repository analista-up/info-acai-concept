from bs4 import BeautifulSoup as BS

from util import get_products_names as gpn
from util import get_products_info as gpi

DB_NOMES = "./db/db_nomes.txt"
DB_INFO = "./db/db_info.txt"


with open("templates/index.html", encoding = "utf-8") as html:
    soup = BS(html, "html.parser")

tbody = soup.find("tbody", {"id": "info-produtos"})

products = gpn(DB_NOMES)
info = gpi(DB_INFO)

for product in products:
    values = [
        products.get(product),
        f"R$ {info.get(product).get("Preço"):.2f}".replace(".", ","),
        f"{info.get(product).get("Estoque")} BD"
    ]

    tr = soup.new_tag("tr")

    for value in values:
        td = soup.new_tag("td")
        td.append(value)

        tr.append(td)
    
    tbody.append(tr)

html = soup.prettify("utf-8")

with open("index.html", "wb") as output:
    output.write(html)
