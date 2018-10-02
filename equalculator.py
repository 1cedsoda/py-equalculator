# first edit: 2017-09-11
# last edit: 2018-10-02
# last edit from: github.com/phyyyl

from interprete import interpreteEquasion
from solve import solveEquasion


def showBanner():                                                                   # Cool Banner will be printed. Created with network-science.de/ascii/
        print("                               ______            ______      _____")
        print("     ___________ ____  _______ ___  /_________  ____  /_____ __  /____ _________")
        print("     _  _ \  __ `/  / / /  __ `/_  /_  ___/  / / /_  /_  __ `/  __/  __ \_  ___/")
        print("     /  __/ /_/ // /_/ // /_/ /_  / / /__ / /_/ /_  / / /_/ // /_ / /_/ /  /")
        print("     \___/\__, / \__,_/ \__,_/ /_/  \___/ \__,_/ /_/  \__,_/ \__/ \____//_/")
        print("            /_/")
        print("                   github.com/phyyyl/py-equalculator    v1.3 ")


def inputPrompt():                                                                  # when executed the user is able to type in an equasion
    equasion = input("Enter Equasion")
    return equasion                                                                 # returns the input without manipulation


class Term:
    def __init__(self, equasion_as_string):
        self.equasion_as_list = interpreteEquasion(equasion_as_string)
        try:
            self.result = float(solveEquasion(self.equasion_as_list)[0])
        except:
            self.result = None

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
        print(Term(input("Enter an equasion: ")).result)
