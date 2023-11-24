try:
  while True:
    sum = 0
    num = int(input("Enter the number: "))
    if num == 0 :
      break
    else:
      while num >0:
        sum += num%10
        num  //=10 
    print(f"The sum of the digits is: {sum}")  
except ValueError as e:
  print(f"Dude! take care of your inputs: {e}")    

except Exception as e:
  print(f"Something is wrong with your input: {e}")
finally:
  print("Thanks for using our facilities")  
