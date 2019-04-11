# Katelyn Dever HW4 Part 1

def Introduction():
    print("This program evaluates a job candidate and prints a result.\n")

def getUserQ1():
    # 4.2.1 - ask the user about a particular skill, store as a variable
    q1ans = input("Are you skilled in algorithm analysis(y/n)? ")
    if q1ans == 'n':
        print("We are sorry, you are not eligible for this position")
        x = input("Press <Enter> to exit")
        exit()

def getUserAnswers():
    # 4.2.2 - gets users input of years of experience, evals, and stores
    userExp = eval(input("How many years of work experience do you have? "))
    # 4.2.3 - gets user input y/n on Python skill and stores
    userPython = input("Do you have Python programming experience (y/n)? ")
    
    # 4.2.4 - if/else statements to evaluate and print qualification
    if userPython == "y":
        # yes python, at least 2 years exp
        if userExp >= 2:
            print("\n You are an excellent candidate with Python skill and")
            print(" at least 2 years of work experience. Congratulations!")
        # yes python, less than 2 years exp
        else:
            print("\n While you have Python skills, you do not have at least")
            print(" 2 years of work experience.  You are not qualified.")
    else:
        # no python, at least 4 years exp
        if userExp >= 4:
            print("\n Although you don't have Python skill, you have enough")
            print(" work experience and are qualified for this position.")
            print(" Congratulations!")
        # no python, less than 4 years exp
        else:
            print("\n Since you do not have Python skill or at least 4 years")
            print(" of work experience, you are not qualified.")

def main():
    Introduction()
    getUserQ1()
    getUserAnswers()
    
main()
    
