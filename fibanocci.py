n=int(input("enter your size: "))
t1=0
t2=1
if n==1:
    print(t1)
elif n==2:
    print(t2)
else:
   for i in range(n):
      t3=t1+t2
      t1=t2
      t2=t3
      print( t3 )