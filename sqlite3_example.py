
import memory_graph as mg
import sqlite3

mg.extend_sqlite3()

conn = sqlite3.connect(":memory:")
conn.execute("PRAGMA foreign_keys = ON")

# Create tables
conn.executescript("""
    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    );

    CREATE TABLE courses (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );

    CREATE TABLE teachers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );

    CREATE TABLE enrollments (
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    );

    CREATE TABLE teaching_assignments (
        teacher_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        PRIMARY KEY (teacher_id, course_id),
        FOREIGN KEY (teacher_id) REFERENCES teachers(id),
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

# Insert teachers
conn.executemany(
    "INSERT INTO teachers VALUES (?, ?)",
    [
        (1, "Smith"),
        (2, "Johnson"),
        (3, "Williams"),
        (4, "Brown"),
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

# Assign teachers to courses
conn.executemany(
    "INSERT INTO teaching_assignments VALUES (?, ?)",
    [
        (1, 1), (2, 1),  # Python: Smith, Johnson
        (2, 2), (3, 2),  # Databases: Johnson, Williams
        (3, 3), (4, 3),  # Algorithms: Williams, Brown
    ]
)

conn.commit()

# Query students and their courses
print("=== Students and courses ===")

query = """
    SELECT students.name, courses.name
    FROM enrollments
    JOIN students ON enrollments.student_id = students.id
    JOIN courses ON enrollments.course_id = courses.id
    ORDER BY students.id, courses.id
"""

for student, course in conn.execute(query):
    print(f"{student:10} -> {course}")

# Query courses and their teachers
print("\n=== Courses and teachers ===")

query = """
    SELECT courses.name, teachers.name
    FROM teaching_assignments
    JOIN courses ON teaching_assignments.course_id = courses.id
    JOIN teachers ON teaching_assignments.teacher_id = teachers.id
    ORDER BY courses.id, teachers.id
"""

for course, teacher in conn.execute(query):
    print(f"{course:10} -> {teacher}")

# Query all teachers teaching a specific student
print("\n=== Teachers teaching Alice ===")

student_name = "Alice"

query = """
    SELECT teachers.name, courses.name
    FROM students
    JOIN enrollments ON students.id = enrollments.student_id
    JOIN courses ON courses.id = enrollments.course_id
    JOIN teaching_assignments
        ON enrollments.course_id = teaching_assignments.course_id
    JOIN teachers ON teaching_assignments.teacher_id = teachers.id
    WHERE students.name = ?
    ORDER BY teachers.name
"""

for teacher, course in conn.execute(query, (student_name,)):
    print(f"{student_name} -> {teacher} for {course}")

conn.close()
