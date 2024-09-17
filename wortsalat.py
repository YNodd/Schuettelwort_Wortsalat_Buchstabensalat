
from random import randint, sample

# minimum and maximum length for the guess word
minlength = 4
maxlength = 11  # the maximum length could be reduced to make the game easier

# build a list with the possible words, from a csv file
dict_file = "Wortsalat-Dictionnaire.csv"
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

def may_restart():
    ifcontinue = ""
    while ifcontinue.lower() not in ["y", "n"]:  # to make sure the program continues as expected when the player types it wrong
        ifcontinue = input("Do you want to continue to play? y/n ")
        if ifcontinue.lower() == "n":
            exit()
        if ifcontinue.lower() == "y":
            print()
            startscramblegame()

def startscramblegame():
    print("To display a scrambled word, type 'go' or 'g'.\nTo see the solution, type 'show' or 's'. And 'hint' or 'h' to ask if a certain combination of letter is part of the word.\nType 'exit' or 'e' to quit.")
    typedinput = "placeholder"
    trialstatus = False
    pressed_g = False  # helper variable to check if the player already requested a word to guess (with "g" or "go")

    # let the program shuffle a random word. The original word can be asked in the game by typing "show"
    while typedinput != "exit" and typedinput != "e":

        if trialstatus == False:  # helper variable to ensure that this line doesn't run if the player exits from the trials with "s" or similar
            typedinput = input("Type your command or guess: ")

        trialstatus = False  # to reset it to False if it was True previously because the game was started again

        if typedinput.lower() == "go" or typedinput.lower() == "g":
            if pressed_g == True:
                # to ensure that the player can't request a new word without having seen or guessed the old one (to make sure that he doesn't request a new one by chance and wants to know the old one, which than would be "vanished")
                print(f"The previous word was: {randomword}. The new scrambled word to guess is:")
            pressed_g = True
            # select random word to be shuffled:
            indexnumber = randint(0, len(dict_list))  # todo: simplify this with the random shuffle method??
            randomword = dict_list[indexnumber]
            # scramble the random word:
            indexlist = sample(range(len(randomword)), len(randomword))
            scrambledword = ""
            for singlenr in indexlist:
                scrambledword += randomword[singlenr]
            #print(randomword)  # uncomment to test/debug
            print(scrambledword.upper())

        elif typedinput.lower() == "show" or typedinput.lower() == "s":
            if pressed_g == True:  # if the randomword variable already exists
                print(f"The word to guess was: {randomword}\n")
                may_restart()
            else:
                print("You have not yet requested a word to guess. Type 'g' or 'go'.\n")

        elif typedinput.lower() == "hint" or typedinput.lower() == "h":
            if pressed_g == True:  # if the randomword variable already exists
                hint_req = input("Write here the part of the word you want to know if it is included: ")
                if hint_req.lower() in randomword.lower():
                    print("Yes, it is a part of the word.")
                else:
                    print("No, this isn't a part of the word.")
            else:
                print("You have not yet requested a word to guess. Type 'g' or 'go'.\n")

        elif typedinput.lower() != "exit" and typedinput.lower() != "e":  #checking if the player guessed right:
                trialstatus = True  # helper variable to ensure that no new input is asked when the main loop restarts
                if pressed_g == False:
                    print()
                    print("You have not yet requested a word to guess.\n")
                    startscramblegame()

                else:
                    while typedinput.lower() != randomword.lower():
                        if typedinput.lower() not in ["s", "show", "g", "go", "h", "hint", "e", "exit"]:  # to make sure these commands can be typed (and not be treated as an attempt to guess the word)
                            typedinput = input("No, try it again: ")
                        elif typedinput.lower() in ["e", "exit"]:
                            exit()  # ends the program completely (instead of break which only stops the actual loop)
                        else:
                            break  # restarts the trial loop / the player can guess again
                    else:
                        print("Great! You guessed it right.")
                        may_restart()


startscramblegame()

