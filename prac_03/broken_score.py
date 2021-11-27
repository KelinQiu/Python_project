def main():
    score=float(input("Enter score: "))
    print(determine_score(score))

def determine_score(score):
    if score<0 or score>100:
        return "Invalid score"
    elif score>=90:
        return "Excellent"
    elif score>=50:
        return "Pass"
    else:
        return "Bad"
main()