array1=input("enter word 1:")
array2=input("enter word 2:")
array3=input("enter word 3:")
print("In dictionary order:")
if array1<array2 and array1<array3:
    print(array1)
    if array2<array3:
        print(array2)
        print(array3)
        
    else:
        print(array3)
        print(array2)
else:
    if array2<array3:
        print(array2)
        print(array3)
        print(array1)
        
    else:
        print(array3)
        print(array2)
        print(array1)
    
        
