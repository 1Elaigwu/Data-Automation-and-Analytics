import os
import pyodbc

class Database:
    def __init__(self):
        self.db_config = {
            'server': os.getenv('DB_HOST'),
            'database': os.getenv('DB_NAME'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'driver': 'ODBC Driver 17 for SQL Server'  # Adjust driver based on your setup
        }

    def connect(self):
        try:
            connection = pyodbc.connect(**self.db_config)
            print("Connected to SQL Server database")
            return connection
        except pyodbc.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def update_room_rate(self, room_id, new_rate):
        try:
            connection = self.connect()
            if connection:
                cursor = connection.cursor()
                update_query = "UPDATE rooms SET rate = ? WHERE room_id = ?;"
                cursor.execute(update_query, new_rate, room_id)
                connection.commit()
                print(f"Room rate updated successfully for room_id: {room_id}")
        except pyodbc.Error as e:
            print(f"Error updating room rate: {e}")
        finally:
            if connection:
                connection.close()
                print("SQL Server connection closed")

    def perform_analytics(self):
        try:
            connection = self.connect()
            if connection:
                cursor = connection.cursor()
                # Implement your analytics queries here
                pass
        except pyodbc.Error as e:
            print(f"Error performing analytics: {e}")
        finally:
            if connection:
                connection.close()
                print("SQL Server connection closed")
