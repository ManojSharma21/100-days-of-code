s1=int(input("enter the marks of subject 1:"))
s2=int(input("enter the marks of subject 2:"))
s3=int(input("enter the marks of subject 3:"))
s4=int(input("enter the marks of subject 4:"))
s5=int(input("enter the marks of subject 5:"))
result=((s1+s2+s3+s4+s5)/500)*100
if result >=0 and result <=50:
    print("Fail")
if result >=50 and result <=60:
    print(result,"Division-E")
if  result >=60 and result <=70:
    print(result,"Division-D")
if result >=70 and result <=80:
    print(result,"Division-C")
if result >=80 and result <=90:
    print(result,"Division-B")
if  result >=90 and result <=100:
    print(result,"Division-A")
if result >=100:
    print("Input error")
        
