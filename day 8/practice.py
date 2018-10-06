#Anti-Lychrel number
def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return (str(b)+str(a))

num=int(input("Enter any number:"))
sum1=num

a=round(num%10,2)
b=int(num/10)

y=swap(a,b)

x=int(y)+sum1

c=round(x%10,2)
d=int(x/10)
z=swap(c,d)
print(z)



if (int(z)==x):
    print("True")

else:
     print("False")

     

    
    
