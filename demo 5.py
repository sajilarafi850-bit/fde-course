

# program 1
orders = [
    {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": 12800, "status": "pending"},
    {"id": "A103", "total": 2300, "status": "delivered"},
]

revenue = 0

for order in orders:
    if order["status"] == "delivered":
        revenue += order["total"]

print(f"Delivered revenue: Rs {revenue:,}")

# program 2 
prices = [850, 1200, 400, 3100, 650]

counter = 0
total = 0
expensive_count = 0

for price in prices:
    counter += 1
    total += price

    print(f"Item {counter}: Rs {price:,}")

    if price > 1000:
        expensive_count += 1

print(f"Total: Rs {total:,}")
print(f"Items over Rs 1,000: {expensive_count}")

# program 3
# 1. Start with the first order as the biggest.
# 2. Check every order in the list.
# 3. If an order is bigger, update the biggest order.
# 4. Print its ID and total.

orders = [
    {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": 12800, "status": "pending"},
    {"id": "A103", "total": 2300, "status": "delivered"},
]

biggest = orders[0]

for order in orders:
    if order["total"] > biggest["total"]:
        biggest = order

print(f"Biggest order: {biggest['id']} (Rs {biggest['total']:,})")

# program 4 


orders = [
    {"customer": "Noor Foods", "total": 4500},
    {"customer": "Karachi Crafts", "total": 12800},
    {"customer": "Noor Foods", "total": 2300},
    {"customer": "Bilal Traders", "total": 7600},
    {"customer": "Karachi Crafts", "total": 3900},
    {"customer": "Noor Foods", "total": 6100},
]

customer_totals = {}

for order in orders:
    customer = order["customer"]
    total = order["total"]

    if customer in customer_totals:
        customer_totals[customer] += total
    else:
        customer_totals[customer] = total

for customer, total in customer_totals.items():
    print(f"{customer}: Rs {total:,}")


# program 5

# 1. Start total cost at zero.
# 2. Loop through every product.
# 3. If stock is below reorder_level, calculate the target stock.
# 4. Calculate quantity to order and its cost.
# 5. Print each product and add its cost.
# 6. If nothing needs reordering, print All stock OK.
# 7. Otherwise, print the total cost.

inventory = [
    {"name": "Notebook", "stock": 8, "reorder_level": 15, "unit_cost": 90},
    {"name": "Pen", "stock": 140, "reorder_level": 50, "unit_cost": 25},
    {"name": "Stapler", "stock": 2, "reorder_level": 5, "unit_cost": 650},
    {"name": "Marker", "stock": 30, "reorder_level": 30, "unit_cost": 120},
    {"name": "Folder", "stock": 11, "reorder_level": 20, "unit_cost": 60},
]

total_cost = 0
products_to_reorder = 0

for product in inventory:
    if product["stock"] < product["reorder_level"]:
        target_stock = product["reorder_level"] * 2
        quantity = target_stock - product["stock"]
        cost = quantity * product["unit_cost"]

        print(f"Reorder {quantity} x {product['name']} (Rs {cost:,})")

        total_cost += cost
        products_to_reorder += 1

if products_to_reorder == 0:
    print("All stock OK")
else:
    print(f"Total cost: Rs {total_cost:,}")