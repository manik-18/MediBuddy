import datetime
import os
from random import randint
from voice import speak
import usermenu
import admindata
import mysql.connector
import mail
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


def insert1(table_name, pname, gender, contact, address, gmail, bno, an):
    try:
        mycursor.execute(
            "CREATE TABLE {} (Booking_id int, Name VARCHAR(300), Gender VARCHAR(10),Contact VARCHAR(10),Address VARCHAR(500),Gmail VARCHAR(50),Ambulance_number varchar(100),Booking_date_and_time varchar(30))".format(table_name))
    except:
        print()
    sql = "INSERT INTO {} (Booking_id, Name, Gender, Contact, Address, Gmail, Ambulance_number, Booking_date_and_time) VALUES (%s, %s, %s, %s, %s, %s,%s,%s)".format(
        table_name)
    dt_string = datetime.datetime.now()
    val = (bno, pname, gender, contact, address, gmail, an, dt_string)
    mycursor.execute(sql, val)
    mydb.commit()


def insert2(table_name, pname, gender, contact, address, gmail, bno, tn):
    try:
        mycursor.execute(
            "CREATE TABLE {} (Booking_id int, Name VARCHAR(300), Gender VARCHAR(10),Contact VARCHAR(10),Address VARCHAR(500),Gmail VARCHAR(50),Test_Name varchar(100),Booking_date_and_time varchar(30))".format(table_name))
    except:
        print()
    sql = "INSERT INTO {} (Booking_id, Name, Gender, Contact, Address, Gmail, Test_Name, Booking_date_and_time) VALUES (%s, %s, %s, %s, %s, %s,%s,%s)".format(
        table_name)
    dt_string = datetime.datetime.now()
    val = (bno, pname, gender, contact, address, gmail, tn, dt_string)
    mycursor.execute(sql, val)
    mydb.commit()


def insert3(table_name, pname, gender, contact, address, gmail, bno, dn):
    try:
        mycursor.execute(
            "CREATE TABLE {} (Booking_id int, Name VARCHAR(300), Gender VARCHAR(10),Contact VARCHAR(10),Address VARCHAR(500),Gmail VARCHAR(50),Doctor_Name varchar(100),Booking_date_and_time varchar(30))".format(table_name))
    except:
        print()
    sql = "INSERT INTO {} (Booking_id, Name, Gender, Contact, Address, Gmail, Doctor_Name, Booking_date_and_time) VALUES (%s, %s, %s, %s, %s, %s,%s,%s)".format(
        table_name)
    dt_string = datetime.datetime.now()
    val = (bno, pname, gender, contact, address, gmail, dn, dt_string)
    mycursor.execute(sql, val)
    mydb.commit()


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


def searchbookings():
    while (True):
        os.system("cls")
        mycursor.execute("USE medibuddy")
        speak("select the type of booking")
        print("\n1. Ambulance booking.")
        print("2. Lab Test booking.")
        print("3. Appointment booking.")
        print("4. Bookings menu.")
        print("\nEnter your choice: ", end="")
        speak("Enter your choice")
        choice = input()
        os.system("cls")
        match choice:
            case "1":
                print("Booking id: ", end="")
                speak("Enter the booking id to search booking")
                bookid = input()
                search(bookid, "Booking_id", "Ambulance_Bookings")
            case "2":
                print("Booking id: ", end="")
                speak("Enter the booking id to search booking")
                bookid = input()
                search(bookid, "Booking_id", "Lab_Test_Bookings")
            case "3":
                print("Booking id: ", end="")
                speak("Enter the booking id to search booking")
                bookid = input()
                search(bookid, "Booking_id", "Doctor_Bookings")
            case "4":
                speak("Redirecting back to the bookings menu")
                make_bookings()
            case default:
                print("\nWRONG INPUT !!!")
                speak("Sorry, wrong input")
        print()
        print("Press enter to continue....", end="")
        speak("Press enter to continue")
        choice = input()


