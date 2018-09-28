while(1):
    n=int(input("Enter a number:"))
    def isPrime( n ): 
      
 
        if n <= 1: 
            return False 
        for i in range(2, n): 
            if n % i == 0: 
                return False
      
        return True
  
    def isEmirp( n): 
       
        n = int(n) 
        if isPrime(n) == False: 
            return False 
        rev = 0
        while n != 0: 
            d = n % 10
            rev = rev * 10 + d 
            n = int(n / 10) 
          
    
        return isPrime(rev) 
  
    if isEmirp(n): 
        print("Yes") 
    else: 
        print("No") 
      
