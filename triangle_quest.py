import math
N=int(input())
for i in range(1,N):
    mul=int((math.pow(10,i)-1)/9)*i
    print(mul)