def updatebookings():
    while (True):
        os.system("cls")
        mycursor.execute("USE medibuddy")
        speak("select the type of booking")
        print("\n1. Ambulance booking.")
        print("2. Lab Test booking.")
        print("3. Appointment booking.")
        print("4. Bookings menu.")
        print("\nEnter your choice: ", end="")
        speak("Enter your choice")
        choice = input()
        os.system("cls")
        match choice:
            case "1":
                print("Booking id: ", end="")
                speak("Enter the booking id which you want to update")
                bookid = input()
                x = search(bookid, "Booking_id", "Ambulance_Bookings")
                if x == 0:
                    print()
                else:
                    print("\nEnter the new data")
                    speak("Enter the new data")
                    print("\nPatient name: ", end="")
                    speak("Enter the name of the patient")
                    pname = input()
                    if (any(i.isdigit() for i in pname)):
                        print("Invalid Name !!!")
                        speak("Invalid Name")
                    else:
                        print("Gender(Male/Female/Other): ", end="")
                        speak("Enter gender")
                        gender = input()
                        if (gender != 'male' and gender != 'female' and gender != 'other'):
                            print("Invalid Gender !!!")
                            speak("Invalid Gender")
                        else:
                            print("Contact: ", end="")
                            speak("Enter the contact of the patient")
                            contact = input()
                            if (len(contact) != 10):
                                print("Invalid Contact number !!!")
                                speak("Invalid Contact number")
                            else:
                                print("Address: ", end="")
                                speak("Enter the address")
                                address = input()
                                print("Gmail: ", end="")
                                speak("Enter the gmail id")
                                gmail = input()
                                if ((gmail.endswith('@gmail.com'))):
                                    sql = "UPDATE Ambulance_Bookings SET Name= %s, Gender= %s, Contact= %s, Address= %s, Gmail= %s WHERE Booking_id = %s"
                                    val = (pname, gender, contact,
                                           address, gmail, bookid)
                                    mycursor.execute(sql, val)
                                    mydb.commit()
                                    print("\nData updated successfully !!!")
                                    speak("Data updated successfully")
                                else:
                                    print("Invalid email !!!")
                                    speak("Invalid email")
            case "2":
                print("Booking id: ", end="")
                speak("Enter the booking id which you want to update")
                bookid = input()
                x = search(bookid, "Booking_id", "Lab_Test_Bookings")
                if x == 0:
                    print()
                else:
                    print("\nEnter the new data")
                    speak("Enter the new data")
                    print("\nPatient name: ", end="")
                    speak("Enter the name of the patient")
                    pname = input()
                    if (any(i.isdigit() for i in pname)):
                        print("Invalid Name !!!")
                        speak("Invalid Name")
                    else:
                        print("Gender(Male/Female/Other): ", end="")
                        speak("Enter gender")
                        gender = input()
                        if (gender != 'male' and gender != 'female' and gender != 'other'):
                            print("Invalid Gender !!!")
                            speak("Invalid Gender")
                        else:
                            print("Contact: ", end="")
                            speak("Enter the contact of the patient")
                            contact = input()
                            if (len(contact) != 10):
                                print("Invalid Contact number !!!")
                                speak("Invalid Contact number")
                            else:
                                print("Address: ", end="")
                                speak("Enter the address")
                                address = input()
                                print("Gmail: ", end="")
                                speak("Enter the gmail id")
                                gmail = input()
                                if ((gmail.endswith('@gmail.com'))):
                                    sql = "UPDATE Lab_Test_Bookings SET Name= %s, Gender= %s, Contact= %s, Address= %s, Gmail= %s WHERE Booking_id = %s"
                                    val = (pname, gender, contact,
                                           address, gmail, bookid)
                                    mycursor.execute(sql, val)
                                    mydb.commit()
                                    print("\nData updated successfully !!!")
                                    speak("Data updated successfully")
                                else:
                                    print("Invalid email !!!")
                                    speak("Invalid email")
            case "3":
                print("Booking id: ", end="")
                speak("Enter the booking id which you want to update")
                bookid = input()
                x = search(bookid, "Booking_id", "Doctor_Bookings")
                if x == 0:
                    print()
                else:
                    print("\nEnter the new data")
                    speak("Enter the new data")
                    print("\nPatient name: ", end="")
                    speak("Enter the name of the patient")
                    pname = input()
                    if (any(i.isdigit() for i in pname)):
                        print("Invalid Name !!!")
                        speak("Invalid Name")
                    else:
                        print("Gender(Male/Female/Other): ", end="")
                        speak("Enter gender")
                        gender = input()
                        if (gender != 'male' and gender != 'female' and gender != 'other'):
                            print("Invalid Gender !!!")
                            speak("Invalid Gender")
                        else:
                            print("Contact: ", end="")
                            speak("Enter the contact of the patient")
                            contact = input()
                            if (len(contact) != 10):
                                print("Invalid Contact number !!!")
                                speak("Invalid Contact number")
                            else:
                                print("Address: ", end="")
                                speak("Enter the address")
                                address = input()
                                print("Gmail: ", end="")
                                speak("Enter the gmail id")
                                gmail = input()
                                if ((gmail.endswith('@gmail.com'))):
                                    sql = "UPDATE Doctor_Bookings SET Name= %s, Gender= %s, Contact= %s, Address= %s, Gmail= %s WHERE Booking_id = %s"
                                    val = (pname, gender, contact,
                                           address, gmail, bookid)
                                    mycursor.execute(sql, val)
                                    mydb.commit()
                                    print("\nData updated successfully !!!")
                                    speak("Data updated successfully")
                                else:
                                    print("Invalid email !!!")
                                    speak("Invalid email")

            case "4":
                speak("Redirecting back to the bookings menu")
                make_bookings()
            case default:
                print("\nWRONG INPUT !!!")
                speak("Sorry, wrong input")
        print()
        print("Press enter to continue....", end="")
        speak("Press enter to continue")
        choice = input()


