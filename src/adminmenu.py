import os
import mainmenu
from voice import speak
import admindata
import bookings
import mysql.connector


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


def adminmenu():
    os.system("cls")
    mycursor.execute("USE medibuddy")
    print("\t***** ADMIN SECTION *****")
    speak("Welcome to admin section.")
    while (True):
        os.system("cls")
        print("\n1. Add data.")
        print("2. View data.")
        print("3. Delete data.")
        print("4. Update data.")
        print("5. Search data.")
        print("6. View bookings.")
        print("7. Delete bookings.")
        print("8. Search bookings.")
        print("9. Main menu.")
        print("\nEnter your choice: ", end="")
        speak("Enter your choice")
        choice = input()
        match choice:
            case "1":
                admindata.adddata()
            case "2":
                admindata.viewdata()
            case "3":
                admindata.deletedata()
            case "4":
                admindata.updatedata()
            case "5":
                admindata.searchdata()
            case "6":
                admindata.viewbookings()
            case "7":
                bookings.deletebookings()
            case "8":
                bookings.searchbookings()
            case "9":
                speak("Redirecting back to main menu")
                mainmenu.mainmenu()
            case default:
                print("\nWRONG INPUT !!!")
                speak("Sorry, wrong input")
        print()
        print("Press enter to continue....", end="")
        speak("Press enter to continue")
        choice = input()
