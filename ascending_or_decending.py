n = 0
while n <= 0 :
  n = int(input("Enter how many numbers you want to use: "))
message = "So lets do some calculation with {} numbers!"
print(message.format(n))  

i = 0
num1 = int(input("Enter: "))

dec = False
inc = False
both = True

while i < n - 1 :
  num2 = int(input("Enter: "))
  dif = num2 - num1

  if dif > 0 :
    inc = True
    both = False
  if dif < 0 :
    dec = True
    both = False

  num1 = num2
  i += 1   

if both:
  print("it could be both")
elif inc and dec :
  print("its not incremental or decremental")
elif inc :
  print("its incremental")
else:
  print("decremental")      
