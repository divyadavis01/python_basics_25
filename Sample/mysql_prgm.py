import pymysql
connection=pymysql.connect(user="root",host="localhost",password="root123",database="clinic",cursorclass=pymysql.cursors.DictCursor)

cursor=connection.cursor()

def addDoctor():
    name=input("Enter the doctor name: ")
    designation=input("Enter the designation: ")
    date=input("Enther the join date: ")
    salary=input("Enter the salary: ")
    department=input("Enther the department: ")
    cursor.execute(f"INSERT INTO doctor(name, designation, date, salary, department)VALUES('{name}','{designation}','{date}',{salary},{department})")
    print("New doctor added successfully")
    connection.commit()    # to save

def displayDoctorDetails(doc_id):
    cursor.execute(f"SELECT * FROM doctor WHERE doc_id={doc_id}")
    if cursor.rowcount>0:
        doctor=cursor.fetchone()
        print("\nCurrent Details:")
        print("Name :",doctor.get("name"))
        print("Designation: ",doctor.get("designation"))
        print("Join Date: ",doctor.get("date"))
        print("Department: ",doctor.get("department"))
        print("Salary: ",doctor.get("salary"))
    else:
        print("No data found")


def viewDepartment():
    cursor.execute("SELECT * FROM department;")
    print("ID    Department")
    for dept in cursor.fetchall():
        print(f"{dept.get('dept_id')}    {dept.get('name')}")

def updateDoctor():
    doc_id=int(input("Enter the id of the doctor to be updated:"))
    displayDoctorDetails(doc_id)
    print("Field to be updated: ")
    print("1.Department\n2.Designation\n3.Salary\n4.Name\n5.Join Date")
    choice=int(input("Enter your choice: "))
    if choice==1:
        viewDepartment()
        dept_id=int(input("Enter new department id: "))
        cursor.execute(f"UPDATE doctor SET department={dept_id} WHERE doc_id={doc_id}")
        print("Department updated successfully")
        connection.commit()
    elif choice==2:
        designation=input("Enter the new designation: ")
        cursor.execute(f"UPDATE doctor SET designation='{designation}' WHERE doc_id={doc_id}")
        print("Designation updated successfully")
        connection.commit()
    elif choice==3:
        salary=input("Enter the new salary: ")
        cursor.execute(f"UPDATE doctor SET salary={salary} WHERE doc_id={doc_id}")
        print("Salary updated successfully")
        connection.commit()
    elif choice==4:
        name=input("Enter the updated name of the doctor: ")
        cursor.execute(f"UPDATE doctor SET name='{name}' WHERE doc_id={doc_id}")
        print("Doctor name updated successfully")
        connection.commit()
    elif choice==5:
        date=input("Enter the updateded join date: ")
        cursor.execute(f"UPDATE doctor SET date='{date}' WHERE doc_id={doc_id}")
        print("Join date updated successfully")
        connection.commit()
    else:
        print(f"Choice {choice} does not exist")

def viewDoctors():
    cursor.execute("SELECT * FROM doctor")
    doc=cursor.fetchall()
    print("Id    name    designation     join_date    department     salary")
    for dr in doc:
        print(f"{dr['doc_id']}       {dr['name']}      {dr['designation']}   {dr['date']}    {dr['department']}   {dr['salary']}")

def deleteDoctor():
    doc_id=int(input("Enter the id of the doctor to be deleted"))
    cursor.execute(f"DELETE FROM doctor WHERE doc_id={doc_id}")
    print(f"Deleted doctor with id {doc_id}")
    connection.commit()

while True:
    print()
    print("1.Add Doctor\n2.Update Doctor Details\n3.View All Doctors\n4.Delete Doctor\n5.Exit")
    choice=int(input("Enter your choice :"))
    if choice==1:
        addDoctor()
    elif choice==2:
        updateDoctor()
    elif choice==3:
        viewDoctors()
    elif choice==4:
        deleteDoctor()
    elif choice==5:
        break
    else:
        print(f"Choice {choice} does not exist")
    
