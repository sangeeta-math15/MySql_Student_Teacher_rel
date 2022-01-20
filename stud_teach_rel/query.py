import logging
from connection import DBConnection

logging.basicConfig(filename='my_sql.log', filemode='w', level=logging.ERROR,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')


class MySql:
    """
        Description:
            This class to execute the MySql concept
    """

    def __init__(self):

        self.connection = DBConnection.postgres_connection()
        self.db_connection = self.connection.cursor()


    def insert_query(self, query, parameter):
        """
        :param query: insert query
        :param parameter: insert values
        :return:fetch data
        """
        try:
            res = self.db_connection.executemany(query, parameter)
            return res
        except Exception as e:
            logging.error(e)

    def select_query(self, query):
        """
        :param query: insert query
        :return: fetch data
        """

        try:
            result = self.db_connection.execute(query)
            res = self.db_connection.fetchall()
            return res
        except Exception:
            logging.error("incorrect query")


class Teacher:
    """
    create teacher class
    """

    def __init__(self):
        self.my_sql = MySql()

    def insert_teachers_row(self, parameter):
        """
        :return:inserted values
        """
        try:
            query = "insert into teachers(tid, tname) values(%s, %s)"
            self.my_sql.insert_query(query, parameter)
            self.my_sql.conn.commit()

        except Exception:
            logging.error("Table alreay added")

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
        :return:inserted values
        """
        try:
            query = "insert into students(sid, sname, grade, tid) values(%s, %s, %s, %s)"
            self.my_sql.insert_query(query, parameter)
            self.my_sql.conn.commit()

        except Exception:
            logging.error("Exception Occur duplicate values are not allowed")


    def get_students_name(self):
        """
        :return: student name whoes id less than 6 using view
        """
        try:
            query = "SELECT sname, grade FROM students WHERE sid < 6"
            output = self.my_sql.select_query(query)
            return output

        except Exception as e:
            logging.error(e)

    def stud_teach_rel(self):
        """
        :return: students in class taught by deepa
        """
        try:
            query = "select sname from students left outer join teachers on students.tid = teachers.tid " \
                    "where teachers.tname = 'deepa'"
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
        try:
            """
            :return:
            """
            query = "insert into department(did, dname) values(%s, %s)"
            self.my_sql.insert_query(query, parameter)
            self.my_sql.db_conn.commit()

        except Exception as e:
            print("duplicate values are not allowed", e)



class TeacherDepartment:
    """
    create Techer and department class
    """

    def __init__(self):
        self.my_sql = MySql()

    def insert_teach_dept(self, parameter):
        """
        :return: inserted value
        """
        try:
            query = "insert into teach_dept(id, tid, did) values(%s, %s, %s)"
            self.my_sql.insert_query(query, parameter)
            self.my_sql.conn.commit()

        except Exception:
            logging.error("duplicate values are not allowed")

    def teacher_dept_rel(self):
        """
        :return: teacher name who taught biology
        """
        try:
            query = " select tname from teachers join teach_dept on teach_dept.tid = teachers.tid " \
                    "join department on department.did = teach_dept.did where dname='biology'"
            output = self.my_sql.select_query(query)
            return output

        except Exception as e:
            logging.error(e)
