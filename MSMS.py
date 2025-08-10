# MSMS.py
# Frag 1.1 Data Models

class Student:  # Helps make a class for students
    """A blueprint for student objects. Holds their info."""  # Tell what the class does
    def __init__(self, student_id, name):  # Set up a new student
        self.id = student_id  # Save the student's ID
        self.name = name  # Save the student's name
        self.enrolled_in = []  # Make an empty list for instruments

class Teacher:  # Make a class for teachers
    """A blueprint for teacher objects."""  # Tell what the class does
    def __init__(self, teacher_id, name, speciality):  # Set up a new teacher
        self.id = teacher_id  # Save the teacher's ID
        self.name = name  # Save the teacher's name
        self.speciality = speciality  # Save the teacher's speciality

# Frag 1.1 In-Memory Databases

student_db = []  # List to hold all students
teacher_db = []  # List to hold all teachers
next_student_id = 1  # Starting number for student IDs
next_teacher_id = 1  # Starting number for teacher IDs

# Frag 1.2 Core Helper Functions

def add_teacher(name, speciality):  # Add a new teacher
    """Makes a Teacher and adds it to the list."""  # Tell what it does
    global next_teacher_id  # Use the ID from outside
    new_teacher = Teacher(next_teacher_id, name, speciality)  # Make a new teacher
    teacher_db.append(new_teacher)  # Add to the teacher list
    next_teacher_id = next_teacher_id + 1  # Add 1 to the ID
    print("Teacher", name, "added.")  # Show it worked

def list_students():  # Show all students
    """Shows all students."""  # Tell what it does
    print("\nStudent List")  # Print a title
    if not student_db:  # Check if list is empty
        print("No students.")  # Say if no students
        return  # Stop here
    for student in student_db:  # Look at each student
        print("ID:", student.id, "Name:", student.name, "Instruments:", student.enrolled_in)  # Show details

def list_teachers():  # Show all teachers
    """Shows all teachers."""  # Tell what it does
    print("\nTeacher List")  # Print a title
    if not teacher_db:  # Check if list is empty
        print("No teachers.")  # Say if no teachers
        return  # Stop here
    for teacher in teacher_db:  # Look at each teacher
        print("ID:", teacher.id, "Name:", teacher.name, "Speciality:", teacher.speciality)  # Show details

def find_students(term):  # Find students by name
    """Looks for students by name."""  # Tell what it does
    print("\nLooking for students with", term)  # Print what we're looking for
    results = []  # Empty list for matches
    for student in student_db:  # Check each student
        if term.lower() in student.name.lower():  # See if name matches
            results.append(student)  # Add to list if match
    if not results:  # If no matches
        print("No students found.")  # Say no match
    else:  # If there are matches
        for student in results:  # Check each match
            print("ID:", student.id, "Name:", student.name, "Instruments:", student.enrolled_in)  # Show details

def find_teachers(term):  # Find teachers by name or speciality
    """Looks for teachers by name or speciality."""  # Tell what it does
    print("\nLooking for teachers with", term)  # Print what we're looking for
    results = []  # Empty list for matches
    for teacher in teacher_db:  # Check each teacher
        if term.lower() in teacher.name.lower() or term.lower() in teacher.speciality.lower():  # See if match
            results.append(teacher)  # Add to list if match
    if not results:  # If no matches
        print("No teachers found.")  # Say no match
    else:  # If there are matches
        for teacher in results:  # Check each match
            print("ID:", teacher.id, "Name:", teacher.name, "Speciality:", teacher.speciality)  # Show details

# Frag 1.3 Front Desk Functions

def find_student_by_id(student_id):  # Find a student by ID
    """Finds one student by their ID."""  # Tell what it does
    for student in student_db:  # Look at each student
        if student.id == student_id:  # Check if ID matches
            return student  # Give back the student
    return None  # Give nothing if not found

def front_desk_register(name, instrument):  # Register a new student
    """Adds a student and enrolls them."""  # Tell what it does
    global next_student_id  # Use the ID from outside
    new_student = Student(next_student_id, name)  # Make a new student
    student_db.append(new_student)  # Add to student list
    next_student_id = next_student_id + 1  # Add 1 to the ID
    front_desk_enrol(new_student.id, instrument)  # Enroll them
    print("Registered", name, "with instrument", instrument)  # Show it worked

def front_desk_enrol(student_id, instrument):  # Enroll a student
    """Adds an instrument to a student."""  # Tell what it does
    student = find_student_by_id(student_id)  # Find the student
    if student:  # If found
        student.enrolled_in.append(instrument)  # Add the instrument
        print("Enrolled ID", student_id, "in", instrument)  # Show it worked
    else:  # If not found
        print("Error: ID", student_id, "not found.")  # Show error

def front_desk_lookup(term):  # Look up students or teachers
    """Searches for students or teachers."""  # Tell what it does
    print("\nLooking for", term)  # Print what we're searching
    find_students(term)  # Search students
    find_teachers(term)  # Search teachers

# Frag 1.4 Main Application

def main():  # Main function to run the program
    """Runs the menu for the program."""  # Tell what it does
    # Add some test teachers
    add_teacher("Dr. Keys", "Piano")  # Add a teacher
    add_teacher("Ms. Fret", "Guitar")  # Add a teacher

    while True:  # Keep running until quit
        print("\nMusic School Menu")  # Show menu title
        print("1. Register Student")  # Option 1
        print("2. Enroll Student")  # Option 2
        print("3. Lookup")  # Option 3
        print("4. List Students")  # Option 4
        print("5. List Teachers")  # Option 5
        print("q. Quit")  # Quit option
        
        choice = input("Pick 1-5 or q: ")  # Ask for choice

        if choice == "1":  # If choice 1
            name = input("Student name: ")  # Ask name
            instrument = input("Instrument: ")  # Ask instrument
            front_desk_register(name, instrument)  # Register
        elif choice == "2":  # If choice 2
            student_id = int(input("Student ID: "))  # Ask ID
            instrument = input("Instrument: ")  # Ask instrument
            front_desk_enrol(student_id, instrument)  # Enroll
        elif choice == "3":  # If choice 3
            term = input("Search term: ")  # Ask term
            front_desk_lookup(term)  # Lookup
        elif choice == "4":  # If choice 4
            list_students()  # Show students
        elif choice == "5":  # If choice 5
            list_teachers()  # Show teachers
        elif choice.lower() == "q":  # If quit
            print("Goodbye!")  # Say goodbye
            break  # Stop the loop
        else:  # Wrong choice
            print("Try again.")  # Ask to try again

# [Program Start]
if __name__ == "__main__":  # If running this file
    main()  # Start the program