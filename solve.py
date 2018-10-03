from type import getType
import re


def replaceVars(equasion_as_list, variables={}):
    equasion = equasion_as_list.copy()
    # >>> replace vars <<<
    for n in range(len(equasion)):
        if equasion[n] in variables:
            equasion[n] = variables[equasion[n]]
    return equasion


def solveEquasion(equasion_as_list):                                       # solving an equasion (recursive, because of brackets)
    equasion = equasion_as_list.copy()                                   # code will look cleaner with shorter variables
    # >>> solve brackets <<<
    bracket = 0
    for n in range(len(equasion)):                                                      # every entry in the equasionlist will be checked for brackets
        if equasion[n] == "(":
            bracket = bracket + 1
        if equasion[n] == ")":
            bracket = bracket + 1
    if bracket > 0:                                                                 # if there are brackets
        for missions in range(bracket // 2):                                        # In every mission one bracket pair will be solved
            missionCompleted = False
            leftBracket = 0
            rightBracket = 0
            subequasion = []
            for index in range(len(equasion)):                                      # checking every entry in the equasionlist
                if missionCompleted:                                                # the program should not keep sereaching in the equasion whis in this mission already one bracket pair was solved
                    continue
                else:                                                               # when the mission is still searching for one bracket pair
                    if equasion[index] == "(":                                      # when it's a left bracket...
                        leftBracket = index                                         # ...the index will be saved
                    elif equasion[index] == ")":                                    # if it's a right bracket it will solve the part in between the last left bracket and the current one
                        rightBracket = index                                        # the index will be saved
                        if leftBracket + 1 == rightBracket - 1:
                            subequasion.append(equasion[leftBracket + 1])
                        else:
                            for n in range(leftBracket + 1, rightBracket):          # every entry in between will be appendet to list, which will be recursed tho the solveEquasion() funcion
                                subequasion.append(equasion[n])
                        subresult = solveEquasion(subequasion)           # recusing the subequasion to the solveEquasion() funcion
                        equasion[rightBracket] = (subresult)[0]                     # replacing the result with the right bracket
                        for n in range(leftBracket + 1, rightBracket + 1):          # poping the left bracket and everything inbetween the two brackets
                            equasion.pop(leftBracket)
                        missionCompleted = True                                     # One bracket pair was solved so the next scanned indexed (above) will be skipped

    # >>> analyse the equasion <<<
    minus = 0                                                                       # declaring the variables vor each action char
    plus = 0                                                                        # with every found action char in the equasion the accordingly variable will get +1
    multiply = 0
    divide = 0
    percent = 0
    power = 0
    for n in range(len(equasion)):                                                  # every entry in the equasionlistwill be checked
        if equasion[n] == "%":                                                      # from here if there is a matching char the accordingly variable will get +1
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
        for missions in range(percent):                                             # for every counted percent char
            missionCompleted = False                                                # declaring
            for index in range(len(equasion)):                                      # check every entry of the equasion
                if missionCompleted:                                                # skipping if the compute-sign was already found in the current mission
                    continue
                else:                                                               # when this mission still have to find one compute-sign
                    if equasion[index] == "%":                                      # executed when a percent char was found
                        subresult = float(equasion[index - 1]) * 0.01               # multiply the entry of the equasion before the percent
                        equasion[index] = str(subresult)                            # replace the percent char with the subresult
                        equasion.pop(index - 1)                                     # remove the number entry which was in the calculation above
                        missionCompleted = True                                     # the compute-sign was solved so the next scanned indexed (above) will be skipped

    # >>> solve POWER ^ <<<                                                           >>> solve POWER ^ <<<
    if power > 0:                                                                   # Every mission will solve one compute-sign
        for missions in range(power):                                               # for every counted power char
            missionCompleted = False                                                # declaring
            for index in range(len(equasion)):                                      # check every entry of the equasion
                if missionCompleted:                                                # skipping if the compute-sign was already found in the current mission
                    continue
                else:                                                               # when this mission still have to find one compute-sign
                    if equasion[index] == "^":                                      # executed when a power char was found
                        subresult = float(equasion[index - 1]) ** float(equasion[index + 1])  # potentiates the entry before and after the multiplication char
                        equasion[index] = str(subresult)                            # replace the power char with the subresult
                        equasion.pop(index - 1)                                     # remove the number entry which was in the calculation above
                        equasion.pop(index)                                         # remove the number entry which was in the calculation above
                        missionCompleted = True                                     # the compute-sign was solved so the next scanned indexed (above) will be skipped

    # >>> solve MULTIPLICATION * <<<                                                  >>> solve MULTIPLICATION * <<<
    if multiply > 0:                                                                # Every mission will solve one compute-sign
        for missions in range(multiply):                                            # for every counted multiplication char
            missionCompleted = False                                                # declaring
            for index in range(len(equasion)):                                      # check every entry of the equasion
                if missionCompleted:                                                # skipping if the compute-sign was already found in the current mission
                    continue
                else:                                                               # when this mission still have to find one compute-sign
                    if equasion[index] == "*":                                      # executed when a multiplication char was found
                        subresult = float(equasion[index - 1]) * float(equasion[index + 1])  # multiplies the entry before and after the multiplication char
                        equasion[index] = str(subresult)                            # replace the multiplication char with the subresult
                        equasion.pop(index - 1)                                     # remove the number entry which was in the calculation above
                        equasion.pop(index)                                         # remove the number entry which was in the calculation above
                        missionCompleted = True                                     # the compute-sign was solved so the next scanned indexed (above) will be skipped

    #  >>> solve DIVIDATION / <<<                                                     >>> solve DIVIDATION / <<<
    if divide > 0:                                                                  # Every mission will solve one compute-sign
        for missions in range(divide):                                              # for every counted dividation char
            missionCompleted = False                                                # declaring
            for index in range(len(equasion)):                                      # check every entry of the equasion
                if missionCompleted:                                                # skipping if the compute-sign was already found in the current mission
                    continue
                else:                                                               # when this mission still have to find one compute-sign
                    if equasion[index] == "/":                                      # executed when a dividation char was found
                        subresult = float(equasion[index - 1]) / float(equasion[index + 1])  # divides the entry before and after the dividation char
                        equasion[index] = str(subresult)                            # replace the dividation char with the subresult
                        equasion.pop(index - 1)                                     # remove the number entry which was in the calculation above
                        equasion.pop(index)                                         # remove the number entry which was in the calculation above
                        missionCompleted = True                                     # the compute-sign was solved so the next scanned indexed (above) will be skipped

    # >>> solve PLUS + <<<                                                            >>> solve PLUS + <<<
    if plus > 0:                                                                    # Every mission will solve one compute-sign
        for missions in range(plus):                                                # for every counted plus
            missionCompleted = False                                                # declaring
            for index in range(len(equasion)):                                      # check every entry of the equasion
                if missionCompleted:                                                # skipping if the compute-sign was already found in the current mission
                    continue
                else:                                                               # when this mission still have to find one compute-sign
                    if equasion[index] == "+":                                      # executed when a plus char was found
                        subresult = float(equasion[index - 1]) + float(equasion[index + 1])  # adds the entry before and after the plus
                        equasion[index] = str(subresult)                            # replace the plus with the subresult
                        equasion.pop(index - 1)                                     # remove the number entry which was in the calculation above
                        equasion.pop(index)                                         # remove the number entry which was in the calculation above
                        missionCompleted = True                                     # the compute-sign was solved so the next scanned indexed (above) will be skipped

    # >>> solve MINUS - <<<                                                           >>> solve MINUS - <<<
    if minus > 0:                                                                   # Every mission will solve one compute-sign
        for missions in range(minus):                                               # for every counted dividation char
            missionCompleted = False                                                # declaring
            for index in range(len(equasion)):                                      # check every entry of the equasion
                if missionCompleted:                                                # skipping if the compute-sign was already found in the current mission
                    continue
                else:                                                               # when this mission still have to find one compute-sign
                    if equasion[index] == "-":                                      # executed when a minus char was found
                        subresult = float(equasion[index - 1]) - float(equasion[index + 1])  # subsracts the entry before and after the dividation char
                        equasion[index] = str(subresult)                            # replace the dividation char with the subresult
                        equasion.pop(index - 1)                                     # remove the number entry which was in the calculation above
                        equasion.pop(index)                                         # remove the number entry which was in the calculation above
                        missionCompleted = True                                     # the compute-sign was solved so the next scanned indexed (above) will be skipped
    return equasion
