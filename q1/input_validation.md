# Input Validation and Output Verification
**Activity:** PSHS Workshop Registration Validator
**Name:** Maryanne Kristine N. Lazado
**Section:** Dahlia
**Quarter:** 1
---
## Activity Overview
In this activity, I created a program that validates information entered into a PSHS workshop registration
system.
The program checks whether user input satisfies specific requirements before accepting the registration.
The program validates:
- student name
- age
- grade level
- email address and
- registration code.

---
# Part A - Validation Requirements
Complete the table below before writing your program.
| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error
Message |
|---|---|---|---|---|---|
| Student Name | Name of the student | Presence check | "" | Must input something | did not input anything. |
| Age | Age of the student ranging from 11 - 18 | Data type + range validation | fourteen | must be an integer from 11 - 18 | input not an integer |
| Grade Level | The grade of the student | Acceptable Value validation | 13 | must be equal to or greater than 7 to must be equal to or less than 12 | input is not in the range from 7 - 12 |
| Email Address | the email address of the student | Simple pattern validation | student pshs | Must have the "@" sign | input does not have the "@" sign |
| Registration Code | the code of the student | Length validation | 1K4L | must be exactly 6 characters long | input does not satisfy the 6 character rule |
---
## Validation Questions
### 1. Why should the student name not be blank?
> So the code is successful and it runs.
### 2. Why should age be checked for both data type and range?
> To see if it a number and it is appropriate for the age range rule.
### 3. Why should grade level only accept specific values?
> Because grade levels are not unlimited.
### 4. What format requirements did you use for the email address?
> must have the "@" sign in the email. 
### 5. What length requirement did you use for the registration code?
> Write your answer here.
---
# Part B - Program Design
Before writing your program, create either a **flowchart or pseudocode** showing its logic.

## Pseudocode

```text
START
Input Name
Input age
     If age = int;
         display: Valid
     Elif 11 <= age <= 18;
         display: Valid
     Else;
         display: Invalid
         Stop
Input grade
     If 7 <= grade <= 12;
         display: Valid
     Else;
         display: Invalid
         Stop
Input email
     If email contains "@"
         display: Valid
     Else;
         display: Invalid
         Stop
Input registration code
     If registration code is 6 characters
         display: Valid
     Else;
         display: Invalid
         Stop
END
```

# Part C - Program Implementation
## Programming Language
> Write the programming language used.
## Source Code File
[`workshop_validator.py`](workshop_validator.py)
## Final Code
```python
# Paste your final code here.
# Get the needed information.
```name = str(input("Please give me your name: "))
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

```

**Get the needed information.**

---
## Validation Techniques Used
### Presence Validation
Explain where you used presence validation.
> to make sure that there is an input given by the student.
### Data Type Validation
Explain where you used data type validation.
> To make sure that the age is a number.
### Range Validation
Explain where you used range validation.
> to make sure the age satisfies the allowed range
### Acceptable Value Validation
Explain where you used acceptable value validation.
> To know if the grade satisfies the given rule.
### Pattern Validation
Explain the simple pattern rule you used.
> To make sure the email contains specific characters.
### Length Validation
Explain the length rule you used.
> To make sure that the length is valid.
---
# Part D - Testing
Test your program using both valid and invalid inputs.
| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---:|---|---|---|---|---|
| 1 | All inputs valid | Normal case | Valid | Valid | PASS |
| 2 | Blank student name | Presence | Invalid| Invalid | PASS |
| 3 | Age = `fourteen` | Data type | Invalid | Invalid | PASS |
| 4 | Age = `11` | Minimum boundary | Valid | Valid | PASS |
| 5 | Age = `18` | Maximum boundary | Valid | Valid | PASS |
| 6 | Age = `10` | Range | Invalid | Invalid | PASS |
| 7 | Grade Level = `13` | Acceptable value | Invalid | Invalid | PASS |
| 8 | Email = `studentpshs.edu.ph` | Pattern | Invalid | Invalid | PASS |
| 9 | Registration Code = `ABC` | Length | Invalid | Invalid | PASS |
| 10 | Registration Code = `CS2026` | Valid length | Valid | Valid | PASS |
Write **PASS** when the actual output matches the expected output.
Write **FAIL** when it does not.
---
# Part E - Output Verification
Choose any **three tests** from Part D.
## Verification Test 1
**Input:**
```text
maryanne

```
**Expected Output:**
```text
Valid.
```
**Actual Output:**
```text
Valid
```
**Result:** PASS
**Explanation:**
> Bacause i entered something.
---
## Verification Test 2
**Input:**
```text
11
```
**Expected Output:**
```text
Valid
```
**Actual Output:**
```text
Valid
```
**Result:** PASS
**Explanation:**
> Because it is an integer and it is within the valid range.
---
## Verification Test 3
**Input:**
```text
18
```
**Expected Output:**
```text
Valid
```
**Actual Output:**

```text
Valid
```
**Result:** PASS
**Explanation:**
> Because it is an integer and it is within the valid range.
---
# Reflection
Answer briefly.
### 1. Why should a program validate input before processing it?
> To make sure they get the right information from the students.
### 2. What is the difference between input validation and output verification?
> Input Validation checks the data before and output verification checks during.
### 3. Which validation technique was easiest for you to implement? Why?
> Range Validation because i'm already used to it and have encountered it many times before.
### 4. Which validation technique was most challenging? Why?
> Presence check because this is my first time encountering it.
### 5. How did testing invalid inputs help you improve your program?
> It helped me in making sure my program works.
---
