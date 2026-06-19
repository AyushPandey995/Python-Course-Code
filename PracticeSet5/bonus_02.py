p_c = {"Pen": 10, "Chart paper": 20, "Pencil": 5, "Eraser": 3}

max_price = 0
max_product = ""

for product, price in p_c.items():
    if price > max_price:
        max_price = price
        max_product = product

print(max_product, ":", max_price)
