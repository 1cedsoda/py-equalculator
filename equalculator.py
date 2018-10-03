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
    def __init__(self, equasion_as_string, variables={}, loadVariablesFromHeap=False):
        if loadVariablesFromHeap:
            self.variables = variables
        else:
            self.variables = variables.copy()
        self.equasion = interpreteEquasion(equasion_as_string)
        self.calculate()

    def set(self, variable, value):
        self.variables[variable] = value

    def requiredVariables(self):
        reqVars = []
        for segment in self.equasion:
            if re.search('[a-zA-Z]', segment):
                reqVars.append(segment)
        return reqVars

    def __checkVariableAvailability(self):
        allAvailable = True
        for reqVar in self.reqVars:
            if reqVar not in self.variables:
                if __name__ == "__main__":
                    self.variables[reqVar] = str(input(reqVar + " = "))
                else:
                    allAvailable = False
        return allAvailable

    def calculate(self):
        if __name__ == "__main__":
            print("Interpreted:", "".join(self.equasion))
        self.reqVars = self.requiredVariables()
        if self.__checkVariableAvailability():
            self.result = float(solveEquasion(self.equasion, self.variables)[0])
        else:
            self.result = None
        return self.result

    def __repr__(self):
        return str(self.result)

    def __float__(self):
        return float(self.result)

    def __int__(self):
        return int(self.result)


if __name__ == "__main__":
    showBanner()
    while True:
        print("")
        print(Term(input("Enter an equasion: ")))
