from spy_details import spy , Spy , ChatMessage #importing variables and class from spy_details.py
from steganography.steganography import Steganography #importing steganography module from steganography class of steganography library
from datetime import datetime #importing datetime module from datetime class
from colorama import Fore,Style
import csv
time=datetime.now() #.now() function which will return current date and time
print time #printing returned current date and time
print "hello buddy" #printing hello
print "let\'s get started"
status_message = ['But man is not made for defeat. A man can be destroyed but not defeated','There is nothing permanent except change','learning never exhaust the mind'] #display menu of old status listed
frnd1 = Spy('Aman','Mr.',27,2.3)
frnd2 = Spy('Vishal','Mr.',30,3.3)
friends=[frnd1,frnd2]

def load_frnds():
    with open('friends.csv', 'rb') as friends_data:
        reader = list(csv.reader(friends_data))
        for row in reader[1:]:
            spy=Spy(name=row[0],salutation=row[1],age=row[2],rating=row[3])
            friends.append(spy)

load_frnds()
def load_chats():
    with open('friends.csv','rb') as chats_data:
        reader = list(csv.reader(chats_data))
        for message,date,sent_by_me,receiver_name in reader[1:]:
            print Fore.BLACK+message.Fore.BLUE+sent_by_me,Fore.CYAN+receiver_name
            print (Style.RESET_ALL)

def selected_chat():
    s_name=raw_input("Enter the name of friend whose name chat you want to see.")
    with open('chat.csv','rb')as chats_data:
        reader=list(csv.reader(chats_data))
        for message,date,sent_by_me,receiver_name in reader[1:]:
            if s_name==receiver_name:
                print Fore.BLUE+date,Fore.RED+sent_by_me,Fore.BLACK+message
                print (Style.RESET_ALL)
            else:
                print ("NO,Chat is available")
def add_status(c_status): #defining function add status
    if c_status != None: #if there is nothing mention to choosed in or from status
        print "Your current status is " + c_status
    else:
        print "You dont have any status currently"
    existing_status = raw_input("You want to select from old status? Y/N ") #asking option which option you want to select either old status or not
    if existing_status.upper()=="N": #if user dont want to choose from existing status
        new_status=raw_input("Enter your status: ") #asking new status from user
        if len(new_status)>0: #checking length of status
            with open('sts.csv','a')as friend_status:
                writer=csv.writer(friend_status)
                writer.writerow([new_status])
                updated_status=new_status
            status_message.append(new_status)
    elif existing_status.upper()=="Y": #option when user want to choose from existing status
        serial_no = 1
        for old_status in status_message: #traversing in list status_message
            print str(serial_no) +". " + old_status #concatinating serial number with choosed status
            serial_no = serial_no + 1
        user_choice = input("Enter your choice: ") #asking choice of user to choose options
        new_status = status_message[user_choice-1] #deducting by 1 from user choice so that it can point current index as status_message list
    updated_status = new_status #will return to the function add_status
    return updated_status
