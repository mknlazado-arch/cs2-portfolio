# Get the needed information.
name = str(input("Please give me your name: "))
while name.strip() == "":
    print("Student name is required.")
    name = input("Please give me your name: ")
    
print("Valid.")
age = int(input("Please enter me your age: "))
   if 11 <= age <= 18:
   print("Valid.")
else:
  print("Invalid.")
grade = int(input("Please enter your grade level: "))
if 7 <= grade <= 12:
  print("Valid.")
else:
  print("Inavalid.")
email = str(input("Please enter your email address: "))
if "@" not in email or not email.endswith(".pshs.edu.ph"):
  print("Invalid.")
else:
  print("Valid.")
code = str(input("Please enter your registration code: "))
if len(code) != 6:
  print("Invalid.")
else:
  print("Valid.")

print("Name: ", name)
print("Age: ", age)
print("Grade: ", grade)
print("Email address: ", email)
print("Registration Code: ", code)
print("If even one of the requirements is invalid, please retry.")
