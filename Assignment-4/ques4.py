def nextPrime(num):
    if num==1:
        return(2)
    while True:
        for i in range(2,num):
            if (num)%i==0:
                num+=1
                break
        else:
            return (num)

def primeProducer(N1,N2):
    while True:
        if(N1<N2):
            N1=nextPrime(N1)
            if(N1<N2):
                yield N1
                N1+=1
        else:
            break
        
    
print("Enter two numbers to print prime numbers between them")
N1=int(input("Enter number 1: "))
N2=int(input("Enter number 2: "))
l=[x for x in primeProducer(N1,N2)]
print(l)

                
