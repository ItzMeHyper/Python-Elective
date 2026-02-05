cafe_stock = {"Coffee": 100, "Sugar": 50, "Milk": 20}

items = cafe_stock.keys()
print(f"Items in stock: {list(items)}")

quantities = cafe_stock.values()
print(f"Quantities in stock: {list(quantities)}")

for item, amount in cafe_stock.items():
    print(f"We havr {amount} units of {item} in stock.")

tea_count = cafe_stock.get("Tea", 0)
print(f"Tea in stock: {tea_count} units")

removed_value = cafe_stock.pop("Sugar")
print(f"Removed Sugar. It had {removed_value} units.")

new_delivery = {"Coffee": 150, "Cups" : 500}
cafe_stock.update(new_delivery)
print("Updated stock:", cafe_stock)

cafe_stock.clear()
print(f"Stock after closing: {cafe_stock}")