import os
import mysql.connector
import adminmenu
from tabulate import tabulate
from voice import speak


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


def insert(table_name, field1, field2, val1, val2):
    try:
        mycursor.execute(
            "CREATE TABLE {} ({} VARCHAR(300), {} VARCHAR(3000))".format(table_name, field1, field2))
        print()
    except:
        print()
    sql = "INSERT INTO {} ({}, {}) VALUES (%s, %s)".format(
        table_name, field1, field2)
    val = (val1, val2)
    mycursor.execute(sql, val)
    mydb.commit()
    print("\nData entered successfully !!!")
    speak("Data entered successfully !!!")


def display2(table_name):
    try:
        mycursor.execute("SELECT * FROM {}".format(table_name))
        myresult = mycursor.fetchall()
        print(tabulate(myresult, tablefmt='psql'))
        return 1
    except:
        print("Data not found !!!")
        speak("Data not found")
        return 0


def viewbookings():
    while (True):
        os.system("cls")
        mycursor.execute("USE medibuddy")
        speak("select the type of data")
        print("\n1. Ambulance")
        print("2. Lab Test ")
        print("3. Doctor")
        print("4. Admin menu.")
        print("\nEnter your choice: ", end="")
        speak("enter your choice")
        choice = input()
        os.system("cls")
        match choice:
            case "1":
                display2("Ambulance_Bookings")
            case "2":
                display2("Lab_Test_Bookings")
            case "3":
                display2("Doctor_Bookings")
            case "4":
                speak("Redirecting to the admin menu")
                adminmenu.adminmenu()
            case default:
                print("\nWRONG INPUT !!!")
                speak("Sorry, wrong input")
        print()
        print("Press enter to continue....", end="")
        speak("Press enter to continue")
        choice = input()


def adddata():
    while (True):
        os.system("cls")
        mycursor.execute("USE medibuddy")
        speak("select the type of data")
        print("\n1. Medicine Recommendation.")
        print("2. Lab Test.")
        print("3. Doctor.")
        print("4. Ambulance.")
        print("5. Admin menu.")
        print("\nEnter your choice: ", end="")
        speak("enter your choice")
        choice = input()
        os.system("cls")
        match choice:
            case "1":
                speak("Enter the problem name and its Suggestion")
                problem_name = input("Problem name: ")
                Suggestion_name = input(
                    "Suggestion for the above Problem: ")
                insert("Medicine_Recommendation", "Problem",
                       "Suggestion", problem_name, Suggestion_name)
            case "2":
                speak("Enter the test's name and its price")
                lab_Test_Name = input("Test name: ")
                price = input("Price: ")
                insert("Lab_Test_Record", "Test_Name",
                       "Price", lab_Test_Name, price)
            case "3":
                speak("Enter the name of the doctor and its designation")
                doctor_name = input("Doctor's name: ")
                designation = input("Designation: ")
                insert("Doctors_Record", "Name",
                       "Designation", doctor_name, designation)
            case "4":
                speak("Enter the ambulance type and its number")
                ambulance_type = input("Ambulance type: ")
                number = input("Vehicle number: ")
                insert("Ambulance_Record", "Ambulance_Type",
                       "Number", ambulance_type, number)
            case "5":
                speak("Redirecting back to the admin menu")
                adminmenu.adminmenu()
            case default:
                print("\nWRONG INPUT !!!")
                speak("Sorry, wrong input")
        print()
        print("Press enter to continue....", end="")
        speak("Press enter to continue")
        choice = input()


def display(table_name, col1, col2):
    try:
        mycursor.execute("SELECT * FROM {}".format(table_name))
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=[col1, col2], tablefmt='psql'))
        speak("Here is your data")
        return 1
    except:
        print("Data not found !!!")
        speak("Data not found")
        return 0


