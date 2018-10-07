#voodoo prime

def isPrime( n ): 
      
 
        if n <= 1: 
            return False 
        for i in range(2, n): 
            if n % i == 0: 
                return False
      
        return True

voodoo=int(input("Enter the number:"))
ivoodoo=str(1/voodoo)
if str(voodoo) in ivoodoo and isPrime(voodoo):
    print("{} is a Voodoo prime".format(voodoo))
else:
    print("{} isn't a Voodoo prime".format(voodoo))
        


    

