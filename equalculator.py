#first edit: 2017-09-11
#last edit: 2017-09-15
#last edit from: github.com/Phyyyl

def showBanner():                                                                   # Cool Banner will be printed. Created with network-science.de/ascii/
        print("                               ______            ______      _____")
        print("     ___________ ____  _______ ___  /_________  ____  /_____ __  /____ _________")
        print("     _  _ \  __ `/  / / /  __ `/_  /_  ___/  / / /_  /_  __ `/  __/  __ \_  ___/")
        print("     /  __/ /_/ // /_/ // /_/ /_  / / /__ / /_/ /_  / / /_/ // /_ / /_/ /  /")
        print("     \___/\__, / \__,_/ \__,_/ /_/  \___/ \__,_/ /_/  \__,_/ \__/ \____//_/")
        print("            /_/")
        print("                   github.com/Phyyyl/py-equalculator    v1.0 ")

def inputPrompt():                                                                  # when executed the user is able to type in an equasion
    equasion = input("Enter Equasion")
    return equasion                                                                 # returns the input without manipulation

def splitEquasion(equasion_as_string):                                              # splits a equasion in a string into different parts
    string = equasion_as_string                                                     # code will look cleaner with shorter variables
   #equasion = equasion_as_list                                                     # code will look cleaner with shorter variables

    lasttype = ""                                                                   # the chartype (getType()) from the last checked char
    currenttype = ""                                                                # the crurrent checked chartype (getType())
    equasionindex = 0                                                               # the index of the last added entry to the equasion list
    equasion = []                                                                   # declaring the equasion list

    currenttype = string[0]                                                         # the first char haven't to compared with the one before, because there is no one before :D
    equasion.append(str(string[0]))                                                 # ...and will be direcly a new entry in the equasionlist

    for i in range(1, len(string)):                                                 # for every char in the string except the first
        lasttype = currenttype                                                      # the currenttype from the last run of the for-loop will now become
        currenttype = getType(str(string[i]))                                       # getting a new currenttype from a char with the getType() function from the equasion string
        if currenttype == "space":                                                  # checking if the currenttype is "space" and ...
            continue                                                                # ...doing nothing, because spaces should be ignored
        elif getType(equasion[equasionindex][-1]) == getType(string[i]):            # when the current and last chartype is equal to each other...
            equasion[equasionindex] = str(equasion[equasionindex]) + str(string[i]) # ...add the current char to the last entry in the equasionlist
        else:                                                                       # when it's an other type of char is should...
            equasion.append(str(string[i]))                                         # ...create a new entry in the equasionlist with the current char
            equasionindex = equasionindex + 1                                       # there is anew entry, so the programm should easily remember the highest index of the equasionlist

    equasion_as_list = equasion                                                     # converting back to a longer variablename to keep an order
    return equasion_as_list                                                         # the equasion interpreted to a list will get returned

def getType(char):                                                                  # returns the type of a char
    char = str(char)                                                                # only strings will get a match

    #number
    if char == "0":
        return "number"
    elif char == "1":
        return "number"
    elif char == "2":
        return "number"
    elif char == "3":
        return "number"
    elif char == "4":
        return "number"
    elif char == "5":
        return "number"
    elif char == "6":
        return "number"
    elif char == "7":
        return "number"
    elif char == "8":
        return "number"
    elif char == "9":
        return "number"
    elif char == ",":
        return "number"
    elif char == ".":
        return "number"

    #action
    elif char == "*":
        return "action"
    elif char == "/":
        return "action"
    elif char == "+":
        return "action"
    elif char == "-":
        return "action"
    elif char == "^":
        return "action"
    elif char == "%":
        return "action"

    #bracket
    elif char == "(":
        return "bracket"
    elif char == ")":
        return "bracket"

    #variable
    elif char == "a":
        return "variable"
    elif char == "b":
        return "variable"
    elif char == "c":
        return "variable"
    elif char == "d":
        return "variable"
    elif char == "e":
        return "variable"
    elif char == "f":
        return "variable"
    elif char == "g":
        return "variable"
    elif char == "h":
        return "variable"
    elif char == "i":
        return "variable"
    elif char == "j":
        return "variable"
    elif char == "k":
        return "variable"
    elif char == "l":
        return "variable"
    elif char == "m":
        return "variable"
    elif char == "n":
        return "variable"
    elif char == "o":
        return "variable"
    elif char == "p":
        return "variable"
    elif char == "q":
        return "variable"
    elif char == "r":
        return "variable"
    elif char == "s":
        return "variable"
    elif char == "t":
        return "variable"
    elif char == "u":
        return "variable"
    elif char == "v":
        return "variable"
    elif char == "w":
        return "variable"
    elif char == "x":
        return "variable"
    elif char == "y":
        return "variable"
    elif char == "z":
        return "variable"

    elif char == " ":
        return "space"
    elif char == "_":
        return "space"

    else:
        print("The char \"", char, "\" is not valid")

