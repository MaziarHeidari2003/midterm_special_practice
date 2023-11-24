conditionCheck = True
while conditionCheck :
  n = int(input("Enter a natural number: "))
  if n !=0 :  
    # We are going to check if the numbers are prime or not and we will continue as long as the input is 0
    cnt = 0
    m =1
    while  m<=n:
      if n%m == 0 :
        cnt +=1
      m += 1
    if cnt > 2 :
      print("Its not a prime number")
    else:
      print("It is actaully a prime number")      
  else:
    conditionCheck = False
    print("Good bye")    