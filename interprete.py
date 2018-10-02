from type import getType


def interpreteEquasion(equasion_as_string):                                         # splits a equasion in a string into different parts
    string = equasion_as_string                                                     # code will look cleaner with shorter variables
    # equasion = equasion_as_list                                                     # code will look cleaner with shorter variables

    lasttype = ""                                                                   # the chartype (getType()) from the last checked char
    currenttype = ""                                                                # the crurrent checked chartype (getType())

    # >>> remove SPACE <<<
    indexcorrection = 0
    for i in range(0, len(string)):                                                 # for every char in the string except the first
        i = i + indexcorrection
        lasttype = currenttype                                                      # the currenttype from the last run of the for-loop will now become
        currenttype = getType(str(string[i]))                                       # getting a new currenttype from a char with the getType() function from the equasion string
        if currenttype == "space":
            string = string[:i] + string[i + 1:]
            indexcorrection = indexcorrection - 1

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
    maxIndex = len(string) - 1
    i = 0
    finished = False                                                                # these 3 lines are a ranged for loop
    while not finished:                                                             # , which can change its lenght
        if (i == maxIndex) or (i < maxIndex):                                       # while in work
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
                if (lastchar2 == "(") or (lasttype2 == "action") or (lasttype2 == "nothing"):  # detecting if the current index is an negative variable
                    for lenght in range(i + 1, len(string) - i + 1):                      # scanning all chars after the variable
                        if not variableInnterruption:
                            if getType(string[lenght]) == "variable":
                                variableLenght = variableLenght + 1                 # detecting the lenght of the variable
                            else:
                                variableInnterruption = True
                        else:
                            continue
                    try:                                                            # now the equasion string will parted in thre fragments
                        stringFragment1 = string[:i - 1] + "("
                    except Exception:
                        continue
                    try:
                        stringFragment2 = "$" + string[i:i + variableLenght]         # the negative minus char will be replaced by an $ sign
                    except Exception:
                        continue
                    try:
                        stringFragment3 = ")" + string[i + variableLenght:]
                    except Exception:
                        continue
                    string = stringFragment1 + stringFragment2 + stringFragment3    # now the equasion string get assembled by thee fragments
                    i = i + 1                                                       # part of the raged for(while) loop
                    maxIndex = len(string) - 1                                        # updating the lenght of the string for the ranged for(while) loop

            elif (currenttype == "number") and (lastchar == "-"):
                if (lastchar2 == "(") or (lasttype2 == "action") or (lasttype2 == "nothing"):  # detecting if the current index is an negative number
                    for lenght in range(i + 1, len(string) - i + 1):                      # scanning all chars after the number
                        if not numberInterruption:
                            if getType(string[lenght]) == "number":
                                numberLenght = numberLenght + 1                     # detecting the lenght of the variable
                            else:
                                numberInterruption = True
                        else:
                            continue
                    try:                                                            # now the equasion string will parted in thre fragments
                        stringFragment1 = string[:i - 1] + "("
                    except Exception:
                        continue
                    try:
                        stringFragment2 = "€" + string[i:i + numberLenght]           # the negative minus char will be replaced by an € sign
                    except Exception:
                        continue
                    try:
                        stringFragment3 = ")" + string[i + numberLenght:]
                    except Exception:
                        continue
                    string = stringFragment1 + stringFragment2 + stringFragment3    # now the equasion string get assembled by thee fragments
                    i = i + 1                                                       # part of the raged for(while) loop
                    maxIndex = len(string) - 1                                        # updating the lenght of the string for the ranged for(while) loop
            else:
                i = i + 1                                                           # part of the raged for(while) loop
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
            equasion[equasionindex] = str(equasion[equasionindex]) + str(string[i])  # ...add the current char to the last entry in the equasionlist
        else:                                                                       # when it's an other type of char is should...
            equasion.append(str(string[i]))                                         # ...create a new entry in the equasionlist with the current char
            equasionindex = equasionindex + 1                                       # there is anew entry, so the programm should easily remember the highest index of the equasionlist

    for i in range(0, len(equasion)):                                               # replacing € and $ with -
        if (equasion[i][0] == "$") or (equasion[i][0] == "€"):
            try:
                equasion[i] = "-" + equasion[i][1:]
            except Exception:
                continue

    for i in range(0, len(equasion)):                                               # replacing € and $ with -
        if (getType(str(equasion[i][-1])) == "action") and (len(equasion[i]) > 1):
            try:
                equasion[i] = equasion[i][-1]
            except Exception:
                continue

    equasion_as_list = equasion                                                     # converting back to a longer variablename to keep an order
    return equasion_as_list                                                         # the equasion interpreted to a list will get returned
