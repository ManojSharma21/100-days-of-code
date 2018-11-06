n=int(input("Enter the number:"))
p=True
i=n-1
for i in range(i,2,-1):
    if n%i!=0:
        pass
         
    else:
        p=False
        
if p==True:
    print ("number is prime")
else:
    print ("number is not prime")
        
        
    
