#Trimorphic numbers
count = 0
num = int(input("Enter a number "))
num1=num
while (num > 0):
  num = num//10
  count = count + 1

  
cube=num1**3
y=10**count
if(cube%y==num1):
    print("True")
else:
    print("False")
