# Ask for a score
score = float(input("Please give me the score: "))
# Validate that the score is within the allowed range
if 0 > score:
  print("The score is invalid.")
elif score > 100:
  print("The score is invalid.")
# Categorize the given score
elif score < 75:
  print("The score needs Improvement.")
elif 75 <= score <= 79:
  print("The score is satisfactory.")
elif 80 <= score <= 89:
  print("The score is very Satisfactory.")
else:
  print("The score is outstanding.")
