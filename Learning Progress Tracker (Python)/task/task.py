"""
Learning Progress Tracker. Tracks student's progress. Function: learning_progress_tracker()
"""
import re
students_db = {}
notified_db = {}

def add_students():
    """Add students to the database."""
    print("Enter student credentials or 'back' to return:")
    count = 0
    while True:
        var_input2 = input()
        check = True
        if var_input2 == "back":
            print(f"Total {count} students have been added.")
            break
        else:
            var_input2 = var_input2.split(" ")
            if len(var_input2) < 3:
                print("Incorrect credentials")
                continue
            if not re.match("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+"
                            "(\.[A-Z0-9|a-z0-9]{1,})+", var_input2[len(var_input2)-1]) or \
                    var_input2[len(var_input2)-1].count("@") > 1:
                print("Incorrect email")
                continue
            for i in range(0, len(var_input2)-1):
                if not re.match("^[A-Za-z]+[A-Za-z-']*[A-Za-z]+$", var_input2[i]) or \
                        re.match("^[A-Za-z]+(-'|'-|--|'')+[A-Za-z]+$", var_input2[i]):
                    print("Incorrect first name" if i == 0 else "Incorrect last name")
                    check = False
                    break
            if check is True:
                if abs(hash(var_input2[len(var_input2)-1])) in students_db:
                    print("This email is already taken.")
                else:
                    students_db[abs(hash(var_input2[len(var_input2)-1]))] = var_input2 + [0, 0, 0, 0]
                    print("The student has been added.")
                    count += 1


def list_students():
    """List the students in the database."""
    if len(students_db) > 0:
        students = students_db.keys()
        print("Students:")
        for id in students:
            print(id)
    else:
        print("No students found.")


def add_points():
    """Add points to the students' courses"""
    print("Enter an id and points or 'back' to return.")
    while True:
        var_input3 = input()
        if var_input3 == "back":
            break
        var_input3 = var_input3.split(" ")
        correct_format = True
        try:
            var_input3 = [var_input3[0]] + [int(var) for var in var_input3[1:]]
        except:
            print("Incorrect points format.")
            continue
        if len(var_input3) != 5:
            correct_format = False
        for i in range(1, len(var_input3)):
            if var_input3[i] < 0:
                correct_format = False
        if correct_format is False:
            print("Incorrect points format.")
            continue
        try:
            student_id = int(var_input3[0])
        except:
            print(f"No student is found for id={var_input3[0]}")
            continue
        #student_id = var_input3[0]
        if student_id not in students_db:
            print(f"No student is found for id={student_id}")
        else:
            for i in range(-4, 0):
                students_db[student_id][i] += var_input3[i]
            print("Points updated.")


def find_student():
    """Lists the points of a student, expects the student id."""
    print("Enter an id or 'back' to return.")
    while True:
        var_input4 = input()
        if var_input4 == "back":
            break
        correct_id = True
        try:
            student_id = int(var_input4)
            if student_id not in students_db:
                correct_id = False
        except:
            correct_id = False
        if correct_id is False:
            print(f"No student is found for id={var_input4}")
        else:
            print(f"{student_id} points: Python={students_db[student_id][-4]}; "
                  f"DSA={students_db[student_id][-3]}; Databases={students_db[student_id][-2]}; "
                  f"Flask={students_db[student_id][-1]}")