def add_friend(): # defining function add_friend()
    frnd = Spy('','',0,0.0)
    frnd.name = raw_input("What is your friend name? ")
    frnd.sal = raw_input("What should we call your friend? ")
    frnd.age = input("What is your friend age? ")
    frnd.rating = input("What is your friend rating? ")
    frnd.is_online = True
    if len(frnd.name)>2 and 12<frnd.age<50 and frnd.rating>spy.rating: #conditions for adding new friend
        with open('feiends.csv', 'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([frnd.name, frnd.salutation, frnd.rating, frnd.age, frnd.is_online])
    else:
        print "Friend cannot be added"
    return len(friends) #will return to add friend()
def select_a_friend(): #defining function
    serial_no = 1
    for frnd in friends:
        print str(serial_no) + " " +frnd.name
        serial_no = serial_no+1
    user_selected_frnd = input("Enter your choice: ") #asking user choice to which friend to select
    user_selected_frnd_index = user_selected_frnd-1
    return user_selected_frnd_index #returning date to select_a_friend()
def send_message(): #defining function
    selected_frnd = select_a_friend()
    original_image=raw_input("what is the name of your image?") #asking user about the name of image
    secret_text=raw_input("what is your secret text?") #asking about what secret text you need to save in image
    list = ['HELP ME', 'SOS', 'SAVE ME', 'EMERGENCY']
    if secret_text.upper() in list:
        print "Inappropriate message"
        print (Style.RESET_ALL)
    else:
        output_path="output.jpg"
        Steganography.encode(original_image,output_path,secret_text) #encoding the image with secret text,
        print "your secret text has been successfully encoded"
        with open ('chat.csv','a') as chats_data:
            writer=csv.writer(chats_data)
            writer.writerow([secret_text,time,spy.name,friends[selected_frnd].name])

def read_a_message():
    selected_frnd=select_a_friend()
    output_path=raw_input("Which image you want to decode?") #asking about which image user need to decode
    secret_text=Steganography.decode(output_path) #decoding the text from image
    print "secret text is "+secret_text
    new_chat = ChatMessage(secret_text,False)
    friends[selected_frnd].chats.append(new_chat) #appending
    print "your secret message has been saved."
def spy_chat(spy_name,spy_age,spy_rating): #creation of function
    print "Here are your option " + spy_name
    current_status = None
    show_menu = True
    while show_menu:
        spy_choice = input("What do you want to do > \n 1. Add a status \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 0. Exit ") # asked to choose the option
        if spy_choice == 1: #will display the status
            current_status = add_status(current_status)
            print "updated status is " + current_status
        elif spy_choice == 2: #will display numbers of friend user have
            no_of_friends = add_friend()
            print "you have " + str(no_of_friends) + " friends"
        elif spy_choice == 3: #will send encoded message
            send_message()
        elif spy_choice == 4: #will display the decoded message
            read_a_message()
        elif spy_choice == 5:
            load_chats()
        elif spy_choice == 6:
            selected_chat()
        elif spy_choice == 0: #will come out of show_menu option
            show_menu = False
        else: #for any invalid input
            print"Invalid options"
spy_login=raw_input("Enter your username/email.")
spy_password=raw_input("Enter your password.")
if spy_login=='Amit'and spy_password=='hellodbit':
    print "you are logged in."
    spy_exist = raw_input("Are you a new user? Y/N ") #Asking the user if he is a new user or not
    if spy_exist.upper()=="N": #when spy is an old one
        print "Welcome back " +spy.name+ "age: "+ str(spy.age) +" having rating of " +str(spy.rating)
        spy_chat(spy.name,spy.age,spy.rating) #calling function
    elif spy_exist.upper()=="Y": #upper is use to convert user input into capital letter
        spy = Spy("","",0,0.0)
        spy.name = raw_input ('what is your spy name?') #take name as input from user
        if len('name')>2: #checking for length of the string name
            print 'Welcome ' + spy.name + "." #concateningwelcome with spy_name
            spy_salutation = raw_input("What should we call you (Mr. or Ms.)? ")
            if spy_salutation=="Mr." or spy_salutation=="Ms." or spy_salutation=="ms" or spy_salutation=="mr": #applying salutation to the name
                spy.name = spy_salutation + spy.name #concatinating name with salutation
                print "welcome " + spy.name + " Glad to see you back"
                print "Alright" + spy.name + ". I would like to know a little bit more about you "
                spy.age = input("What is your age")
                if 45>spy.age>18: #nested if statement to check range of age
                    print "your age is correct"
                    spy_rating = input("What is your rating? ") #taking rating from user
                    if spy.rating>5.0:
                        print "Great spy"
                    elif 3.5<spy.rating<=5.0: #elif statement for more than one condition
                        print "Average spy"
                    elif 2.5<spy.rating<=3.5:
                        print "Bad spy"
                    else:
                        print "Who hired you?"
                    spy_is_online = True #checking if spy is online
                    print "Authentication completed.Welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " + str(spy.rating) + " proud to have you on board "   #typecasting of integer to string
                    spy_chat(spy.name,spy.age,spy.rating) #calling function spy_chat
                else:
                    print "You are not eligible for spy"
            else: # when salutation is incorrect
                print "Invalid salutation"
        else:
            print "oops please enter a valid name"
    else:
        print "Invalid entry"
else:
    print "you can't log in."