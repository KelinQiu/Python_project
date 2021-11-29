"""
CP1404 - Practical 3
Broken program to determine score status
"""

def main():
    score=float(input("Enter score: "))
    print(determine_score(score))

def determine_score(score):
    if score<0 or score>100:
        return "Invalid score"
    elif score>=85:
        return "High Distinction"
    elif score>=75:
        return "Distinction"
    elif score>=65:
        return "Credit"
    elif score>=50:
        return "Pass"
    else:
        return "Fail"
main()

import random
random_score = random.randint(0, 100)
print(f"Score: {random_score}")
print(determine_score(random_score))
