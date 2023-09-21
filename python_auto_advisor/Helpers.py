
from tkinter import messagebox
# Course columns dict
COURSE_NAME_DICT = {
    '0': 'Course', 
    '1': 'Credit Hours',
    '2': 'Prerequisites',
    '3': 'Planned Semester', 
    '4': 'Grade'
}

# function to format the dict to file format
def createFormatFromDict(courseDict):
    return "\n".join(["|".join(eachValue.values()) for eachValue in courseDict.values()])

# function to create dict from file
def createDictFromtheFileContent(content):
    courseDict = {}
    records = []
    for eachline in content:
        eachline = eachline.rstrip()
        print(eachline, "eachLine")
        if not eachline.isspace() and eachline.rstrip():
            numberOfRecords = eachline.split('|')
            print("numberOfRecords", numberOfRecords)
            if '|' in eachline:
                records.append(eachline.split('|'))
            else:
                messagebox.showerror("Error","Invalid File")
                return courseDict
    print("records", records)
    if not len(records) == 0:
        for eachRow in records:
            courseDict[eachRow[0].strip()] = {}
            for eachItem in range(len(eachRow)):
                if COURSE_NAME_DICT.get(str(eachItem), False):
                    courseDict[eachRow[0].strip()][COURSE_NAME_DICT[str(eachItem)]] = eachRow[eachItem].strip()
    return courseDict