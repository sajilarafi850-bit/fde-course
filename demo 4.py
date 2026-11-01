# program 1

total = 6200
city = "Lahore"

if total >= 5000 and city == "Lahore":
    print("Free delivery")
else:
    print("Delivery charge: Rs 350")


# program 2
marks = 80

if marks >= 80:
    print("A")
elif marks >= 65:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")

# program 3
stock = 12
quantity = 5

if quantity <= 0:
    print("Invalid quantity")
elif quantity > stock:
    print(f"Only {stock} left in stock")
else:
    remaining = stock - quantity
    print(f"Confirmed. {remaining} left after this order")


# program 4
weight_kg = 5
order_total = 6000
city = " karachi "

city = city.strip().title()

if order_total > 10000:
    charge = 0
elif city in ["Karachi", "Lahore", "Islamabad"]:
    if weight_kg <= 5:
        charge = 200
    else:
        charge = 400
else:
    if weight_kg <= 5:
        charge = 350
    else:
        charge = 700

print(f"Shipping to {city}: Rs {charge}")

# program 5
plan = "enterprise"
hours_open = 6
message = "I need a REFUND"

message = message.lower()

# Check Urgent first so enterprise tickets meeting this rule
# remain Urgent even if they also mention a refund.
if plan == "enterprise" and hours_open > 4:
    priority = "Urgent"
elif "refund" in message or "charged twice" in message:
    priority = "High"
elif plan == "pro" and hours_open > 24:
    priority = "High"
else:
    priority = "Normal"

print(priority)