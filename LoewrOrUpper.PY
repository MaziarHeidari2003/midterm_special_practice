letter = ''
while letter != '!':
  letter = input("Enter your letter: ")
  if 'a'<= letter <= 'z':
    print("Lower Case")
  if 'A'<= letter <= 'Z':
      print("Upper Case")   

#so lets start prompting the user for an input and see if its lower case or upper case and have a condition to end the loop