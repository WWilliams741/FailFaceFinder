from Student import Student
from FacialRecognition import facialRecognizer

class Class:

    def __init__(self, name):
        self.name = name
        self.students = {}

    # Name getter
    @property
    def name(self):
        return self.__name

    # Name setter
    @name.setter
    def name(self, name):
        self.__name = name

    def add_student(self, name, folder):
        self.students[name.lower()] = Student(name, folder)

    def remove_student(self, student):
        try:
            del self.students[student.name.lower]
            print("You have removed " + student.name + " from the class.")
        except:
            print("This student does not exist, did you type it correctly?")

    def check_attendance(self):
        captured_student = facialRecognizer()

        for a_student in self.students:
            if a_student == captured_student:
                self.students[a_student].attended = True
                print(a_student + " was at class: " + str(self.students[a_student].attended))
            else:
                print(a_student + " was at class: " + str(self.students[a_student].attended))

    # THIS IS/WAS FOR TESTING
    def get_student(self, name):
        return self.students[name].attended


# enrollment = Class("ITCS_6112")
# print(enrollment.name)