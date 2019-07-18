import re
list1=[]
n=int(input())
for i in range(n):
    current=input()
    matched=re.search('^\w@[\d|a-z|A-Z]+\.[a-z]{1,3}$',current)
    if matched!=None:
        list1.append(current)
list1.sort
print(list1)