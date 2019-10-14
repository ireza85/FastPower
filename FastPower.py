base=1000000000

x=int(raw_input('Input first number\n'))

y=int(raw_input('Input second number\n'))

def BinPow(a, n):
 res=[1]
 b=[a % base]
 while (n):
     if (n & 1):
         res = map(lambda x, y: x*y, res, b)
         n-=1
     else:
         n >>= 1
         b =  map(lambda x: x*x, b)
 return res

if(len(str(x)) < 4):
    print x**y
elif(len(str(x)) >= 4):
    print BinPow(x,y)





