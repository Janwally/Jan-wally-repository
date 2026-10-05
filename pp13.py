from enum import nonmember


class student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.advisor = None

    def assing_adivor(self,faculty):
        self.advisor = faculty

class Faculty:
    def __init__(self,name,faculty_id):
        self.name = name
        self.faculty_id = faculty_id
        self.students = []

    def enroll_student(self,student):
        self.students.append(student)

class courses:
    def __init__(self,course_name,course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.facultiy = None
        self.students = []

    def teaching_faculty(self):
        return self.facultiy

    def enroll_student(self):
        return self.students

#List to store objects
mystudentsList =[]
myfacultyList =[]
mycoursesList =[]

#create student objects
student1 = student("Jan","002")
student2 = student("Wally","004")

mystudentsList.append(student1)
mystudentsList.append(student2)

#create Faculty objects
faculty1 = Faculty("professor Justus","001")

myfacultyList.append(faculty1)

#create course objects
courses1 = courses("computer science","05170209")

mycoursesList.append(courses1)

#Assing advisor
stud
