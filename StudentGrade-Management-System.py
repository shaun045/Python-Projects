import json


class Grade:
    def __init__(self, student_id, course_name, score):
        self.student_id = student_id
        self.course_name = course_name
        self.score = score
        self.letter_grade = self.calculate_letter_grade()

    def calculate_letter_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"

    def get_grade_points(self):
        grade_points = {
            "A": 4.0,
            "B": 3.0,
            "C": 2.0,
            "D": 1.0,
            "F": 0.0
        }
        return grade_points[self.letter_grade]

    def __str__(self):
        return f"{self.course_name}: {self.score:.1f} ({self.letter_grade})"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "course_name": self.course_name,
            "score": self.score
        }

    @staticmethod
    def from_dict(data):
        return Grade(
            student_id=data["student_id"],
            course_name=data["course_name"],
            score=data["score"]
        )


class Course:
    def __init__(self, name, credits, semester, teacher):
        self.name = name
        self.credits = credits
        self.semester = semester
        self.teacher = teacher

    def __str__(self):
        return f"{self.name} | {self.credits} | {self.semester} | {self.teacher}"

    def to_dict(self):
        return {
            "name": self.name,
            "credits": self.credits,
            "semester": self.semester,
            "teacher": self.teacher
        }

    @staticmethod
    def from_dict(data):
        return Course(
            name=data["name"],
            credits=data["credits"],
            semester=data["semester"],
            teacher=data["teacher"]
        )


class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.grades_list = []

    def add_grade(self, grade):
        self.grades_list.append(grade)

    def get_gpa(self):
        if len(self.grades_list) == 0:
            return 0.0

        total = 0
        for grade in self.grades_list:
            total += grade.get_grade_points()

        return total / len(self.grades_list)

    def get_grades_by_semester(self, semester, gradebook):
        results = []
        for grade in self.grades_list:
            course = gradebook.get_course_by_name(grade.course_name)
            if course and course.semester == semester:
                results.append(grade)

        return results

    def get_transcript(self):
        transcript = f"{self.name}:\n"
        for grade in self.grades_list:
            transcript += f"{grade}\n"
        return transcript

    def is_honor_roll(self):
        return self.get_gpa() >= 3.5

    def __str__(self):
        honor = "HONOR ROLL" if self.is_honor_roll() else ""
        return f"{self.student_id} | {self.name} | GPA: {self.get_gpa():.2f} | {honor}"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "grades": [grade.to_dict() for grade in self.grades_list]
        }

    @staticmethod
    def from_dict(data):
        student = Student(
            student_id=data["student_id"],
            name=data["name"],
            email=data["email"]
        )

        if "grades" in data:
            for grade_dict in data["grades"]:
                grade = Grade.from_dict(grade_dict)
                student.add_grade(grade)

        return student


