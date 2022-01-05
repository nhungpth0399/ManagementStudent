import pandas as pd
import csv
import Student
import numpy as np
import os.path
from os import path


# Student data
listStudents = []

# create database
infor = ['ID', 'First Name', 'Last Name', 'Date of birth', 'Gender', 'Phone Number', 'Midterm', 'Final', 'GPA']
student_database = 'students.csv'

# with open('students.csv', 'a') as csv_file:
#     writer = csv.DictWriter(csv_file, fieldnames = infor)
#     writer.writeheader()
if path.exists("students.csv") == False:
    with open('students.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['ID', 'First Name', 'Last Name', 'Date of birth', 'Gender', 'Phone Number', 'Midterm', 'Final', 'GPA'])
else:
    with open('students.csv', 'r+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['ID', 'First Name', 'Last Name', 'Date of birth', 'Gender', 'Phone Number', 'Midterm', 'Final', 'GPA'])

def create_student():
    global infor
    global student_database 

    print("--------------------------")
    print("Create Student Information")
    print("--------------------------")

    # Enter ID, if the ID is identical, then re-enter it 
    print("Enter ID:")
    id = Student.get_ID()
    data = pd.read_csv("students.csv")
    x = data[data["ID"] == id]
    check = x.to_numpy()

    while True:
        if check.size != 0:
            print("Database already has this ID.")
            print("Re-enter ID:")
            id = Student.get_ID()  
        else:
            break  
    infor[0] = id


    # Enter Name
    print("Enter First Name:")
    infor[1] = Student.get_fname()

    # Enter Name
    print("Enter Last Name:")
    infor[2] = Student.get_lname()

    # Enter Date of birth
    print("Enter Date of birth:")
    infor[3] = Student.get_dob()

    # Enter Gender
    infor[4] = Student.get_gender()

    # Enter Phone Number
    print("Enter Phone Number: ")
    infor[5] = Student.get_phone()

    # Enter Score
    print("Enter Mid-term Score:")
    midterm = Student.get_midterm()
    infor[6] = midterm

    print("Enter Final Score:")
    final = Student.get_final()  
    infor[7] = final

    gpa = float(midterm * 0.3 + final * 0.7)
    infor[8] = gpa

    # Save information
    listStudents.append(infor)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([infor])

    print("Data saved successfully")
    input("Press any key to continue")
    return

def search_student():
    
    global infor 
    global student_database

    print("--- Search Student ---")
    print("1. Search by ID")
    print("2. Search by Name")
    print("-----------------------")
    #id = int(input("Enter ID no. to search: "))
    data = pd.read_csv("students.csv")
    #data = pd.read_csv("test.csv")
    choice = int(input("Choice: "))
    if choice == 1:
        id = int(input("Enter ID to search: "))
        x = data[data["ID"] == id]
        check = x.to_numpy()

        if check.size != 0:
            print(x)
        else:
            print("ID not found in our database.")
    elif choice == 2:
        na = input("Enter First Name to search: ")
        name = na.title()
        x = data[data["First Name"] == name]
        check = x.to_numpy()

        if check.size == 0:
            print("Name not found in our database.")
        else:
            print(x)
        
    input("Press any key to continue")

def view_students():

    print("--- Student Records ---")

    data = pd.read_csv("students.csv")
    #data = pd.read_csv("test.csv")
    print(data)

    input("Press any key to continue")

def get_student_by_id (id):
    data = pd.read_csv("students.csv")
    x = data[data["ID"] == id]
    check = x.to_numpy()
    return check

def update_student():
    global infor
    global student_database

    print("--- Update Student ---")
    id = int(input("Enter ID to update: "))
    data = pd.read_csv("students.csv")
    check = get_student_by_id(id)
    print(check[0])
    counter = 0

    if check[0] == [] :
        print("Student doesn't exist")
        # updated_data.append(row)
    else:
        print("1. Update First Name")
        print("2. Update Last Name")
        print("3. Update Date of birth")
        print("4. Update Gender")
        print("5. Update Midterm Score")
        print("6. Update Final Score")
        print("-------------------------")
        print("Choice: ")
        choice = int(input())
        if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
            print("Re-enter choice:")
            choice = int(input())
        elif choice  == 1:
            check[0][1] = Student.get_fname()
        elif choice == 2:
            check[0][2] = Student.get_dob()
        elif choice == 3:
            check[0][3] = Student.get_gender()
        elif choice == 4:
            check[0][4] = Student.get_midterm()
        elif choice == 5:
            check[0][5] = Student.get_final()
    #     updated_data.append(check)
        print(check[0])
        # infor = ['ID', 'Name', 'Date of birth', 'Gender', 'Midterm', 'Final', 'GPA']
        # updated_data.append()
    
    # with open(student_database, "r", encoding="utf-8") as f:
    #     reader = csv.reader(f)
    #     counter = 0
    #     for row in reader:
    #         if len(row) > 0:
    #             if id == row[0]:
    #                 index_student = counter
    #                 print("Student Found: at index ",index_student)
    #                 student_data = []
    #                 for field in student_fields:
    #                     value = input("Enter " + field + ": ")
    #                     student_data.append(value)
    #                 updated_data.append(student_data)
    #             else:
    #                 updated_data.append(row)
    #             counter += 1
    # # Check if the record is found or not
    # if index_student is not None:
    #     # with open(student_database, "w", encoding="utf-8") as f:
    #     #     writer = csv.writer(f)
    #     #     writer.writerows(updated_data)
    #     with open(student_database, mode = "a", encoding="utf-8") as f:
    #         writer = csv.writer(f)
    #         writer.writerows(updated_data)
    # else:
    #     print("ID No. not found in our database")

    input("Press any key to continue")

def delete_student():
    global infor
    global student_database

    print("--- Delete Student ---")
    print("1. Delete 1 Student.")
    print("2. Delete All Student.")
    print("-----------------------")
    print("Choice: ")
    choice = int(input())
    while choice != 1 and choice != 2:
        print("Re-enter choice:")
        choice = int(input())

    if choice == 1:
        ID = input("Enter ID no. to delete: ")
        student_found = False
        updated_data = []
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if ID != row[0]:
                        updated_data.append(row)
                        counter += 1
                    else:
                        student_found = True

        if student_found is True:
            with open(student_database, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
            print("ID no. ", ID, "deleted successfully")
        else:
            print("ID No. not found in our database")

    elif choice == 2:
        update_student = []
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(update_student) 

    input("Press any key to continue")

    
def good_student():
    global infor
    global student_database
    data = pd.read_csv("students.csv")
    x = data[data["GPA"] >= 8.0]
    sorted_x = x.sort_values(by='GPA')
    print(sorted_x)
    print("Total Number of Good Student: " + str(len(x)))
    input("Press any key to continue")