def viewdata():
    while (True):
        os.system("cls")
        mycursor.execute("USE medibuddy")
        speak("select the type of data")
        print("\n1. Medicine Recommendation.")
        print("2. Lab Test.")
        print("3. Doctor.")
        print("4. Ambulance.")
        print("5. Admin menu.")
        print("\nEnter your choice: ", end="")
        speak("enter your choice")
        choice = input()
        os.system("cls")
        match choice:
            case "1":
                display("Medicine_Recommendation", "Problem", "Suggestion")
            case "2":
                display("Lab_Test_Record", "Test_Name", "Price")
            case "3":
                display("Doctors_Record", "Name", "Designation")
            case "4":
                display("Ambulance_Record", "Ambulance_Type", "Number")
            case "5":
                speak("Redirecting back to the admin menu")
                adminmenu.adminmenu()
            case default:
                print("\nWRONG INPUT !!!")
                speak("Sorry, wrong input")
        print()
        print("Press enter to continue....", end="")
        speak("Press enter to continue")
        choice = input()


def deletedata():
    while (True):
        os.system("cls")
        mycursor.execute("USE medibuddy")
        speak("select the type of data")
        print("\n1. Medicine Recommendation.")
        print("2. Lab Test.")
        print("3. Doctor.")
        print("4. Ambulance.")
        print("5. Admin menu.")
        print("\nEnter your choice: ", end="")
        speak("enter your choice")
        choice = input()
        os.system("cls")
        match choice:
            case "1":
                speak("Enter the problem name which you want to delete")
                problem_name = input("Problem name: ")
                x = search(problem_name, "Problem", "Medicine_Recommendation")
                if x == 0:
                    print()
                else:
                    mycursor.execute(
                        "DELETE FROM Medicine_Recommendation WHERE Problem='{}'".format(problem_name))
                    mydb.commit()
                    print("\nData deleted successfully !!!")
                    speak("Data deleted successfully")
            case "2":
                speak("Enter the name of the lab test which you want to delete")
                lab_Test_Name = input("Lab Test name: ")
                x = search(lab_Test_Name, "Test_Name", "Lab_Test_Record")
                if x == 0:
                    print()
                else:
                    mycursor.execute(
                        "DELETE FROM Lab_Test_Record WHERE Test_Name='{}'".format(lab_Test_Name))
                    mydb.commit()
                    print("\nData deleted successfully !!!")
                    speak("Data deleted successfully")
            case "3":
                speak("Enter the name of the doctor whose record you want to delete")
                doctor_name = input("Doctor's name: ")
                x = search(doctor_name, "Name", "Doctors_Record")
                if x == 0:
                    print()
                else:
                    mycursor.execute(
                        "DELETE FROM Doctors_Record WHERE Name='{}'".format(doctor_name))
                    mydb.commit()
                    print("\nData deleted successfully !!!")
                    speak("Data deleted successfully")
            case "4":
                speak("Enter the ambulance number whose record you want to delete")
                Number = input("Ambulance number: ")
                x = search(Number, "Number", "Ambulance_Record")
                if x == 0:
                    print()
                else:
                    mycursor.execute(
                        "DELETE FROM Ambulance_Record WHERE Number='{}'".format(Number))
                    mydb.commit()
                    print("\nData deleted successfully !!!")
                    speak("Data deleted successfully")
            case "5":
                speak("Redirecting back to the admin menu")
                adminmenu.adminmenu()
            case default:
                print("\nWRONG INPUT !!!")
                speak("Sorry, wrong input")
        print()
        print("Press enter to continue....", end="")
        speak("Press enter to continue")
        choice = input()


def search(name, field1, table):
    sql = "SELECT * FROM {} WHERE {} ='{}'".format(table, field1, name)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if myresult == []:
        print("\nData not found !!!")
        speak("Data not found")
        return 0
    else:
        for x in myresult:
            print("\n", x)
        speak("Data found")
        return 1


