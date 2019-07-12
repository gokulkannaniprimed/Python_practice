import re
string="if a==b && c==d || &&& && |||"
list1=string.split(' ')
for i in list1:
    if i=='&&':
        matched=re.sub(r'&&','and',i)
        print(matched, end=" ")
    elif i=='||':
        matched2=re.sub(r'\|\|','or',i)
        print(matched2, end=" ")
    else:
        print(i, end=" ")