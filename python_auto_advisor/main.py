from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
from save_records import save_records
import Helpers
import UIConstants
from checkForPrerequites import checkForPrerequitesPassed
from checkForPrerequites import isCourseCompleted
from calculateGPA import calculateGPA
courseDict = {}
neworexisting=''
filepath=""

# Below function helps in saving the record
def saveRecord():
    global termEvent, courseEvent, gradeEvent, modifiedData, courseDict
    ty = termEvent.get()
    course = courseEvent.get()
    grade = gradeEvent.get()
    # Checking for minimum data before we perform operations
    if ty == "Select":
        messagebox.showerror("Error","Please select valid term")
        return
    if course == "Select":
        messagebox.showerror("Error","Please select valid course")
        return
    if grade == "Select":
        messagebox.showerror("Error","Please select valid grade")
        return
    # Checking for the prereq condition 
    prerequisite_state = checkForPrerequitesPassed(courseDict, course)

    if prerequisite_state == True:
        if isCourseCompleted(courseDict,course):
            messagebox.showerror("Error","Course selected is already graded")
        else:
            # Pushing selected data to course dict
            courseDict[course]['Grade'] = grade
            courseDict[course]['Planned Semester'] = ty
            modifiedData.delete("1.0","end")
            modifiedData.insert(END, Helpers.createFormatFromDict(courseDict))
            termEvent.set('Select')
            courseEvent.set('Select')
            gradeEvent.set('Select')
            setCourseOptions()
            messagebox.showinfo("Success","Selected course information is added")
            calculateAndShowGPA()
    else:
        messagebox.showwarning("Error","The Selected course has prerequisites which need to be completed first.\n Selected Course: {}\nPrequistes: {}".format(course,prerequisite_state))

# Following function handles the open file logic with and process file data
def openFile():
    global course_dropdown_options, courseEvent, neworexisting, filepath, modifiedData, courseDict
    neworexisting='existing'
    setDefaultsToDropDown()
    inputfile = filedialog.askopenfile(initialdir="./")
    filepath=inputfile
    if inputfile!=None:
        courseDict = Helpers.createDictFromtheFileContent(inputfile)
        modifiedData.insert(END, Helpers.createFormatFromDict(courseDict))
        setCourseOptions()
        calculateAndShowGPA()
    else:
        print("No File Selected")

# Following function handles the pressing on the new student
def onPressNewStudent():
    global mainwindow, neworexisting, courseDict
    neworexisting='new'
    setDefaultsToDropDown()
    courseData = open('courseData.txt')
    courseDict = Helpers.createDictFromtheFileContent(courseData)
    modifiedData.insert(END, Helpers.createFormatFromDict(courseDict))
    setCourseOptions()
    calculateAndShowGPA()

# Following function calculates and show the data in the label fields
def calculateAndShowGPA():
    global mainwindow, courseDict
    wholeCourseGPA,selectedCourseGPA = calculateGPA(courseDict)
    wholeGpa = Label(mainwindow , text = "Calculated GPA for whole course: "+ str(wholeCourseGPA)+"/4.0", font=(UIConstants.FONT_NAME, 16), background=UIConstants.BG_COLOR)
    wholeGpa.grid(row=4,column=3,padx=10,pady=10)
    selectedGpa = Label(mainwindow , text = "Calculated GPA for selected courses: "+ str(selectedCourseGPA)+"/4.0", font=(UIConstants.FONT_NAME, 16), background=UIConstants.BG_COLOR)
    selectedGpa.grid(row=5,column=3,padx=3,pady=10)

# Following function set the courses list to the dropdown from the course dict
def setCourseOptions():
    global course_dropdown_options, mainwindow, courseDict, courseEvent
    courseEvent = StringVar()
    courseList = []
    for singleCourse in courseDict.keys():
       if isCourseCompleted(courseDict, singleCourse)==0:
           courseList.append(singleCourse)
    print(courseList, courseDict.keys(), "setCourseOptions")       
    course_dropdown_options = OptionMenu(mainwindow, courseEvent,"Select", *courseList)
    course_dropdown_options.grid(row=5,column=2,padx=10,pady=10)

