while True:
  sum = 0
  course_num = int(input("Enter the amount of courses: "))
  course_num_copy = course_num   # i wish i hadnt to use this line !i have no better ideas
  if course_num == 0 :
    break
  while course_num != 0 : 
    sum += float(input("Enter your score: "))
    course_num -=1
  average = sum/course_num_copy
  print("Your average of scores is",average)  
