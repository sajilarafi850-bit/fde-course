orders = [
    {"id": "A101", "customer": "Ali Traders", "total": 4500, "status": "delivered"},
    {"id": "A102", "customer": "Noor Foods", "total": 12800, "status": "pending"},
    {"id": "A103", "customer": "Zain Electronics", "total": 2300, "status": "delivered"},
    {"id": "A104", "customer": "Ali Traders", "total": 7600, "status": "cancelled"},
    {"id": "A105", "customer": "Hira Textiles", "total": 15200, "status": "pending"},
]

print(f"Orders today: {len(orders)}")

revenue = 0

for order in orders:
    if order["status"] != "cancelled":
        revenue += order["total"]

print(f"Revenue (excluding cancelled): Rs {revenue:,}")


print("Pending orders:")

for order in orders:
    if order["status"] == "pending":
        print(f"  {order['id']}  {order['customer']}  Rs {order['total']:,}")