n=int(input("Enter the number:"))
m=int(input("Enter the number:"))
p=int(input("Enter the number:"))

if n>p:
    if n>m:
        print("%d is greatest"%(n))
    else:
        print("%d is greatest"%(m))
else:
    print("%d is greatest"%(p))