def updatedata():
    while (True):
        os.system("cls")
        mycursor.execute("USE medibuddy")
        speak("select the type of data")
        print("\n1. Medicine Recommendation.")
        print("2. Lab Test.")
        print("3. Doctor.")
        print("4. Ambulance.")
        print("5. Admin menu.")
        print("\nEnter your choice: ", end="")
        speak("enter your choice")
        choice = input()
        os.system("cls")
        match choice:
            case "1":
                speak("Enter the problem name which you want to update")
                problem_name = input("Problem name: ")
                x = search(problem_name, "Problem", "Medicine_Recommendation")
                if x == 0:
                    print()
                else:
                    speak("Enter the new data")
                    print("\nEnter the new data")
                    new_problem_name = input("\nProblem name: ")
                    new_Suggestion = input("Suggestion: ")
                    sql = "UPDATE Medicine_Recommendation SET Problem = %s, Suggestion = %s WHERE Problem = %s"
                    val = (new_problem_name, new_Suggestion, problem_name)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print("\nData updated successfully !!!")
                    speak("Data updated successfully")
            case "2":
                speak("Enter the name of the lab test which you want to update")
                lab_Test_Name = input("Lab Test name: ")
                x = search(lab_Test_Name, "Test_Name", "Lab_Test_Record")
                if x == 0:
                    print()
                else:
                    speak("Enter the new data")
                    print("\nEnter the new data")
                    new_lab_Test_Name = input("\nTest name: ")
                    new_price = input("Price: ")
                    sql = "UPDATE Lab_Test_Record SET Test_Name = %s, price = %s WHERE Test_Name = %s"
                    val = (new_lab_Test_Name, new_price, lab_Test_Name)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print("\nData updated successfully !!!")
                    speak("Data updated successfully")
            case "3":
                speak("Enter the name of the doctor whose record you want to update")
                doctor_name = input("Doctor's name: ")
                x = search(doctor_name, "Name", "Doctors_Record")
                if x == 0:
                    print()
                else:
                    speak("Enter the new data")
                    print("\nEnter the new data")
                    new_doctor_name = input("\nDoctor's name: ")
                    new_designation = input("Designation: ")
                    sql = "UPDATE Doctors_Record SET Name = %s, Designation = %s WHERE Name = %s"
                    val = (new_doctor_name, new_designation, doctor_name)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print("\nData updated successfully !!!")
                    speak("Data updated successfully")
            case "4":
                speak("Enter the ambulance number whose record you want to update")
                Number = input("Ambulance number: ")
                x = search(Number, "Number", "Ambulance_Record")
                if x == 0:
                    print()
                else:
                    speak("Enter the new data")
                    print("\nEnter the new data")
                    new_ambulance_type = input("\nAmbulance type:")
                    new_Number = input("Number:")
                    sql = "UPDATE Ambulance_Record SET Ambulance_Type = %s, Number = %s WHERE Number = %s"
                    val = (new_ambulance_type, new_Number, Number)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print("\nData updated successfully !!!")
                    speak("Data updated successfully")
            case "5":
                speak("Redirecting back to the admin menu")
                adminmenu.adminmenu()
            case default:
                print("\nWRONG INPUT !!!")
                speak("Sorry, wrong input")
        print()
        print("Press enter to continue....", end="")
        speak("Press enter to continue")
        choice = input()


def searchdata():
    while (True):
        os.system("cls")
        mycursor.execute("USE medibuddy")
        speak("select the type of data")
        print("\n1. Medicine Recommendation.")
        print("2. Lab Test.")
        print("3. Doctor.")
        print("4. Ambulance.")
        print("5. Admin menu.")
        print("\nEnter your choice: ", end="")
        speak("enter your choice")
        choice = input()
        os.system("cls")
        match choice:
            case "1":
                speak("Enter the problem name you want to search")
                problem_name = input("Problem name: ")
                search(problem_name, "Problem", "Medicine_Recommendation")
            case "2":
                speak("Enter the name of the test you want to search")
                Test_Name = input("Lab Test name: ")
                search(Test_Name, "Test_Name", "Lab_Test_Record")
            case "3":
                speak("Enter the doctor name you want to search")
                doctor_name = input("Doctor's name: ")
                search(doctor_name, "Name", "Doctors_Record")
            case "4":
                speak("Enter the ambulance number you want to search")
                ambulance_no = input("Ambulance number: ")
                search(ambulance_no, "Number", "Ambulance_Record")
            case "5":
                speak("Redirecting back to the admin menu")
                adminmenu.adminmenu()
            case default:
                print("\nWRONG INPUT !!!")
                speak("Sorry, wrong input")
        print()
        print("Press enter to continue....", end="")
        speak("Press enter to continue")
        choice = input()