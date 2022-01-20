"""
import pymysql package
"""
import logging
import pymysql.cursors

logging.basicConfig(filename='my_sql.log', filemode='w', level=logging.ERROR)


class MySql:
    """
        Description:
            This class to execute the MySql concept
    """

    def __init__(self):
        """
        establish database connection
        """
        self.db_conn = pymysql.connect(
            host='localhost',
            user='root',
            password="Sang@123",
            db='db_view'

        )
        self.db_connection = self.db_conn.cursor()

    def insert_query(self, query, parameter):
        """
        :param query: insert query
        :param parameter: insert values
        :return:inserted data
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
            res = self.db_connection.fetchmany(result)
            return res

        except Exception:
            logging.error("incorrect query")