class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, student):
        for existing_student in self.student_list:
            if existing_student.name.lower() == student.name.lower():
                print("Student name already exist")
                return False

        self.student_list.append(student)
        print(f"Student '{student.name}' added successfully")
        return True

    def add_course(self, course):
        for existing_course in self.course_list:
            if existing_course.name.lower() == course.name.lower():
                print("Course already exist!")
                return False

        self.course_list.append(course)
        print(f"Course '{course.name}' added successfully")
        return True

    def get_course_by_name(self, course_name):
        for course in self.course_list:
            if course.name.lower() == course_name.lower():
                return course

        return None

    def record_grade(self, student_id, course_name, score):
        student = None
        for s in self.student_list:
            if s.student_id == student_id:
                student = s
                break

        if student is None:
            print("Student not found!")
            return False

        course = None
        for c in self.course_list:
            if c.name.lower() == course_name.lower():
                course = c
                break

        if course is None:
            print("Course not found!")
            return False

        grade = Grade(student_id, course_name, score)
        student.add_grade(grade)

        print(
            f"Grade recorded for {student.name}: {course.name} = {score} ({grade.letter_grade})")
        return True

    def get_student_by_id(self, student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                return student

        return None

    def get_class_average(self, course_name):
        scores = []
        for student in self.student_list:
            for grade in student.grades_list:
                if grade.course_name.lower() == course_name.lower():
                    scores.append(grade.score)

        if not scores:
            print(f"No grades recorded for course '{course_name}'")
            return None

        average = sum(scores) / len(scores)
        return average

    def get_honor_roll_students(self):
        honor = []
        for student in self.student_list:
            if student.get_gpa() >= 3.5:
                honor.append(student)

        return honor

    def get_student_ranking(self):
        return sorted(self.student_list, key=lambda s: s.get_gpa(), reverse=True)

    def generate_report(self, student_id):
        student = self.get_student_by_id(student_id)

        if not student:
            print(f"Studen '{student_id}' not found!")
            return

        print(f"{"="*50}")
        print(f"STUDENT REPORT - {student.name}")
        print(f"ID:{student.student_id} | Email: {student.email}")
        print(f"'='*50")

        print("TRANSCRIPT")
        print(student.get_transcript())

        print(f"Overall GPA: {student.get_gpa():.2f}")
        print(f"Honor Roll:{'✅ YES' if student.is_honor_roll() else '❌ NO'}")
        print("'='*50")

    def show_all_students(self):
        if len(self.student_list) == 0:
            print("No students enrolled")
            return

        print("=== All Students ===")
        for student in self.student_list:
            print(student)
            print()

    def show_all_courses(self):
        if len(self.course_list) == 0:
            print("No courses available")
            return

        print("=== All Courses ===")
        for course in self.course_list:
            print(course)
            print()

    def save_to_file(self, filename="gradebook.json"):
        data = {
            "students": [student.to_dict() for student in self.student_list],
            "courses": [course.to_dict() for course in self.course_list]
        }

        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Saved gradebook to '{filename}'")
            return True
        except IOError as e:
            print(f"Error saving: {e}")
            return False

    def load_from_file(self, filename="gradebook.json"):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)

            self.course_list = []
            for course_dict in data.get("courses", []):
                course = Course.from_dict(course_dict)
                self.course_list.append(course)

            self.student_list = []
            for student_dict in data.get("students", []):
                student = Student.from_dict(student_dict)
                self.course_list.append(course)

            print(
                f"Loaded {len(self.student_list)} students and {len(self.course_list)} courses")
            return True

        except FileNotFoundError:
            print(f"File '{filename}' not found")
            return False
        except json.JSONDecodeError:
            print(f"File '{filename}' is corrupted")
            return False


