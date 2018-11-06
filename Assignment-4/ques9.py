print("Enter two numbers to find the LCM ")
n1=int(input("Enter  number 1:"))
n2=int(input("Enter  number 2:"))

for i in range(1,n1*n2+1):
    if i%n1==0 and i%n2==0:
        print(i)

        
        
    
