#HannaGao S3C3 option1 ordered list

null=-1

class node:
    def i(s):
        s.d=''
        s.p=''

def newlist():
    l=[node()for i in range(6)]
    sp=null
    fp=0
    for i in range(5):
        l[i].p=i+1
    l[5].p=null
    return(l,sp,fp)

def add(l,sp,fp,newi):
    if fp==null:
        print('no space')
    else:
        newa=fp
        l[newa].d=newi
        fp=l[fp].p
        p=null
        t=sp
        while t!=null and l[t].d<newi:
            p=t
            t=l[t].p
        if p==null:
            l[newa].p=sp
            sp=newa
        else:
            l[newa].p=l[p].p
            l[p].p=newa
    return(l,sp,fp)

def delete(l,sp,fp,item):
    t=sp
    while t!=null and l[t].d!=item:
        p=t
        t=l[t].p
    if t==null:
        print('NA')
    else:
        if t==sp:
            sp=l[sp].p
        else:
            l[p].p=l[t].p
        l[t].p=fp
        fp=t
    return(l,sp,fp)

def find(l,sp,tobefind):
    newa=sp
    while newa!=null and l[newa].d!=tobefind:
        newa=l[newa].p
    if newa==null:
        print('NA')
    else:
        print(newa)

def output(l,sp):
    nexta=sp
    if sp==null:
        print('NA')
    while nexta!=null:
        print(l[nexta].d)
        nexta=l[nexta].p

l,sp,fp=newlist()
newi=12
l,sp,fp=add(l,sp,fp,newi)
newi=113
l,sp,fp=add(l,sp,fp,newi)
newi=56
l,sp,fp=add(l,sp,fp,newi)
newi=19
l,sp,fp=add(l,sp,fp,newi)
newi=1
l,sp,fp=add(l,sp,fp,newi)
output(l,sp)
print('')
item=12
l,sp,fp=delete(l,sp,fp,item)
output(l,sp)
print('')
item=34
l,sp,fp=delete(l,sp,fp,item)
output(l,sp)
print('')
tobefind=113
find(l,sp,tobefind)
tobefind=45
find(l,sp,tobefind)

        
    
