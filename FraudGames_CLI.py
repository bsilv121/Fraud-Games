from os import system, name

def menu():
    count = 1
    while(count == 1):
        print("Would you like to be a fraudster (a) or a fighter (b)")
        answer = input("type a or b\n")
        if (answer == "a"):
            fraud1()
        elif (answer =="b"):
            fighter1()
        else:
            print("please enter a valid answer")
            menu()
        
def fraud1():
    system('clear')
    print("You are one of the top financial managers at Play the Game Inc. You just recently experienced a rise in the price of your rent at your apartment complex.  You could pitch a fraud scheme to a vendor that you know to overcharge for their products, and you will give them the profit from this fraud.")
    print("\nWould you like to commit fraud?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fraud2()
    elif (answer =="n"):
        fraud9()
    else:
        print("please enter a valid answer")
        fraud1()
        
def fraud2():
    system('clear')
    print("The CFO of the company has started to place greater internal controls upon the various purchases of the company after being pressured by the CEO. You are good friends with the CFO and think you can convince him to be a part of your current fraud scheme")
    print("\nDo you try to convince the CFO?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fraud3()
    elif (answer =="n"):
        fraud4()
    else:
        print("please enter a valid answer")
        fraud2()

def fraud3():
    system('clear')
    print("The CFO is not compliant to your request and puts in a tip to the company tip hotline to report you. You are caught by the fraud fighter (auditor). Go back to the beginning.")
    print("\nDo you want to retry?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fraud1()
    elif (answer =="n"):
        quit()
    else:
        print("please enter a valid answer")
        fraud3()
        
def fraud4():
    system('clear')
    print("You realize that the CFO of the company is very loyal to the company despite their frustrations with the CEO. You decide to commit the fraud with the vendor on your own. You slowly increase the amount of overcharging on the vendor’s products. Money is rolling in like crazy and you are VERY well off now.")
    print("\nDo you buy a new flashy watch you have been waiting for the past year?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fraud5()
    elif (answer =="n"):
        fraud6()
    else:
        print("please enter a valid answer")
        fraud4()
        
def fraud5():
    system('clear')
    print("Your purchase of the watch sparks rumors in the company that you might be colluding with a vendor. The auditors begin to surveil you and see your next purchase of a new Lamborghini. You are caught by the fraud fighter (auditor). Go back to the beginning.")
    print("\nDo you want to retry?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fraud1()
    elif (answer =="n"):
        quit()
    else:
        print("please enter a valid answer")
        fraud5()
        
def fraud6():
    system('clear')
    print("You decide that buying something flashy might alert your coworkers that you are committing fraud. You could launder the stolen money through various dirty restaurants and stores in the area. ")
    print("\nDo you bring the dirty money to these establishments?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fraud7()
    elif (answer =="n"):
        fraud8()
    else:
        print("please enter a valid answer")
        fraud6()

def fraud7():
    system('clear')
    print("You decide to launder the money through the local pizzeria where you know the manager will let you circulate your dirty money to launder it. Unfortunately for you, the pizzeria was being surveilled as they had raised suspicions within law enforcement that they were laundering money. You are caught by the local police Go back to the beginning.")
    print("\nDo you want to retry?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fraud1()
    elif (answer =="n"):
        quit()
    else:
        print("please enter a valid answer")
        fraud7()

def fraud8():
    system('clear')
    print("You decided to find another way to launder the money you have obtained from your fraud. You decide to buy cryptocurrency and convert the stolen money through several different types of cryptocurrencies. As the company has no cyber unit to audit the purchases in the company, you get away with committing this fraud. You decide it’s time to retire and live your life in Cabo. You won the fraud game!!! Feel free to play again or be done.")
    print("\n CONGRATS!!!!! \n")
    print("\nDo you want to play again?")
    answer = input("type y or n\n")
    if (answer == "y"):
        menu()
    elif (answer =="n"):
        quit()
    else:
        print("please enter a valid answer")
        fraud8()
        
def fraud9():
    system('clear')
    print("You decided to wait and not collude with the vendor to commit fraud. However, in addition to increased rent, your car got totaled in an accident and you must know replace it as your insurance company could not cover the cost of the accident. Luckily for you, you work closely with the investor side of the company and could ask one of the people in that department to up the investing prices and use previous investor money to pay back current investors, putting your company in a good light on Wallstreet.")
    print("\nDo you commit a ponzi scheme?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fraud10()
    elif (answer =="n"):
        fraud13()
    else:
        print("please enter a valid answer")
        fraud9()

def fraud10():
    system('clear')
    print("You start the ponzi scheme and you are getting very rich. You could continue the scheme, or you could try to leave the company quickly with the money you have already obtained.")
    print("\nDo you stay at the company and expand your ponzi scheme?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fraud11()
    elif (answer =="n"):
        fraud12()
    else:
        print("please enter a valid answer")
        fraud10()
        
def fraud11():
    system('clear')
    print("You decide to expand your ponzi scheme and include more of the employees in your department. Unfortunately, one of the investors did not receive their money back in time, and they have personally contacted the CFO, who opens an investigation into your department. You are caught by the fraud fighter (auditor). Go back to the beginning.")
    print("\nDo you want to retry?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fraud1()
    elif (answer =="n"):
        quit()
    else:
        print("please enter a valid answer")
        fraud11()

def fraud12():
    system('clear')
    print(" You decided you are done with the ponzi scheme, and you quickly leave the company before arising any noticeable suspicion. You use your money to buy a house and now live comfortably for the next thirty years. You won the fraud game!!! Feel free to play again or be done.")
    print("\n CONGRATS!!!! \n")
    print("\nDo you want to play again?")
    answer = input("type y or n\n")
    if (answer == "y"):
        menu()
    elif (answer =="n"):
        quit()
    else:
        print("please enter a valid answer")
        fraud12()

def fraud13():
    system('clear')
    print("You decide that committing fraud is too risky. Sadly, you can no longer afford your apartment and you must now move to a smaller place. You now realize that if you had committed the fraud, you could be living in a mansion. You have failed to commit fraud as the fraudster. I thought that’s why you picked this path. You can go back to the beginning and see what would have happened had you decided to commit fraud. Who knows?")
    print("\nDo you want to retry?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fraud1()
    elif (answer =="n"):
        quit()
    else:
        print("please enter a valid answer")
        fraud13()
        
def fighter1():
    system('clear')
    print("You are a top internal auditor at Play the Game Inc. You are severely overworked and don’t have lots of extra time to personally investigate customer/employee tips of fraud or look closely at all the employees of Play the Game Inc. You could hire auditors to lighten the load to allow for more timely investigations and precise audits of the company financial statements.")
    print("\nDo you hire additional staff?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fighter2()
    elif (answer =="n"):
        fighter12()
    else:
        print("please enter a valid answer")
        fighter1()

def fighter2():
    system('clear')
    print("You have hired more staff for the internal auditing department at Play the Game Inc. The CEO recognizes your initiative and personally confides in you that they have noticed higher company costs than normal for this fiscal year. The increased cost is more than double the previous fiscal year and is suspicious because the company has not made many purchases in the past year according to invoices and other financial documents. However, there are rumors within the company that the CFO is the person behind this increase in costs, and that the CFO has recently gone through a divorce.")
    print("\nDo you wish to investigate the CFO and inform the department of the rumor?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fighter3()
    elif (answer =="n"):
        fighter4()
    else:
        print("please enter a valid answer")
        fighter2()
        
def fighter3():
    system('clear')
    print("You decided to personally investigate this rumor and have alerted your department of the situation. However, in your hasty investigation, you conducted poor surveillance and covert operations, opting for electronic surveillance. In addition, one of your team members was very close to the CFO of the company and alerted them to the presence of an investigation. Your investigation was quickly shut down and you were reprimanded by the CEO for your poor handling of the situation. You have failed as an internal auditor, go back to the beginning.")
    print("\nDo you want to retry?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fighter1()
    elif (answer =="n"):
        quit()
    else:
        print("please enter a valid answer")
        fighter3()

def fighter4():
    system('clear')
    print("You decided to wait for there to be more information on this suspected case of fraud. Over the next month, you performed an audit on all the financial statements in the company. Your audit uncovered five large unusual purchases. You have also discovered that one of your team members is very close to the CFO. You could alert the CEO of this delicate situation before the team member finds out that the person most likely behind these fraudulent purchases is the CFO.")
    print("\ndo you alert the CEO of this situation?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fighter5()
    elif (answer =="n"):
        fighter13()
    else:
        print("please enter a valid answer")
        fighter4()
        
def fighter5():
    system('clear')
    print("You have decided to alert the CEO of the situation before proceeding with an investigation in conjunction with law enforcement. The CEO moves the team member that is close to the CFO to another fiscal department. You begin your investigation and must choose which type of surveillance and covert operation you will use to catch the CFO conducting fraudulent purchases.")
    print("\nDo you use stationary observation?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fighter6()
    elif (answer =="n"):
        fighter7()
    else:
        print("please enter a valid answer")
        fighter5()
        
def fighter6():
    system('clear')
    print("You have decided to use stationary observation and set up surveillance to look over the CFO’s office. You spend an entire month conducting this type of surveillance and discover nothing. Law enforcement and the CEO decide they are dropping the investigation and once the investigation is dropped. The CFO suddenly resigns after this. You failed to catch the fraudster. Go back to the beginning.")
    print("\nDo you want to retry?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fighter1()
    elif (answer =="n"):
        quit()
    else:
        print("please enter a valid answer")
        fighter6()
        
def fighter7():
    system('clear')
    print("You decided to conduct moving surveillance and have cooperating law enforcement tail the CFO to and from Play the Game Inc. They discover that the CFO is paying another low-level employee in cash at a nearby restaurant once every two weeks. You could always have the low-level employee interviewed. Or you could continue to just tail the CFO.")
    print("\nDo you contniue to tail the CFO?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fighter8()
    elif (answer =="n"):
        fighter9()
    else:
        print("please enter a valid answer")
        fighter7()
        
def fighter8():
    system('clear')
    print("You have decided to just tail the CFO and see if you can spot any other suspicious behavior. Nothing happens and the CFO suddenly decides to quit before the investigation is finished, growing paranoid that someone is following them. You have failed as an auditor. Go back to the beginning.")
    print("\nDo you want to retry?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fighter1()
    elif (answer =="n"):
        quit()
    else:
        print("please enter a valid answer")
        fighter8()
        
def fighter9():
    system('clear')
    print("You have decided to interview the low-level employee and try to discover the true nature of the fraud. The low-level employee is a woman, you are unsure of the personal life of the low-level employee.")
    print("\nDo you wish to use a woman as a witness for the interveiw?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fighter10()
    elif (answer =="n"):
        fighter11()
    else:
        print("please enter a valid answer")
        fighter9()
        
def fighter10():
    system('clear')
    print("You have decided to use a woman as the witness for the interview. The low-level employee feels very comfortable with the interview and tells the interviewer that they make the fraudulent purchases for the CFO on their computer as their department has few internal controls. This evidence leads to the prosecution of the CFO and a light sentence for the low-level employee. You have successfully completed the investigation of the CFO and done your job as an auditor very well. You can play again or choose to quit.")
    print("\n CONGRATS!!!! \n")
    print("\nDo you want to play again?")
    answer = input("type y or n\n")
    if (answer == "y"):
        menu()
    elif (answer =="n"):
        quit()
    else:
        print("please enter a valid answer")
        fighter10()
        
def fighter11():
    system('clear')
    print("You have decided to use a man as the witness for the interview. The low-level employee does not say anything about the cash exchanges and tells the interviewer that they are gifts between friends. You are unsuccessful at getting anything out of the low-level employee, and the CFO quickly resigns before any further investigation can be done. You have failed to catch the fraudster. You could try again if you wanted.")
    print("\nDo you want to retry?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fighter1()
    elif (answer =="n"):
        quit()
    else:
        print("please enter a valid answer")
        fighter11()
        
def fighter12():
    system('clear')
    print("You have decided to not hire any more staff and have become swamped with the audits you need to conduct and completely miss the fraudulent purchases made by a low-level employee in conjunction with the CFO. You have failed as an auditor. Go back to the beginning. ")
    print("\nDo you want to retry?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fighter1()
    elif (answer =="n"):
        quit()
    else:
        print("please enter a valid answer")
        fighter12()
        
def fighter13():
    system('clear')
    print("You have decided to not alert the CEO and accept the risk of investigating five unusual purchases on your own. The team member that knows the CFO alert them of the situation. The CFO resigns and the investigation is quickly dropped. You have failed as an auditor. Go back to the beginning. ")
    print("\nDO you want to retry?")
    answer = input("type y or n\n")
    if (answer == "y"):
        fighter1()
    elif (answer =="n"):
        quit()
    else:
        print("please enter a valid answer")
        fighter13()
        
menu()