if __name__ == "__main__":
    print("="*60)
    print("STUDENT GRADE MANAGEMENT SYSTEM - TESTING")
    print("="*60)

    # TEST 1: Create gradebook
    print("\n--- TEST 1: Creating GradeBook ---")
    gradebook = GradeBook()
    print("✅ GradeBook created")

    # TEST 2: Add courses
    print("\n--- TEST 2: Adding Courses ---")
    gradebook.add_course(Course("Math 101", 3, "Fall 2024", "Dr. Smith"))
    gradebook.add_course(
        Course("English 101", 3, "Fall 2024", "Prof. Johnson"))
    gradebook.add_course(Course("Physics 101", 4, "Fall 2024", "Dr. Brown"))
    gradebook.add_course(
        Course("History 101", 3, "Spring 2025", "Prof. Davis"))
    gradebook.add_course(
        Course("Chemistry 101", 4, "Spring 2025", "Dr. Wilson"))

    # TEST 3: Show all courses
    print("\n--- TEST 3: All Courses ---")
    gradebook.show_all_courses()

    # TEST 4: Add students
    print("\n--- TEST 4: Adding Students ---")
    gradebook.add_student(Student("S001", "Alice Johnson", "alice@school.edu"))
    gradebook.add_student(Student("S002", "Bob Smith", "bob@school.edu"))
    gradebook.add_student(
        Student("S003", "Charlie Brown", "charlie@school.edu"))
    gradebook.add_student(Student("S004", "Diana Prince", "diana@school.edu"))

    # TEST 5: Show all students (before grades)
    print("\n--- TEST 5: All Students (No Grades Yet) ---")
    gradebook.show_all_students()

    # TEST 6: Record grades for Alice (excellent student)
    print("\n--- TEST 6: Recording Grades for Alice ---")
    gradebook.record_grade("S001", "Math 101", 95)
    gradebook.record_grade("S001", "English 101", 92)
    gradebook.record_grade("S001", "Physics 101", 98)
    gradebook.record_grade("S001", "History 101", 90)

    # TEST 7: Record grades for Bob (average student)
    print("\n--- TEST 7: Recording Grades for Bob ---")
    gradebook.record_grade("S002", "Math 101", 78)
    gradebook.record_grade("S002", "English 101", 82)
    gradebook.record_grade("S002", "Physics 101", 75)
    gradebook.record_grade("S002", "History 101", 80)

    # TEST 8: Record grades for Charlie (honor roll)
    print("\n--- TEST 8: Recording Grades for Charlie ---")
    gradebook.record_grade("S003", "Math 101", 88)
    gradebook.record_grade("S003", "English 101", 94)
    gradebook.record_grade("S003", "Physics 101", 91)

    # TEST 9: Record grades for Diana (struggling)
    print("\n--- TEST 9: Recording Grades for Diana ---")
    gradebook.record_grade("S004", "Math 101", 65)
    gradebook.record_grade("S004", "English 101", 70)
    gradebook.record_grade("S004", "Physics 101", 68)

    # TEST 10: Show all students (with GPAs)
    print("\n--- TEST 10: All Students (With Grades) ---")
    gradebook.show_all_students()

    # TEST 11: Generate report for Alice
    print("\n--- TEST 11: Alice's Full Report ---")
    gradebook.generate_report("S001")

    # TEST 12: Generate report for Bob
    print("\n--- TEST 12: Bob's Full Report ---")
    gradebook.generate_report("S002")

    # TEST 13: Class averages
    print("\n--- TEST 13: Class Averages ---")
    math_avg = gradebook.get_class_average("Math 101")
    english_avg = gradebook.get_class_average("English 101")
    physics_avg = gradebook.get_class_average("Physics 101")

    print(f"Math 101 average: {math_avg:.2f}")
    print(f"English 101 average: {english_avg:.2f}")
    print(f"Physics 101 average: {physics_avg:.2f}")

    # TEST 14: Honor roll students
    print("\n--- TEST 14: Honor Roll Students ---")
    honor_students = gradebook.get_honor_roll_students()
    if honor_students:
        print(f"🏆 {len(honor_students)} student(s) on honor roll:")
        for student in honor_students:
            print(f"  {student.name} - GPA: {student.get_gpa():.2f}")
    else:
        print("No students on honor roll yet")

    # TEST 15: Student rankings
    print("\n--- TEST 15: Student Rankings (By GPA) ---")
    rankings = gradebook.get_student_ranking()
    print("🏅 Class Rankings:")
    for i, student in enumerate(rankings, start=1):
        print(f"  {i}. {student.name} - GPA: {student.get_gpa():.2f}")

    # TEST 16: Try to record grade for non-existent student
    print("\n--- TEST 16: Error Handling - Invalid Student ---")
    gradebook.record_grade("S999", "Math 101", 95)

    # TEST 17: Try to record grade for non-existent course
    print("\n--- TEST 17: Error Handling - Invalid Course ---")
    gradebook.record_grade("S001", "Biology 101", 95)

    # TEST 18: Get student by ID
    print("\n--- TEST 18: Get Student By ID ---")
    student = gradebook.get_student_by_id("S001")
    if student:
        print(f"Found: {student.name} (GPA: {student.get_gpa():.2f})")

    # TEST 19: Save to file
    print("\n--- TEST 19: Saving to File ---")
    gradebook.save_to_file("gradebook.json")

    # TEST 20: Load from file (new gradebook)
    print("\n--- TEST 20: Loading from File (New GradeBook) ---")
    gradebook2 = GradeBook()
    gradebook2.load_from_file("gradebook.json")

    # TEST 21: Verify loaded data
    print("\n--- TEST 21: Verify Loaded Data ---")
    print(f"Students loaded: {len(gradebook2.student_list)}")
    print(f"Courses loaded: {len(gradebook2.course_list)}")

    # Show one student's data to verify
    alice = gradebook2.get_student_by_id("S001")
    if alice:
        print(f"\nAlice's GPA after loading: {alice.get_gpa():.2f}")
        print(f"Alice's grades: {len(alice.grades_list)}")

    # TEST 22: Final summary
    print("\n--- TEST 22: Final Summary ---")
    print(f"Total Students: {len(gradebook.student_list)}")
    print(f"Total Courses: {len(gradebook.course_list)}")
    print(f"Honor Roll Students: {len(gradebook.get_honor_roll_students())}")

    all_gpas = [s.get_gpa() for s in gradebook.student_list]
    avg_gpa = sum(all_gpas) / len(all_gpas)
    print(f"Class Average GPA: {avg_gpa:.2f}")

    print("\n" + "="*60)
    print("ALL TESTS COMPLETE! ✅")
    print("="*60)
