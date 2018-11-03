from Student import Student
#from FacialRecognition import facialRecognizer

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

    def add_student(self, student):
        self.students[student.name.lower] = student

    def remove_student(self, student):
        try:
            del self.students[student.name.lower]
            print("You have removed " + student.name + " from the class.")
        except:
            print("This student does not exist, did you type it correctly?")

    def check_attendance(self, student):
        try:
            """
            recognized_student = facialRecognizer().lower()
            if recognized_student == student.name.lower():
                self.students[student.name.lower].attended = True
            else:
                print("This student is not recognized, would you like to ")
            """
        except:
            input("This student doesn't exist, would you like to add them? (Y/N): ")


enrollment = Class("ITCS_6112")
print(enrollment.name)