# Get the needed information.
name = str(input("Please give me your name: "))
while name.strip() == "":
    print("Student name is required.")
    name = input("Please give me your name: ")
    
print("Valid.")
section = str(input("Please enter your section: "))
if section == "Dahlia":
   print("Valid.")
elif section == "Sampaguita":
   print("Valid.")
elif section == "Ilang Ilang":
   print("Valid.")
elif section == "Rosal":
   print("Valid.")
else:
  print("Invalid.")

club = str(input("Please enter your club choice: "))
if club == "Robotics":
   print("Valid.")
elif club == "Science":
   print("Valid.")
elif club == "Mathematics":
   print("Valid.")
elif club == "Programming":
   print("Valid.")
else:
  print("Invalid.")

email = str(input("Please enter your school email: "))
if "@" not in email or "." not in email:
  print("Invalid.")
else:
  print("Valid.")

attendance = str(input("Please enter the attendance of the student: "))
if attendance == "Present":
   print("Valid.")
elif attendance == "Absent":
   print("Valid.")
elif attendance == "Late":
   print("Valid.")
else:
  print("Invalid.")

print("Name: ", name)
print("Section: ", section)
print("Club: ", club)
print("School Email: ", email)
print("Attendance Status: ", attendance)
print("If even one of the requirements is invalid, please retry.")
print("If all are valid, congratulations! You have successfully registered yourself in a club.")
