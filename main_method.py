from my_sql_view import Teacher, Student, Department, TeacherDepartment

if __name__ == "__main__":
    t = Teacher()
    s = Student()
    d = Department()
    t_d = TeacherDepartment()
    while True:
        print("Enter your choice")
        print("1 Teacher details")
        print("2 student details")
        print("3 Department details")
        print("4 Teacher and Department details")

        choice = int(input("Enter your choice"))
        if choice == 1:
            t.insert_teachers_row()
            output = t.get_teacher_name()
            print("name of the teachers who have not yet taught")
            for q_output in output:
                print(q_output)

            output1 = t.get_teach_order()
            print("teachers oder by name")
            for q_output1 in output1:
                print(q_output1)

        elif choice == 2:
            s.insert_student_row()
            output = s.get_students_name()
            print("dispaly the student name whoes id less than 105 using view")
            for q_output in output:
                print(q_output)

            output = s.stud_teach_rel()
            print("name of the students in class taught by prakash")
            for q_output in output:
                print(q_output)

        elif choice == 3:
            d.insert_department()

        elif choice == 4:

            t_d.insert_teach_dept()
            output = t_d.teacher_dept_rel()
            print("Names of teachers who taught department of Biology:")
            for q_output in output:
                print(q_output)
        else:
            break
