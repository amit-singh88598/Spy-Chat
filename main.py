from spy_details import spy_name , spy_age , spy_rating #importing variables from spy_details.py

print "hello buddy" #printing hello
print "let's get started"

def start_chat(spy_name,spy_age,spy_rating): #creation of function
    print "Here are your option " + spy_name
    show_menu = True
    while show_menu:
        choice = input("What do you want to do > \n 1. Add a status \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 0. Exit ")
        if choice == 1: #choice variable set to 1
            print "Add a status" #choice 1
        elif choice == 2:
            print "Add a friend" #choice 2
        elif choice == 3:
            print "Send a secret message" #choice 3
        elif choice == 4:
            print "Read a secret message" #choice 4
        elif choice == 0: #exit
            show_menu = False
        else: #for any invalid input
            print"Invalid Input"

spy_exist = raw_input("Are you a new user? Y/N ") #Asking the user if he is a new user or not

if spy_exist.upper()=="N":
    print "Welcome back " +spy_name+ "age: "+ str(spy_age) +" having rating of " +str(spy_rating)
elif spy_exist.upper()=="Y": #upper is use to convert user input into capital letter
    spy_name = raw_input ('what is your spy name?') #take name as input from user
    if len(spy_name)>2: #checking for length of the string name
        print 'Welcome ' + spy_name + '. Glad to have you back with us. ' #concatening strings
        spy_salutation = raw_input("What should we call you (Mr. or Ms.)? ")
        if spy_salutation=="Mr." or spy_salutation=="Ms.": #using if to check condition to take input of salutation
            spy_name = spy_salutation + " " + spy_name
            print "Alright" + spy_name + ". I would like to know a little bit more about you"
            spy_is_online = True
            spy_age = input("What is your age")
            if 45>spy_age>18: #nested if statement to check range of age
                print "your age is correct"
                spy_rating = input("What is your rating? ")
                if spy_rating>5.0:
                    print "Great spy"
                elif 3.5<spy_rating<=5.0: #elif statement for more than one condition
                    print "Average spy"
                elif 2.5<spy_rating<=3.5:
                    print "Bad spy"
                else:
                    print "Who hired you?"
                spy_is_online = True #boolean expression
                print "Authentication complete Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " proud to have you on board " #typecasting of integer to string
                start_chat(spy_name,spy_age,spy_rating) #calling function spy_chat
            else:
                print "You are not eligible for spy"
        else:
            print "Invalid salutation"
    else:
        print "oops please enter a valid name"
else:
    print "Invalid entry"