
#  variable ,data types, list and dictionary


animal="snake"
print("test")
print(animal)
print(type(animal))



number1=True
number2=20
number3=10

number1=number1+number2+number3
print(number1)


email="Sajila@gmail.com"
print(email.lower())

email=abs(True)      # used only woth integer and float valuse boolean  bhi
print(email)
import math               # floor returns the lowest value
print(math.floor(2.4))

print (math.ceil(3.1))    #  round up  float ko integer mein convetkarta
x= "   hello world  "
print(x.strip())    # spaces ko remove karta string k shuru or akhir se

print(len(x))     # len of character also the spaces 

datebirth = 5
#print("my birthdate is",date_birth)
print( "my birthdate is",datebirth ,"april")

list_of_name=[2.5,21,True]      # list carry indexes starting from 0  its also an array
print(list_of_name[0])       # why indxes of array starts with 0?

# to add a number in the list
list_of_name.append(7)
print(list_of_name)              #difference between method and function?


#operative presistance
#print(list_0f_name.append(""))   #  its not valid syntex

print(sum(list_of_name))       # array and list k andar sttringd ko concatenate nhi kar sakty 

# dictionary
# key values instead of indexes 
#key_value  like name wo seprate hogi values se by :



userdata={
    "name":"saji",
    "age": "4",
}
print(userdata["age"])
userdata["age"]="20"
userdata["color"]="pink"
print(userdata)


orders = [
    {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": 12800, "status": "pending"},
    {"id": "A103", "total": 2300, "status": "pending"},
]

pending_count = 0    # variable with starting value 0.
for order in orders:   # ye loop har order ko check kary ga
    if order["status"] == "pending":   # ye loop check karta hai ki order pending mein hai ya nhi 
        pending_count += 1    # pending orders ki counting karta.
        print(f"Pending: {order['id']}")

print(f"{pending_count} order(s) pending")

#  practice problems 
# 1
customer = "karachi_crafts"
orders = 3
price = 2400
delivery_cost = 350
total = orders * price + delivery_cost
print(total)

#2
order_subtottal = 7200
sales_tax= 18 / 100
tax_amount = order_subtottal * sales_tax
totalwith_tax = order_subtottal + tax_amount
print(tax_amount)
print(totalwith_tax)
print(type(tax_amount))   #  18% ka result python mein 0.18 hota hai jo float hai
#jab 7200 se multiply karte hain to float ka result aata hai jo 1296.0 hai


#3
bill = 4750
friends = 4

share = bill / friends    # normal division per head kitna paisa hoga
whole_rupees = bill // friends # har frined kitna dega
leftover = bill % friends   #remainder

print(share)
print(whole_rupees)
print(leftover)
#4

price = 15000

discounted_price = price * 0.90
final_price = discounted_price * 1.18

print(final_price)

# Now apply tax first, then discount
price_with_tax = price * 1.18
other_final_price = price_with_tax * 0.90

print(other_final_price)

# Both methods give the same result because
# multiplying by 0.90 and 1.18 gives the same product
# regardless of their order.

#5
items = 23
capacity = 6
shipping_per_box = 120

full_boxes = items // capacity
leftover_items = items % capacity

# Add 1 if there are any leftover items, without using if
total_boxes = full_boxes + (leftover_items > 0)

shipping_cost = total_boxes * shipping_per_box

print(full_boxes)
print(leftover_items)
print(total_boxes)
print(shipping_cost)


# Practice problems 2
#1
name = " aMNA rAZA "

name = name.strip().title()

print(f"Welcome, {name}! Your name has {len(name)} characters.")

#2
email = " Ali.Khan@GMAIL.com "

email = email.strip().lower()

print(f"Email: {email} ({len(email)} characters)")

#3
item = " wireless MOUSE "
price = 2499
quantity = 3

item = item.strip().title()
total = price * quantity

print(f"{item} x{quantity} = Rs {total:,}")

#4
code = " ord-2024-0042 "

code = code.strip().replace("-", "").upper()

print(f"Order {code} has {len(code)} characters")

#5
first = " bilal "
last = "QURESHI "
city = "lahore"

username = first.strip().lower() + "." + last.strip().lower() + "_" + city[:3]

print(username)


#practice_problems 3
# 1
prices = [850, 1200, 400]

print(prices[-1])
print(sum(prices))

product = {
    "name": "Notebook",
    "price": 1200,
    "in_stock": True
}

product["in_stock"] = False

print(product["name"])

#2
sales = [18500, 22300, 19800, 25400, 31200, 42800, 38600]

print(f"Monday: Rs {sales[0]:,}")
print(f"Sunday: Rs {sales[6]:,}")

weekly_total = sum(sales)
daily_average = weekly_total / len(sales)

print(f"Weekly total: Rs {weekly_total:,}")
print(f"Daily average: Rs {daily_average:,.0f}")

print(f"Best sales: Rs {max(sales):,}")
print(f"Worst sales: Rs {min(sales):,}")


# 3
stock = {
    "pens": 120,
    "notebooks": 45,
    "staplers": 8
}

stock["notebooks"] = stock["notebooks"] - 30

stock["markers"] = 60

print(len(stock))
print(stock)

#4
orders = [
    {"id": "A101", "customer": "Ali", "total": 4500},
    {"id": "A102", "customer": "Sara", "total": 12800},
    {"id": "A103", "customer": "Bilal", "total": 2300}
]

print(orders[1]["customer"])

orders[2]["total"] = orders[2]["total"] - 500

orders.append({
    "id": "A104",
    "customer": "Noor",
    "total": 6100
})

print(f"{len(orders)} orders. The first is {orders[0]['id']} and the last is {orders[-1]['id']}.")


#5
customer = {
    "name": "Noor Foods",
    "address": {"city": "Karachi", "area": "Clifton"},
    "order_totals": [4500, 12800, 2300],
}

print(customer["address"]["city"])
print(len(customer["order_totals"]))
print(sum(customer["order_totals"]))

customer["order_totals"].append(6100)

print(sum(customer["order_totals"]))

print(customer.get("phone", "No phone number"))