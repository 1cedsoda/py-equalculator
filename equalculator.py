# first edit: 2017-09-11
# last edit: 2018-10-02
# last edit from: github.com/phyyyl

from interprete import interpreteEquasion
from solve import solveEquasion
from type import getType
import re


def showBanner():                                                                   # Cool Banner will be printed. Created with network-science.de/ascii/
        print("                               ______            ______      _____")
        print("     ___________ ____  _______ ___  /_________  ____  /_____ __  /____ _________")
        print("     _  _ \  __ `/  / / /  __ `/_  /_  ___/  / / /_  /_  __ `/  __/  __ \_  ___/")
        print("     /  __/ /_/ // /_/ // /_/ /_  / / /__ / /_/ /_  / / /_/ // /_ / /_/ /  /")
        print("     \___/\__, / \__,_/ \__,_/ /_/  \___/ \__,_/ /_/  \__,_/ \__/ \____//_/")
        print("            /_/")
        print("                   github.com/phyyyl/py-equalculator    v1.4 ")


def inputPrompt():                                                                  # when executed the user is able to type in an equasion
    equasion = input("Enter Equasion")
    return equasion                                                                 # returns the input without manipulation


class Term:
    def __init__(self, equasion_as_string, variables={}):
        self.variables = variables.copy()
        variables = None
        self.equasion_as_list = interpreteEquasion(equasion_as_string)
        self.reqVars = self.requiredVariables(self.equasion_as_list)
        if self.checkVariableAvailability():
            self.result = float(solveEquasion(self.equasion_as_list, self.variables)[0])
        else:
            self.result = None

    def set(self, variable, value):
        self.variables[variable] = value

    def requiredVariables(self, equasion):
        reqVars = []
        for segment in equasion:
            if re.search('[a-zA-Z]', segment):
                reqVars.append(segment)
        return reqVars

    def checkVariableAvailability(self):
        allAvailable = True
        for reqVar in self.reqVars:
            if reqVar not in self.variables:
                if __name__ == "__main__":
                    self.variables[reqVar] = str(input(reqVar + " = "))
                else:
                    allAvailable = False
        return allAvailable

    def __repr__(self):
        return str(self.result)

    def __float__(self):
        return float(self.result)

    def __int__(self):
        return int(self.result)


if __name__ == "__main__":
    showBanner()
    t = 0
    while True:
        print("")
        print(Term(input("Enter an equasion: ")))
