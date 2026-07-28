# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


students = []

def add_student():
    name = input("Student name: ")
    id_num = input("Student ID: ")
    id_num = int(id_num)
    count = input("How many scores? ")
    count = int(count)
    scores = []
    for i in range(count):
        s = input("Enter score " + str(i+1) + ": ")
        s = int(s)
        scores.append(s)

    record = {}
    record["name"] = name
    record["id"] = id_num
    record["scores"] = scores
    students.append(record)
    print("Student \"" + name + "\" added successfully.")

def get_average(scores):
    total = 0
    for s in scores:
        total = total + s
    avg = total / len(scores)
    avg = round(avg, 2)
    return avg

def display_students():
    if len(students) == 0:
        print("No students added yet.")
    else:
        print("--------------------------------------------------")
        print("Name           ID          Scores         Average")
        print("--------------------------------------------------")
        for stu in students:
            avg = get_average(stu["scores"])
            scores_text = ""
            for s in stu["scores"]:
                scores_text = scores_text + str(s) + ", "
            scores_text = scores_text[0:len(scores_text)-2]
            print(stu["name"], "  ", stu["id"], "  ", scores_text, "  ", avg)
        print("--------------------------------------------------")

def average_for_id():
    search_id = input("Enter student ID: ")
    search_id = int(search_id)
    found = False
    for stu in students:
        if stu["id"] == search_id:
            found = True
            avg = get_average(stu["scores"])
            print(stu["name"] + "'s average score: " + str(avg))
    if found == False:
        print("Error, student ID not found")

running = True
while running == True:
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        average_for_id()
    elif choice == "4":
        print("Goodbye!")
        running = False
    else:
        print("Error, invalid choice")