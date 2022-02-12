from codecs import getreader
import os

class Course:
    def __init__(self, name, units):
        self.name = name
        self.units = units
        self.notes = []
        self.meet_link = ''
        self.grade = 0

    def view_course(self):
        print(f"\nName: {self.name}    Units: {self.units}    Link: {self.meet_link}    Grade: {self.grade}")

    def add_meet_link(self, link):
        self.meet_link = link

    def edit_notes(self):
        while True:
            print ("\nCreate(c)      Read(r)     Delete(d)     Back(q)")
            opt = input()
            file_name = self.name + 'Notes.txt'
            if opt == 'c':
                if not file_exist(file_name):
                    print("Write your notes...")
                    notes = input()
                    with open(file_name, 'w', encoding='utf-8') as fil:
                        fil.writelines(notes)
                else:
                    print(file_name + ' already exists.')
            elif opt == 'r':
                if file_exist(file_name):
                    with open(file_name, 'r', encoding='utf-8') as f:
                        note = f.read()
                        print(note)
                else:
                    print("Please create a notes first")
            elif opt =='d':
                if file_exist(file_name):
                    os.remove(file_name)
                else:
                    print("The file does not exist")
            elif opt == 'q':
                break

    def add_grade(self, grade):
        self.grade = grade

def file_exist(file):
    if os.path.exists(file):
        return True
    else:
        return False

def edit(name):    
    while True:
        print("\nNotes(n)     Add Meet Link(l)      Add Grade(g)     Return to Main Page(q)")
        opt = input()
        if opt == 'n':
            name.edit_notes()
        elif opt == 'l':
            link = input("Enter the Gmeet link: ")
            name.add_meet_link(link)
        elif opt == 'g':
            grade = input("Enter your grade: ")
            name.add_grade(grade)
        elif opt == 'q':
            break

courses = []

while True:
    print("\nAdd Course(a)     Remove Course(r)    Edit Course(e)     View Courses(v)     Quit(q)")
    option = input()
    if option == 'a':
        name = input('Please enter Course Name: ')
        units = input('Please enter Course Units: ')
        name = Course(name, units)
        if name not in courses:
            courses.append(name)
        else:
            courses.remove(name)
            print("This course already exists..")
    elif option == 'r':
        course_name = input("Please enter the name of the course you want to remove: ")
        is_course = False
        for x in courses:
            if course_name == x.name:
                courses.remove(x)
                print('The course ' + course_name + ' has been removed.')
                is_course = True
                break
        if not is_course:
            print("ERROR!! There is no such course.")
    elif option == 'e':
        course_name = input("Enter the Name of the course: ")
        is_course = False
        for x in courses:
            if course_name == x.name:
                edit(x)
                is_course = True
                break
        if not is_course:
            print("ERROR!! There is no such course.")
    elif option == 'v':
        for course in courses:
            course.view_course()
    elif option == 'q':
        break
