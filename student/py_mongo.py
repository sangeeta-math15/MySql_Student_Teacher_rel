import logging

logger = logging

# logging basic config method and saving log files
logger.basicConfig(filename='indexongo.log', level=logging.INFO,
                   format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')
logger.basicConfig(filename='indexmongo.log', level=logging.ERROR,
                   format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineno)d')


class PyMongoDB:
    """
        Description:
            This generic class to execute the PyMongoDB
    """

    def __init__(self):
        """
        establish mongo database connection
        """
        self.db_connection = pymongo.MongoClient("mongodb://localhost:27017")
        self.my_db = self.db_connection['College_Management_System']

    def insert_mongo(self, parameter, collection):
        """
        :param parameter:passing documents
        :param collection:passing collection
        :return:
        """

        try:
            my_col = self.my_db[collection]
            document = my_col.insert_many(parameter)
            return document

        except Exception as err:
            logger.error(err)
            logger.info("Inserted multiple documents\n")

    def find_mongo(self, collection):
        """

        :param collection:
        :return:
        """
        try:
            my_col = self.my_db[collection]
            result = my_col.find()
            for data in result:
                logger.info(data)
            logger.info("Showed all documents\n")
        except Exception as err:
            logger.error(err)


class Teacher:
    """
          Description:
              This class to execute the Teacher
      """

    def __init__(self):
        self.py_mongo = PyMongoDB()

    def insert_teachers(self, parameter, collection):
        """
        created function to insert teacher data
        :param parameter:passing data
        :param collection:passing collection
        :return:document
        """
        doc = self.py_mongo.insert_mongo(parameter, collection)
        return doc


class Student:
    """
          Description:
              This class to execute the student
      """

    def __init__(self):
        self.py_mongo = PyMongoDB()

    def insert_students(self, parameter, collection):
        """
         created function to insert student data
        :param parameter:passing data
        :param collection:passing collection
        :return:document
        """
        doc = self.py_mongo.insert_mongo(parameter, collection)
        return doc


class Department:
    """
          Description:
              This class to execute the Department
      """

    def __init__(self):
        self.py_mongo = PyMongoDB()

    def insert_departments(self, parameter, collection):
        """
         created function to insert_departments data
        :param parameter:passing data
        :param collection:passing collection
        :return:document
        """
        doc = self.py_mongo.insert_mongo(parameter, collection)
        return doc
