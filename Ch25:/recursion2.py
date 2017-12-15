#HannaGao
#recursion-2

def groupSum(x,y,z):
    if z==0:
        return True

    if x==len(y):
        return False

    return groupSum(x+1,y,z-y[x]) or groupSum(x+1,y,z)

def groupSum6(x,y,z):
    if x==len(y):
        return (z==0)

    if y[x]==6:
        return groupSum6(x+1,y,z-6)
    else:
        return groupSum6(x+1,y,z-y[x]) or groupSum6(x+1,y,z)

def groupNoAdj(x,y,z):
    if z==0:
        return True
    if x==len(y):
        return False
    if x==len(y)+1:
        return False

    return groupNoAdj(x+2,y,z-y[x]) or groupNoAdj(x+1,y,z)
       
def groupSum5(x,y,z):
    if z==0:
        return True
    if x==len(y):
        return False

    if y[x]%5==0:
        if x==len(y)-1:
            return groupSum5(x+1,y,z-y[x])
        else:
            if y[x+1]==1:
                return groupSum5(x+2,y,z-y[x])
            else:
                return groupSum5(x+1,y,z-y[x])
    else:
        return groupSum5(x+1,y,z-y[x]) or groupSum5(x+1,y,z)

def groupSumClump(x,y,z):
    if z==0:
        return True
    if x==len(y):
        return False

    a=0
    b=0

    for i in range(x,len(y)-1):
        if y[i]==y[i+1] or y[i-1]==y[i]:
            a=a+y[i]
            b+=1
            
    if a>0:
        return groupSumClump(x+b,y,z-a) or groupSumClump(x+b,y,z)
    else:
        return groupSumClump(x+b,y,z-a) or groupSumClump(x+b,y,z)


def helppp(start,x,s1,s2):
    if start==len(x):
        return s1==s2
    
    return helppp(start+1,x,s1+x[start],s2) or helppp(start+1,x,s1,s2+x[start])
    
def spiltArray(x):
    return helppp(0,x,0,0)

def helper(x,y,s1,s2):
    if x==len(y):
        return (s1%10==0) and (s2%2==1)

    return helper(x+1,y,s1+y[x],s2) or helper(x+1,y,s1,s2+y[x])

def spiltOdd10(y):
    return helper(0,y,0,0)

def helper2(x,y,s5,s3):
    if x==len(y):
        return (s3==s5)
    if y[x]%5==0:
        return helper2(x+1,y,s5+y[x],s3)
    else:
        if y[x]%3==0:
            return helper2(x+1,y,s5,s3+y[x])
        else:
            return helper2(x+1,y,s5+y[x],s3) or helper2(x+1,y,s5,s3+y[x])
    
    

def spilt53(y):
    return helper2(0,y,0,0)
    
x=spilt53([3,5,5,1,2])
print(x)
    
