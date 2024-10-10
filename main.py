import sqlite3

# Connect to Sqlite database (if not exist, create)
conn = sqlite3.connect('student.db')

# create cursor object to run sql command
cursor = conn.cursor()

# create table to student.db
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(32) NOT NULL,
    age INTEGER NOT NULL,
    course VARCHAR(32) NOT NULL
    );                                
''')
# create first function to add input (CREATE)
def add_student(name, age, course):
    cursor.execute('''
    INSERT INTO students (name, age, course) VALUES (?, ?, ?)
''', (name, age, course))
    conn.commit()
    print(f"{name} was added.")

# create read function
def show_students():
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    for student in students:
        print(student)  

show_students()

# add_student('stephi', 39, 'Techstarter')    

