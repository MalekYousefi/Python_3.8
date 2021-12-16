t=int(input("Please enter temperature: "))
if t<0:
    x="Ice"
    print(x.upper())
else:
    if t>100:
        x="Steam"
        print(x.lower())
    else:
        x="Water"
        print(x.title())