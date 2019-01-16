oneTable = ["", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine"]

elevensTable = ["eleven", "twelve", "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "nineteen", "tweenty"]

tensTable = ["", "ten", "tweenty", "thirty", "fourty", "fifty", "sixty",
             "seventy", "eighty", "ninety"]

hundreds = " hundred "

thousandsAndUp = ["thousand", "millon", "billion"]


def getInput():
    num = input("Enter your number -> ")
    return num


def getLength(num_length):
    return len(num_length)


def findTheNumber():
    num = getInput()
    length = getLength(num)
    word = ""

    if length is 1:
        word += oneTable[int(num)]
        return word
    elif length is 2:
        listNum = list(num)
        if listNum[0] is '1' and listNum[1] is "0":
            word += tensTable[1]
            return word
        elif listNum[0] is '1':
            word += elevensTable[int(num)-10-1]
            return word
        elif int(listNum[0]) > 1:
            word += tensTable[int(listNum[0])] + " " + oneTable[int(listNum[1])]
            return word
    elif length > 2:
        listNum = list(num)
        if len(listNum) is 3:
            word += oneTable[int(listNum[0])] + hundreds + \
                tensTable[int(listNum[1])] + " " + oneTable[int(listNum[2])]
            return word


print(findTheNumber())
