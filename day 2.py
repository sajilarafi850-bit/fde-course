

# conditional statements
age = 20
if age > 18:                    # < > = operands   (single qual = value assign karne k liye)  (== equal k liye)
    print("adult")                 # compiler used to trsnslste the code into machine langauge
elif age < 18:                        # jab uper wala statement true hoga wo neechy nhi aye ga agar cndition true bhi hui 
    print("teenager")




total= 6200
city = "lahore"

if total >= 5000 and city == "lahore":               # "and" "or " operator. and k liye donu conditions true hona chahiye or k liye koi aik# != not equal   e.g 5 != 6
    print("free delivery")                           # checking multiple conditions in one line s1 and s2 and s3
elif total >= 5000 or city == "islamabad":
    print("delivery charge Rs:150")
else:
    print("delivery charge Rs:350")




print(10 / 3)
print(10 // 3)
print(-7 / 2)
print(-7 // 2)


arr=[1, 2, 3, 4, 5]
for i in range(len(arr)):               # len() function is used to get the length of the array
    print(arr[i]) 
    
                   # range() function is used to generate a sequence of numbers
#for i in range(5,-1,-1):               # i varaible decleared
    #print(i)


# finding delivery revenue...

orders = [
    {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": 12800, "status": "pending"},
    {"id": "A103", "total": 2300, "status": "delivered"},
]
delivered_count = 0
for order in orders:
    if order["status"] == "delivered":
        delivered_count += order["total"]

print(f"Delivered: {delivered_count} order(s) delivered")


# functions............
def apply_discount(total , rate):
    discount = total * rate
    return total - discount

print(apply_discount(1000, 0.1))   # function call


def add_rs(amount):
    return "Rs " + str(amount)

print(add_rs(13))                0