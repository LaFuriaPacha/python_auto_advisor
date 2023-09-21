
# functions to return whether course is been completed or not
def isCourseCompleted(courseDict,course):
    # extracting grade from courseDict and giving default values
    courseGrade = courseDict.get(course.strip(), {}).get('Grade', '')
    # checking if course is graded
    if not (courseGrade.isspace() or courseGrade == ""):
        return 1
    else:
        return 0
 
# function to check whether required prerequites for the course is finished or not
def checkForPrerequitesPassed(courseDict, course):
    # using strip to remove any wide spaces across
    courseRecord = courseDict[course.strip()]
    # extracting prerequisitesForCourse from courseDict and giving default values
    prerequisitesForCourse = courseRecord.get('Prerequisites', '')
    if prerequisitesForCourse.isspace() or prerequisitesForCourse == "":
        return True
    
    for eachCourse in courseDict.keys():
        if (prerequisitesForCourse.strip() == eachCourse) and isCourseCompleted(courseDict,eachCourse) == 1:
            return True
    # checking the format of the prerequites
    preReqGroups = prerequisitesForCourse.split()
    preReqGroupPassedOrFailedDetails = []
    # loop on the each prequest group
    for each_group in preReqGroups:
        each_preReqCourse = each_group.split(',')
        completedPreReq = 0
        for each in each_preReqCourse:
            completedPreReq = completedPreReq + isCourseCompleted(courseDict,each) 
        if completedPreReq == len(each_preReqCourse):
            preReqGroupPassedOrFailedDetails.append(1)
        else:
            preReqGroupPassedOrFailedDetails.append(0)
    if any(preReqGroupPassedOrFailedDetails):
        return True
    else:
        # check preq string in case of preqs available
        return " ".join(preReqGroups)