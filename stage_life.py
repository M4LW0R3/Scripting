person = 2

if person < 2:
    print('You are a baby.')
elif person < 4:
    print("You are a toddler.")
elif person < 13:
    print("You are a Kid.")
elif person < 20:
    print("You are a teenager.")
elif person < 65:
    print("You are an adult.")
elif person > 65:
    print("You are an elderly.")
else:
    print("Age not found.")
