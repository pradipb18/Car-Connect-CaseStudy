import mysql.connector


class DBConnUtil:
    @staticmethod
    def get_connection(connection_string):
        try:
            connection = mysql.connector.connect(
                host=connection_string['host'],
                port=connection_string['port'],
                user=connection_string['user'],
                password=connection_string['password'],
                database=connection_string['database']
            )
            return connection
        except mysql.connector.Error as err:
            print(f"Error connecting to the database: {err}")
            raise