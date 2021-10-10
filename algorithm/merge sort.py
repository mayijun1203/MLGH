l=[3,2,1,5,4,6,7,2,8]

# Divide
a=l[0:int(len(l)/2)]
b=l[int(len(l)/2):]


# Sort
def st(x):
    fn=[]
    tp=x.copy()
    for i in range(0,len(x)):
        pos=0
        for j in range(1,len(tp)):
            if tp[j]<tp[pos]:
                pos=j
        fn.append(tp[pos])
        del tp[pos]
    return fn
        


a=st(a).copy()
b=st(b).copy()


# Merge
df=[]
i=0
j=0
for k in range(0,len(l)):
    if (i<=len(a)-1)&(j<=len(b)-1):
        if a[i]<=b[j]:
            df.append(a[i])
            i+=1
        else:
            df.append(b[j])
            j+=1
    elif i>len(a)-1:
        df=df+b[j:]
        break
    else:
        df=df+a[i:]
        break
        

            


