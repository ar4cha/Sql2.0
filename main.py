import sqlite3
from os import system

cnt = sqlite3.connect("backup.dp")  
cursor  =  cnt.cursor ()

#cursor.execute('''CREATE TABLE Student (id INTEGER(3) UNIQUE PRIMARY KEY,name TEXT NOT NULL,surname TEXT NOT NULL,stem_grade INTEGER NOT NULL,humanitarian_grade INTEGER NOT NULL,hobbies TEXT);''')


#cursor.execute("ALTER TABLE Student ADD final_year INTEGER DEFAULT 2023")

#cursor.execute(('''INSERT INTO student(id, name, surname,stem_grade,humanitarian_grade,hobbies) VALUES(2, 'Janis', 'Broks',7, 6, 'futbols muzikas skola');'''))

#cursor.execute("INSERT INTO student (id,name,surname, stem_grade, humanitarian_grade,hobbies) VALUES (3 , 'Elina', 'Liepa', 6, 5, 'peldesana');")
#cursor.execute("INSERT INTO student (id,name, stem_grade,surname, humanitarian_grade, hobbies) VALUES (4 , 'Krista', 'Salajeva', 9, 7,'NaN');")
#cursor.execute("INSERT INTO student (id,name, stem_grade,surname, humanitarian_grade, hobbies) VALUES (5 , 'Zane', 'Miega', 4, 3,'NaN');")

#cursor.execute("INSERT INTO student (id,name, stem_grade,surname, humanitarian_grade, hobbies) VALUES (6 , 'Emils', 'Beka', 3, 3, 'peldesana');")
#cursor.execute("INSERT INTO student (id,name, stem_grade,surname, humanitarian_grade, hobbies) VALUES (7 , 'Kristers', 'Ratnieks', 4, 5, 'futbols');")

#cursor.execute("INSERT INTO student (id,name,surname, stem_grade, humanitarian_grade, hobbies) VALUES (8 , 'Elina', 'Liepa', 6, 5, 'peldesana');")

#cursor.execute("INSERT INTO student (id,name, stem_grade,surname, humanitarian_grade, hobbies) VALUES (9 , 'Krista', 'Salajeva', 9, 7,'NaN');")

#cursor.execute("INSERT INTO student (id,name, stem_grade,surname, humanitarian_grade, hobbies) VALUES (10 , 'Zane', 'Miega', 4, 3, 'Nan');")

#cursor.execute("INSERT INTO student (id,name, stem_grade,surname, humanitarian_grade, hobbies) VALUES (11 , 'Emils', 'Beka', 3, 3, 'peldesana');")

#cursor.execute("INSERT INTO student (id,name, stem_grade,surname, humanitarian_grade, hobbies)VALUES (12 , 'Kristers', 'Ratnieks', 4, 5, 'futbols');")


#cursor.execute("ALTER TABLE student add genre TEXT ")
cursor.execute("UPDATE student SET genre = 'M' WHERE name LIKE '%s' ") 

cursor.execute("UPDATE student SET genre = 'F' WHERE name LIKE '%e' OR name LIKE'%a'")

cursor.execute("UPDATE student SET final_year = 2024 WHERE stem_grade < 4 AND humanitarian_grade < 5 ")

#cursor.execute("ALTER TABLE student ADD extra TEXT;")

cursor.execute("UPDATE student SET extra = 'vasaras skola' WHERE final_year > 2023 ")
print("id","name","surname","stem grand","humanitaryan grade","hobbies")
cursor.execute("SELECT * FROM student ORDER BY stem_grade,name ASC")
data = cursor.fetchall()
for w in data:
 print(w)
print("___________________________________________________________")

print("hobbies")
cursor.execute("SELECT DISTINCT hobbies FROM student;")
data = cursor.fetchall()
for c in data:
 print(c)

cnt.commit()


