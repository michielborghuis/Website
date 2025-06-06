import numpy as np
from Plot import plot
from ODECalculator import calculate_ode
import populations as pop


class Derivatives:
    def __init__(self, population, e0, spreaddays, leninc, r0, deathrate, deathtime, lockdown, lockdownr0, method):
        """Takes all arguments necessary for calculating the ODE's."""
        self.count_while = 0    # counts times of calculating the ODE's

        self.method = method    # method used for calculating the graphs

        self.population = self.population_function(population)  # total amount of people in the population
        self.exposed = e0                                       # initial amount of people exposed by the disease
        self.infected = 0                                       # initial amount of people infected by the disease
        self.susceptible = self.population - self.exposed       # initial amount of people susceptible for the disease
        self.recovered = 0                                      # initial amount of people recovered from the disease
        self.dead = 0                                           # initial amount of people who died from the disease

        self.spreadDays = spreaddays                # number of days an infected person has and can spread the disease
        self.spreadPerDay = 1 / self.spreadDays     # proportion of infected recovering per day
        self.incubationRate = 1 / leninc            # rate at which exposed people become infected
        self.r0 = r0                                # number of people an infected person infects
        self.deathRate = deathrate                  # death rate
        self.deathPerDay = 1/deathtime              # rate at which people die
        self.lockdown = lockdown                    # day at which a lockdown is implemented
        self.locksownr0 = lockdownr0                # number of people an infected person infects after the lockdown

    def R_0_function(self, t):
        """Calculates the number of people an infected person infects."""
        if t < self.lockdown:
            return self.r0
        else:
            return self.locksownr0

    def population_function(self, population):
        """Calculates the total amount of people in the population."""
        if type(population) == int or type(population) == float:
            return population
        else:
            return pop.world_population(population)

    def contacts_function(self, t):
        """Calculates the aount of people an infected person infects per day."""
        return self.R_0_function(t) * self.spreadPerDay

    def susceptible_function(self, t, S, I):
        """"Calculates the derivative (rate of change) of the susceptible people at a given time (t)."""
        return -self.contacts_function(t) * S * I / self.population

    def exposed_function(self, t, S, E, I):
        """Calculates the derivative (rate of change) of the exposed people at a given time (t)."""
        return self.contacts_function(t) * S * I / self.population - self.incubationRate * E

    def infected_function(self, E, I):
        """Calculates the derivative (rate of change) of the infected people at a given time (t)."""
        return self.incubationRate * E - (1-self.deathRate) * self.spreadPerDay * I - self.deathRate * self.deathPerDay * I

    def recovered_function(self, I):
        """Calculates the derivative (rate of change) of the recovered people at a given time (t)."""
        return (1-self.deathRate) * self.spreadPerDay * I

    def dead_function(self, I):
        """Calculates the derivative (rate of change) of the dead people at a given time (t)."""
        return self.deathPerDay * self.deathRate * I

    def deriv(self, y, t):
        """Calculates the derivatives (rates of change) for all of the different groups of people, using the
        y-coordinates at a given time (t) and the formulas for calculating these derivatives."""
        S, E, I, R, D = y
        dSdt = self.susceptible_function(t, S, I)
        dEdt = self.exposed_function(t, S, E, I)
        dIdt = self.infected_function(E, I)
        dRdt = self.recovered_function(I)
        dDdt = self.dead_function(I)
        return dSdt, dEdt, dIdt, dRdt, dDdt

    def calculate(self, days, steps):
        """Calculates all the points for every graph over time (t), if no epidemic has occurred in the given days,
         100 days will be added to the current amount of days, with a maximum of 2000 days."""
        # initial amount of people per group
        S0, E0, I0, R0, D0 = self.susceptible, self.exposed, self.infected, self.recovered, self.dead
        t = np.linspace(0, days, steps)  # list of time points (in days)
        y0 = S0, E0, I0, R0, D0

        # calculate all the points for every graph over time (t), using one of the three methods
        # for solving ordinary differential equations
        S, E, I, R, D = calculate_ode(self.deriv, y0, t, self.method)
        if I[-1] > self.population/100 or S[-500] > self.population/100*99:  # adds 100 days if the
            self.count_while += 1
            if self.count_while > 20:   # stops calculation if there hasn't been an outbreak in 2000 days
                plot(t, S, E, I, R, D)
            else:
                try:
                    self.calculate(days+100, steps+1000)
                except:
                    self.calculate(days+100.1, steps+1000)
        else:
            plot(t, S, E, I, R, D)
