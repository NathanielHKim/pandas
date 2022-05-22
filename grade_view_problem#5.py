import csv 
import os
from classes.personnel import Student
from classes.personnel import Student
from classes.courses import Course
from data.student_data import first_names, surnames, scores
from collections.abc import Iterable


class Grader:
    def __init__(self, course_name: str, course_code: str, dept_code: str, infile: str, outfile: str = None):
        self.course = None
        self.initialize_course(course_name, course_code, dept_code, infile)
        if outfile:
            self.write_results(outfile)

    def initialize_course(self, crs_num, crs_code, dept_code, filepath):  # TODO
        """ Initializes course object attribute
         Reads data from csv using read_src method
         Creates student objects with names read from csv file
         Enrolls created student objects using course object's enroll method
         Updates and calculates students grades
         Using course object's update_gradebook method """
        coors = Course('130', '006', 'CYSE')
        Grader.read_source()
        coors.enroll(*Grader.read_source())
        for i in range('student_data.csv' -1):
            if i == 4:
                coors.update_gradebook(coors.score)

    def read_source(self, filepath) -> Iterable:   # TODO
        """ Checks if the given filepath exists, Raises a FileNotFoundError if False
        Reads student's first names, surnames and scores from csv file
        NOTE: remember to convert score to a number
        Returns a collection object with first names, surnames and scores """


        
        filepath = os.path.join(os.getcwd(), 'data', 'student_data.csv')
        if os.path.isfile(filepath):
            with open('student_data.csv', 'r') as nf:
                reader = csv.reader(nf)
        else:
            raise FileNotFoundError(filepath)

        with open('student_data.csv', 'r') as nf:
            reader = csv.reader(nf)
            next(reader)
            values = []
            for row in reader:
                values.append(row[1:4])

        for val in values:
            print(val)

        students = []
        for names in values:
            students.append(Student(names[0], names[1]))

        for stud in students:
            print(stud)

    def write_results(self, filepath):  # TODO
        """ Writes a csv file to store the data in the GradeBook dictionary
        Hint: access from the course attribute i.e. self.course.grade_book.grade_book
        CSV file header: ['G-number', 'First_name', 'Surname', 'Score', 'Grade'] """
        filepath = os.path.join(os.getcwd(), 'data', 'new_file.csv')
        header = ['G-number', 'First_name', 'Surname', 'Score', 'Grade']
        with open(filepath, 'w', newline = '') as nf:
            writer = csv.writer(nf)
            writer.writerow(header)
            for stud in Grader.read_source.students:
                writer.writerow([stud.g_num, stud.full_name(), stud.score, stud.Grade])


if __name__ == '__main__':
    try:
        inp = os.path.join(os.getcwd(), 'data', 'student_data.csv')
    except FileNotFoundError as e:
        print(e)
        print('As a start verify that your project structure conforms with what is specified for the assignment')
    else:
        out = os.path.join(os.getcwd(), 'data', 'graded_data')
        Grader('130', '004', 'CYSE', infile=inp, outfile=out)
