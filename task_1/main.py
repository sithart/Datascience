import os
import sys


def store_credentials():
    while True:
        print("--------Usename Must be a valid Email Address--------")
        username = input("Enter the username : ")
        print("--------Password Must be included atleast one Numerical, one Special Character, one Uppercase and one Lowecase----")
        password = input("Enter the password : ")
        spl_char_check = username[0].isalnum()
        num_char_check = username[0].isnumeric()
        spl_char_pass  = password.isalnum()

        m = False
        n = False
        o = False
        for pwd in password:
            if pwd.isupper() == True:
                m = True
            elif pwd.islower() == True:
                n = True
            elif pwd.isnumeric() == True:
                o = True
            else:
                pass

        if spl_char_pass == False and m == True and n == True and o == True and "@" in username and "@." not in username and "." in username and spl_char_check == True and num_char_check == False:
            cred = open('credentials.txt', 'a')
            data = username + ";" + password
            cred.write('\n' + data)
            print(f"You entered {username}, {password}")
            print("password and usernames are saved successfully !.")
            print("\n"*2)
            cred.close()
            break
        else:
            print("Please Enter the Valid Inputs also satisfy the constraints.")
            print("\n"*2)


def login():
    x = input("Enter User Name :")
    with open("credentials.txt") as file:
        flag = 0
        for item in file:
            if item != "\n":
                u_name = item.strip('\n').split(';')
                if x == u_name[0]:
                    print(f"Your username and corresponsing Password are : {u_name[0]}, {u_name[1]}")
                    print("\n"*2)
                    flag = 1
                else:
                    pass
        if flag == 1:
            pass
        else:
            print("\n"*2)
            print("***Username was not Registered, Please re-enter the Username for Registration***")
            store_credentials()



def forget_password():
    y = input("Enter your Username :")
    flag = 0
    with open("credentials.txt") as file:
        for item in file:
            if item != "\n":
                u_name = item.strip('\n').split(';')
                if y == u_name[0]:
                    print(f"Your username and Password are : {u_name[0]}, {u_name[1]}")
                    print("\n"*2)
                    flag = 1
                else:
                    pass
    if flag == 1:
        pass
    else:
        print("*** User name was not there, Please register here !***")
        print("\n"*2)
        # store_credentials()

while True:
    try:
        # User selection
        print("Please choose the options For Registration Enter - 1")
        print("Please choose the options For Login Enter - 2")
        print("Please choose the options For Forget password Enter - 3")
        print("Press 0 will Stop the program.")
        y = int(input("Enter your Option :"))
        if y == 1 or y == 2 or y == 3:
            print(f"You Entered the option {y}")
            if y == 1:
                store_credentials()
            elif y == 2:
                login()
            else:
                forget_password()
        elif y  == 0:
            sys.exit()
        else:
            print("Invalid Input, Accepted options are 1 or 2 or 3. Please rerun the program.")
            print("\n"*2)
    except Exception as e:
        print(e)
        print("Invalid Input. please enter options 1 or 2 or 3 only")
