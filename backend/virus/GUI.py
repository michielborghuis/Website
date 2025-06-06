from tkinter import *
import Derivatives
import populations as pop


class GUI:
    def __init__(self, choice):
        """Takes the choice of choosing the population manually or choosing it by country and year."""
        self.root = Tk()

        self.choice = choice
        self.labels()
        self.buttons()
        self.information_button()

        if self.choice == 0:  # create dropdown menu for the country and year
            self.country_list = pop.list_of_countries()
            self.clickedCountry = StringVar(self.root)
            self.clickedCountry.set("Netherlands")
            self.dropCountry = OptionMenu(self.root, self.clickedCountry, *self.country_list)
            self.dropCountry.grid(row=10, column=1)

            self.year_list = pop.list_of_years()
            self.clickedYear = StringVar(self.root)
            self.clickedYear.set("2019")
            self.dropYear = OptionMenu(self.root, self.clickedYear, *self.year_list)
            self.dropYear.grid(row=11, column=1)

        if self.choice == 1:    # create entry for the population
            self.inPopulation = Entry(self.root, width=25, fg='grey')
            self.inPopulation.insert(0, 'Enter population')
            self.inPopulation.grid(row=10, column=1)
            self.inPopulation.bind("<Button-1>", lambda event: self.clear_entry(event, self.inPopulation))

        # create entry boxes
        self.inInitialExposed = Entry(self.root, width=25, fg='grey')
        self.inInitialExposed.insert(0, 'Enter initial exposed')
        self.inInitialExposed.grid(row=12, column=1)
        self.inInitialExposed.bind("<Button-1>", lambda event: self.clear_entry(event, self.inInitialExposed))
        self.inSpreadDays = Entry(self.root, width=25, fg='grey')
        self.inSpreadDays.insert(0, 'Enter days of spread')
        self.inSpreadDays.grid(row=13, column=1)
        self.inSpreadDays.bind("<Button-1>", lambda event: self.clear_entry(event, self.inSpreadDays))
        self.inIncubation = Entry(self.root, width=25, fg='grey')
        self.inIncubation.insert(0, 'Enter days of incubation')
        self.inIncubation.grid(row=14, column=1)
        self.inIncubation.bind("<Button-1>", lambda event: self.clear_entry(event, self.inIncubation))
        self.inR0 = Entry(self.root, width=25, fg='grey')
        self.inR0.insert(0, 'Enter R0')
        self.inR0.grid(row=15, column=1)
        self.inR0.bind("<Button-1>", lambda event: self.clear_entry(event, self.inR0))
        self.inDeathRate = Entry(self.root, width=25, fg='grey')
        self.inDeathRate.insert(0, 'Enter deathrate')
        self.inDeathRate.grid(row=16, column=1)
        self.inDeathRate.bind("<Button-1>", lambda event: self.clear_entry(event, self.inDeathRate))
        self.inDeathTime = Entry(self.root, width=25, fg='grey')
        self.inDeathTime.insert(0, 'Enter days until death')
        self.inDeathTime.grid(row=17, column=1)
        self.inDeathTime.bind("<Button-1>", lambda event: self.clear_entry(event, self.inDeathTime))
        self.inLockdown = Entry(self.root, width=25, fg='grey')
        self.inLockdown.insert(0, 'Enter day of lockdown')
        self.inLockdown.grid(row=18, column=1)
        self.inLockdown.bind("<Button-1>", lambda event: self.clear_entry(event, self.inLockdown))
        self.inLockdownR0 = Entry(self.root, width=25, fg='grey')
        self.inLockdownR0.insert(0, 'Enter R0 after lockdown')
        self.inLockdownR0.grid(row=19, column=1)
        self.inLockdownR0.bind("<Button-1>", lambda event: self.clear_entry(event, self.inLockdownR0))

        # create option for the ODE calculation
        self.methodOptions = ["Euler's Method (1st order)", "Heun's Method (2nd order)", "Runge-Kutta (4th order)"]
        self.clickedMethod = StringVar(self.root)
        self.clickedMethod.set(self.methodOptions[-1])
        self.dropMethod = OptionMenu(self.root, self.clickedMethod, *self.methodOptions)
        self.dropMethod.grid(row=20, column=1)

        # create error messages
        self.error_label_population = Label(self.root, text='Population has to be a whole number and at least two.')
        self.error_label_e0 = Label(self.root, text='Initial exposed must be a whole number, lower than population '
                                                    'and higher than zero.')
        self.error_label_spread_days = Label(self.root, text='Days of spread must be higher than zero.')
        self.error_label_incubation = Label(self.root, text='Days of incubation must be higher than zero.')
        self.error_label_r0 = Label(self.root, text='R0 must be at least zero.')
        self.error_label_death_rate = Label(self.root, text='Death rate must be at least zero and at most one.')
        self.error_label_death_time = Label(self.root, text='Days until death must at least days of '
                                                            'spread plus days of incubation.')
        self.error_label_lockdown = Label(self.root, text='Day of lockdown must be at least zero.')
        self.error_label_lockdown_r0 = Label(self.root, text='R0 during lockdown must be at least 0.')
        self.except_label = Label(self.root, text='All inputs must be numbers.')
        self.error_label = Label(self.root)

    def labels(self):
        """Creates all labels."""
        if self.choice == 0:
            labelCountry = Label(self.root, text='Country', width=25, anchor='e').grid(row=10, column=0)
            labelYear = Label(self.root, text='Year', width=25, anchor='e').grid(row=11, column=0)
        elif self.choice == 1:
            labelPopulation = Label(self.root, text='Population', width=25, anchor='e').grid(row=10, column=0)

        myLabel2 = Label(self.root, text='Fill in the variables.').grid(row=0, column=1, sticky='w')
        labelInitialExposed = Label(self.root, text='Initial exposed', width=25, anchor='e').grid(row=12, column=0)
        labelSpreadDays = Label(self.root, text='Days of spread', width=25, anchor='e').grid(row=13, column=0)
        labelIncubation = Label(self.root, text='Days of incubation', width=25, anchor='e').grid(row=14, column=0)
        labelR0 = Label(self.root, text='R0', width=25, anchor='e').grid(row=15, column=0)
        labelDeathRate = Label(self.root, text='Deathrate', width=25, anchor='e').grid(row=16, column=0)
        labelDeathTime = Label(self.root, text='Days until death', width=25, anchor='e').grid(row=17, column=0)
        labelLockdown = Label(self.root, text='Day of lockdown', width=25, anchor='e').grid(row=18, column=0)
        labelLockdownR0 = Label(self.root, text='R0 after lockdown', width=25, anchor='e').grid(row=19, column=0)
        labelMethod = Label(self.root, text='Method', width=25, anchor='e').grid(row=20, column=0)

    def buttons(self):  # Creating a button which plots the graphs
        """Creates a button for checking the variables, for plotting the graphs and to exit the window."""
        checkButton = Button(self.root, text='Check variables', padx=40, pady=10, command=self.check).grid(row=30,
                                                                                                           column=0)
        graphButton = Button(self.root, text='Plot graphs!', padx=40, pady=10, command=self.calculate).grid(row=30,
                                                                                                            column=1)
        exitButton = Button(self.root, text='Exit', padx=40, pady=10, command=self.close).grid(row=30, column=2)

    def information_button(self):
        """Creates the buttons which gives you the explanation of the variable."""
        country = 'The country of which you want the population.'
        year = 'The year of which you want the population of the country above.'
        population = 'The total population of the area where the disease is spreading.'
        initial_exposed = 'The initial amount of people who are exposed by the disease. Exposed means you have the ' \
                          'disease, but you are not able to spread it yet.'
        spread_days = 'The total amount of days an infected person is able to spread the disease.'
        incubation_days = 'The total amount of days a person is infected, but is not able to spread it yet.'
        r0 = 'The average number of infections caused by an infected person during the entire period of spreading' \
             ' the disease.'
        death_rate = 'The number of people who die per infected person. (E.g. if 2% of the infected people die, then ' \
                     'the deathrate is 0.02)'
        days_until_death = 'The number of days it takes until someone infected dies.'
        lockdown = 'The day at which the lockdown is implemented with the first exposed person at day 0.'
        lockdown_r0 = 'R0 during the lockdown. (See R0 and lockdown)'
        method = 'The graphs are calculated by differential equations. The higher the order the better the ' \
                 'calculation of the graphs.'

        if self.choice == 0:
            countryButton = Button(self.root, text='Explanation')
            countryButton.grid(row=10, column=2)
            countryButton.bind("<Button-1>", lambda event: self.explanation(event, country, 10))
            yearButton = Button(self.root, text='Explanation')
            yearButton.grid(row=11, column=2)
            yearButton.bind("<Button-1>", lambda event: self.explanation(event, year, 11))
        elif self.choice == 1:
            populationButton = Button(self.root, text='Explanation')
            populationButton.grid(row=10, column=2)
            populationButton.bind("<Button-1>", lambda event: self.explanation(event, population, 10))

        initialExposedButton = Button(self.root, text='Explanation')
        initialExposedButton.grid(row=12, column=2)
        initialExposedButton.bind("<Button-1>", lambda event: self.explanation(event, initial_exposed, 12))
        spreadDaysButton = Button(self.root, text='Explanation')
        spreadDaysButton.grid(row=13, column=2)
        spreadDaysButton.bind("<Button-1>", lambda event: self.explanation(event, spread_days, 13))
        incubationButton = Button(self.root, text='Explanation')
        incubationButton.grid(row=14, column=2)
        incubationButton.bind("<Button-1>", lambda event: self.explanation(event, incubation_days, 14))
        R0Button = Button(self.root, text='Explanation')
        R0Button.grid(row=15, column=2)
        R0Button.bind("<Button-1>", lambda event: self.explanation(event, r0, 15))
        deathrateButton = Button(self.root, text='Explanation')
        deathrateButton.grid(row=16, column=2)
        deathrateButton.bind("<Button-1>", lambda event: self.explanation(event, death_rate, 16))
        deathTimeButton = Button(self.root, text='Explanation')
        deathTimeButton.grid(row=17, column=2)
        deathTimeButton.bind("<Button-1>", lambda event: self.explanation(event, days_until_death, 17))
        lockdownButton = Button(self.root, text='Explanation')
        lockdownButton.grid(row=18, column=2)
        lockdownButton.bind("<Button-1>", lambda event: self.explanation(event, lockdown, 18))
        lockdownR0Button = Button(self.root, text='Explanation')
        lockdownR0Button.grid(row=19, column=2)
        lockdownR0Button.bind("<Button-1>", lambda event: self.explanation(event, lockdown_r0, 19))
        methodButton = Button(self.root, text='Explenation')
        methodButton.grid(row=20, column=2)
        methodButton.bind("<Button-1>", lambda event: self.explanation(event, method, 20))

    def explanation(self, event, text, row):
        """Makes labels for the explanations and shows them in the window."""
        label = Label(self.root, text=text)
        label.grid(row=row, column=3, sticky='w')

    def clear_entry(self, event, entry):
        """Clears an entry after you click it."""
        entry.delete(0, END)

    def calculate(self):
        """Makes a model of the entered variables."""
        self.check()
        if self.check() == 0:
            method = self.methodOptions.index(self.clickedMethod.get())
            if self.choice == 0:
                model = Derivatives.Derivatives([self.clickedCountry.get(), self.clickedYear.get()], float(self.inInitialExposed.get()),
                                    float(self.inSpreadDays.get()), float(self.inIncubation.get()), float(self.inR0.get()),
                                    float(self.inDeathRate.get()), float(self.inDeathTime.get()),
                                    float(self.inLockdown.get()),
                                    float(self.inLockdownR0.get()), method)
                model.calculate(99.8, 1000)
            elif self.choice == 1:
                model = Derivatives.Derivatives(float(self.inPopulation.get()), float(self.inInitialExposed.get()),
                                    float(self.inSpreadDays.get()), float(self.inIncubation.get()), float(self.inR0.get()),
                                    float(self.inDeathRate.get()), float(self.inDeathTime.get()),
                                    float(self.inLockdown.get()),
                                    float(self.inLockdownR0.get()), method)
                model.calculate(99.8, 1000)

    def close(self):
        """Closes the window."""
        self.root.destroy()

    def check(self):
        """Checks if all of the variables are entered correctly."""
        error_count = 0

        def represents_int(s):
            try:
                int(s)
                return True
            except:
                return False

        try:
            if self.choice == 1:
                if float(self.inPopulation.get()) < 2 or not represents_int(self.inPopulation.get()):
                    self.error_label_population.grid(row=100, columnspan=4, sticky='w')
                    error_count += 1
                else:
                    self.error_label_population.grid_forget()
                if float(self.inPopulation.get()) <= float(self.inInitialExposed.get()) or \
                        not represents_int(self.inInitialExposed.get()) or float(self.inInitialExposed.get()) < 1:
                    self.error_label_e0.grid(row=101, columnspan=4, sticky='w')
                    error_count += 1
                else:
                    self.error_label_e0.grid_forget()
            if float(self.inSpreadDays.get()) <= 0:
                self.error_label_spread_days.grid(row=102, columnspan=4, sticky='w')
                error_count += 1
            else:
                self.error_label_spread_days.grid_forget()
            if float(self.inIncubation.get()) <= 0:
                self.error_label_incubation.grid(row=103, columnspan=4, sticky='w')
                error_count += 1
            else:
                self.error_label_incubation.grid_forget()
            if float(self.inR0.get()) < 0:
                self.error_label_r0.grid(row=104, columnspan=4, sticky='w')
                error_count += 1
            else:
                self.error_label_r0.grid_forget()
            if float(self.inDeathRate.get()) < 0 or float(self.inDeathRate.get()) > 1:
                self.error_label_death_rate.grid(row=105, columnspan=4, sticky='w')
                error_count += 1
            else:
                self.error_label_death_rate.grid_forget()
            if float(self.inDeathTime.get()) < (float(self.inIncubation.get()) + float(self.inSpreadDays.get())):
                self.error_label_death_time.grid(row=106, columnspan=4, sticky='w')
                error_count += 1
            else:
                self.error_label_death_time.grid_forget()
            if float(self.inLockdown.get()) < 0:
                print(self.inLockdown)
                self.error_label_lockdown.grid(row=107, columnspan=4, sticky='w')
                error_count += 1
            else:
                self.error_label_lockdown.grid_forget()
            if float(self.inLockdownR0.get()) < 0:
                self.error_label_lockdown_r0.grid(row=108, columnspan=4, sticky='w')
                error_count += 1
            else:
                self.error_label_lockdown_r0.grid_forget()
            self.except_label.grid_forget()
        except:
            self.except_label.grid(row=33, columnspan=4, sticky='w')
            error_count += 1

        if error_count == 1:
            self.error_label.config(text=str(error_count) + ' error:')
            self.error_label.grid(row=32, sticky='w')
        else:
            self.error_label.config(text=str(error_count) + ' errors:')
            self.error_label.grid(row=32, sticky='w')
        return error_count

    def run(self):
        """Starts the second window."""
        self.root.mainloop()
