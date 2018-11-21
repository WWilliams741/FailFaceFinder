from Student import Student
from FacialRecognition import facial_recognizer
from datetime import datetime
import os


class Class:

    def __init__(self, name):
        self.name = name
        self.students = dict()

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
            del self.students[student.name.lower()]
            print("You have removed " + student.name + " from the class.")
        except KeyError:
            print("This student does not exist, did you type it correctly?")

    def check_attendance(self):
        captured_student = facial_recognizer()

        # Checks the students and sets that student to have "attended" the class if the facial_recognizer finds them.
        for a_student in self.students:
            if a_student == captured_student:
                self.students[a_student].attended = True
                print(a_student + " was present")

    def create_sheet(self, reset):

        # Getting the directory or creating one if it does not exist
        print("Attendance sheet being created for: " + self.name)
        dirname = os.path.dirname(__file__)
        if not os.path.exists(dirname + "/Attendance/" + self.name):
            os.makedirs(dirname + "/Attendance/" + self.name)

        # Writing to the attendance sheet and creating one for the current date if it does not exist
        with open("Attendance/" + self.name + "/" + str(datetime.date(datetime.now())) + ".txt", "w") as attendance_sheet:
            attendance_sheet.write(str(datetime.date(datetime.now())) + ":\n")

            for student in self.students:
                attendance_sheet.write(self.students[student].name + ": " + str(self.students[student].attended) + "\n")
                if reset:
                    self.students[student].attended = False
