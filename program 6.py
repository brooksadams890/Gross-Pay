

#import modules
from tkinter import *
from tkinter import filedialog
import os

# Calculate gross pay. Overtime is past 40 at 1.5 times rate
def GrossPay(hours, rate):
    pay = 0.0
    if hours > 40:
        pay = (40 * rate) + ((hours-40) * 1.5 * rate)
    else:
        pay = hours * rate
    return pay

# Displays the File Save dialog and allows user to create a file
def CreateFile():
    PayApp.filename = filedialog.asksaveasfilename(parent = PayApp,
                                    initialdir = os.getcwd(),
                                    title = "Please create a file name",
                                    filetypes = (("Text File", "*.txt"),("All Files", "*,.*")))
    fileContents = str(PayApp.filename) + ".txt"
    global payFile #Creates a global variable that is avilable to all functions
    payFile = open(fileContents, "w") #Opens the file to write to it

#This function retrieves the data entered into the textboxes and calls the GrossPay def
def CalcPay():
    hoursWorked = float(txtHours.get())
    payRate = float(txtRate.get())
    grossPay = GrossPay(hoursWorked, payRate) #Finishes the GrossPay function to deliever the variables made its made up of
    txtPay.insert(END, format(grossPay, ".2f")) #Inserts the calculated gross pay at the end
    return
#Retrieves the contents from the textboxes, and writes them to the file
def SavePay():
    fName = txtFName.get()
    lName = txtLName.get()
    hours = txtHours.get()
    rate = txtRate.get()
    pay = txtPay.get()
    payFile.write(fName + "," + lName + "," + hours + "," + rate + "," + pay + ",")
    return

    #Closes the file and terminates the program by destroying the application window
def ExitApp():
    payFile.close()
    PayApp.destroy()
    return

    #Main GUI Window
PayApp = Tk() #Creates main GUI Window
PayApp.title("Gross Pay Calculator") #Sets the applicaion window title
PayApp.geometry("800x400") #Sizes the application window
#Create Textboxes
txtFName = Entry(PayApp, width = 30) #First name textbox
txtFName.grid(column = 50, row = 2)
txtLName = Entry(PayApp, width = 30) #Last name textbox
txtLName.grid(column = 50, row = 3)
txtHours = Entry(PayApp, width = 30) #Hours worked textbox
txtHours.grid(column = 50, row = 4)
txtRate = Entry(PayApp, width = 30) #Pay rate textbox
txtRate.grid(column = 50, row = 5)
txtPay = Entry(PayApp, width = 30) #Gross pay textbox
txtPay.grid(column = 50, row = 6)
#Create Labels
lblFName = Label(PayApp, text = "First name: ") #First name textbox title
lblFName.grid(column = 20, row = 2)
lblLName = Label(PayApp, text = "Last name: ") #Last name textbox title
lblLName.grid(column = 20, row = 3)
lblHours = Label(PayApp, text = "Hours Worked: ") #Hours worked textbox title
lblHours.grid(column = 20, row = 4)
lblRate = Label(PayApp, text = "Hourly Pay Rate: ") #Pay rate textbox title
lblRate.grid(column = 20, row = 5)
lblGrossPay = Label(PayApp, text = "Gross Pay: ") #Gross pay textbox title
lblGrossPay.grid(column = 20, row = 6)
#Create Buttons
btnCalc = Button(PayApp, text = "Calculate Pay", command = CalcPay) #Button to calculate pay
btnCalc.grid(column = 70, row = 6)
btnCreateFile = Button(PayApp, text = "Create a Pay File", command = CreateFile) #Button to create a pay file
#Button to call CreateFile function
btnCreateFile.grid(column = 70, row = 2)
btnSavePay = Button(PayApp, text = "Save Pay Data", command = SavePay) #Button to save pay data
btnSavePay.grid(column = 70, row = 3)
#Button to exit
btnExitApp = Button(PayApp, text = "Exit", command = ExitApp) #Button to exit app
btnExitApp.grid(column = 90, row = 2)

#Function to clear all entry widgets
def ClearFields():
    txtFName.delete(0, END)
    txtLName.delete(0, END)
    txtHours.delete(0, END)
    txtRate.delete(0, END)
    txtPay.delete(0, END)
# Create Clear button
btnClear = Button(PayApp, text = "Clear", command = ClearFields)
btnClear.grid(column = 90, row = 3) 

#Sets focus
txtFName.focus()
txtLName.focus()
txtHours.focus()
txtRate.focus()
txtPay.focus()

#Creates a file after window is opened
PayApp.after(1,FileSave) #The after method runs 1 millisecond after the window is created
PayApp.mainloop()

    


    


    
