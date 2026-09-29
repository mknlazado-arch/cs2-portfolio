# Fundamentals of Cybersecurity and Data Privacy
**Activity:** PSHS Secure Club Registration System
**Name:** Maryanne Kristine N. Lazado
**Section:** Dahlia
**Quarter:** 1
---
## Activity Overview
In this activity, I analyzed a cybersecurity threat and developed secure data-capture rules for a simple
PSHS Club Registration System.
The goal is to create a program that collects only necessary information and accepts only correct,
expected, and appropriate input.
---
# Part A - Cybersecurity Threat Analysis
## Assigned Case

**Case Number: 2** 
**Case Title: Fake Prize**
> A student supposedly wins a prize but must provide personal and payment information.
---
### 1. What cybersecurity threat is shown?
> It requires personal and payment information
### 2. What warning signs make the situation suspicious?
> It requires personal and payment information
### 3. What may be affected?
Check or describe all that apply:
/ - Data
- Account
- Application
- Device
- Network
/ - Financial information
> because it requires personal and payment information putting our financial information and data at risk
### 4. What information could be exposed or misused?
> financial information
### 5. What should the user do to reduce the risk?
> Do not engage
---
# Part B - Data Privacy and Secure Data Capture
A proposed Club Registration System wants to collect the following information.
Determine whether each item is really necessary.
| Data | Collect / Do Not Collect | Reason |
|---|---|---|
| Student Name | Collect | to know the name of the person |
| Section | Collect | to know the section of the person |
| Club Choice | Collect | to know the wanted club of the person |
| School Email | Collect | to know the school email of the person |
| Attendance Status | Collect | to know if the person attends the club |
| Password | Do not collect | we do not need the password |
| OTP | Do not collect | we do not need the OTP |
| Home Address | Do not collect | we do not need the Home Address |
| Parent Bank Account | Do not collect | we do not need the parent's back account |
---
## Privacy Question
Why is it safer to collect only information that the program actually needs?
> So the student/person has a safer environment to be in with minimal risks as possible
---
# Part C - Security-Focused Validation Rules
Complete the table before writing your program.
| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error
Message |
|---|---|---|---|---|---|
| Student Name | The name of the person | Someone could try to impersonate the person | [Blank] | Must have an answer | Blank |
| Section | The section of the person | Someone could try to impersonate the person | not specified by the teacher | Must only be the sections specified by the teacher. | not specified by the teacher |
| Club Choice | The club choice of the person | Someone could try to impersonate the person | not included in the club list | Must be included in the club list | not included in the club list |
| School Email | The school email of the person | Someone could try to impersonate the person | does not have the "@" and "." sign | must have the "@" and "." sign  | does not have the "@" and "." sign |
| Attendance Status | The attendance status of the person | Someone could try to impersonate the person | [Blank] | Is not either absent, present, or late | Is not either absent, present, or late |
---
## Secure Data Capture Questions
### 1. What should your program accept?
> right answers.
### 2. What should your program reject?
> Wrong answers.
### 3. How do your validation rules help reduce incorrect or unsafe input?
> It helps by checking and making sure and making rules if the input is correct or safe.
---
# Part D - Secure Program Implementation
## Program
Create a simple **PSHS Club Registration System**.
The program should collect only:
- Student Name
- Section
- Club Choice
- School Email

- Attendance Status
It should **not request passwords, OTPs, banking information, or unnecessary personal information**.
---
## Source Code File
[`secure_registration.py`](secure_registration.py)
---
## Final Code
```python
# # Get the needed information.
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
```
---
## Security Practices Applied
### Required Input
> I copied my previous code
### Allowed Values
> section, club, and attendance
### Format Check
> The email must contain the "@" and "." symbol
### Error Messages
> It helps us correct our work
### Data Minimization
> passwords, OTPs, banking information, or unnecessary personal information because it is not needed and it helps keep the students safe from possible threats
---
# Part E - Testing and Reflection
## Testing
| Test | Input Situation | Expected Output | Actual Output | Result |
|---:|---|---|---|---|
| 1 | All data valid | Valid | Valid | PASS |
| 2 | Blank student name | Invalid | Invalid | PASS |
| 3 | Invalid section | Invalid | Invalid | PASS |
| 4 | Invalid club choice | Invalid | Invalid | PASS |
| 5 | Email missing `@` | Invalid | Invalid | PASS |
| 6 | Email missing `.` | Invalid | Invalid | PASS |
| 7 | Invalid attendance status | Invalid | Invalid | PASS |
| 8 | Different valid inputs | Valid | Valid | PASS |
Use:
- **PASS** if the actual result matches the expected result.
- **FAIL** if it does not.
---
# Reflection
### 1. What is one cybersecurity threat that can affect an application or user?
> Asking for unnecessary information from the user
### 2. How can users reduce the risk of phishing or suspicious messages?
> Become more mindful and do not give your info away
### 3. How can validation rules improve the security of user input?
> Its helps by protection the user from potential phishing
### 4. Why should a program avoid collecting unnecessary personal information?
> it helps protect the user from potential phishing
### 5. How did SG7's input validation concepts become security practices in SG8?
> It helped in the application part
---
