import csv
import sys
    
def askUser():
    userinput = ""
    while userinput not in ["LOGIN", "CREATE"]: 
        login_prompt = "LOGIN or CREATE?"
        userinput = input(login_prompt)
        userinput = userinput.upper()
    return userinput

def login():
    details_check = ""
    email = ""
    username = ""
    password = ""    
    print("Log in")    
    while details_check != "pass":
        email = input("Enter email: ")
        username = input("Enter username: ")
        password = input("Enter password: ")        
        details_check = checkDetails(email, username, password)
        if details_check == "fail":
            print("Details incorrect")    
    print("Logged in")
    
def checkDetails(email, username, password):
    #read csv, and split on "," the line
    user_info = csv.reader(open('user_info.csv', "r"), delimiter=",")
    #loop through the csv list
    for row in user_info:
        #if current rows 1st, 2nd and 3rd values are equal to input, print that row
        if email == row[0] and username == row[1] and password == row[2]:
             details_check = "pass"
        else: details_check = "fail"
    return details_check

def createUser(): 
    email_exists = ""
    username_exists = ""
    email = ""
    username = "" 
    password = ""
    print("Create user")
    email = input("Enter email: ")     
    username = input("Enter username: ")    
    password = askPassword()
    with open('user_info.csv', mode='a', newline='') as user_info:
        user_writer = csv.writer(user_info, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        user_writer.writerow([email, username, password])    
    print("User created")

def askPassword():
    password1 = "password1"
    password2 = "password2"
    while password1 != password2:
        password1 = input("Enter password: ")
        password2 = input("Re-enter password: ")
        if password1 != password2: 
            print("Passwords don't match. Re-enter matching passwords.")
    password = password2
    return password

userinput = askUser()
if userinput == "LOGIN":
    login()       
else:
    createUser()