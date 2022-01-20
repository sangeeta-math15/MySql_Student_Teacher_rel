import psycopg2


class DBConnection:

    @staticmethod
    def postgres_connection():
        # Establishing the connection
        try:
            conn = psycopg2.connect(
                database="stud_teach_db",
                user='postgres',
                password='Sang@123',
                host='localhost',
                port='5432'
                )
            print("Database Connection is Established")
            return conn
        except Exception as e:
            print("Database Connection is not Established",e)



