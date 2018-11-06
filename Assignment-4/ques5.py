def coprime(N1,N2):
    while True:
        for i in range(2,N1):
            if (N1)%i==0 and (N2)%i==0:
                N1+=1
                return(False)
        else:  
            return (True)
    
print("Enter two numbers to check co-prime numbers ")
N1=int(input("Enter number 1: "))
N2=int(input("Enter number 2: "))
if(N1<N2):
    pass
else:
    N1=N1+N2
    N2=N1-N2
    N1=N1-N2
l=coprime(N1,N2)
if l==True:
    print("%d and %d are co-prime"%(N1,N2))
else:
    print("%d and %d are not co-prime"%(N1,N2))
