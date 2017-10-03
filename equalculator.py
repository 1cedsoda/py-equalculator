#first edit: 2017-09-11
#last edit: 2017-10-03
#last edit from: github.com/phyyyl

def showBanner():                                                                   # Cool Banner will be printed. Created with network-science.de/ascii/
        print("                               ______            ______      _____")
        print("     ___________ ____  _______ ___  /_________  ____  /_____ __  /____ _________")
        print("     _  _ \  __ `/  / / /  __ `/_  /_  ___/  / / /_  /_  __ `/  __/  __ \_  ___/")
        print("     /  __/ /_/ // /_/ // /_/ /_  / / /__ / /_/ /_  / / /_/ // /_ / /_/ /  /")
        print("     \___/\__, / \__,_/ \__,_/ /_/  \___/ \__,_/ /_/  \__,_/ \__/ \____//_/")
        print("            /_/")
        print("                   github.com/phyyyl/py-equalculator    v1.2 ")

def inputPrompt():                                                                  # when executed the user is able to type in an equasion
    equasion = input("Enter Equasion")
    return equasion                                                                 # returns the input without manipulation

def interpreteEquasion(equasion_as_string):                                         # splits a equasion in a string into different parts
    string = equasion_as_string                                                     # code will look cleaner with shorter variables
   #equasion = equasion_as_list                                                     # code will look cleaner with shorter variables

    lasttype = ""                                                                   # the chartype (getType()) from the last checked char
    currenttype = ""                                                                # the crurrent checked chartype (getType())

    # >>> remove SPACE <<<
    indexcorrection = 0
    for i in range(0, len(string)):                                                 # for every char in the string except the first
        i = i + indexcorrection
        lasttype = currenttype                                                      # the currenttype from the last run of the for-loop will now become
        currenttype = getType(str(string[i]))                                       # getting a new currenttype from a char with the getType() function from the equasion string
        if currenttype == "space":
            string = string[:i] + string[i+1:]
            indexcorrection = indexcorrection -1

    # >>> 2x -> 2*x <<<
    currenttype = getType(str(string[0]))                                           # the first char haven't to compared with the one before, because there is no one before :D
    indexcorrection = 0
    for i in range(1, len(string)):                                                 # for every char in the string except the first
        i = i + indexcorrection
        lasttype = currenttype                                                      # the currenttype from the last run of the for-loop will now become
        currenttype = getType(str(string[i]))                                       # getting a new currenttype from a char with the getType() function from the equasion string
        if (currenttype == "variable") and (lasttype == "number"):
            string = str(string[:i]) + "*" + str(string[i:])
            indexcorrection = indexcorrection + 1

    # >>> negative number marking -1 -> €1   -x -> $x <<<
    lasttype2 = "nothing"
    lasttype = "nothing"
    currenttype = "nothing"
    currentchar = ""
    lastchar = ""
    lastchar2 = ""
    maxIndex = len(string)-1
    i = 0
    finished = False                                                                # these 3 lines are a ranged for loop
    while not finished:                                                             # , which can change its lenght
        if (i == maxIndex) or (i < maxIndex):                                       #while in work
            lasttype2 = lasttype
            lasttype = currenttype
            currenttype = getType(string[i])
            lastchar2 = lastchar
            lastchar = currentchar
            currentchar = string[i]
            variableInnterruption = False
            numberInterruption = False
            numberLenght = 1
            variableLenght = 1
            stringFragment1 = "("
            stringFragment2 = ""
            stringFragment3 = ")"

            if (currenttype == "variable") and (lastchar == "-"):
                if (lastchar2 == "(") or (lasttype2 == "action") or (lasttype2 == "nothing"): #detecting if the current index is an negative variable
                    for lenght in range(i+1, len(string)-i+1):                      #scanning all chars after the variable
                        if not variableInnterruption:
                            if getType(string[lenght]) == "variable":
                                variableLenght = variableLenght + 1                 #detecting the lenght of the variable
                            else:
                                variableInnterruption = True
                        else:
                            continue
                    try:                                                            #now the equasion string will parted in thre fragments
                        stringFragment1 = string[:i-1] + "("
                    except Exception as e:
                        continue
                    try:
                        stringFragment2 =  "$" + string[i:i+variableLenght]         #the negative minus char will be replaced by an $ sign
                    except Exception as e:
                        continue
                    try:
                        stringFragment3 = ")" + string[i+variableLenght:]
                    except Exception as e:
                        continue
                    string = stringFragment1 + stringFragment2 + stringFragment3    #now the equasion string get assembled by thee fragments
                    i = i + 1                                                       #part of the raged for(while) loop
                    maxIndex = len(string)-1                                        #updating the lenght of the string for the ranged for(while) loop

            elif (currenttype == "number") and (lastchar == "-"):
                if (lastchar2 == "(") or (lasttype2 == "action") or (lasttype2 == "nothing"): #detecting if the current index is an negative number
                    for lenght in range(i+1, len(string)-i+1):                      #scanning all chars after the number
                        if not numberInterruption:
                            if getType(string[lenght]) == "number":
                                numberLenght = numberLenght + 1                     #detecting the lenght of the variable
                            else:
                                numberInterruption = True
                        else:
                            continue
                    try:                                                            #now the equasion string will parted in thre fragments
                        stringFragment1 = string[:i-1] + "("
                    except Exception as e:
                        continue
                    try:
                        stringFragment2 =  "€" + string[i:i+numberLenght]           #the negative minus char will be replaced by an € sign
                    except Exception as e:
                        continue
                    try:
                        stringFragment3 = ")" + string[i+numberLenght:]
                    except Exception as e:
                        continue
                    string = stringFragment1 + stringFragment2 + stringFragment3    #now the equasion string get assembled by thee fragments
                    i = i + 1                                                       #part of the raged for(while) loop
                    maxIndex = len(string)-1                                        #updating the lenght of the string for the ranged for(while) loop
            else:
                i = i + 1                                                           #part of the raged for(while) loop
        else:
            finished = True

    # >>> interprete to list <<<
    equasionindex = 0                                                               # the index of the last added entry to the equasion list
    equasion = []                                                                   # declaring the equasion list
    currenttype = string[0]                                                         # the first char haven't to compared with the one before, because there is no one before :D
    equasion.append(str(string[0]))                                                 # ...and will be direcly a new entry in the equasionlist
    for i in range(1, len(string)):                                                 # for every char in the string except the first
        lasttype = currenttype                                                      # the currenttype from the last run of the for-loop will now become
        currenttype = getType(str(string[i]))                                       # getting a new currenttype from a char with the getType() function from the equasion string
        if getType(string[i]) == "bracket":
            equasion.append(str(string[i]))                                         # ...create a new entry in the equasionlist with the current char
            equasionindex = equasionindex + 1                                       # there is anew entry, so the programm should easily remember the highest index of the equasionlist
        elif getType(equasion[equasionindex][-1]) == getType(string[i]):            # when the current and last chartype is equal to each other...
            equasion[equasionindex] = str(equasion[equasionindex]) + str(string[i]) # ...add the current char to the last entry in the equasionlist
        else:                                                                       # when it's an other type of char is should...
            equasion.append(str(string[i]))                                         # ...create a new entry in the equasionlist with the current char
            equasionindex = equasionindex + 1                                       # there is anew entry, so the programm should easily remember the highest index of the equasionlist

    for i in range(0, len(equasion)):                                               #replacing € and $ with -
        if (equasion[i][0] == "$") or (equasion[i][0] == "€"):
            try:
                equasion[i] = "-" + equasion[i][1:]
            except Exception as e:
                continue

    for i in range(0, len(equasion)):                                               #replacing € and $ with -
        if (getType(str(equasion[i][-1])) == "action") and (len(equasion[i]) > 1):
            try:
                equasion[i] = equasion[i][-1]
            except Exception as e:
                continue

    equasion_as_list = equasion                                                     # converting back to a longer variablename to keep an order
    return equasion_as_list                                                         # the equasion interpreted to a list will get returned

