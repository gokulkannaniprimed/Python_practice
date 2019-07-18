postal_code=input()
f=0
count=1
new_post=[x for x in postal_code]
print(new_post)
if int(postal_code)<999999 and int(postal_code)>100000:
    for i in range(2,len(new_post)):
        if new_post[i]==new_post[i-2]:
            if count>1:
                print('invalid')
                f=1
                break
            count+=1
    if f==0:
        print('valid')
else:
    print('invalid')