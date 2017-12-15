#HannaGao S3C3 stack

null=-1


class node:
    def i(self):
        self.d=''
        self.p=''

def stack():
    stack=[node()for i in range(6)]
    sp=null
    fp=0
    for i in range(5):
        stack[i].p=i+1
    stack[5].p=null
    return(stack,sp,fp)

def push(stack,sp,fp,new):
    newa=fp
    fp=stack[fp].p
    stack[newa].d=new
    stack[newa].p=sp
    sp=newa
    return(stack,sp,fp)

def pop(stack,sp,fp):
    fp=sp
    sp=stack[sp].p
    return(stack,sp,fp)

def output(stack,sp):
    nexta=sp
    if nexta==null:
        print('no')
    while nexta!=null:
        print(stack[nexta].d)
        nexta=stack[nexta].p


stack,sp,fp=stack()
new=10
stack,sp,fp=push(stack,sp,fp,new)
output(stack,sp)
print('')
new=12
stack,sp,fp=push(stack,sp,fp,new)
output(stack,sp)
print('')
new=2
stack,sp,fp=push(stack,sp,fp,new)
output(stack,sp)
print('')
stack,sp,fp=pop(stack,sp,fp)
output(stack,sp)
print('')
stack,sp,fp=pop(stack,sp,fp)
output(stack,sp)

    

