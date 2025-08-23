from table_create import create_connection
import sqlite3


db_name = "ashlesha.db"

def create_connection():
    return sqlite3.connect(db_name)

def insert_sample_data(conn):
    cursor = conn.cursor()

    # Insert into Department
    cursor.execute("INSERT INTO Department (DepartmentName, Location) VALUES (?, ?)", 
                   ("Computer Science", "Building A"))
    cursor.execute("INSERT INTO Department (DepartmentName, Location) VALUES (?, ?)", 
                   ("Business", "Building B"))

    # Insert into Program
    cursor.execute("INSERT INTO Program (ProgramName, Duration, DepartmentID) VALUES (?, ?, ?)", 
                   ("BSc Computer Science", 3, 1))
    cursor.execute("INSERT INTO Program (ProgramName, Duration, DepartmentID) VALUES (?, ?, ?)", 
                   ("BBA Business Administration", 3, 2))

    # Insert into Lecturer
    cursor.execute("INSERT INTO Lecturer (FirstName, LastName, Email, Phone, DepartmentID) VALUES (?, ?, ?, ?, ?)",
                   ("Alice", "Johnson", "alica@ybcollege.ac.nz", "1234567890", 1))
    cursor.execute("INSERT INTO Lecturer (FirstName, LastName, Email, Phone, DepartmentID) VALUES (?, ?, ?, ?, ?)",
                   ("Bob", "Smith", "bobmarley@ybcollege.ac.nz", "0987654321", 2))

    # Insert into Student
    cursor.execute("INSERT INTO Student (FirstName, LastName, DOB, Gender, Address, Email, Phone, ProgramID) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   ("John", "Doe", "2000-05-10", "M", "123 Street", "johnhones.doe@email.com", "5551234", 1))
    cursor.execute("INSERT INTO Student (FirstName, LastName, DOB, Gender, Address, Email, Phone, ProgramID) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   ("Jane", "Smith", "2001-07-15", "F", "456 Avenue", "janesmith@email.com", "5555678", 2))

    # Insert into Course
    cursor.execute("INSERT INTO Course (CourseName, Credits, ProgramID, DepartmentID) VALUES (?, ?, ?, ?)",
                   ("Database Systems", 15, 1, 1))
    cursor.execute("INSERT INTO Course (CourseName, Credits, ProgramID, DepartmentID) VALUES (?, ?, ?, ?)",
                   ("Marketing Basics", 15, 2, 2))

    # Insert into Class
    cursor.execute("INSERT INTO Class (CourseID, LecturerID, Semester, Year, Schedule) VALUES (?, ?, ?, ?, ?)",
                   (1, 1, "Semester 1", 2025, "Mon 9-11"))
    cursor.execute("INSERT INTO Class (CourseID, LecturerID, Semester, Year, Schedule) VALUES (?, ?, ?, ?, ?)",
                   (2, 2, "Semester 1", 2025, "Tue 10-12"))

    # Insert into Enrollment
    cursor.execute("INSERT INTO Enrollment (StudentID, ClassID, Grade) VALUES (?, ?, ?)", 
                   (1, 1, "A"))
    cursor.execute("INSERT INTO Enrollment (StudentID, ClassID, Grade) VALUES (?, ?, ?)", 
                   (2, 2, "B"))
    


    conn.commit()
    print(" Sample data inserted successfully!")

def view_data(conn, table_name):
    """
    View all data from a specific table.

    :param conn: SQLite connection object
    :param table_name: Name of the table to view
    """
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        if rows:
            # Get column names
            col_names = [description[0] for description in cursor.description]
            print(f"\n--- Data from {table_name} ---")
            print("\t".join(col_names))
            print("-" * 30)
            for row in rows:
                print("\t".join(str(item) for item in row))
        else:
            print(f"No data found in table {table_name}.")

    except sqlite3.Error as e:
        print(f"Error reading table {table_name}: {e}")

def view_all_tables(conn):
    tables = ["Department", "Program", "Student", "Lecturer", "Course", "Class", "Enrollment"]
    for t in tables:
        view_data(conn, t)

    view_all_tables(conn)
