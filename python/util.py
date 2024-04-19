import re

def get_products_names(file: str) -> dict[int, str] | None:
    """
    Esta função vai ler a base de dados e retornar um dicionário onde a
    chave será o código SKU do produto e o valor será seu nome de exibição
    """
    if not isinstance(file, str):
        return None
    
    # Matcher em RegEx para separar pelas ","
    matcher = re.compile(r"[^,]*")

    products_names = dict()

    with open(file, "r", encoding = "utf-8") as db:
        for line in db:
            matches = list(filter(lambda x: x != "", matcher.findall(line.strip())))

            sku = int(matches[0])
            name = str(matches[1])

            update = {
                sku: name
            }

            products_names.update(update)
    
    return products_names

def get_products_info(file: str) -> dict[int, dict[str, int | float | None]] | None:
    """
    Esta função vai ler a base de dados e retornar um dicionário onde a chave será
    o código SKU do produto e o valor será um objeto com seu preço e estoque
    """
    if not isinstance(file, str):
        return None
    
    # Matcher em RegEx para separar pelas ","
    matcher = re.compile(r"(\"[^\"]*\"|[^,]*)")

    products_info = dict()

    with open(file, "r", encoding = "utf-8") as db:
        for line in db:
            matches = matcher.findall(line.strip())

            i = matches.index("PV:")
            j = matches.index("MC:")

            if j - i == 8:
                sku = int(matches[0])
                price = float(matches[j - 4].replace("\"", "").replace(".", "").replace(",", "."))
                stock = int(matches[j - 2].replace("\"", "").replace(".", "").replace(",00", ""))
            else:
                sku = int(matches[0])
                price = None
                stock = int(matches[j - 2].replace("\"", "").replace(".", "").replace(",00", ""))
            
            update = {
                sku: {
                    "Preço": price,
                    "Estoque": stock
                }
            }

            products_info.update(update)
    
    return products_info
