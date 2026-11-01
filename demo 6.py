
# program 1
def format_rupees(amount):
    return f"Rs {amount:,}"


print(format_rupees(12800))
print(format_rupees(999))
print(format_rupees(1250000))

print(f"Noor Foods owes {format_rupees(11520)}")

# program 2 
def add_tax(subtotal, rate=0.18):
    return subtotal + (subtotal * rate)


result1 = add_tax(7200)
result2 = add_tax(7200, 0.05)

print(result1)
print(result2)

# program 3
def shipping_charge(weight_kg, city, order_total=0):
    city = city.strip().title()

    if order_total > 10000:
        return 0

    if city in ["Karachi", "Lahore", "Islamabad"]:
        charge = 200
    else:
        charge = 350

    if weight_kg > 5:
        charge = charge * 2

    return charge


print(f"Shipping to Karachi: {format_rupees(shipping_charge(5, ' karachi '))}")
print(f"Shipping to Lahore: {format_rupees(shipping_charge(6, 'Lahore'))}")
print(f"Shipping to Peshawar: {format_rupees(shipping_charge(4, 'Peshawar'))}")
print(f"Shipping to Islamabad: {format_rupees(shipping_charge(7, 'Islamabad'))}")
print(f"Shipping to Karachi: {format_rupees(shipping_charge(8, 'Karachi', 12000))}")

# program 4
def total_by_status(orders, status):
    total = 0

    for order in orders:
        if order["status"] == status:
            total += order["total"]

    return total


orders = [
    {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": 12800, "status": "pending"},
    {"id": "A103", "total": 2300, "status": "delivered"},
]


print(total_by_status(orders, "delivered"))
print(total_by_status(orders, "pending"))
print(total_by_status(orders, "cancelled"))

# program 5
inventory = [
    {"name": "Notebook", "stock": 8, "reorder_level": 15, "unit_cost": 90},
    {"name": "Pen", "stock": 140, "reorder_level": 50, "unit_cost": 25},
    {"name": "Stapler", "stock": 2, "reorder_level": 5, "unit_cost": 650},
    {"name": "Marker", "stock": 30, "reorder_level": 30, "unit_cost": 120},
    {"name": "Folder", "stock": 11, "reorder_level": 20, "unit_cost": 60},
]


def needs_reorder(product):
    return product["stock"] < product["reorder_level"]


def reorder_quantity(product):
    target_stock = product["reorder_level"] * 2
    return target_stock - product["stock"]


def reorder_cost(product):
    return reorder_quantity(product) * product["unit_cost"]


# Separate functions make each rule easier to test and change.
total_cost = 0
products_to_reorder = 0

for product in inventory:
    if needs_reorder(product):
        quantity = reorder_quantity(product)
        cost = reorder_cost(product)

        print(f"Reorder {quantity} x {product['name']} (Rs {cost:,})")

        total_cost += cost
        products_to_reorder += 1

if products_to_reorder == 0:
    print("All stock OK")
else:
    print(f"Total cost: Rs {total_cost:,}")
