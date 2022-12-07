from math import sqrt
n=int(input("enter a limit:"))
#p=0
for i in range(1000,n):
    if sqrt(i)==int(sqrt(i))and i%2==0:
        print(i)