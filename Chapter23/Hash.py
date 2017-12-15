#HannaGao option1 hash table


l=[(-1)for i in range(10)]

def hasha(key):
    a=key%10
    return a

def insert(key):
    a=hasha(key)
    while l[a]!=-1:
        a+=1
        if a>9:
            a=0
    print(a)
    l[a]=key

def find(searchk):
    a=hasha(searchk)
    i=1
    while l[a]!=searchk and l[a]!=-1 and i==len(l):
        a+=1
        if a>9:
            a=0
        i+=1
    if i==10:
        print('does not exist')
    if l[a]!=-1:
        print(a,l[a])

key=25
insert(key)
key=26
insert(key)
key=36
insert(key)
searchk=36
find(searchk)
searchk=37
find(searchk)
print(l)

    
    