def course_statistics():
    """Shows statistics of courses and students' grades."""
    students_4, students_3, students_2, students_1 = set(), set(), set(), set()
    course_activity = [0, 0, 0, 0]
    course_grades = [0, 0, 0, 0]
    students_list = []
    for key in students_db:
        students_list.append(key)
        for i in range(-4, 0):
            if students_db[key][i] != 0:
                course_activity[i] += 1
                course_grades[i] += students_db[key][i]
                ph_var = vars()["students_"+str(abs(i))]
                ph_var.add(int(key))
    students_list.sort()
    max_students = max(len(students_1), len(students_2), len(students_3), len(students_4))
    min_students = min(len(students_1), len(students_2), len(students_3), len(students_4))
    most_popular, least_popular = [], []
    high_activity, low_activity = [], []
    easy_course, hard_course = [], []
    if max_students == 0:
        most_popular = least_popular = high_activity = low_activity = easy_course = hard_course = ["n/a"]
    else:
        if len(students_4) == max_students:
            most_popular.append("Python")
        if len(students_3) == max_students:
            most_popular.append("DSA")
        if len(students_2) == max_students:
            most_popular.append("Databases")
        if len(students_1) == max_students:
            most_popular.append("Flask")
        if max_students == min_students:
            least_popular = ["n/a"]
        else:
            if len(students_4) == min_students:
                least_popular.append("Python")
            if len(students_3) == min_students:
                least_popular.append("DSA")
            if len(students_2) == min_students:
                least_popular.append("Databases")
            if len(students_1) == min_students:
                least_popular.append("Flask")
        if course_activity[0] == max(course_activity):
            high_activity.append("Python")
        elif course_activity[0] == min(course_activity):
            low_activity.append("Python")
        if course_activity[1] == max(course_activity):
            high_activity.append("DSA")
        elif course_activity[1] == min(course_activity):
            low_activity.append("DSA")
        if course_activity[2] == max(course_activity):
            high_activity.append("Databases")
        elif course_activity[2] == min(course_activity):
            low_activity.append("Databases")
        if course_activity[3] == max(course_activity):
            high_activity.append("Flask")
        elif course_activity[3] == min(course_activity):
            low_activity.append("Flask")
        if course_grades[0] == max(course_grades):
            easy_course.append("Python")
        elif course_grades[0] == min(course_grades):
            hard_course.append("Python")
        if course_grades[1] == max(course_grades):
            easy_course.append("DSA")
        elif course_grades[1] == min(course_grades):
            hard_course.append("DSA")
        if course_grades[2] == max(course_grades):
            easy_course.append("Databases")
        elif course_grades[2] == min(course_grades):
            hard_course.append("Databases")
        if course_grades[3] == max(course_grades):
            easy_course.append("Flask")
        elif course_grades[3] == min(course_grades):
            hard_course.append("Flask")
    if not low_activity:
        low_activity.append("n/a")
    if not hard_course:
        hard_course.append("n/a")
    print("Type the name of a course to see details or 'back' to quit:")
    print("Most popular:", end=" ")
    print(*most_popular, sep=", ")
    print("Least popular:", end=" ")
    print(*least_popular, sep=", ")
    print("Highest activity:", end=" ")
    print(*high_activity, sep=", ")
    print("Lowest activity:", end=" ")
    print(*low_activity, sep=", ")
    print("Easiest course:", end=" ")
    print(*easy_course, sep=", ")
    print("Hardest course:", end=" ")
    print(*hard_course, sep=", ")
    while True:
        var_input5 = input().lower()
        if var_input5 == "back":
            break
        if var_input5 == "python":
            print("Python")
            print("id                  points  completed")
            points = [students_db[key][-4] for key in students_db]
            if sum(points) == 0:
                continue
            points.sort(reverse=True)
            student_ids = [0 for entry in points]
            for key in students_list:
                for pos, point in enumerate(points):
                    if point == students_db[key][-4] and student_ids[pos] == 0:
                        student_ids[pos] = key
                        break
            for num in range(len(points)):
                print(f"{student_ids[num]:19d}    {points[num]:3d}       {round(points[num] / 6, 1)}%")
        elif var_input5 == "dsa":
            print("DSA")
            print("id                  points  completed")
            points = [students_db[key][-3] for key in students_db]
            if sum(points) == 0:
                continue
            points.sort(reverse=True)
            student_ids = [0 for entry in points]
            for key in students_list:
                for pos, point in enumerate(points):
                    if point == students_db[key][-3] and student_ids[pos] == 0:
                        student_ids[pos] = key
                        break
            for num in range(len(points)):
                print(f"{student_ids[num]:19d}    {points[num]:3d}       {round(points[num] / 4, 1)}%")
        elif var_input5 == "databases":
            print("Databases")
            print("id                  points  completed")
            points = [students_db[key][-2] for key in students_db]
            if sum(points) == 0:
                continue
            points.sort(reverse=True)
            student_ids = [0 for entry in points]
            for key in students_list:
                for pos, point in enumerate(points):
                    if point == students_db[key][-2] and student_ids[pos] == 0:
                        student_ids[pos] = key
                        break
            for num in range(len(points)):
                print(f"{student_ids[num]:19d}    {points[num]:3d}       {round(points[num] / 4.8, 1)}%")
        elif var_input5 == "flask":
            print("Flask")
            print("id                  points  completed")
            points = [students_db[key][-1] for key in students_db]
            if sum(points) == 0:
                continue
            points.sort(reverse=True)
            student_ids = [0 for entry in points]
            for key in students_list:
                for pos, point in enumerate(points):
                    if point == students_db[key][-1] and student_ids[pos] == 0:
                        student_ids[pos] = key
                        break
            for num in range(len(points)):
                print(f"{student_ids[num]:19d}    {points[num]:3d}       {round(points[num] / 5.5, 1)}%")
        else:
            print("Unknown course.")


