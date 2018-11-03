#from Class import Class
import pickle

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

def check_class_attendance():
    exited = False
    check_attendance = input("Would you like to check attendance now? (Y/N): ").lower()

    while (not exited):
        if (check_attendance.lower() == "y" or check_attendance.lower() == "yes"):
            pass  # for student in Class.students
        elif (check_attendance.lower() == "n" or check_attendance.lower() == "no"):
            exited = True
        else:
            check_attendance = input("Please insert a valid input (Y/N): ").lower()

    print("Glad that I could check the attendance for you good sir! Have a wonderful day.")

def get_class():

    with open('/Classes/classes.pickle', 'rb') as classes:
        the_classes = pickle.load(classes)

    this_class = input("Which class is this? (type q/quit to go back): ").lower()
    if (again == "q" or again == "quit"):
        return

    for a_class in the_classes:
        if this_class == a_class.name.lower():
            return a_class

    again = input(" That class was not found, please try again or type q/quit to exit: ").lower
    if(again == "q" or again == "quit"):
        return
    else:
        get_class()

def create_class():

    try:
        the_class = input("What is the class name: ")
        new_class = Class(the_class)

        try:
            with open('/Classes/classes.pickle', 'wb') as classes:
                pickle.dump(new_class, classes, protocol=pickle.HIGHEST_PROTOCOL)
        except:
            pass
    except:
        print("Sorry you did not type in a valid class name try again.")
        create_class()