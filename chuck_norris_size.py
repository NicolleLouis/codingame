b="".join(list(map(lambda i:bin(ord(i))[2:].zfill(7),input())))
t=[]
x=b[0]
for i in b[1:]+"a":
    if i!=x[0]:
        t+=[x]
        x=""
    x+=i
print(" ".join(list(map(lambda a:' '.join([["0","00"][a[0]!="1"],"".zfill(len(a))]),t))))