month=int(input("Enter the month in numberic form:"))
if month>0 and month<8:
    if month==2:
        print(" month %d has 28 days"%(month))
    elif month%2==0 and month!=2:
        print(" month %d has 30 days"%(month))
    else:
        print(" month %d has 31 days"%(month))
if month>7 and month<13:
    if month%2==0:
        print(" month %d has 31 days"%(month))
    else:
        print(" month %d has 30 days"%(month))
        
        



