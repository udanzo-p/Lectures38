import math
k=int(input())
target=int(input())
print("To find largest digit no. divisible by ",target)
pow=math.pow
a=(pow(10,k)-1)
x=1
while(x):
    x=a%target
    if(x==0):
        print("The largest no. divisible by  is ",target,a)
    else:
        a=a-1
        
    