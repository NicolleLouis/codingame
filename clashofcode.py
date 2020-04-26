d=input()
r=""
d=d.split(" ")
for e in d:
    c=e[len(e)-1]
    e=e.replace(c,"")
    for e in range(int(e)):
        r+=c
print(r)