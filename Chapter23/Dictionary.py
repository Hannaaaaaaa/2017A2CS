#HannaGao option1 Dictionary


class node:
    def __init__(s):
        s.key=''
        s.value=''

l=[(node())for i in range(26)]

def hasha(key):
    a=ord(key[0])-65
    return a

def insert(key,value):
    a=hasha(key)
    while l[a].key!='':
        a+=1
        if a>25:
            a=0
    print(a)
    l[a].key=key
    l[a].value=value

def find(searchk):
    a=hasha(searchk)
    i=1
    while l[a].key!=searchk and l[a].value!='' and i<len(l):
        a+=1
        if a>25:
            a=0
        i+=1
    if i==26:
        print('does not exist')
    if l[a].key!='':
        print(a,l[a].key,l[a].value)
        


def output():
    for i in range(len(l)):
        if l[i].key!='':
            print(l[i].key,'=',l[i].value)

key='CU'
value='control unit'
insert(key,value)
key='SP'
value='Start Pointer'
insert(key,value)
key='LG'
value='logic Gate'
insert(key,value)
output()
print('')
key='SP'
find(key)
key='A'
find(key)



    
    
