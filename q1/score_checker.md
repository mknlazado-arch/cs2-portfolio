# Part 1 - Analyze The Logic

Input:                  What information does the program need?      The score of a student
Boundary:               What is the minimum valid score?             0
Boundary:               What is the maximum valid score?             100
Possible Outputs:       What outcomes can the program produce?       Invalid Score, Needs improvement, Satisfactory, Very Satisfactory, and Outstanding
Selection Pattern:      Which part uses a boundary condition?        The Validation if the score passes the allowed range of the score
Selection Pattern:      Which part uses multiple decision paths?     The categorization of the given score

# Part 2 - Create The Flowchart

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/dae0d385-31c2-46e0-9eab-3c72673da7bf" />

# Part 3 - Write the Pseudocode

Start
Declare Real score
Input score
If 0 > score
     Output "INVALID"
False:
     If score > 100
          Output "INVALID"
     False:
          If score < 75
               Output "NEEDS IMPROVEMENT"
          False:
               If score 75 <= score <=
                    Output "SATISFACTORY"
               False:
                    If 80 <= score <= 89
                         Output "VERY SATISFACTORY"
                    False:
                         Output "OUTSTANDING"
                    END
                 END
             END
         END
     END
  END

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/2f1926b8-90e3-48c7-9f4e-dfa2e2279342" />

# Part 4 - Clean Code Implementation
/

# Part 5 - Test The Program

Test      Input     Purpose                          Expected Output        Actual Output          Result

1          -1       Below Minimum                    Invalid                Invalid                PASS
2           1       Minimum Boundary                 Needs Improvement      Needs Improvement      PASS
3          74       Below Satisfactory Boundary      Needs Improvement      Needs Improvement      PASS
4          75       Satisfactory Boundary            Satisfactory           Satisfactory           PASS
5          80       Very Satisfactory Boundary       Very Satisfactory      Very Satisfactory      PASS
6          90       Outstanding Boundary             Outstanding            Outstanding            PASS
7          100      Maximum Boundary                 Outstanding            Outstanding            PASS
8          101      Above Maximum                    Invalid                Invalid                PASS

TESTING REFLECTION:
1. It's important to test the values 0 and 100 to make sure it is still counted as a valid score. 
2. I also checked the values -1 and 101 to check if it resulted as an invalid score. 
3. The test that helped me understand the boundary conditions the most is the 0 and 100 values.
4. No.

REFLECTION:
1. The selection structures made the program more useful by helping in sorting the category of the score given.
2. Proper commenting and readable formatting helped in organizing the program and helping me identify what part of the program i am on.
3. It is useful to use a flowchart and psuedocode first before writing the code because the flowchart and psuedocode serves as the outline of the python code. Helping us be more organized in writing the code.












          
