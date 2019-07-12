import re

list1=[]
card_number="4455667767495369"
matcher1=re.search("[456]\d{3}\d{4}\d{4}\d{4}",card_number)
matcher2=re.search("^[456]\d{3}-\d{4}-\d{4}-\d{4}",card_number)
k=0
if matcher1!=None or matcher2!=None:
    for i in card_number:
        if i!='-':
            list1.append(i)
    count=0
    for i in range(4,16):
        if int(list1[i])==int(list1[i-1]):
            if int(list1[i])==int(list1[i-2]):
                if int(list1[i])==int(list1[i-3]):
                    print('Invalid')
                    k=1
                    break
else:
    k=1
    print('Invalid')
if k==0:
    print('Valid')
