import datetime
import os
import mysql.connector
import datetime
import usermenu
import adminmenu
from voice import speak
import webbrowser


def wishMe():
    os.system("cls")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    os.system("cls")
    print("\t***** Medibuddy *****")
    speak("Welcome to life buddy. Please tell me how may I help you")


def login():
    os.system("cls")
    print("\nEnter login Credentials:")
    speak("Enter your login credentials to access admin section")
    print("\nUsername: ", end="")
    speak("Enter your Username")
    username = input()
    print("Password: ", end="")
    speak("Enter your Password")
    password = input()
    if username == "admin" and password == "12345":
        print("\nLogin Successfull !!!")
        speak("Login Successfull")
        adminmenu.adminmenu()
    else:
        print("\nIncorrect credentials !!!")
        speak("Incorrect credentials")
        tryagain(login)


def tryagain(value):
    while (True):
        print("\nDo you want to try again? (y/n):", end="")
        speak("Do you want to try again?")
        retry = input()
        if retry == 'y':
            value()
        elif retry == 'n':
            speak("Redirecting back to main menu")
            mainmenu()
        else:
            print("\nWRONG INPUT !!!")
            speak("Sorry, wrong input")
        print()
        print("Press enter to continue....", end="")
        speak("Press enter to continue")
        choice = input()


def mainmenu():
    mydb = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    l = mycursor.fetchall()
    if not ('medibuddy',) in l:
        mycursor.execute("CREATE DATABASE medibuddy")

    while (True):
        os.system("cls")
        mycursor.execute("USE medibuddy")
        print("\t***** MAIN MENU *****")
        speak("Welcome to main menu")
        print("\n1. Admin section.")
        print("2. User section.")
        print("3. Contact section.")
        print("4. Exit.")
        print("\nEnter your choice: ", end="")
        speak("Select your section")
        choice = input()
        match choice:
            case "1":
                login()
                adminmenu.adminmenu()
            case "2":
                usermenu.usermenu()
            case "3":
                s = "https://github.com/manik-18"
                webbrowser.open(s)
                break
            case "4":
                print("\nBYE !!!")
                speak("Thank you for visiting, Have a nice day !!!")
                exit()
            case default:
                print("\nWRONG INPUT !!!")
                speak("Sorry, wrong input")
        print()
        print("Press enter to continue....", end="")
        speak("Press enter to continue")
        choice = input()


if __name__ == "__main__":

    wishMe()
    mainmenu()
