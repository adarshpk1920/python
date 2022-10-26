import math
#print("area of the triengle three sides")
a=int(input("enter the area of triengle"))
b=int(input("enter the area of triengle"))
c=int(input("enter the area of triengle"))
s=a+b+c/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of the triengle is",area)