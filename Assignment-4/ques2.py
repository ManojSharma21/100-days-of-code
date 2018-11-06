n=int(input("Enter the number:"))
if n==1:
    print("2")
if n==2:
    print("3")
if n==3:
    print("5")
    
while True:
    for i in range(2,n):
        if (n+1)%i==0:
            n=n+1         
    else:
        print ("Next prime number:",n+1)
        break
        
        
        
    
