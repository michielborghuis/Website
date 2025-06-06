from tkinter import *
import GUI


class MainGUI:
    def __init__(self):
        self.root = Tk()

        self.label1 = Label(self.root, text='Advanced SIR model for disease spread.',
                            font=('Calibri', 20)).grid(row=0, columnspan=2)
        self.label2 = Label(self.root, text='Would you like to enter the population manually or to choose a country and'
                                            ' a year corresponding to a population?').grid(row=1, columnspan=2)
        self.buttonManually = Button(self.root, text='Manually', command=self.open_manually).grid(row=2, column=0)
        self.buttonAutomatic = Button(self.root, text='Automatic', command=self.open_automatic).grid(row=2, column=1)

    def open_automatic(self):
        """Opens the second window where you can choose the population by selecting a country and year."""
        automatic = GUI.GUI(0)
        automatic.run()

    def open_manually(self):
        """Opens the second window where you have to choose the population manually."""
        manually = GUI.GUI(1)
        manually.run()

    def run(self):
        """Starts the main window."""
        self.root.geometry('610x400')
        self.root.iconbitmap('C:/Users/michi/Documents/GitHub/Website/pages/virus/COVID-19_icon.ico')
        self.root.mainloop()