def deletebookings():
    while (True):
        os.system("cls")
        mycursor.execute("USE medibuddy")
        speak("select the type of booking")
        print("\n1. Ambulance booking.")
        print("2. Lab Test booking.")
        print("3. Appointment booking.")
        print("4. Bookings menu.")
        print("\nEnter your choice: ", end="")
        speak("Enter your choice")
        choice = input()
        os.system("cls")
        match choice:
            case "1":
                print("Booking id: ", end="")
                speak("Enter the booking id which you want to delete")
                bookid = input()
                x = search(bookid, "Booking_id", "Ambulance_Bookings")
                if x == 0:
                    print()
                else:
                    mycursor.execute(
                        "DELETE FROM Ambulance_Bookings WHERE Booking_id='{}'".format(bookid))
                    mydb.commit()
                    print("\nData deleted successfully !!!")
                    speak("Data deleted successfully")

            case "2":
                print("Booking id: ", end="")
                speak("Enter the booking id which you want to delete")
                bookid = input()
                x = search(bookid, "Booking_id", "Lab_Test_Bookings")
                if x == 0:
                    print()
                else:
                    mycursor.execute(
                        "DELETE FROM Lab_Test_Bookings WHERE Booking_id='{}'".format(bookid))
                    mydb.commit()
                    print("\nData deleted successfully !!!")
                    speak("Data deleted successfully")
            case "3":
                print("Booking id: ", end="")
                speak("Enter the booking id which you want to delete")
                bookid = input()
                x = search(bookid, "Booking_id", "Doctor_Bookings")
                if x == 0:
                    print()
                else:
                    mycursor.execute(
                        "DELETE FROM Doctor_Bookings WHERE Booking_id='{}'".format(bookid))
                    mydb.commit()
                    print("\nData deleted successfully !!!")
                    speak("Data deleted successfully")

            case "4":
                speak("Redirecting back to the bookings menu")
                make_bookings()
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
        speak("Data found")
        return 1
    except:
        print("Data not found !!!")
        speak("Data not found")
        return 0


def servicebooking(opt, pname, gender, contact, address, gmail):
    os.system("cls")
    mycursor.execute("USE medibuddy")
    if opt == 1:
        c = display("Ambulance_Record", "Ambulance_Type", "Number")
        if (c == 1):
            print("\nAmbulance number: ", end="")
            speak("Enter ambulance number")
            an = input()
            mycursor.execute(
                "SELECT Number FROM Ambulance_Record WHERE Number = '{}'".format(an))
            myresult = mycursor.fetchall()
            if myresult == []:
                os.system("cls")
                speak("Data not found")
                speak("Redirecting back to booking menu")
                make_bookings()
            else:
                print("\nBooking successfull !!! Kindly check your mail.....")
                speak("your booking has been successfull kindly check your mail")
                bno = randint(111111, 999999)
                insert1("Ambulance_Bookings", pname,
                        gender, contact, address, gmail, bno, an)
                msg = """BOOKING SUCCESSFULL !!!
                Thank you {} for the booking.
                Your ambulance bearing number
                {} has been booked successfully
                and it will reaches you within
                10 minutes.

                *** BOOKING DETAILS ***
                    
                BOOKING ID: {}
                PATIENT NAME: {}
                GENDER: {}
                CONTACT: {}
                ADDRESS: {}

                With Regards,
                medibuddy
                    """.format(pname, an, bno, pname, gender, contact, address)
                mail.mail("receiver_mail_id", msg)
    elif opt == 2:
        c = display("Lab_Test_Record", "Test_Name", "Price")
        if (c == 1):
            print("Test name: ", end="")
            speak("Enter Test name")
            tn = input()
            mycursor.execute(
                "SELECT Test_Name FROM Lab_Test_Record WHERE Test_Name = '{}'".format(tn))
            myresult = mycursor.fetchall()
            if myresult == []:
                os.system("cls")
                speak("Data not found")
                speak("Redirecting back to booking menu")
                make_bookings()
            else:
                print("\nBooking successfull !!! Kindly check your mail.....")
                speak("your booking has been successfull kindly check your mail")
                bno = randint(111111, 999999)
                insert2("Lab_Test_Bookings", pname,
                        gender, contact, address, gmail, bno, tn)
                msg = """BOOKING SUCCESSFULL !!!
                Thank you {} for the booking.
                Your lab test ({}) booking has been confirmed
                our agent will reach your address within 90
                minutes with all the material. Please be 
                available at your location.

                *** BOOKING DETAILS ***
                    
                BOOKING ID: {}
                PATIENT NAME: {}
                GENDER: {}
                CONTACT: {}
                ADDRESS: {}

                With Regards,
                medibuddy
                    """.format(pname, tn, bno, pname, gender, contact, address)
                mail.mail("receiver_mail_id", msg)
    else:
        c = display("Doctors_Record", "Name", "Designation")
        if (c == 1):
            print("\nDoctor name: ", end="")
            speak("Enter the name of the doctor")
            dn = input()
            mycursor.execute(
                "SELECT Name FROM Doctors_Record WHERE Name = '{}'".format(dn))
            myresult = mycursor.fetchall()
            if myresult == []:
                os.system("cls")
                speak("Data not found")
                speak("Redirecting back to booking menu")
                make_bookings()
            else:
                print("\nBooking successfull !!! Kindly check your mail.....")
                speak("your booking has been successfull kindly check your mail")
                bno = randint(111111, 999999)
                insert3("Doctor_Bookings", pname,
                        gender, contact, address, gmail, bno, dn)
                msg = """BOOKING SUCCESSFULL !!!
                Thank you {} for the booking.
                Your appointment with doctor {} has been booked successfully.
                The doctor will connect with you soon.

                *** BOOKING DETAILS ***
                
                BOOKING ID: {}
                PATIENT NAME: {}
                GENDER: {}
                CONTACT: {}
                ADDRESS: {}

                With Regards,
                medibuddy
                    """.format(pname, dn, bno, pname, gender, contact, address)
                mail.mail("receiver_mail_id", msg)


