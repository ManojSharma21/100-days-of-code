
num=int(input("Enter any number:"))
factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

fact=factorial
digit=0
for i in range(factorial):
    if(factorial%10==0):
        digit=digit+1
        factorial=factorial/10
        
      

print("Zeros:",digit,"in",fact)
