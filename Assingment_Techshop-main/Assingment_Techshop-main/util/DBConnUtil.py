import pyodbc

class DBConnUtil:
    __connection = None

    def getConnection():
        connection_string = (
        "DRIVER={SQL Server};" 
        "SERVER=LAPTOP-AT863VNS\SQLEXPRESS;" 
        "DATABASE=TechShop1;")
        try:
            DBConnUtil.__connection = pyodbc.connect(connection_string)
            return DBConnUtil.__connection
        except:
            print("Error")
            return None

    @staticmethod
    def close_connection():
        if DBConnUtil.__connection:
            DBConnUtil.__connection.close()
            print("Connection closed.")
            DBConnUtil.__connection = None
