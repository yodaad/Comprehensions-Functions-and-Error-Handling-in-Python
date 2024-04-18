# Map function with dictionaries and lambda function.

items = [
    {
        "product": "shirt",
        "price": 100
    },
    {
        "product": "pants",
        "price": 300
    },
    {
        "product": "pants 2",
        "price": 200
    }
]


# Map function with dictionaries and lambda function.
prices = list(map(lambda item: item["price"], items))
print(prices)

products = list(map(lambda item: item["product"], items))
print(products)

def add_taxes(item):
    item["taxes"] = item["price"] * .19
    item["final_price"] = item["price"] + item["taxes"]
    return item
    
new_items = list(map(add_taxes, items))
print(new_items)