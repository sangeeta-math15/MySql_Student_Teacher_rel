from utility  import MySql


class Teacher:
    """
    create teacher class
    """

    def __init__(self):
        self.my_sql = MySql()

    def insert_teachers_row(self):
        """
        :return:inserted values
        """
        try:

            query = "insert into teachers (tid, tname) values(%s, %s)"
            parameter = [("7", "Pavana")]
            self.my_sql.insert_query(query, parameter)
            self.my_sql.db_conn.commit()

        except Exception as err:
            print(err)

    def get_teacher_name(self):
        """
        :return:name of the teachers who have not yet taught
        """
        query = "select tname from teachers left outer join students on students.tid = teachers.tid where " \
                "students.tid is null "
        output = self.my_sql.select_query(query)
        return output

    def get_teach_order(self):
        """
        :return:teachers oder by name
        """
        query = "select * from teachers order by tname asc"
        output = self.my_sql.select_query(query)
        return output


class Student:
    """
    create student class
    """

    def __init__(self):
        self.my_sql = MySql()

    def insert_student_row(self):
        """
        :return:inserted values
        """
        try:
            query = "insert into students(sid, name, grade, tid) values(%s, %s, %s, %s)"
            parameter = [("107", "divya", "B+", "1")]
            self.my_sql.insert_query(query, parameter)
            self.my_sql.db_conn.commit()

        except Exception as e:
            print("Exception Occur", e)

    def get_students_name(self):
        """
        :return: student name whoes id less than 105 using view
        """
        query = "SELECT name,grade FROM students WHERE sid < 106"
        output = self.my_sql.select_query(query)
        return output

    def stud_teach_rel(self):
        """
        :return: students in class taught by prakas
        """
        query = "select name from students left outer join teachers on students.tid = teachers.tid " \
                "where teachers.tname = 'Prakash'"
        output = self.my_sql.select_query(query)
        return output


class Department:
    """
    create department class
    """

    def __init__(self):
        self.my_sql = MySql()

    def insert_department(self):
        try:
            """
            :return:
            """
            query = "insert into department(d_id, dname) values(%s, %s)"
            parameter = [("20", "chemistry"), ("30", "CS")]
            self.my_sql.insert_query(query, parameter)
            self.my_sql.db_conn.commit()
        except Exception as e:
            print(e)


class TeacherDepartment:
    """
    create Techer and department class
    """

    def __init__(self):
        self.my_sql = MySql()

    def insert_teach_dept(self):
        """
        :return:
        """
        query = "insert into teach_dept(id, tid, d_id) values(%s, %s, %s)"
        parameter = [("3", "3", "10"), ("4", "4", "10"), ("5", "5", "20")]
        self.my_sql.insert_query(query, parameter)
        self.my_sql.db_conn.commit()

    def teacher_dept_rel(self):
        """
        :return:
        """
        query = " select tname from teachers join teach_dept on teach_dept.tid = teachers.tid " \
                "join department on department.d_id = teach_dept.d_id where dname='biology'"
        output = self.my_sql.select_query(query)
        return output

