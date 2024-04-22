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

# Map function with dictionaries and lambda function that returns a dictionary.
add_taxes = lambda item: {
    "product": item["product"],
    "price": item["price"],
    "taxes": item["price"] * .19,
    "final_price": item["price"] + item["price"] * .19
}
   
new_items = list(map(add_taxes, items))
products_with_taxes = [(item["product"], item["taxes"]) for item in new_items]
print(items)
print(new_items)
print(products_with_taxes)
