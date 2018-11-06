print("Enter two numbers to find the LCM ")
n1=int(input("Enter  number 1:"))
n2=int(input("Enter  number 2:"))
if n2<n1:
    n1,n2=n2,n1  
for i in range(n1,0,-1):
    if n1%i==0 and n2%i==0:
        print(i)
        break

        
        
    
