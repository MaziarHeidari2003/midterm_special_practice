try:
    n = int(input("How many numbers are you going to use? "))
    m = n

    #i wish i knew a way so that i could do something else rather than making a copy of n . becouse i cant use the value of n after teh loop , its 0!!!!

    sum = 0
    while n !=0:
      number = int(input("Enter the number: "))
      sum += number
      n -= 1
    average = sum/m 
    print(average)

except ZeroDivisionError as e:
  print(f"Do you even know math? : {e}")
except ValueError as e:
  print(f"Please watch your inputs : {e}")  
except Exception as e:
  print(f"Something went wrong dude {e}")  
finally:
  print("The code ran smoothly")  