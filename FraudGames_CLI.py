def menu():
    count = 1
    while(count == 1):
        print("Would you like to play a game")
        answer = input("type y or n\n")
        if (answer == "y"):
            play()
        elif (answer =="n"):
            break
        else:
            print("please enter a valid answer")
            menu()
            
def play():
    print("choices1-2")
    print("Would you like to commit fraud")
    answer = input("type y or n\n")
    if (answer == "y"):
        fraud()
    elif (answer =="n"):
        fighter()
    else:
        print("please enter a valid answer")
        play()
        
def fraud():
    print("choices1-2")
    print("Would you like to commit fraud")
    answer = input("type y or n\n")
    if (answer == "y"):
        fraud1()
    elif (answer =="n"):
        fraud2()
    else:
        print("please enter a valid answer")
        fraud()
        
def fraud1():
    print("choices1-2")
    print("Would you like to commit fraud")
    answer = input("type y or n\n")
    if (answer == "y"):
        fraud1_1()
    elif (answer =="n"):
        fraud1_2()
    else:
        print("please enter a valid answer")
        fraud1()

def fraud2():
    print("choices1-2")
    print("Would you like to commit fraud")
    answer = input("type y or n\n")
    if (answer == "y"):
        fraud2_1()
    elif (answer =="n"):
        fraud2_2()
    else:
        print("please enter a valid answer")
        fraud2()

def fighter():
    print("choices1-2")
    print("Would you like to commit fraud")
    answer = input("type y or n\n")
    if (answer == "y"):
        fighter1()
    elif (answer =="n"):
        fighter2()
    else:
        print("please enter a valid answer")
        fighter()

def fighter1():
    print("choices1-2")
    print("Would you like to commit fraud")
    answer = input("type y or n\n")
    if (answer == "y"):
        fighter1_1()
    elif (answer =="n"):
        fighter1_2()
    else:
        print("please enter a valid answer")
        fighter1()
        
def fighter2():
    print("choices1-2")
    print("Would you like to commit fraud")
    answer = input("type y or n\n")
    if (answer == "y"):
        fighter2_1()
    elif (answer =="n"):
        fighter2_2()
    else:
        print("please enter a valid answer")
        fighter2()

menu()
