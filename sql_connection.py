import pandas as pd
import mysql.connector
from mysql.connector import Error


# Define the MySQL database connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Savi@415",
        database="redbus_datas"
    )

# Define the insert query
insert_query = """
INSERT INTO bus_details 
(Route, Bus_Name, Bus_Type, Departing_Time, Reaching_Time, Duration, Star_Rating, Price, Seats_Availability)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Prepare the data for insertion
data = [tuple(row) for row in df2.to_records(index=False)]

# Connect to MySQL and execute the insert query
try:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.executemany(insert_query, data)
    connection.commit()
    print("Values inserted successfully")
except Error as e:
    print(f"Error: {e}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
