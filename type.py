def getType(char):                                                                  # returns the type of a char
    char = str(char)                                                                # only strings will get a match

    # numbers
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
    # actions
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

    # brackets
    elif char == "(":
        return "bracket"
    elif char == ")":
        return "bracket"

    # variables
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
