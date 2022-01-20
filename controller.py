import logging

from sql import Teacher, Student, Department, TeacherDepartment


def get_teacher_details():
    """
    :return:name of the teachers who have not yet taught
    and teachers oder by name
    """
    t = Teacher()
    t.insert_teachers_row([("8", "Pavana")])
    output = t.get_teacher_name()
    print("name of the teachers who have not yet taught")
    for q_output in output:
        print(q_output)

    output = t.get_teach_order()
    print("teachers oder by name")
    for q_output in output:
        print(q_output)


def get_stud_details():
    """
    :return:dispaly the student name whoes id less than 106 using view
    and name of the students in class taught by prakash
    """
    s = Student()
    # s.insert_student_row([("107", "divya", "B+", "1")])
    output = s.get_students_name()
    print("dispaly the student name whoes id less than 106 using view")
    for q_output in output:
        print(q_output)

    output = s.stud_teach_rel()
    print("name of the students in class taught by prakash")
    for q_output in output:
        print(q_output)


def get_teach_dept():
    """
    :return: names of teachers who taught department of biology:
    """
    t_d = TeacherDepartment()
    t_d.insert_teach_dept([("3", "3", "10")])
    output = t_d.teacher_dept_rel()
    print("Names of teachers who taught department of biology:")
    for q_output in output:
        print(q_output)


if __name__ == "__main__":
    while True:
        print("""Enter your choice:
                1 Teacher details"
                2 student details"
                3 Teacher and Department details""")

        choice = int(input("Enter your choice:-"))
        dict_choice = {1: get_teacher_details, 2: get_stud_details, 3: get_teach_dept}
        dict_choice.get(choice)()
