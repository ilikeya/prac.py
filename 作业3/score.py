m = int(input("Enter your student numbers: "))
while m>0:
    def main():
        score =float(input("Enter your score: "))
        print(get_score(score))
    def get_score(score):
        if score < 0 or score > 100:
            return "Invalid score"
        elif score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Possibal"
        else:
            return "Bad"
    m=m-1
    main()
