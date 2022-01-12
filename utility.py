"""
import pymysql package
"""
import pymysql.cursors


class MySql:
    """
        Description:
            This class to execute the MySql View concept
    """

    def __init__(self):
        self.db_conn = pymysql.connect(
            host='localhost',
            user='root',
            password="Sang@123",
            db='db_view',

        )
        self.db_connection = self.db_conn.cursor()


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
            print(e)


    def select_query(self, query):
        """
        :param query: insert query
        :return: fetch data
        """
        result = self.db_connection.execute(query)
        res = self.db_connection.fetchmany(result)
        return res

