print("Form of quadratic equation:  ax^2 + bx + c = 0" ,end="\n ")
a=int(input("Enter the coefficient of x^2"))
b=int(input("Enter the coefficient of x"))
c=int(input("Enter the coefficient of c"))
if b**2-4*c*a>0:
    print("nature of quadratic equation is real and unequal")
if b**2-4*c*a<0:
    print("nature of quadratic equation is real and equal")
if b**2-4*c*a==0:
    print("nature of quadratic equation is real and imaginary")


        
        



