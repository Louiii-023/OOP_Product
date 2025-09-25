class student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.student_id = (student_id, student_name) # tuple combine ID and name
        self.email = email # string
        self.grades =  grades if grades is not None else {} # dictionary {subject: score}
        self.courses = courses if courses is not None else set () # set of enrolled courses

    def __str__(self):
        return  (f"Student ID: {self.student_id[0]} \n"
                f"Name: {self.student_id[1]} \n"
                f"Email: {self.email} \n"
                f"grades: {self.grades} \n"
                f"Courses: {', '.join(self.courses) if self.courses else 'None'}")
# Challenge Mag Claculate ng GPA base sa grades
    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        
        total_points = 0
        for score in self.grades.values():
            if score >= 90:
                total_points += 4.0
            elif score >= 80:
                total_points += 3.0
            elif score >= 70:
                total_points += 2.0
            elif score >= 60:
                total_points += 1.0
            else:
                total_points += 0.0 
        return round(total_points / len(self.grades), 2)

# Student Records Conatainer
class Student_records:
    def __init__(self):
        self.student = []

    # Adding students
    def add_students(self, student_id, student_name, email=None, grades=None, courses=None):
        new_student = student(student_id, student_name, email, grades, courses)
        self.student.append(new_student)
        return "Student added successfully"
    
    # Update student information
    def update_student(self, student_id, email = None, grades = None, courses = None):
        for student in self.student:
            if student.student_id[0] == student_id:
                if email is not None:
                    student.email = email
                if grades is not None:
                    student.grades = grades
                if courses is not None:
                    student.courses = courses
                return "Success"
        return "Not Found"
    
    # Delete student
    def delete_student(self, student_id):
        for i in range(len(self.student)):
            if self.student[i].student_id[0] == student_id:
                del self.student[i]
                return "Student deleted successfully"
        return "Student not found"
    
    # Enroll course
    def enroll_course(self, student_id, course):
        for student in self.student:
            if student.student_id[0] == student_id:
                student.courses.add(course)
                return "Course enrolled successfully"
        return "Student not found"
    
    # Search student by ID
    def search_student(self, student_id):
        for student in self.student:
            if student.student_id[0] == student_id:
                return str(student)
        return "Student not found"
    
    #  Challenge number 2 ni sir Search student by partial name
    def search_by_name(self, name):
        matches = []
        for student in self.student:
            if name.lower() in student.student_id[1].lower():
                matches.append(str(student))
        return matches if matches else ["No student found"]
    
records = Student_records()

# Add students
print(records.add_students(1, "Louis Navarro", "louis.navarro@bsu.com", {"DSA": 80}, {"DSA", "OOP"}))
print(records.add_students(2, "Louii Emmanuel", "louii.emmanuel@bsu.com", {"ARTAPP": 85}, {"ARTAPP", "TCW"}))

# Update a student's information
print(records.update_student(1, email="louis.navarro@bsu.com", grades={"DSA": 80}, courses={"DSA", "OOP"}))

# Enroll a student in a new course
print(records.enroll_course(2, "modmath"))

# Search for a student
print(records.search_student(1))
print(records.search_student(2)) 
print(records.delete_student(3))  # Non-existent student to check if it will return "Student not found"


# Delete a student
print(records.delete_student(1))
print(records.delete_student(3))  # Non-existent student to check if it will return "Student not found"

# Search for the student
print(records.search_student(2))

print("GPA of Student 1:", records.student[0].calculate_gpa())

# Search by partial name
print("Search results for 'Louis':", records.search_by_name("Louis"))
print("Search results for 'Louii':", records.search_by_name("Louii"))
print("Search results for 'Nav':", records.search_by_name("Nav"))
print("Search results for 'ghgjhghgug':", records.search_by_name("ghgjhghgug"))  # dapat "No student found" lalabas
