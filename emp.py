import mysql.connector as m1

con = m1.connect(username="root", host="localhost", password="")

if con.is_connected():
    print("Successfully connected to the database server")

c = con.cursor()

def Create_database():
    #c.execute("CREATE DATABASE employeeinformationsystem")
    
    c.execute("USE employeeinformationsystem")
    
    q=("""
    CREATE TABLE  Emp1 (
        EId INT PRIMARY KEY,
        Ename VARCHAR(50),
        EmailID VARCHAR(100),
        Phone VARCHAR(15),
        Address VARCHAR(255),
        Designation VARCHAR(50),
        DateofBirth DATE
    )
    """)
    #c.execute(q)
    
    q1=("""
    CREATE TABLE  Emp2 (
        EId INT PRIMARY KEY,
        BasicSalary FLOAT,
        TA FLOAT,
        DA FLOAT,
        Bonus FLOAT
    )
    """)
    #c.execute(q1)
 
    q2=("""
    INSERT INTO Emp1 (EId, Ename, EmailID, Phone, Address, Designation, DateofBirth)
    VALUES 
    (1, 'John Doe', 'john.doe@example.com', '1234567890', '123 Elm St', 'Software Engineer', '1990-05-15'),
    (2, 'Jane Smith', 'jane.smith@example.com', '0987654321', '456 Oak St', 'Data Analyst', '1985-07-22'),
    (3, 'Alice Johnson', 'alice.johnson@example.com', '2345678901', '789 Pine St', 'HR Manager', '1988-11-03'),
    (4, 'Bob Brown', 'bob.brown@example.com', '3456789012', '101 Maple St', 'Marketing Specialist', '1992-03-25'),
    (5, 'Charlie Davis', 'charlie.davis@example.com', '4567890123', '202 Birch St', 'Sales Manager', '1987-06-30'),
    (6, 'Diana Evans', 'diana.evans@example.com', '5678901234', '303 Cedar St', 'Product Manager', '1991-09-12'),
    (7, 'Ethan Fisher', 'ethan.fisher@example.com', '6789012345', '404 Fir St', 'Systems Analyst', '1984-12-05'),
    (8, 'Fiona Green', 'fiona.green@example.com', '7890123456', '505 Spruce St', 'UI/UX Designer', '1993-04-18'),
    (9, 'George Harris', 'george.harris@example.com', '8901234567', '606 Redwood St', 'Network Engineer', '1986-08-22'),
    (10, 'Hannah Irwin', 'hannah.irwin@example.com', '9012345678', '707 Willow St', 'Business Analyst', '1989-01-25')
    """)
    #c.execute(q2)
    
    q3=("""
    INSERT INTO Emp2 (EId, BasicSalary, TA, DA, Bonus)
    VALUES 
    (1, 60000.00, 2000.00, 1500.00, 5000.00),
    (2, 50000.00, 1500.00, 1200.00, 3000.00),
    (3, 70000.00, 2500.00, 1800.00, 6000.00),
    (4, 55000.00, 1800.00, 1300.00, 3500.00),
    (5, 65000.00, 2200.00, 1600.00, 5500.00),
    (6, 58000.00, 1700.00, 1400.00, 3200.00),
    (7, 72000.00, 2600.00, 1900.00, 6200.00),
    (8, 54000.00, 1900.00, 1250.00, 3400.00),
    (9, 60000.00, 2100.00, 1550.00, 5000.00),
    (10, 57000.00, 1800.00, 1350.00, 3300.00)
    """)
    
    #c.execute(q3)
    
def check_employee_name(employee_name):
    sql = 'SELECT * FROM Emp1 WHERE Ename=%s'
    data = (employee_name,)
    c.execute(sql, data)
    employee = c.fetchone()
    if employee:
        return True  
    else:
        return False  

def check_employee(employee_id):
    sql = 'SELECT * FROM Emp1 WHERE EId=%s'
    data = (employee_id,)
    c.execute(sql, data)
    employee = c.fetchone()
    if employee:
        return True  
    else:
        return False
    

#function to add employees
def Add_Employ():
    print("\n-->> Add Employee Record <<--\n")
    
    Id = input("Enter Employee Id: ")
    if check_employee(Id):
        print("Employee ID already exists. Please use a different ID.")
        return choice()
    
    Name = input("Enter Employee Name: ")

    
    Email_Id = input("Enter Employee Email ID: ")
    Phone_no = input("Enter Employee Phone No.: ")
    Address = input("Enter Employee Address: ")
    Designation = input("Enter Employee's Designation: ")
    DOB = input("Enter Employee's Date of Birth (YYYY-MM-DD): ")
    sql = 'INSERT INTO Emp1  VALUES (%s,%s,%s,%s,%s,%s,%s)'
    data = (Id, Name, Email_Id, Phone_no, Address, Designation, DOB)
    c.execute(sql, data)

    BasicSalary = float(input("Enter Employee Basic Salary: "))
    TA = BasicSalary * 0.10
    DA = BasicSalary * 0.15

    Bonus = float(input("Enter Employee Bonus: "))


    sql = 'INSERT INTO Emp2  VALUES (%s,%s,%s,%s,%s)'
    A=(Id, BasicSalary, TA, DA, Bonus)
    c.execute(sql,A )
    con.commit()
    print("Successfully Added Employee Record")
    print("DO YOU WANT TO ADD MORE EMPLOYEES?")
    ch=input("y/n   ")
    if ch=="y" or ch=="Y":
        Add_Employ()
    else:
        choice()

