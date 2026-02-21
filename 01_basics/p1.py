# classify a person's age group: Child(<13), teenager(13-18), adult(20-59), senior(60+)
age= int(input("enter your age : "))

if age < 0:
    print("invalid age")
    exit()
elif age <13 :
    print("child")
elif age <19 :
    print("teenager")
elif age <59 :
    print("adult")
else:
    print("senior")