def solveEquasion(equasion_as_list):                                                # solving an equasion (recursive, because of brackets)
    equasion = equasion_as_list                                                     # code will look cleaner with shorter variables

    bracket = 0
    for n in range(0, len(equasion)):                                               # every entry in the equasionlist will be checked for brackets
        if equasion[n] == "(":
            bracket = bracket + 1
        if equasion[n] == ")":
            bracket = bracket + 1

    if bracket > 0:                                                                 #if there are brackets
        for missions in range(0,bracket//2):                                        #In every mission one bracket pair will be solved
            missionCompleted = False
            leftBracket = 0
            rightBracket = 0
            sublist = []
            for index in range(0, len(equasion)):                                   #checking every entry in the equasionlist
                if missionCompleted == True:                                        # the program should not keep sereaching in the equasion whis in this mission already one bracket pair was solved
                    continue
                else:                                                               # when the mission is still searching for one bracket pair
                    if equasion[index] == "(":                                      # when it's a left bracket...
                        leftBracket = index                                         # ...the index will be saved
                    elif equasion[index] == ")":                                    # if it's a right bracket it will solve the part in between the last left bracket and the current one
                        rightBracket = index                                        # the index will be saved
                        for n in range(leftBracket+1,index):                        # every entry in between will be appendet to list, whick will be recursed tho the solveEquasion() funcion
                            subequasion.append(equasion[n])
                        subresult = solveEquasion(subequasion)                      # recusing the subequasion to the solveEquasion() funcion
                        equasion[rightBracket] = subresult[0]                       # replacing the result with the right bracket
                        for n in range(leftBracket+1, rightBracket+1):              # poping the left bracket and everything inbetween the two brackets
                            equasion.pop(leftBracket)
                        missionCompleted = True                                     # One bracket pair was solved so the next scanned indexed (above) will be skipped

    minus = 0                                                                       # declaring the variables vor each action char
    plus = 0                                                                        # with every found action char in the equasion the accordingly variable will get +1
    multiply = 0
    divide = 0
    percent = 0
    power = 0

    for n in range(0, len(equasion)):                                               # every entry in the equasionlistwill be checked
        if equasion[
            n] == "%":                                                              # from here if there is a matching char the accordingly variable will get +1
            percent = percent + 1
        if equasion[n] == "^":
            power = power + 1
        if equasion[n] == "*":
            multiply = multiply + 1
        if equasion[n] == "/":
            divide = divide + 1
        if equasion[n] == "+":
            plus = plus + 1
        if equasion[n] == "-":
            minus = minus + 1

    # % percent                                                                       >>> solve PERCENT % <<<
    if percent > 0:                                                                 # Every mission will solve one compute-sign
        for missions in range(0,percent):                                           # for every counted percent char
            missionCompleted = False                                                # declaring
            for index in range(0, len(equasion)):                                   # check every entry of the equasion
                if missionCompleted == True:                                        # skipping if the compute-sign was already found in the current mission
                    continue
                else:                                                               # when this mission still have to find one compute-sign
                    if equasion[index] == "%":                                      # executed when a percent char was found
                        subresult =  float(equasion[index-1]) * 0.01                # multiply the entry of the equasion before the percent
                        equasion[index]= str(subresult)                             # replace the percent char with the subresult
                        equasion.pop(index-1)                                       # remove the number entry which was in the calculation above
                        missionCompleted = True                                     # the compute-sign was solved so the next scanned indexed (above) will be skipped

    # >>> solve POWER ^ <<<                                                           >>> solve POWER ^ <<<
    if power > 0:                                                                   # Every mission will solve one compute-sign
        for missions in range(0,power):                                             # for every counted power char
            missionCompleted = False                                                # declaring
            for index in range(0, len(equasion)):                                   # check every entry of the equasion
                if missionCompleted == True:                                        # skipping if the compute-sign was already found in the current mission
                    continue
                else:                                                               # when this mission still have to find one compute-sign
                    if equasion[index] == "^":                                      # executed when a power char was found
                        subresult = float(equasion[index-1]) ** float(equasion[index+1])# potentiates the entry before and after the multiplication char
                        equasion[index]= str(subresult)                             # replace the power char with the subresult
                        equasion.pop(index-1)                                       # remove the number entry which was in the calculation above
                        equasion.pop(index)                                         # remove the number entry which was in the calculation above
                        missionCompleted = True                                     # the compute-sign was solved so the next scanned indexed (above) will be skipped

    # >>> solve MULTIPLICATION * <<<                                                  >>> solve MULTIPLICATION * <<<
    if multiply > 0:                                                                # Every mission will solve one compute-sign
        for missions in range(0,multiply):                                          # for every counted multiplication char
            missionCompleted = False                                                # declaring
            for index in range(0, len(equasion)):                                   # check every entry of the equasion
                if missionCompleted == True:                                        # skipping if the compute-sign was already found in the current mission
                    continue
                else:                                                               # when this mission still have to find one compute-sign
                    if equasion[index] == "*":                                      # executed when a multiplication char was found
                        subresult =  float(equasion[index-1]) * float(equasion[index+1])# multiplies the entry before and after the multiplication char
                        equasion[index]= str(subresult)                             # replace the multiplication char with the subresult
                        equasion.pop(index-1)                                       # remove the number entry which was in the calculation above
                        equasion.pop(index)                                         # remove the number entry which was in the calculation above
                        missionCompleted = True                                     # the compute-sign was solved so the next scanned indexed (above) will be skipped

    #  >>> solve DIVIDATION / <<<                                                     >>> solve DIVIDATION / <<<
    if divide > 0:                                                                  # Every mission will solve one compute-sign
        for missions in range(0,divide):                                            # for every counted dividation char
            missionCompleted = False                                                # declaring
            for index in range(0, len(equasion)):                                   # check every entry of the equasion
                if missionCompleted == True:                                        # skipping if the compute-sign was already found in the current mission
                    continue
                else:                                                               # when this mission still have to find one compute-sign
                    if equasion[index] == "/":                                      # executed when a dividation char was found
                        subresult =  float(equasion[index-1]) / float(equasion[index+1])# divides the entry before and after the dividation char
                        equasion[index]= str(subresult)                             # replace the dividation char with the subresult
                        equasion.pop(index-1)                                       # remove the number entry which was in the calculation above
                        equasion.pop(index)                                         # remove the number entry which was in the calculation above
                        missionCompleted = True                                     # the compute-sign was solved so the next scanned indexed (above) will be skipped

    # >>> solve PLUS + <<<                                                            >>> solve PLUS + <<<
    if plus > 0:                                                                    # Every mission will solve one compute-sign
        for missions in range(0,plus):                                              # for every counted plus
            missionCompleted = False                                                # declaring
            for index in range(0, len(equasion)):                                   # check every entry of the equasion
                if missionCompleted == True:                                        # skipping if the compute-sign was already found in the current mission
                    continue
                else:                                                               # when this mission still have to find one compute-sign
                    if equasion[index] == "+":                                      # executed when a plus char was found
                        subresult =  float(equasion[index-1]) + float(equasion[index+1])# adds the entry before and after the plus
                        equasion[index]= str(subresult)                             # replace the plus with the subresult
                        equasion.pop(index-1)                                       # remove the number entry which was in the calculation above
                        equasion.pop(index)                                         # remove the number entry which was in the calculation above
                        missionCompleted = True                                     # the compute-sign was solved so the next scanned indexed (above) will be skipped

    # >>> solve MINUS - <<<                                                           >>> solve MINUS - <<<
    if minus > 0:                                                                   # Every mission will solve one compute-sign
        for missions in range(0,minus):                                             # for every counted dividation char
            missionCompleted = False                                                # declaring
            for index in range(0, len(equasion)):                                   # check every entry of the equasion
                if missionCompleted == True:                                        # skipping if the compute-sign was already found in the current mission
                    continue
                else:                                                               # when this mission still have to find one compute-sign
                    if equasion[index] == "/":                                      # executed when a minus char was found
                        subresult =  float(equasion[index-1]) - float(equasion[index+1])# subsracts the entry before and after the dividation char
                        equasion[index]= str(subresult)                             # replace the dividation char with the subresult
                        equasion.pop(index-1)                                       # remove the number entry which was in the calculation above
                        equasion.pop(index)                                         # remove the number entry which was in the calculation above
                        missionCompleted = True                                     # the compute-sign was solved so the next scanned indexed (above) will be skipped

    return equasion

if __name__ == "__main__":
    showBanner()
    while True:

        try:
            print("")
            solve = solveEquasion(splitEquasion(str(input("enter equasion: "))))[0]
            print(" f() = " ,solve)
        except Exception as e:
            print("ERROR!: ", e)
