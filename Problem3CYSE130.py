from random import randint, shuffle
from student_data import first_names, surnames, scores, students
from itertools import count

first_names = [
    'Clare', 'Sandra', 'Shona', 'Kathleen', 'Paula', 'Shirley', 'Denise', 'Melanie',
    'Patricia', 'Audrey', 'Ruth', 'Jill', 'Lee', 'Leigh', 'Catriona', 'Rachel', 'Morag',
    'Kirsten', 'Kirsteen', 'Katrina', 'Joanna', 'Lynsey', 'Cheryl', 'Debbie', 'Maureen', 'Janet',
    'Aileen', 'Arlene', 'Zoe', 'Lindsay', 'Stephanie', 'Judith', 'Mandy', 'Jillian', 'Mhairi',
    'Barbara', 'Carolyn', 'Gayle', 'Maria', 'Valerie', 'Christina', 'Marion', 'Nicola', 'Karen',
    'Susan', 'Claire', 'Fiona', 'Angela', 'Sharon', 'Gillian', 'Julie', 'Alastair', 'Bryan', 'Marc',
    'Jamie', 'Hugh', 'Euan', 'Gerard', 'Sean', 'Wayne', 'Adam', 'Calum', 'Alasdair', 'Robin', 'Greig',
    'Angus', 'Russell', 'Cameron', 'Roderick', 'Norman', 'Murray', 'Gareth', 'Dean', 'Eric', 'Adrian',
    'Gregor', 'Samuel', 'Gerald', 'Henry', 'Justin', 'Benjamin', 'Shaun', 'Callum', 'Campbell', 'Frank',
    'Roy', 'Timothy', 'David', 'John', 'Paul', 'James', 'Mark', 'Scott', 'Andrew', 'Steven', 'Robert', 'Stephen', 'Craig', 'Christopher', 'Alan']

surnames = [
    'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor',
    'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez',
    'Lewis', 'Robinson', 'Walker', 'Young', 'Allen', 'King', 'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill',
    'Flores', 'Green', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell', 'Carter', 'Roberts',
    'Gomez', 'Phillips', 'Evans', 'Turner', 'Diaz', 'Parker', 'Cruz', 'Edwards', 'Collins', 'Reyes', 'Stewart',
    'Morris', 'Morales', 'Murphy', 'Cook', 'Rogers', 'Gutierrez', 'Ortiz', 'Morgan', 'Cooper', 'Peterson',
    'Bailey', 'Reed', 'Kelly', 'Howard', 'Ramos', 'Kim', 'Cox', 'Ward', 'Richardson', 'Watson',' Brooks', 'Chavez',
    'Wood', 'James', 'Bennett', 'Gray', 'Mendoza', 'Ruiz', 'Hughes', 'Price', 'Alvarez', 'Castillo', 'Sanders',
    'Patel', 'Myers', 'Long', 'Ross', 'Foster', 'Jimenez', 'Powell', 'Jenkins', 'Perry', 'Russell', 'Sullivan',
    'Bell', 'Coleman', 'Butler']

shuffle(first_names), shuffle(surnames)

scores = [randint(67, 100) for a in range(0, 100)]

sessions = ['003']*30 + ['004']*30 + ['005']*40

id_numbers = ['C0' + str(a) for a in range(1000, 1100)]

students = {_id: {'first_name': first_name, 'last_name': last_name, 'session': session, 'score': score}
    for _id, first_name, last_name, session, score in zip(id_numbers, first_names, surnames, sessions, scores)
}



class ID:
    """Offers a Unique ID number with a user specified starting number"""
    counter = count(1)

    def __init__(self, start=1000):
        self.__start = start
        self.__value = start + next(self.__class__.counter)

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return self.__class__.__name__ + '(start={})'.format(self.__start)

class MasonPerson:
    ID_STARTS_WITH = 'G00'

    def __init__(self, first_name, last_name, role):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.g_num = MasonPerson.ID_STARTS_WITH + str(ID())

    def full_name(self):
        return self.first_name + '_' + self.last_name

    def __str__(self):
        return self.g_num + '_' + self.full_name()

    def __repr__(self):
        return self.__class__.__name__ + \
               '(first_name={}, last_name={}, role={})'.format(self.first_name, self.last_name, self.role)
    
class Student:
    def __init__(self,first_name,lastname,score,session_num):
        self.first_name=first_name
        self.lastname=lastname
        self.score=score
        self.session_num=session_num
        self.grade=""
        self.course_num=""
        self.dept_code=""

        
class Course:
    def __init__(self,course_num, session_num, dept_code):
        self.course_num=course_num
        self.session_num=session_num
        self.dept_code=dept_code
    def enroll(self,objs):
        for obj in objs:
            obj.course_num=self.course_num
            obj.dept_code=self.dept_code
    def update_gradebook(self,objs):
        for obj in objs:
            GB=GradeBook(obj)
            GB.update_grades()
    def print_gradebook(self,objs):
        for obj in objs:
            GB=GradeBook(obj)
            GB.print_gradebook()



class GradeBook:
    def __init__(self,student_obj):
        self.student_obj=student_obj
        
    def update_grades(self):
        if self.student_obj.score>=90 and self.student_obj.score<=100:
            self.student_obj.grade='A'
        elif self.student_obj.score>=80 and self.student_obj.score<=89:
            self.student_obj.grade='B'
        elif self.student_obj.score>=70 and self.student_obj.score<=79:
            self.student_obj.grade='C'
        elif self.student_obj.score>=60 and self.student_obj.score<=69:
            self.student_obj.grade='D'
        else:
            self.student_obj.grade='F'
        
    def print_gradebook(self):
        print("{} {}: score={}, grade={}".format(self.student_obj.first_name,self.student_obj.lastname,self.student_obj.score,self.student_obj.grade))
  
Student_objects=[]
for i in students:
    Student_objects.append(Student(students[i]['first_name'],students[i]['last_name'],students[i]['score'],students[i]['session']))
    
course_obj=Course("130","003","CYSE")
course_obj.enroll(Student_objects)
course_obj.update_gradebook(Student_objects)
course_obj.print_gradebook(Student_objects)
