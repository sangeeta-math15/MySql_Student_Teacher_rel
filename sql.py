import logging

from connection import MySql

logging.basicConfig(filename='my_sql.log', filemode='w', level=logging.ERROR,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')


class Teacher:
    """
    create teacher class
    """
    def __init__(self):
        self.my_sql = MySql()

    def insert_teachers_row(self, parameter):
        """
         created insert data into teachers table
        :param parameter:passing value
        :return:
        """
        try:
            query = "insert into teachers(tid, tname) values(%s, %s)"
            self.my_sql.insert_query(query, parameter)
            self.my_sql.db_conn.commit()

        except Exception:
            logging.error("Table data already added")

    def get_teacher_name(self):
        """
        :return:name of the teachers who have not yet taught
        """
        try:
            query = "select tname from teachers left outer join students on students.tid = teachers.tid where " \
                    "students.tid is null "
            output = self.my_sql.select_query(query)
            return output

        except Exception as e:
            logging.error(e)

    def get_teach_order(self):
        """
        :return:teachers oder by name
        """
        try:
            query = "select * from teachers order by tname asc"
            output = self.my_sql.select_query(query)
            return output

        except Exception as e:
            logging.error(e)


class Student:
    """
    create student class
    """

    def __init__(self):
        self.my_sql = MySql()

    def insert_student_row(self, parameter):
        """
         created insert data into student table
        :param parameter:passing value
        :return:
        """
        try:
            query = "insert into students(sid, name, grade, tid) values(%s, %s, %s, %s)"
            self.my_sql.insert_query(query, parameter)
            self.my_sql.db_conn.commit()

        except Exception:
            logging.error("Exception Occur duplicate values are not allowed")

    def get_students_name(self):
        """
        :return: student name whoes id less than 105 using view
        """
        try:
            query = "SELECT name,grade FROM students WHERE sid < 106"
            output = self.my_sql.select_query(query)
            return output

        except Exception as e:
            logging.error(e)

    def stud_teach_rel(self):
        """
        :return: students in class taught by prakash
        """
        try:
            query = "select name from students left outer join teachers on students.tid = teachers.tid " \
                    "where teachers.tname = 'Prakash'"
            output = self.my_sql.select_query(query)
            return output

        except Exception as e:
            logging.error(e)


class Department:
    """
    create department class
    """

    def __init__(self):
        self.my_sql = MySql()

    def insert_department(self, parameter):
        """
         created insert data into department table
        :param parameter:passing value
        :return:
        """
        try:
            query = "insert into department(d_id, dname) values(%s, %s)"
            self.my_sql.insert_query(query, parameter)
            self.my_sql.db_conn.commit()

        except Exception:
            print("duplicate values are not allowed")


class TeacherDepartment:
    """
    create Techer and department class
    """

    def __init__(self):
        self.my_sql = MySql()

    def insert_teach_dept(self, parameter):
        """
         created insert data into teacher department table
        :param parameter: passing value
        :return:
        """
        try:
            query = "insert into teach_dept(id, tid, d_id) values(%s, %s, %s)"
            self.my_sql.insert_query(query, parameter)
            self.my_sql.db_conn.commit()

        except Exception:
            logging.error("duplicate values are not allowed")

    def teacher_dept_rel(self):
        """
        :return: teacher name who taught biology
        """
        try:
            query = " select tname from teachers join teach_dept on teach_dept.tid = teachers.tid " \
                    "join department on department.d_id = teach_dept.d_id where dname='biology'"
            output = self.my_sql.select_query(query)
            return output

        except Exception as e:
            logging.error(e)
