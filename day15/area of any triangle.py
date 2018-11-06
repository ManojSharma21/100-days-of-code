from math import sqrt 
n=int(input("Enter side 1"))
m=int(input("Enter side 2"))
o=int(input("Enter side 3"))
s=(n+m+o)/2
area=sqrt(s*(s-n)*(s-m)*(s-o))
print(area)
