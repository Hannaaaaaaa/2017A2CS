#HannaGao S3C3 queue

null=-1


class node:
    def i(self):
        self.d=''
        self.p=''

def stack():
    stack=[node()for i in range(8)]
    sp=null
    ep=null
    fp=0
    for i in range(7):
        stack[i].p=i+1
    stack[7].p=null
    return(stack,sp,fp,ep)

def push(stack,sp,fp,ep,new):
    if fp!=null:
        newa=fp
        stack[newa].d=new
        fp=stack[fp].p
        stack[newa].p=null
        if ep==null:
            sp=newa
        else:
            stack[ep].p=newa
        ep=newa
    else:
        print('NA')
    return(stack,sp,fp,ep)

def pop(stack,sp,fp,ep):
    nexta=sp
    if stack[sp].p==null:
        print('NA')
    else:
        temp=stack[sp].p
        if stack[sp].p==null:
            ep=null
        stack[sp].p=fp
        fp=sp
        sp=temp
    return(stack,sp,fp,ep)

def output(stack,sp):
    nexta=sp
    if nexta==null:
        print('NA')
    while nexta!=null:
        print(stack[nexta].d)
        nexta=stack[nexta].p


stack,sp,fp,ep=stack()
new=34
stack,sp,fp,ep=push(stack,sp,fp,ep,new)
new=56
stack,sp,fp,ep=push(stack,sp,fp,ep,new)
output(stack,sp)
print('')
new=78
stack,sp,fp,ep=push(stack,sp,fp,ep,new)
output(stack,sp)
stack,sp,fp,ep=pop(stack,sp,fp,ep)

output(stack,sp)
print('')




    

