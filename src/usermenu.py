import os
import time
import wikipedia
import mysql.connector
import mainmenu
import bookings
from voice import speak
from tabulate import tabulate


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


def wiki():
    try:
        os.system("cls")
        print(
            "Problem or Disease name: ", end="")
        speak("Enter the name of the problem or a disease")
        data = input()
        print("\nSearching..", end="")
        speak("Searching")
        time.sleep(1)
        print("..", end="")
        time.sleep(1)
        print("..", end="")
        time.sleep(1)
        print("..")
        answer = wikipedia.summary(
            "{}".format(data), sentences=4, auto_suggest=False)
        print("\n{}".format(answer))
        speak(answer)
    except wikipedia.DisambiguationError as e:
        speak(
            "Sorry, the word {} refer to many things. Please be specific.".format(data))
        print(e)
    except:
        print("Data not found in wikipedia !!!")
        speak("Data not found in wikipedia")


def usermenu():
    while True:
        os.system("cls")
        mycursor.execute("USE medibuddy")
        print("\t***** USER SECTION *****")
        speak("Welcome to user section")
        print("\n1. Search in wikipedia for a disease or a problem.")
        print("2. Medicine recommendation.")
        print("3. Bookings.")
        print("4. Main menu.")
        print("\nEnter your choice: ", end="")
        speak("Enter your choice")
        choice = input()
        match choice:
            case "1":
                wiki()
            case "2":
                os.system("cls")
                mycursor.execute("USE medibuddy")
                print("Problem name: ", end="")
                speak("Enter the name of the problem")
                problem_name = input()
                mycursor.execute(
                    "SELECT Suggestion FROM medicine_recommendation WHERE Problem = '{}'".format(problem_name))
                myresult = mycursor.fetchall()
                if myresult == []:
                    print("\nData not found !!!")
                    speak("Data not found")
                    print(
                        "\nIf you have a major problem you can book ambulance or you can book appointment with a doctor")
                    speak(
                        "If you have a major problem you can book ambulance or you can book appointment with a doctor")
                    print("\n1. Ambulance booking.")
                    print("2. Doctor appointment. ")
                    print("3. User menu")
                    print("\nEnter your choice: ", end="")
                    speak("Enter your choice")
                    c = input()
                    if (c == '1'):
                        bookings.book(1)
                    elif (c == '2'):
                        bookings.book(3)
                    elif (c == '3'):
                        speak("Redirecting back to the user menu")
                        usermenu()
                    else:
                        print("\nWRONG INPUT !!!")
                        speak("Sorry, wrong input")
                else:
                    print(tabulate(myresult, headers=[
                          "Suggestion"], tablefmt='psql'))

            case "3":
                bookings.make_bookings()
            case "4":
                speak("Redirecting back to the main menu")
                mainmenu.mainmenu()
            case default:
                print("\nWRONG INPUT !!!")
                speak("Sorry, wrong input")
        print()
        print("Press enter to continue....", end="")
        speak("Press enter to continue")
        choice = input()
