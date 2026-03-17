# 8. Student Grade System
# Problem
# Write a program that determines the grade of a student based on the marks obtained.
# Input
# marks
# Constraints
# - 0 ≤ marks ≤ 100
# Example
# Input: 92
# Output: Grade A

def gradeSystem(marks):
  if (marks>=91):
    print("Grade A")
  elif (marks>=71):
    print("Grade B")
  elif (marks>=51):
    print("Grade C")
  elif (marks>=35):
    print("Grade D")
  else:
    print("Fail")
marks = int(input())
gradeSystem(marks)