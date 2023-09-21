from checkForPrerequites import isCourseCompleted
# Course dict for the the given grades
CREDITS_DICT = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0,
}

# function to calculate GPA for whole course and selected course
def calculateGPA(courseDict={}):
    # checking length of course dict before calculating the course 
    if len(courseDict)==0:
        return 0.0, 0.0
    #  formula reference from https://gpacalculator.net/how-to-calculate-gpa/
    totalCredits = 0
    calculatedCredits = 0
    totalCreditsForSelectedCourses = 0
    calculatedCreditsForSelectedCourses = 0
    for eachCourse in courseDict.values():
        # get credit hours from the course dict project
        credits = eachCourse.get("Credit Hours", 0)
        # get grade from the course dict project
        grade = eachCourse.get("Grade", "F")
        totalCredits = totalCredits + int(credits)
        calculatedCredits = calculatedCredits + (CREDITS_DICT.get(grade, 0.0) * int(credits))
        if isCourseCompleted(courseDict,eachCourse.get("Course", ""))==1:
            totalCreditsForSelectedCourses = totalCreditsForSelectedCourses+ int(credits)
            calculatedCreditsForSelectedCourses = calculatedCreditsForSelectedCourses + (CREDITS_DICT.get(grade, 0.0) * int(credits))
    # formating the calculated GPA to two points
    if not (totalCredits==0 and calculatedCredits==0):
        wholeCourseGPA = format(calculatedCredits/totalCredits,".1f")
    else:
        wholeCourseGPA = 0.0
    

    if not (totalCreditsForSelectedCourses==0 and calculatedCreditsForSelectedCourses==0):
        selectedCourseGPA =  format(calculatedCreditsForSelectedCourses/totalCreditsForSelectedCourses,".1f")
    else:
        selectedCourseGPA = 0.0
    return wholeCourseGPA, selectedCourseGPA