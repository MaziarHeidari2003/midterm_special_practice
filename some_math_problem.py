#  we are going to find the perfect numbers lower than n and print them in a weird way!

n = int(input("Enter: "))
i = 1 
while i <= n :
  m = 1
  sum = 0
  while m <= i :
    if i % m == 0 :
      sum += m
    m += 1
  if (sum == 2 * i) :
    rev = 0
    k = i 
    while k != 0 :
      digit = k % 10
      rev = rev * 10 + digit    
      k //= 10
    print(rev)  
  i += 1

      

