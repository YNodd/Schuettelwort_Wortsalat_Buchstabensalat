
from random import randint, sample


# minimum and maximum length for the guess word
minlength = 4
maxlength = 11  # the maximum length could be reduced to make the game easier

# build a list with the possible words, from a csv file
dict_file = "Wortsalat_woerterbuch.csv"
dict_list = []
with open(dict_file, "r") as readfile:
    for singlerow in readfile:
        # only take nouns (and names):
        if singlerow[0].isupper():
            # because the rows ends with comma and enter:
            if singlerow[-1] == "\n" and singlerow[-2] == ",":
                if len(singlerow[0:-2]) >= minlength and len(singlerow[0:-2]) <= maxlength:  #
                    dict_list.append(singlerow[0:-2])
            # for the last row in the file (without enter):
            elif singlerow[-1] == ",":
                if len(singlerow[0:-1]) >= minlength and len(singlerow[0:-1]) <= maxlength:
                    dict_list.append(singlerow[0:-1])


def startscramblegame():
    print("To display a scrambled word, type 'go' or 'g'.\nTo see the solution, type 'show' or 's'. And 'hint' or 'h' to ask if a certain combination of letter is part of the word.\nType 'exit' or 'e' to quit.")
    typedinput = "placeholder"
    trialstatus = False


    # let the program shuffle a random word. The original word can be asked in the game by typing "show"
    while typedinput != "exit" and typedinput != "e":

        if trialstatus == False:  # helper variable to ensure that this line doesn't run if the player exits from the trials with "s" or similar
            typedinput = input("Type your command or guess: ")

        trialstatus = False

        if typedinput.lower() == "go" or typedinput.lower() == "g":
            # select random word to be shuffled:
            indexnumber = randint(0, len(dict_list))
            randomword = dict_list[indexnumber]
            # scramble the random word:
            indexlist = sample(range(len(randomword)), len(randomword))
            scrambledword = ""
            for singlenr in indexlist:
                scrambledword += randomword[singlenr]
            print(randomword)  # uncomment to test/debug

        elif typedinput.lower() == "show" or typedinput.lower() == "s":
            try:
                randomword.upper()
            except:
                print("You have not yet requested a word to guess. Type 'g' or 'go'.\n")

        elif typedinput.lower() == "hint" or typedinput.lower() == "h":
            try:  # if the randomword variable already exists
                hint_req = input("Write here the part of the word you want to know if it is included: ")
                if hint_req.lower() in randomword.lower():
                    print("Yes, it is a part of the word.")
                else:
                    print("No, this isn't a part of the word.")
            except:
                print("You have not yet requested a word to guess. Type 'g' or 'go'.\n")

        elif typedinput.lower() != "exit" and typedinput.lower() != "e":
                #checking if the player guessed right:
                trialstatus = True  # helper variable to ensure that no new input is asked when the main loop restarts
                try:  # if the randomword variable already exists
                    randomword.upper()
                except:
                    print()
                    print("You have not yet requested a word to guess.\n")
                    startscramblegame()

                while typedinput.lower() != randomword.lower():
                    if typedinput.lower() not in ["s", "show", "g", "go", "h", "hint", "e", "exit"]:  # to make sure these commands can be typed (and not be treated as an attempt to guess the word)
                        typedinput = input("No, try it again: ")
                    elif typedinput.lower() in ["e", "exit"]:
                        exit()  # ends the program completely (instead of break which only stops the actual loop)
                    else:
                        break
                else:
                    print("Great! You guessed it right.")
                    ifcontinue = ""
                    while ifcontinue.lower() not in ["y", "n"]:  # to make sure the program continues as expected when the player types it wrong
                        ifcontinue = input("Do you want to continue to play? y/n ")
                        if ifcontinue.lower() == "n":
                            exit()
                        if ifcontinue.lower() == "y":
                            print()
                            startscramblegame()



startscramblegame()

