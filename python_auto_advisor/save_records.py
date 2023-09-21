from tkinter import filedialog
from tkinter import messagebox

# Following function helps in save the data into new file or 
# saving modified data to the existing file
def save_records(courseDict, neworexisting, filepath={}):
    # Creating a new file 
    if neworexisting == 'new':
        new_file=filedialog.asksaveasfile(initialdir="./", mode='w', defaultextension=".txt")
        # Transforming existing coursedict to required format
        new_file.write("\n".join(["|".join(eachValue.values()) for eachValue in courseDict.values()]))
        new_file.close()
     # saving to new file 
    else:
        existing_file=open(filepath.name, 'w')
        # deleting existing data in the file
        existing_file.truncate()
        # Transforming existing coursedict to required format
        existing_file.write("\n".join(["|".join(eachValue.values()) for eachValue in courseDict.values()]))
        existing_file.close()
    # Message box to show data saved
    messagebox.showinfo("Saved","Saved Successfully...")