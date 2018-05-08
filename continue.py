while True:
    a=int(input("enter a integer "))
    if a<0:
        continue
    elif a==0:
        break
    else: 
        print("Square is ",a*a)
print("Goodbye")
