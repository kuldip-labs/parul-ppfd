class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

class Student(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self.enrolled_courses = []

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)
            print(f"Student {self.name} enrolled in {course.course_name}")

class Teacher(Person):
    def __init__(self, name, id_number, subject_expertise):
        super().__init__(name, id_number)
        self.subject_expertise = subject_expertise

    def __str__(self):
        return f"Teacher: {self.name} (Expertise: {self.subject_expertise})"

class Course:
    def __init__(self, course_name, course_code, teacher):
        self.course_name = course_name
        self.course_code = course_code
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def display_roster(self):
        print(f"\n--- Roster for {self.course_name} ({self.course_code}) ---")
        print(f"Instructor: {self.teacher.name}")
        for student in self.students:
            print(f"- {student.name} (ID: {student.id_number})")

# --- Simulation ---

# 1. Create a Teacher
mr_smith = Teacher("John Smith", "T101", "Computer Science")

# 2. Create a Course
python_101 = Course("Intro to Python", "CS101", mr_smith)

# 3. Create Students
alice = Student("Alice Johnson", "S001")
bob = Student("Bob Miller", "S002")

# 4. Enroll Students
alice.enroll(python_101)
bob.enroll(python_101)

# 5. Display the Roster
python_101.display_roster()