# Создание таблицы Students
import sqlite3

connection = sqlite3.connect('students.db')
cursor = connection.cursor()
query = """CREATE TABLE Students 
(
Student_Id INTEGER NOT NULL PRIMARY KEY, 
Student_Name TEXT NOT NULL, 
School_Id INTEGER NOT NULL
);
"""
cursor.execute(query)
connection.commit()
connection.close()

# Наполнение таблицы Students
import sqlite3

connection = sqlite3.connect('students.db')
cursor = connection.cursor()
query = """INSERT INTO Students (Student_Id, Student_Name, School_Id) 
VALUES 
('201', 'Иван', 1), 
('202', 'Петр', 2), 
('203', 'Анастасия', 3), 
('204', 'Игорь', 4);
"""
cursor.execute(query)
connection.commit()
connection.close()

##Вывод информации о студенте
import sqlite3

def get_connection():
  connection = sqlite3.connect('students.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()
 	
def get_school_name(school_id):
  try:
    connection = sqlite3.connect('school.db')
    cursor = connection.cursor()
    select_query = """SELECT * FROM School WHERE School_Id = ?"""
    cursor.execute(select_query, (school_id,))
    record = cursor.fetchone()
    close_connection(connection)
    return record[1] # Наименование школы
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)

student_id = input ("Введите id студента ")
try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM Students WHERE Student_Id = ?"""
    cursor.execute(select_query, (student_id,))
    records = cursor.fetchall()
    print ("Данные по школе и студенту")
    for row in records:
      st_id = row[0]
      st_name = row[1]
      school_id = row[2]      
    close_connection(connection)
except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе и студенту ", error)
if 'st_id' in locals():
   school_name = get_school_name(school_id)
   print("ID студента:", st_id)
   print("Имя студента:", st_name)
   print("ID школы:", school_id) 
   print("имя школы:", school_name)
else:
   print("Такого id студента не существует")
