def nextPrime(num):
    while True:
        num+=1
        for i in range(2,num):
            if num%i==0:
                break
        else:
            return (num)

def primeProducer(N):
    num,count=1,1
    while count<=N:
        num=nextPrime(num)
        yield num
        count+=1
N=int(input("How many prime numbers do you want to produce: "))
l=[x for x in primeProducer(N)]
print(l)

                