#function to display records of employee
def Display_Employ():
    print("\n-->> Display Employee Records <<--\n")
    query = """
    SELECT Emp1.EId, Ename, EmailID, Phone, Address, Designation, DateofBirth, 
           BasicSalary, TA, DA, Bonus
    FROM Emp1, Emp2  WHERE Emp1.EId = Emp2.EId
    """
    c.execute(query)
    r = c.fetchall()
    for i in r:
        print("Employee Id: ", i[0])
        print("Employee Name: ", i[1])
        print("Employee Email Id: ", i[2])
        print("Employee Phone No.: ", i[3])
        print("Employee Address: ", i[4])
        print("Employee Designation: ", i[5])
        print("Employee Date of Birth: ", i[6])
        print("Employee Basic Salary: ", i[7])
        print("Employee TA: ", i[8])
        print("Employee DA: ", i[9])
        print("Employee Bonus: ", i[10])
        print("\n")
    choice() 

#function to update records
def Update_Employ():
    print("\n-->> Update Employee Record <<--\n")
    Id = input("Enter Employee Id: ")
    if not check_employee(Id):
        print("Employee Record does not exist. Try again.")
        return choice() 
    else:
        Email_Id = input("Enter Employee Email ID: ")
        Phone_no = input("Enter Employee Phone No.: ")
        Address = input("Enter Employee Address: ")
        
        sql = 'UPDATE Emp1 SET EmailID = %s, Phone = %s, Address = %s WHERE EId = %s'
        data = (Email_Id, Phone_no, Address, Id)
        c.execute(sql, data)
        con.commit()
        print("Updated Employee Record")
        ch=input("do you want to update record of another employee? ")
        if ch=="y" or ch=="Y":
            Update_Employ()
        else:
            choice()

#function to promote employee

def Promote_Employ():
    print("\n-->> Promote Employee Record <<--\n")
    Id = input("Enter Employee Id: ")
    if not check_employee(Id):
        print("Employee Record does not exist. Try again.")
        return choice() 
    else:
        Amount = float(input("Enter Increase in Salary: "))
        sql = 'SELECT BasicSalary FROM Emp2 WHERE EId=%s'
        data = (Id,)
        c.execute(sql, data)
        r = c.fetchone()
        if r:
            new_salary = r[0] + Amount
            sql = 'UPDATE Emp2 SET BasicSalary = %s WHERE EId = %s'
            c.execute(sql, (new_salary, Id))
            con.commit()
            print("Employee Promoted")
        else:
            print("Employee does not have salary details.")
        ch=input("do you want to promote another employee? ")
        if ch=="y" or ch=="Y":
            Promote_Employ()
        else:
            choice()

#function to remove employee

def Remove_Employ():
    print("\n-->> Remove Employee Record <<--\n")
    Id = input("Enter Employee Id: ")
    if not check_employee(Id):
        print("Employee Record does not exist. Try again.")
        return choice() 
    else:
        sql = 'DELETE FROM Emp1 WHERE EId = %s'
        data = (Id,)
        c.execute(sql, data)
        
        sql = 'DELETE FROM Emp2 WHERE EId = %s'
        c.execute(sql, data)
        
        con.commit()
        print("Employee Removed")
    ch=input("do you want to REMOVE another employee? ")
    if ch=="y" or ch=="Y":
            Remove_Employ()
    else:
            choice()

#function to search for employee
def fetch_all_employees():
    
    query = """
    SELECT Emp1.EId, Ename, EmailID, Phone, Address, Designation, DateofBirth, 
           BasicSalary, TA, DA, Bonus
    FROM Emp1,Emp2 where Emp1.EId = Emp2.EId
    """
    c.execute(query)
    employees = c.fetchall()
    if employees:
        for emp in employees:
            print(emp)
    else:
        print("No employees found.")
    input("Press Enter to return to the main menu.")


def search_employee_by_eid():
    try:
        eid = int(input("Enter EId to search for: "))

        query = """
        SELECT Emp1.EId, Ename, EmailID, Phone, Address, Designation, DateofBirth, 
               BasicSalary, TA, DA, Bonus
        FROM Emp1, Emp2 WHERE Emp1.EId = Emp2.EId
        AND Emp1.EId = %s
        """
        c.execute(query, (eid,))
        employee = c.fetchone()
        if employee:
            print(f"Employee Details: {employee}")
        else:
            print("No employee found with the given EId.")
    except ValueError:
        print("Invalid input. Please enter a numeric EId.")
    ch=input("do you want to Search record of another employee? ")
    if ch=="y" or ch=="Y":
        search_employee_by_eid()
    else:
            choice()



####main menu###
def intro():
    print("**" * 7)
    print("--" * 10, ">> Employee Information System <<", 10 * "--")
    print("--" * 10, "   >> Including Salary System <<   ", 10 * "--")
    print("**" * 7)
    print()
    
def choice():
    print()
    print("--"*3,"CHOOSE","--"*3) 
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. END\n")
    print("-->> Choice Options: [1/2/3/4/5/6/7] <<--")
          
def menu():
    ch = int(input("Enter your Choice: "))
    if ch == 1:
        Add_Employ()
    elif ch == 2:
        Display_Employ()
    elif ch == 3:
        Update_Employ()
    elif ch == 4:
        Promote_Employ()
    elif ch == 5:
        Remove_Employ()
    elif ch == 6:
        search_employee_by_eid()
    elif ch == 7:
        print("THANK YOU FOR RUNNING THE PROJECT")
        print("PROJECT HAS ENDED SUCCESSFULLY.")
        print("Have A Nice Day :)")
        c.close()
        con.close()
        return
    else:
        print("Invalid Choice!")
        input("Kindly choose another number.")
    menu()



# main     
Create_database()
intro()
choice() 
menu()