def print_letter(username, email, course):
    """Prints a letter to students, after completing a course."""
    print(f"To: {email}")
    print("Re: Your Learning Progress")
    print(f"Hello, {username}! You have accomplished our {course} course!")
def notify_students():
    """Notifies students, who completed a course."""
    notified_students = set()
    for key in students_db:
        if students_db[key][-4] >= 600 and (key not in notified_db or "Python" not in notified_db[key]):
            print_letter(" ".join(students_db[key][0:-5]), students_db[key][-5], "Python")
            if key in notified_students:
                notified_db[key] = [notified_db[key], "Python"]
            else:
                notified_db[key] = "Python"
            notified_students.add(key)
        if students_db[key][-3] >= 400 and (key not in notified_db or "DSA" not in notified_db[key]):
            print_letter(" ".join(students_db[key][:-5]), students_db[key][-5], "DSA")
            if key in notified_students:
                notified_db[key] = [notified_db[key], "DSA"]
            else:
                notified_db[key] = "DSA"
            notified_students.add(key)
        if students_db[key][-2] >= 480 and (key not in notified_db or "Databases" not in notified_db[key]):
            print_letter(" ".join(students_db[key][:-5]), students_db[key][-5], "Databases")
            if key in notified_students:
                notified_db[key] = [notified_db[key], "Databases"]
            else:
                notified_db[key] = "Databases"
            notified_students.add(key)
        if students_db[key][-1] >= 550 and (key not in notified_db or "Flask" not in notified_db[key]):
            print_letter(" ".join(students_db[key][:-5]), students_db[key][-5], "Flask")
            if key in notified_students:
                notified_db[key] = [notified_db[key], "Flask"]
            else:
                notified_db[key] = "Flask"
            notified_students.add(key)
    if len(notified_students) < 2:
        print(f"Total {len(notified_students)} student has been notified.")
    else:
        print(f"Total {len(notified_students)} students have been notified.")


def learning_progress_tracker():
    """Main function."""
    print("Learning progress tracker")
    while True:
        var_input = input()
        if not var_input.strip():
            print("No input")
            continue
        if var_input == "back":
            print("Enter 'exit' to exit the program")
            continue
        elif var_input == "exit":
            print("Bye!")
            break
        elif var_input == "add students":
            add_students()
            continue
        elif var_input == "list":
            list_students()
            continue
        elif var_input == "add points":
            add_points()
            continue
        elif var_input == "find":
            find_student()
            continue
        elif var_input == "statistics":
            course_statistics()
            continue
        elif var_input == "notify":
            notify_students()
            continue
        else:
            print("Unknown command!")
            continue


learning_progress_tracker()
