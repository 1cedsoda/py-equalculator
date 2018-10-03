# first edit: 2017-09-11
# last edit: 2018-10-02
# last edit from: github.com/phyyyl

from interprete import interpreteEquasion
from solve import solveEquasion
from solve import replaceVars
from type import getType
import re
from urllib.parse import quote
import traceback
import json

version = "1.4"


def showBanner():                                                                   # Cool Banner will be printed. Created with network-science.de/ascii/
        print("                               ______            ______      _____")
        print("     ___________ ____  _______ ___  /_________  ____  /_____ __  /____ _________")
        print("     _  _ \  __ `/  / / /  __ `/_  /_  ___/  / / /_  /_  __ `/  __/  __ \_  ___/")
        print("     /  __/ /_/ // /_/ // /_/ /_  / / /__ / /_/ /_  / / /_/ // /_ / /_/ /  /")
        print("     \___/\__, / \__,_/ \__,_/ /_/  \___/ \__,_/ /_/  \__,_/ \__/ \____//_/")
        print("            /_/")
        print("                   github.com/phyyyl/py-equalculator    " + version)


def inputPrompt():                                                                  # when executed the user is able to type in an equasion
    equasion = input("Enter Equasion")
    return equasion                                                                 # returns the input without manipulation


class Term:
    def __init__(self, equasion_as_string, variables={}, loadVariablesFromHeap=False):
        self.inputString = equasion_as_string
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
        try:
            if __name__ == "__main__":
                print("   Interpreted :   ", self.equasion)
                print("   InterpretedStr :", "".join(self.equasion))
                print("   Variables :     ", json.dumps(self.variables, sort_keys=True, indent=2))
            self.reqVars = self.requiredVariables()
            if self.__checkVariableAvailability():
                self.result = float(solveEquasion(replaceVars(self.equasion, self.variables))[0])
            else:
                self.result = None
            return self.result
        except Exception as e:
            errorType = str(type(e))[8:-2]
            tinyEquasion = "".join(self.equasion)
            if len(tinyEquasion) > 20:
                tinyEquasion = tinyEquasion[:17] + "..."
            title = "calculate() " + errorType + " \"" + tinyEquasion + "\""
            body = "Version: _**something for version identification**_\n \
                Input : ```" + self.inputString + "```\n \
                Interpreted : ```" + str(self.equasion) + "```\n \
                Interpreted (string) : ```" + "".join(self.equasion) + "```\n \
                Variables : \n```javascript\n" + json.dumps(self.variables, sort_keys=True, indent=2) + "\n```\n \
                \nException : \n```python\n" + str(traceback.format_exc()) + "```"
            issueLink = "https://github.com/phyyyl/py-equalculator/issues/new?title=" + quote(title, safe='') + "&body=" + quote(body, safe='')
            print("\033[;1mReport Exception: \033[1;31m" + issueLink + "\033[0;0m")

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
        print(Term(input("Enter function: ")))
