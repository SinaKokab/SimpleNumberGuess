import random

SecretNumber = random.randint(1, 100)
StartUp = True
PreviousNumberGuessed = None
GuessResult = False
PlayerConfirmation = False

def CheckNumber(NumberGuessed):

    NumberGuessed = float(NumberGuessed)
    if NumberGuessed > SecretNumber:
        if (StartUp == False):
            print('Your guess was too high!')
            if ((PreviousNumberGuessed > NumberGuessed) and (PreviousNumberGuessed < SecretNumber)):
                print('Closer though!')
            else:
                print('Colder!')
        else:
            print('Your guess was too high!')
    elif NumberGuessed < SecretNumber:
        if StartUp == False:
            print('Your guess was too low!')
            if ((PreviousNumberGuessed < NumberGuessed) and (PreviousNumberGuessed > SecretNumber)):
                print('Closer though!')
            else:
                print('Colder!')
        else:
            print('Your guess was too low!')

    if (NumberGuessed == SecretNumber):
        global GuessResult
        GuessResult = True
        print('Correct! You guessed the right number!')
        #global StartUp
        #Startup = True


def makesureitsanumber():
     #NumberCheck = False
     #while NumberCheck != True:
     global NumberGuessedString
     NumberGuessedString = ''
     print("Guess a number between 1 and a 100")
     NumberGuessedString = (raw_input(""))
     #NumberCheck = True
         #except ValueError:
             #print('Enter a NUMBER between 1 and a 100')
             #NumberCheck = False

     try:
         NumberGuessedString = int(NumberGuessedString)
     except:
         makesureitsanumber()
         return None
     #print(NumberCheck)
     print(NumberGuessedString)
     #return(NumberGuessedString)

def GameLoopAndConfirmation():
    #print('GameLooped')
    global GuessResult
    global PlayerConfirmation
    PlayerDecision = ''
    while (GuessResult == False):
        makesureitsanumber()
        CheckNumber(NumberGuessedString)
    print('Do you want to play again? Yes/No')
    PlayerDecision = raw_input()
    try:
        if (str.lower(PlayerDecision) == ('yes')):
            #print('choice 1')
            PlayerConfirmation = True
            GuessResult = False
            global SecretNumber
            SecretNumber = random.randint(1, 100)
            if (SecretNumber == PreviousNumberGuessed):
                SecretNumber = random.randint(1, 100)
            GameLoopAndConfirmation()
            return None
        elif (str.lower(PlayerDecision) == ('no')):
            #print('choice 2')
            return None
        else:
            #print('choice 3')
            GameLoopAndConfirmation()
            return None
    except:
        #print('whyisthishappening')
        GameLoopAndConfirmation()
        return None





GameLoopAndConfirmation()

#while (GuessResult == False):
    #print(StartUp)
    #if (StartUp == False)# and (PlayerConfirmation == True):
        #PreviousNumberGuessed = float(NumberGuessedString)
    #print("Guess a number between 1 and a 100")
    #try:
        #NumberGuessedString = (raw_input(""))
    #except ValueError:
        #print('Enter a NUMBER between 1 and a 100')
    #NumberGuessedString = makesureitsanumber()
        #makesureitsanumber()
        #CheckNumber(NumberGuessedString)
    #print(SecretNumber)
    #StartUp = False
    #StartUp = False
    #makesureitsanumber()
    #CheckNumber(NumberGuessedString)
