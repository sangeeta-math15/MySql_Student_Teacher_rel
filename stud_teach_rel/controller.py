import logging

from query import Teacher, Student, Department, TeacherDepartment


def get_teacher_details():
    """
    return:
    """
    t = Teacher()
    # t.insert_teachers_row([("Pavana")])
    output = t.get_teacher_name()
    print("name of the teachers who have not yet taught")
    for q_output in output:
        print(q_output)

    print("teachers oder by name")
    output = t.get_teach_order()
    for q_output in output:
        print(q_output)


def get_stud_details():
    """
    :return:
    """
    s = Student()
    # s.insert_student_row([("107", "divya", "B+", "1")])
    output = s.get_students_name()
    print("dispaly the student name whoes id less than 105 using view")
    for q_output in output:
        print(q_output)

    print("name of the students in class taught by deepa")
    output = s.stud_teach_rel()
    for q_output in output:
        print(q_output)


def get_teach_dept():
    """
    :return:
    """
    td = TeacherDepartment()
    # td.insert_teach_dept([("3", "3", "10")])
    output = td.teacher_dept_rel()
    print("Names of teachers who taught department of Biology:")
    for q_output in output:
        print(q_output)


if __name__ == "__main__":

    while True:
        print("""Enter your choice:
                1 Teacher details
                2 student details
                3 Teacher and Department details""")

        choice = int(input("Enter your choice:-"))

        dict_choice = {1: get_teacher_details, 2: get_stud_details, 3: get_teach_dept}
        dict_choice.get(choice)()



