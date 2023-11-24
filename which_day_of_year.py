"""
while True:
  first_day = input("Which day of the week is the first day of the year? ")
  if first_day == '0':
    break
  nth_day = int(input("Enter the specific day of the year from 1 to 366: "))
  days_after_first_day = nth_day % 7
  match days_after_first_day:
    case 0:
      print("That day would be {fist_day}")

  """

# i think i should use arrays or lists for this problem so i we will take care of it later