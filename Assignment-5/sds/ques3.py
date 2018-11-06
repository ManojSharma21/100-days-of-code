print("The armstrong number upto 1000 are:")

def nextarms(num):
    while num<=1000:
        total=0
        orgi=num
        for i in range(1,leng(orgi)):
            li.append(num%10)
            num=num/10
            for item in li:
                total=total+item**leng(orgi)
            if(total==orgi):
                orgi+=1
                return (num)
                break
        else:
            num+=1
                
            
            


def leng(num):
    l=1
    while(num>=0):
        num=num/10
        l+=1

    return (l)

l=[x for x in nextarms(1)]
print(l)



