import memory_graph as mg
import sqlite3
mg.extend_sqlite3()

conn = sqlite3.connect("data.sqlite")
conn.execute("PRAGMA foreign_keys = ON")

# Create tables
conn.executescript("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    );

    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS enrollments (
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    );
""")

# Insert students
conn.executemany(
    "INSERT INTO students VALUES (?, ?, ?)",
    [
        (1, "Alice", 20),
        (2, "Bob", 21),
        (3, "Charlie", 22),
        (4, "Diana", 20),
        (5, "Eve", 23),
    ]
)

# Insert courses
conn.executemany(
    "INSERT INTO courses VALUES (?, ?)",
    [
        (1, "Python"),
        (2, "Databases"),
        (3, "Algorithms"),
    ]
)

# Enroll students in courses
conn.executemany(
    "INSERT INTO enrollments VALUES (?, ?)",
    [
        (1, 1), (1, 2),
        (2, 1), (2, 3),
        (3, 2),
        (4, 1), (4, 2), (4, 3),
        (5, 3),
    ]
)

conn.commit()

# Query students and their courses
query = """
    SELECT students.name, courses.name
    FROM enrollments
    JOIN students ON enrollments.student_id = students.id
    JOIN courses ON enrollments.course_id = courses.id
    ORDER BY students.id, courses.id
"""

for student, course in conn.execute(query):
    print(f"{student:10} -> {course}")

conn.close()