# Following function set default values to the drop down
def setDefaultsToDropDown():
     global termEvent, courseEvent, gradeEvent, modifiedData, courseDict
     termEvent.set('Select')
     courseEvent.set('Select')
     gradeEvent.set('Select')
     modifiedData.delete("1.0","end")
     courseDict = {}
    

# Main window configuration
mainwindow = Tk()
mainwindow.geometry("1100x850")
mainwindow.title("Computer Science | Auto Advisor SEMO ")
mainwindow['bg'] = UIConstants.BG_COLOR
# Added Titles
mainTitle = Label(mainwindow , text = "Southeast Missouri State University", foreground = UIConstants.FONT_COLOR_RED ,font=(UIConstants.FONT_NAME, 30), background=UIConstants.BG_COLOR)
mainTitle.grid(row=0,column=2,pady=10)
helperTitle = Label(mainwindow , text = "Bachelor of Science in Computer Science", font=(UIConstants.FONT_NAME, 25), background=UIConstants.BG_COLOR)
helperTitle.grid(row=1,column=2,pady=10)
header = Label(mainwindow , text = "Degree Progress", foreground = UIConstants.FONT_COLOR_RED, font=(UIConstants.FONT_NAME, 20), background=UIConstants.BG_COLOR)
header.grid(row=2,column=2,padx=10,pady=10)

modifiedData = Text(mainwindow, font=("", 10))
modifiedData.insert(END,Helpers.createFormatFromDict(courseDict))
modifiedData.grid(row=3,column=2)

# drop down UI for term year
term_year_dropdown = Label(mainwindow, text = "Select Term & Year: ", foreground = UIConstants.FONT_COLOR_RED, anchor= 'center', font=(UIConstants.FONT_NAME, 15), background=UIConstants.BG_COLOR)
term_year_dropdown.grid(row=4,column=1,padx=10,pady=10)
termEvent = StringVar()
term_year_dropdown_options = OptionMenu(mainwindow, termEvent , "Select: ",'Fall 2021','Spring 2022','Fall 2022','Spring 2023','Fall 2023','Spring 2024','Fall 2024','Spring 2025')
term_year_dropdown_options.grid(row=4,column=2,padx=10,pady=10)

# drop down UI for courses
courses_dropDown = Label(mainwindow, text = "Course: ", foreground = UIConstants.FONT_COLOR_RED, font=(UIConstants.FONT_NAME, 15), background=UIConstants.BG_COLOR)
courses_dropDown.grid(row=5,column=1,padx=10,pady=10)
courseEvent = StringVar()
course_dropdown_options = OptionMenu(mainwindow, courseEvent , 'Select', *courseDict.keys())
course_dropdown_options.grid(row=5,column=2,padx=10,pady=10)

# drop down UI for grades
grades_dropdown = Label(mainwindow, text = "Grade: ", foreground = UIConstants.FONT_COLOR_RED, font=(UIConstants.FONT_NAME, 15), background=UIConstants.BG_COLOR)
grades_dropdown.grid(row=6,column=1,padx=10,pady=10)
gradeEvent = StringVar()
grades_dropdown_options = OptionMenu(mainwindow, gradeEvent , "Select ", 'A','B','C','D','F')
grades_dropdown_options.grid(row=6,column=2,padx=10,pady=10)

#  drop down UI for add course
add_course_option = Button(mainwindow, text ="Add", command = saveRecord)
add_course_option.grid(row=7,column=2, padx=10, pady=10)

#  Buttons UI
newstudentbutton = Button(mainwindow, text = "New Student File", command = onPressNewStudent)
newstudentbutton.grid(row=9,column=1, padx=10, pady=10)

openstudentbutton = Button(mainwindow, text = "Open Student File", command = openFile)
openstudentbutton.grid(row=9,column=2, padx=10, pady=10)

savestudentbutton = Button(mainwindow , text = "Save Student Records", command = lambda: save_records(courseDict, neworexisting, filepath))
savestudentbutton.grid(row=9,column=3,)

exitbutton = Button(mainwindow , text= "Exit", command=mainwindow.quit )
exitbutton.grid(row=10,column=1)
onPressNewStudent()
mainwindow.mainloop()