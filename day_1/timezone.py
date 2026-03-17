# 10. Determine Time of the Day
# Problem
# Write a program that takes an hour value (0–24) and determines the time of the day category.
# Input
# hour
# Constraints
# - 0 ≤ hour ≤ 24
# Example
# Input: 9
# Output: Morning
# Input: 14
# Output: Afternoon

def timeOfTheDay(n):
  if (n>=6 and n<12):
    print("Morning")
  elif(n>=12 and n<17):
    print("Aternoon")
  elif(n>=17 and n<21):
    print("Evening")
  elif(n>=21 and n<23):
    print("Night")
  elif(n>=0 and n<5):
    print("Early Morning")
n = int(input())
timeOfTheDay(n)