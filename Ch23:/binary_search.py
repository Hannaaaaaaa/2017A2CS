l=[12,19,23,27,33,37,41,45,56,59,60,62,71,75,80,84,88,92,99]
mi=len(l)
si=37
print(mi)
f=False
sf=False
low=0
high=mi-1
while f==False and sf==False:
    m=(low+high)//2
    if l[m]==si:
        f=True
    else:
        if low>high:
            sf=True
        else:
            if l[m]>si:
                high=m-1
            else:
                low=m+1
if f==True:
    print(m+1,si)
else:
    print('-1')
    
            
    
