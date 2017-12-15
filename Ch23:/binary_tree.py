#HannaGao s3c3 Option1 Binary tree

null=-1
l=['']

class node:
    def i(s):
        s.d=''
        s.leftp=null
        s.rightp=null

def tree():
    tree=[node()for i in range(10)]
    sp=null
    fp=0
    for i in range(9):
        tree[i].leftp=i+1
    tree[9].leftp=null
    return(tree,sp,fp)

def add(tree,sp,fp,new):
    if repeat(new)==True:
        print('repeat')
    else:
        if fp==null:
            print('NA')
        else:
            newa=fp
            tree[newa].d=new
            fp=tree[newa].leftp
            tree[newa].leftp=null
            tree[newa].rightp=null
            if sp==null:
                sp=newa
            else:
                t=sp
                while t!=null:
                    p=t
                    if tree[t].d>new:
                        turnleft=True
                        t=tree[t].leftp
                    else:
                        turnleft=False
                        t=tree[t].rightp
                if turnleft==True:
                    tree[p].leftp=newa
                else:
                    tree[p].rightp=newa
    l.append(new)
    return(tree,sp,fp,l)

def repeat(new):
    repeat=False
    for i in range(len(l)):
        if l[i]==new:
            repeat=True
    return repeat
    
def find(tree,sp,findi):
    nexta=sp
    while nexta!=null and tree[nexta].d!=findi:
        if tree[nexta].d>findi:
            nexta=tree[nexta].leftp
        else:
            nexta=tree[nexta].rightp
    print(nexta)
    
def output(tree,sp):
    if sp!=null:
        output(tree,tree[sp].leftp)
        print(tree[sp].d)
        output(tree,tree[sp].rightp)


tree,sp,fp=tree()
new=25
tree,sp,fp,l=add(tree,sp,fp,new)
new=12
tree,sp,fp,l=add(tree,sp,fp,new)
new=90
tree,sp,fp,l=add(tree,sp,fp,new)
new=90
tree,sp,fp,l=add(tree,sp,fp,new)
new=56
tree,sp,fp,l=add(tree,sp,fp,new)
new=100
tree,sp,fp,l=add(tree,sp,fp,new)
new=5678
tree,sp,fp,l=add(tree,sp,fp,new)
print('')
findi=75687
find(tree,sp,findi)
print('')
output(tree,sp)


    
        


