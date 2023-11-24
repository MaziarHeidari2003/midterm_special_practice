a = float(input("Einter an amount for alpha: "))
x = int(input("Enter an amount for x: "))
n = int(input("Enter an amount for n: "))
m = 2*n-1
sign = -1
sum = 0
while n != 0:
  z = True
  y = 1 
  while z :
    if m == 0 or m == 1 :
      z= False
    else:
      y *= m*(m-1)
      m -=2  
    sign *=-1
    sum += (x**(2*n-1))*(sign)/y
    n -= 1
    if sum< a :
      n = 0 

print(sum)
