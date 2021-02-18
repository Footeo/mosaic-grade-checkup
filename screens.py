from tkinter import *
import fetch

class Screens:
	def __init__(self, contentFrame):
		self.contentFrame = contentFrame


class Home:
    def __init__(self, contentFrame, screens):
        self.contentFrame = contentFrame
        self.screens = screens

    def homeDisplay(self):
        self.homemsg1 = Label(self.contentFrame, text="Hello! Thanks for downloading Mosaic Grade Checkup. \nIf you have already been through this intro you can skip it now,\n if not please press the continue intro button.")
        self.homemsg1.grid(row=0, padx=20)

        # self.contBtn = Button(self.contentFrame, text = "Continue Intro", command = lambda: self.intro())
        # self.contBtn.grid(row=1, column=0)

        self.skipBtn = Button(self.contentFrame, text="Skip", command = lambda: self.fetchGrades())
        self.skipBtn.grid(row=2, column=0)
        
        

    def removeContent(self): #Clears screens 
        for widget in self.contentFrame.winfo_children():
            widget.destroy()

    def intro(self):
        self.removeContent()
        self.intromsg1 = Label(self.contentFrame, text="Welcome to the intro, here you will set up the app for future use. \nIf you have questions or concerns please refer to the readme file.")
        self.intromsg1.grid(row=0, padx=20)
        self.intromsg2 = Label(self.contentFrame, text="Input your MacID and McMaster password, \nthese will be saved in the user.txt file for future use.")
        self.intromsg2.grid(row=1)

        self.labelName = Label(self.contentFrame, text ="Enter MacID: ")
        self.labelName.grid(row=2)
        self.inputName = Entry(self.contentFrame)
        self.inputName.grid(row=3)
        self.labelPass = Label(self.contentFrame, text="Enter McMaster Password: ")
        self.labelPass.grid(row=4)
        self.inputPass = Entry(self.contentFrame, show="*")
        self.inputPass.grid(row=5)
        self.labelPass2 = Label(self.contentFrame, text="Reenter McMaster Password: ")
        self.labelPass2.grid(row=6)
        self.inputPass2 = Entry(self.contentFrame, show="*")
        self.inputPass2.grid(row=7)

        self.intromsg3 = Label(self.contentFrame, text="")
        self.intromsg3.grid(row=8)

        self.save = Button(self.contentFrame, text="Save",command = lambda: self.saveMacID(self.inputName.get(),self.inputPass.get(),self.inputPass2.get()))
        self.save.grid(row=9)


    def saveMacID(self, username, password1, password2):
        file = open("user.txt","w")
		# if passwords match
        if (password1==password2):
            self.intromsg3.configure(text = "Passwords Match")
            file.write(username + '\t') #append uName and pass to file
            file.write(password2 + "\n")
            file.close()
            self.intromsg3.configure(text = "Information saved, please continue")
            self.skipBtn = Button(self.contentFrame, text="Continue", command = lambda:self.fetchGrades())
            self.skipBtn.grid(row=10)
        else:
            self.intromsg3.configure(text="Passwords don't match, please try again")
         

    def fetchGrades(self):
        self.removeContent()
        self.fetchMsg = Label(self.contentFrame, text="IMPORTANT!! Before continuing please enter your MacID \nand Password in the fetch.py file and enter the path to your chrome driver\n then restart the app. \n\nWhich term would you like to fetch?")
        self.fetchMsg.grid(row=0, padx=20)
        # Options here

        var1 = IntVar()
        self.currentTerm = Checkbutton(self.contentFrame, text="Current Term", variable=var1)
        self.currentTerm.grid(row=1, column=0)
        var2 = IntVar()
        self.lastTerm = Checkbutton(self.contentFrame, text="Last Term", variable=var2)
        self.lastTerm.grid(row=2, column=0)

        self.fetchMsg2 = Label(self.contentFrame,text="GPA and email coming soon...")
        self.fetchMsg2.grid(row=3)

        self.fetchMsg3 = Label(self.contentFrame, text="Please note it can take up to 30 seconds to complete fetching")
        self.fetchMsg3.grid(row=4, padx=20)
        self.goFetch = Button(self.contentFrame, text="Fetch my grades!", command = lambda: fetch.getGrades(var1.get(),var2.get()))
        self.goFetch.grid(row=5)

        # Current term, or last term
        # Calculate Term GPA?
        # Would you like to be sent an email with the results?

    def gradesMsg(self,grades_msg):
        self.gradesMsg2 = Label(self.contentFrame, text="Here are your results!")
        self.gradesMsg2.grid(row=0, padx=20)
        self.gradesMsg3 = Label(self.contentFrame, text=grades_msg)
        self.gradesMsg3.grid(row=1)
        self.gradesMsg4 = Label(self.contentFrame, text="Close this window and fetch another term, \nor come back later when you get the itch to know.")
        self.gradesMsg4.grid(row=2, padx=20)