def book(option):
    os.system("cls")
    print("Patient name: ", end="")
    speak("Enter the patient name")
    patient_name = input()
    if (any(i.isdigit() for i in patient_name)):
        print("Invalid Name !!!")
        speak("Invalid Name")
    else:
        print("Gender(Male/Female/Other): ", end="")
        speak("Enter the gender")
        gender = input().lower()
        if (gender != 'male' and gender != 'female' and gender != 'other'):
            print("Invalid Gender !!!")
            speak("Invalid Gender")
        else:
            print("Contact number: ", end="")
            speak("Enter your contact number: ")
            contact_number = input()
            if (len(contact_number) != 10):
                print("Invalid Contact number !!!")
                speak("Invalid Contact number")
            else:
                print("Gmail address: ", end="")
                speak("enter your gmail")
                gmail = input()
                if ((gmail.endswith('@gmail.com'))):
                    print("Address: ", end="")
                    speak("enter your address")
                    address = input()
                    servicebooking(option, patient_name, gender,
                                   contact_number, address, gmail)
                else:
                    print("Invalid email !!!")
                    speak("Invalid email")


def make_bookings():
    while True:
        os.system("cls")
        mycursor.execute("USE medibuddy")
        print("\t\t\t\n***** BOOKINGS *****")
        speak("Welcome to Booking section, What you want to do?")
        print("\n1. Make a booking.")
        print("2. Delete a booking.")
        print("3. Update a booking.")
        print("4. Search a booking.")
        print("5. User menu.")
        print("\nEnter your choice: ", end="")
        speak("Enter your choice")
        choice = input()
        match choice:
            case "1":
                makebookings()
            case "2":
                deletebookings()
            case "3":
                updatebookings()
            case "4":
                searchbookings()
            case "5":
                speak("Redirecting back to the user menu")
                usermenu.usermenu()
            case default:
                print("\nWRONG INPUT !!!")
                speak("Sorry, wrong input")
        print()
        print("Press enter to continue....", end="")
        speak("Press enter to continue")
        choice = input()


def makebookings():
    while True:
        os.system("cls")
        mycursor.execute("USE medibuddy")
        print("\t\t\t\n***** MAKE BOOKINGS *****")
        speak("which booking you want to make")
        print("\n1. Ambulance booking.")
        print("2. Lab Test booking.")
        print("3. Appointment booking.")
        print("4. Bookings menu.")
        print("\nEnter your choice: ", end="")
        speak("Enter your choice")
        choice = input()
        match choice:
            case "1":
                book(1)
            case "2":
                book(2)
            case "3":
                book(3)
            case "4":
                speak("Redirecting back to the bookings menu")
                make_bookings()
            case default:
                print("\nWRONG INPUT !!!")
                speak("Sorry, wrong input")
        print()
        print("Press enter to continue....", end="")
        speak("Press enter to continue")
        choice = input()
