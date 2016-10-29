import random
class Rock_Paper_Scissors():
    def __init__(self,userChoice):
        self.userChoiceOriginal=userChoice
        self.userChoicelower=userChoice.lower()

    def Computing(self):
        List = ['rock', 'scissors', 'paper']
        computerCoice = (List[random.randint(0, 2)])
        if ((self.userChoicelower == 'rock' and computerCoice == 'scissors') or (
                        self.userChoicelower == 'scissors' and computerCoice == 'paper')
            or (self.userChoicelower == 'paper' and computerCoice == 'rock')):
            print " Your choice {} \n computer choice {}. You Won !!".format(self.userChoiceOriginal, computerCoice)

        elif ((self.userChoicelower == 'scissors' and computerCoice == 'scissors') or (
                        self.userChoicelower == 'paper' and computerCoice == 'paper')
              or (self.userChoicelower == 'rock' and computerCoice == 'rock')):
            print " Your choice {} \n computer choice {}. Game Draw !!".format(self.userChoiceOriginal,
                                                                               computerCoice)

        else:
            print " Your choice {} \n computer choice {}. You Lose !!".format(self.userChoiceOriginal,
                                                                              computerCoice)

def gameStart():
    print " Game Rule \n -------------\n Rock beats scissors \n Scissors beats paper \n Paper beats rock"
    c = 'Y'
    while (c == 'Y'):
        userChoice = raw_input("Please enter your input :- \n")
        obj=Rock_Paper_Scissors(userChoice)
        obj.Computing()

    c = raw_input("Do you wish to play again  Y/N \n ").upper()


gameStart()