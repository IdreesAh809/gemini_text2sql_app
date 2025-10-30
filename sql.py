import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('students.db')

# Create a cursor object
cursor = connection.cursor()

# Create table (only once)
table_info = '''
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME TEXT,
    CLASS TEXT,
    SECTION TEXT,
    MARKS INT
);
'''
cursor.execute(table_info)

# Insert records
cursor.execute("INSERT INTO STUDENT VALUES ('Idrees', '12th', 'AI', 85);")
cursor.execute("INSERT INTO STUDENT VALUES ('Haseeb', '11th', 'ML', 90);")
cursor.execute("INSERT INTO STUDENT VALUES ('Ayaan', '10th', 'DS', 95);")
cursor.execute("INSERT INTO STUDENT VALUES ('Zayan', '9th', 'CV', 80);")
cursor.execute("INSERT INTO STUDENT VALUES ('Rehan', '8th', 'NLP', 75);")
cursor.execute("INSERT INTO STUDENT VALUES ('Saad', '7th', 'AI', 88);")
cursor.execute("INSERT INTO STUDENT VALUES ('Aariz', '6th', 'ML', 92);")
cursor.execute("INSERT INTO STUDENT VALUES ('Rayyan', '5th', 'DS', 78);")
cursor.execute("INSERT INTO STUDENT VALUES ('Kian', '4th', 'CV', 83);")
cursor.execute("INSERT INTO STUDENT VALUES ('Zain', '3rd', 'NLP', 89);")
cursor.execute("INSERT INTO STUDENT VALUES ('Tariq', '2nd', 'AI', 91);")

# Display all records
print("Displaying all records:")
cursor.execute("SELECT * FROM STUDENT;")
data = cursor.fetchall()  # Fetch all rows

for row in data:
    print(row)

# Close the connection
connection.commit()
connection.close()
