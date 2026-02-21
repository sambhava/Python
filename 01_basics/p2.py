#movie ticket pricing

day= input("enter the today's day:")
age= int(input("enter your age:"))

price = 12 if age >= 18 else 8


if day == "wednesday":
    price= price-2

print("price of ticket is $", price)