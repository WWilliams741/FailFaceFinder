from Class import Class
import pickle
import os

'''
a = {'hello': 'world'}
b = {'hello2': 'world2'}

lists = []

with open('filename.pickle', 'wb') as handle:
    pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('filename.pickle', 'ab') as handle:
    pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('filename.pickle', 'rb') as handle:
    while 1:
        try:
            lists.append(pickle.load(handle))
        except EOFError:
            break

print (a == lists[1])

# check_class_attendance()

exit()
'''

def rewrite_classes(updatable_class):
    # create a classes_list to hold all classes from the pickle file
    classes_list = []

    # find out if the pickle file exists
    exists = os.path.isfile('classes/classes.pickle')
    # if pickle file exists
    if exists:
        # open the pickle file
        with open('classes/classes.pickle', 'rb') as classes:
            # while there are still classes to get from the pickle file
            while 1:
                # try to get the classes
                try:
                    # add class to the classes_list
                    classes_list.append(pickle.load(classes))
                except EOFError:
                    # catch exceptions
                    break

        # get the directory of the current file
        dirname = os.path.dirname(__file__)
        # add desired location of the pickle file to the end of directory name
        pickle_file = os.path.join(dirname, 'classes/classes.pickle')
        # delete the pickle file
        os.remove(pickle_file)

        # create updated classes file
        # for each class in the classes_list
        for a_class in classes_list:
            # try to add classes to the pickle file
            try:
                # if the class from the list is not the same as the class that needs to be updated
                if updatable_class.name != a_class.name:
                    # create/open the pickle file
                    with open('classes/classes.pickle', 'ab') as classes:
                        # add class from the list back to the pickle file
                        pickle.dump(a_class, classes, protocol=pickle.HIGHEST_PROTOCOL)
                else:
                    # else the class from the list is the same as the class that need to be updated
                    # create/open the pickle file
                    with open('classes/classes.pickle', 'ab') as classes:
                        # add updated class to the pickle file in place of the old version in the list
                        pickle.dump(updatable_class, classes, protocol=pickle.HIGHEST_PROTOCOL)
            except:
                # catch exceptions
                pass
    else:
        # catch exceptions
        return

def create_class():
    # try to create a new class
    try:
        # ask for the name of the class
        the_class = input("What is the class name: ")
        # assign the new class to a variable
        new_class = Class(the_class)

        # try to create/append to the pickle file the class variable
        try:
            # add the class to the pickle file
            with open('classes/classes.pickle', 'ab') as classes:
                pickle.dump(new_class, classes, protocol=pickle.HIGHEST_PROTOCOL)
        except:
            # catch exceptions
            pass
    except:
        # catch exceptions
        print("Sorry you did not type in a valid class name try again.")
        # call creat_class() again if an exception is caught
        create_class()

def clear_classes():
    # get the directory of the current file
    dirname = os.path.dirname(__file__)
    # add desired location of the pickle file to the end of directory name
    pickle_file = os.path.join(dirname, 'classes/classes.pickle')
    # delete the pickle file
    os.remove(pickle_file)

def get_class():
    # create a list to hold each class from the pickle file
    classes_list = []

    # ask for the name of the class the user is looking for
    this_class = input("Which class is this?\n").lower()

    # find out if classes.pickle file exists
    exists = os.path.isfile('classes/classes.pickle')

    # if the pickle file exists
    if exists:
        # open pickle file
        with open('classes/classes.pickle', 'rb') as classes:
            # while there are more classes to load
            while 1:
                try:
                    # try to load class into next list location
                    classes_list.append(pickle.load(classes))
                except EOFError:
                    # if no more classes to load
                    break
    else:
        # if pickle file does not exist
        # inform that the user has no classes
        print("You do not have any classes, create one.")
        # prompt for user to create a class
        create_class()
        # return another call to get_class() to ensure no errors are caused
        return get_class()

    # for each of the classes in the classes_list
    for a_class in classes_list:
        # if the desired class is in the classes_list
        if this_class == a_class.name.lower():
            # return the class
            return a_class

    # if not return thus far, the class was not found
    # ask if the user wants to search for another class or create a new one
    input_4 = input("That class was not found.\n1. Search for another class\n2. Create a new class:\n3. Quit Application\n").lower()
    while(input_4 != 1) or (input_4 != 2) or (input_4 != 3):
        if input_4 == "1":
            # call get class again
            return get_class()
        elif input_4 == "2":
            # create a new class
            create_class()
            return get_class()
        elif input_4 == "3":
            exit()

def add_student_to_class():
    # initial prompt followed by prompt in get_class()
    print("The class you like to add a student to,")

    # assign the class that the user wants to add a student to
    intended_class = get_class()

    # ask for the students name
    input_2 = input("What is the students name?\n").lower()

    # add the student to the correct class with that class's add_student function
    intended_class.add_student(input_2, input_2)

    # rewrite the pickle file to have updated student dictionary
    rewrite_classes(intended_class)

def check_class_attendance():
    '''
    exited = False
    check_attendance = input("Would you like to check attendance now? (Y/N): ").lower()

    while (not exited):
        if (check_attendance.lower() == "y" or check_attendance.lower() == "yes"):
            pass  # for student in Class.students
        elif (check_attendance.lower() == "n" or check_attendance.lower() == "no"):
            exited = True
        else:
            check_attendance = input("Please insert a valid input (Y/N): ").lower()
    '''

    # initial prompt followed by prompt in get_class()
    print("The class you are marking attendance for,")

    # assign the class that the user wants to mark attendance for
    intended_class = get_class()

    # call the class mark attendance function to test against it's students
    Class.check_attendance(intended_class)

    # rewrite the pickle file to have updated attendance record
    rewrite_classes(intended_class)

    print("Glad that I could check the attendance for you good sir! Have a wonderful day.")

def activity_request():
    # This is a test to see that the pickle file is updating after a student is marked as attended # print(Class.get_student(get_class(), "rockford"))

    # ask what the user would like to do
    input_1 = input("What would you like to do? \n1. Create a new Class\n2. Add a Student to a Class\n3. Mark attendance of a Student for a Class\n4. Clear Classes\n5. Quit Application\n").lower()

    # determining what to user wants to do
    if input_1 == "1":
        # if adding a class
        create_class()
        activity_request()
    elif input_1 == "2":
        # if adding a student
        add_student_to_class()
        activity_request()
    elif input_1 == "3":
        # if marking a student's attendance
        check_class_attendance()
        activity_request()
    elif input_1 == "4":
        # if clearing pickle file of all classes (deleting pickle file)
        clear_classes()
        activity_request()
    elif input_1 == "5":
        # if exiting the application
        exit()
    else:
        # if incorrect input is given
        print("Sorry, you have not entered a valid number 1, 2, or 3.")
        activity_request()

# initial call of activity request
activity_request()