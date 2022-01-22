from py_mongo import Teacher, Student, Department, PyMongoDB
import logging

logger = logging

# logging basic config method and saving log file
logger.basicConfig(filename='indexmongo.log', level=logging.ERROR,
                   format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineno)d')


def get_teacher_details():
    """
    Description:
                This function is used to insert multiple documents to
                the collection and find the documents to teachers collection
    """
    t = Teacher()
    p_mongo = PyMongoDB()
    my_dict = [{"_id": 1, "tname": "sudha"},
               {"_id": 2, "tname": "raj"}]
    t.insert_teachers(my_dict, 'teachers')
    p_mongo.find_mongo('teachers')


def get_student_details():
    """
        Description:
                    This function is used to insert multiple documents to
                    the collection and find the documents to students collection
    """
    s = Student()
    p_mongo = PyMongoDB()
    my_dict = [{"_id": 1, "sname": "geeta", "subject": "datbase", "score": 80},
               {"_id": 2, "sname": "ram", "subject": "computer science", "score": 90},
               {"_id": 3, "sname": "keerthi", "subject": "computer network", "score": 70}]

    s.insert_students(my_dict,'students')
    p_mongo.find_mongo('students')


def get_dept_details():
    """
        Description:
                    This function is used to insert multiple documents to
                    the collection and find the documents to departments collection
    """

    d = Department()
    p_mongo = PyMongoDB()
    my_dict = [{"_id": 1, "dept_name":"biology"},
               {"_id": 2, "dept_name":"history"},
               {"_id": 3, "dept_name":"physics"},
               {"_id": 4, "dept_name":"chemistry"},]

    d.insert_departments(my_dict, 'departments')
    p_mongo.find_mongo('departments')



if __name__ == '__main__':

    while True:
        print("""Enter your choice:
                1 Teacher details
                2 student details
                3 Teacher and Department details""")

        choice = int(input("Enter your choice:-"))
        dict_choice = {1: get_teacher_details, 2: get_student_details, 3: get_dept_details}
        dict_choice.get(choice)()

