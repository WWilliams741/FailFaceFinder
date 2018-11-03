class Student:

    def __init__(self, name, folder):
        self.name = name
        self.folder = folder # The file path to where the students pictures are stored
        self.attended = False

    # Getters:
    @property
    def name(self):
        return self.__name
    @property
    def folder(self):
        return self.__folder
    @property
    def attended(self):
        return self.__attended

    # Setters:
    @name.setter
    def name(self, name):
        self.__name = name
    @folder.setter
    def folder(self, folder):
        self.__folder = folder
    @attended.setter
    def attended(self, attended):
        self.__attended = attended