def getType(char):                                                                  # returns the type of a char
    char = str(char)                                                                # only strings will get a match

    #numbers
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
    elif char == "~":
        return "number"
    elif char == "€":
        return "number"
    #actions
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

    #brackets
    elif char == "(":
        return "bracket"
    elif char == ")":
        return "bracket"

    #variables
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
    elif char == "$":
        return "variable"

    elif char == " ":
        return "space"
    elif char == "_":
        return "space"

    elif char == "":
        return "nothing"

    else:
        print("The char \"", char, "\" is not valid")

def solveEquasion(equasion_as_list):                                                # solving an equasion (recursive, because of brackets)
    equasion = equasion_as_list                                                     # code will look cleaner with shorter variables

    # >>> replace variables <<<
    lasttype = ""                                                                   # the chartype (getType()) from the last checked char
    currenttype = ""                                                                # the crurrent checked chartype (getType())
    for equasionIndex in range(0, len(equasion)):                                   # for every entry in the equasion
        foundVariable = False
        negativeCorrection = 0
        lasttype = currenttype                                                      # the currenttype from the last run of the for-loop will now become
        if equasion[equasionIndex][0][0] == "-":
            negativeCorrection = 1
        currenttype = getType(str(equasion[equasionIndex])[0][negativeCorrection:])              # getting a new currenttype from a char with the getType() function from the equasion string
        if currenttype == "variable":                                               # found variable
            for variablesIndex  in range(0, len(variables)):                        # searcj for definition in the variable slist
                if foundVariable:
                    continue
                else:
                    if variables[variablesIndex][0][negativeCorrection:] == equasion[equasionIndex]:
                        equasion[equasionIndex] = variables[variablesIndex][1]
                        foundVariable = True
            if not foundVariable:                                              # if there is no definition
                print("Variable ", equasion[equasionIndex], " is not defined. It will be handled as 1.")
                equasion[equasionIndex] = 1

    # >>> solve brackets <<<
    bracket = 0
    for n in range(0, len(equasion)):                                               # every entry in the equasionlist will be checked for brackets
        if equasion[n] == "(":
            bracket = bracket + 1
        if equasion[n] == ")":
            bracket = bracket + 1
    if bracket > 0:                                                                 # if there are brackets
        for missions in range(0,bracket//2):                                        # In every mission one bracket pair will be solved
            missionCompleted = False
            leftBracket = 0
            rightBracket = 0
            subequasion = []
            for index in range(0, len(equasion)):                                   # checking every entry in the equasionlist
                if missionCompleted:                                                # the program should not keep sereaching in the equasion whis in this mission already one bracket pair was solved
                    continue
                else:                                                               # when the mission is still searching for one bracket pair
                    if equasion[index] == "(":                                      # when it's a left bracket...
                        leftBracket = index                                         # ...the index will be saved
                    elif equasion[index] == ")":                                    # if it's a right bracket it will solve the part in between the last left bracket and the current one
                        rightBracket = index                                        # the index will be saved
                        if leftBracket + 1 == rightBracket - 1:
                            subequasion.append(equasion[leftBracket+1])
                        else:
                            for n in range(leftBracket + 1, rightBracket):          # every entry in between will be appendet to list, which will be recursed tho the solveEquasion() funcion
                                subequasion.append(equasion[n])
                        subresult = solveEquasion(subequasion)                      # recusing the subequasion to the solveEquasion() funcion
                        equasion[rightBracket] = (subresult)[0]                     # replacing the result with the right bracket
                        for n in range(leftBracket+1, rightBracket+1):              # poping the left bracket and everything inbetween the two brackets
                            equasion.pop(leftBracket)
                        missionCompleted = True                                     # One bracket pair was solved so the next scanned indexed (above) will be skipped

    # >>> analyse the equasion <<<
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

    # >>> solver percent % <<<                                                        >>> solve PERCENT % <<<
    if percent > 0:                                                                 # Every mission will solve one compute-sign
        for missions in range(0,percent):                                           # for every counted percent char
            missionCompleted = False                                                # declaring
            for index in range(0, len(equasion)):                                   # check every entry of the equasion
                if missionCompleted:                                                # skipping if the compute-sign was already found in the current mission
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
                if missionCompleted:                                                # skipping if the compute-sign was already found in the current mission
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
                if missionCompleted:                                                # skipping if the compute-sign was already found in the current mission
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
                if missionCompleted:                                                # skipping if the compute-sign was already found in the current mission
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
                if missionCompleted:                                                # skipping if the compute-sign was already found in the current mission
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
                if missionCompleted:                                                # skipping if the compute-sign was already found in the current mission
                    continue
                else:                                                               # when this mission still have to find one compute-sign
                    if equasion[index] == "-":                                      # executed when a minus char was found
                        subresult =  float(equasion[index-1]) - float(equasion[index+1])# subsracts the entry before and after the dividation char
                        equasion[index]= str(subresult)                             # replace the dividation char with the subresult
                        equasion.pop(index-1)                                       # remove the number entry which was in the calculation above
                        equasion.pop(index)                                         # remove the number entry which was in the calculation above
                        missionCompleted = True                                     # the compute-sign was solved so the next scanned indexed (above) will be skipped
    return equasion

def compactSolve(equasion_as_string):                                               #combines all steft to solve an equasion in just one gunction
    equasion_as_list = interpreteEquasion(equasion_as_string)
    result = solveEquasion(equasion_as_list)
    result = float(result[0])
    if str(result)[-2] + str(result)[-1] == ".0":
        result = int(result)
    return result

global variables                                                                    # global variable to save all custom ariable definitions
variables = []
def setVariable(variable, value):
    for index in range(0, len(variables)):                                          # pop all other definition for this variable
        if variables[index] == variable:
            variables.pop(index)
    variables.append([variable, value])                                             # write the difinition into the list


if __name__ == "__main__":
    showBanner()
    while True:
        print("")
        print("f() = ", compactSolve(str(input("Enter an equasion: "))))
