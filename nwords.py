#n=int(input())
words=['abc','bcd','efg','abc']
rep={}
#for i in range(0,n):
#    words.append(input())
for i in words:
    if i not in rep.keys():
        rep[i]=1
    else:
        rep[i]+=1
print(len(rep))
print(rep.values())