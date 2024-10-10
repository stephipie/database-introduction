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


# add_student('Abdullah', 25, 'Techstarter')


# create update function to update students data
def update_student(id,  name, age, course):
    cursor.execute('''
    UPDATE students SET name = ?, age = ?, course = ?
    WHERE id = ? 
''', (name, age, course, id))
    conn.commit()
    print(f"updated student with id {id}") 

# create delete function to delete a student from students table
def delete_student(id):
    cursor.execute('''
    DELETE FROM students WHERE id = ?
    ''',(id,))
    conn.commit()
    print(f"Student with id {id} has been deleted.")    

# define main function to get the user input
# user can choose from create, read, update and delete function
def main():
    while True:
        print("\n ------ Studentslist ------ ")
        print("1. Add student")
        print("2. Show student")
        print("3. Update student")
        print("4. Delete student")
        print("5. End the programm")

        choice = input("Please choose one option (1, 2, 3, 4 or 5): ")

        if choice == "1":
            print("Please enter the data o a new student: \n")
            name = input("name: ")
            age = input("age: ")
            course = input("course: ")
            add_student(name, age, course)
        elif choice == "2":
            show_students()
        elif choice == "3":
            print("Please update the data with id: ") 
            id = input("id: ")
            name = input("name: ")
            age = input("age: ")
            course = input("course: ")
            update_student(id, name, age, course)
        elif choice == "4":
            print("Please enter the id of the student you want to delete: ")
            id = input("id: ")
            delete_student()
        elif choice == "5":
            print("Programm is ended. Goodbye.")
            break
        else:
            print("Invalid input. Please choose between 1, 2, 3, 4 or 5")

if __name__ == "__main__":
    main()


