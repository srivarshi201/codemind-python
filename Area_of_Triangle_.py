import math
a,b,c=list(map(int,input().split()))
s=(a+b+c)/2
ar=(s*(s-a)*(s-b)*(s-c))**0.5
re=("{:.2f}".format(ar))
print(re)