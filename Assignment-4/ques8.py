N=int(input("Enter the number to find the prime factor:"))

def nextprime(num):
    while True:
        for i in range(2,num):
            if num%i==0:
                num+=1
                break
        else:
            return (num)
            

num=2
for i in range(2,N):
    num=nextprime(num)
    if(N%num==0):
        print (num,end=" ")
        num+=1
    else:
        num+=1
