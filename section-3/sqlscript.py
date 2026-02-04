import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='parul'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def crud_operations():
    conn = create_connection()
    if conn is None:
        return

    cursor = conn.cursor()

    try:
        # # 1. CREATE (Insert)
        # insert_query = """INSERT INTO Employees (LastName, FirstName, Department, Birth)
        #                   VALUES (%s, %s, %s, %s)"""
        # record = ('Doe', 'John', 'Engineering', '1990-05-15')
        # # a cursor is a database object used to execute SQL statements and manage the context of data fetching operations when interacting with a database
        # cursor.execute(insert_query, record)
        # conn.commit()
        # print("Record inserted successfully.")
        #
        # # 2. READ (Select)
        # cursor.execute("SELECT * FROM Employees")
        # rows = cursor.fetchall()
        # print("\n--- Current Employees ---")
        # for row in rows:
        #     print(row)
        #
        # # 3. UPDATE
        # update_query = "UPDATE Employees SET Department = %s WHERE LastName = %s"
        # cursor.execute(update_query, ('Data Science', 'Doe'))
        # conn.commit()
        # print("\nRecord updated successfully.")

        # 4. DELETE
        delete_query = "DELETE FROM Employees WHERE FirstName = %s"
        cursor.execute(delete_query, ('John',))
        conn.commit()
        print("Record deleted successfully.")

    except Error as e:
        print(f"Failed to execute query: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    crud_operations()