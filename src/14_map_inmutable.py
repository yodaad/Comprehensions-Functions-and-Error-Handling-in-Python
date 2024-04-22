# Map function with inmutable objects

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

# Map function with inmutable objects and copy method.
def add_taxes(item):
    new_item = item.copy()
    new_item["taxes"] = new_item["price"] * .19
    new_item["final_price"] = new_item["price"] + new_item["taxes"]
    return new_item
    
new_items = list(map(add_taxes, items))
print("New List")
print(new_items)
print("Old List")
print(items)