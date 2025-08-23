import sqlite3

# -------------------------------
# Create connection to database
# -------------------------------
def create_connection(db_name="ashlesha.db"):
    """Create a database connection."""
    return sqlite3.connect(db_name)


# -------------------------------
# Create tables
# -------------------------------
def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Department (
            DepartmentID INTEGER PRIMARY KEY,
            DepartmentName TEXT NOT NULL,
            Location TEXT,
            HeadOfDepartment INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Program (
            ProgramID INTEGER PRIMARY KEY,
            ProgramName TEXT NOT NULL,
            Duration INTEGER,
            DepartmentID INTEGER,
            FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Lecturer (
            LecturerID INTEGER PRIMARY KEY,
            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL,
            Email TEXT UNIQUE,
            Phone TEXT,
            DepartmentID INTEGER,
            FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            StudentID INTEGER PRIMARY KEY,
            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL,
            DOB TEXT,
            Gender TEXT,
            Address TEXT,
            Email TEXT UNIQUE,
            Phone TEXT,
            ProgramID INTEGER,
            FOREIGN KEY (ProgramID) REFERENCES Program(ProgramID)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Course (
            CourseID INTEGER PRIMARY KEY,
            CourseName TEXT NOT NULL,
            Credits INTEGER,
            ProgramID INTEGER,
            DepartmentID INTEGER,
            FOREIGN KEY (ProgramID) REFERENCES Program(ProgramID),
            FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Class (
            ClassID INTEGER PRIMARY KEY,
            CourseID INTEGER,
            LecturerID INTEGER,
            Semester TEXT,
            Year INTEGER,
            Schedule TEXT,
            FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
            FOREIGN KEY (LecturerID) REFERENCES Lecturer(LecturerID)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Enrollment (
            EnrollmentID INTEGER PRIMARY KEY,
            StudentID INTEGER,
            ClassID INTEGER,
            Grade TEXT,
            FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
            FOREIGN KEY (ClassID) REFERENCES Class(ClassID)
        )
    """)

    conn.commit()
    print(" All tables created successfully!")


# -------------------------------
# Insert sample data
# -------------------------------


# -------------------------------
# Main Execution
# -------------------------------
