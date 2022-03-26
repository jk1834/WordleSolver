
from turtle import Screen
import pyautogui as pau
import time
import sys
import string


alph = list(string.ascii_lowercase)

wins = 0
losses = 0

aLoc = (671, 747)
bLoc = (1002, 802)
cLoc = (887, 801)
dLoc = (805, 748)
eLoc = (793, 691)
fLoc = (872, 747)
gLoc = (939, 748)
hLoc = (1005, 748)
iLoc = (1092, 692)
jLoc = (1073, 748)
kLoc = (1139, 748)
lLoc = (1204, 747)
mLoc = (1115, 804)
nLoc = (1057, 804)
oLoc = (1153, 693)
pLoc = (1211, 692)
qLoc = (671, 691)
rLoc = (854, 693)
sLoc = (738, 747)
tLoc = (912, 692)
uLoc = (1033, 693)
vLoc = (944, 804)
wLoc = (732, 692)
xLoc = (829, 804)
yLoc = (973, 694)
zLoc = (773, 804)


letterLoc = [aLoc, bLoc, cLoc, dLoc, eLoc, fLoc, gLoc, hLoc, iLoc, jLoc, kLoc, lLoc, mLoc, nLoc, oLoc, pLoc, qLoc, rLoc, sLoc, tLoc, uLoc, vLoc, wLoc, xLoc, yLoc, yLoc, zLoc]



def confirmProgram():

    # Confrims program window
    while 1:

        print("\n======================================================")
        print("Hello and welcome to Wordle Solver!")
        ans = input("When you are ready to start the program, type 'start' and click on your Wordle Browser.\nTo quit, type 'exit'.\nYou will have 4 seconds before the program automatically starts.\n======================================================\n\n")
        

        if ans == 'start':
            
            time.sleep(4)
            break

        if ans == 'exit':
            sys.exit()
        
        print("\nPlease enter a valid command.\n")


def getKey(cha):

    ## For some reason this code below does not work
    ## For now, this ugly 26 if statements will have to do
    if cha != '\n':
        for c in range(len(alph)):
            if alph.index(cha) == c:
                return letterLoc[c]
        

# Checks the keys entered against their respective positions on screen, and alters the
# list of available words based on the colors of the keys
def checkKeys(inputWord, fileName):

    words = []

    f = open(fileName, 'r')
    words = f.readlines()
    print('Words here!')
    print(words)
    f.close()
     
    nf = open('mutable_words.txt', 'w')

    for c in range(len(inputWord)):
        
        # Green
        if pau.pixelMatchesColor(getKey(inputWord[c])[0], getKey(inputWord[c])[1], (87, 172, 87), tolerance = 0.8):
            print(inputWord[c] + ' is Green!')

            for txtWord in list(words):
                # If the letters are not the same at that index, remove the word from the list
                if inputWord[c] != txtWord[c]:
                    words.remove(txtWord)
             
        # Gray
        if pau.pixelMatchesColor(getKey(inputWord[c])[0], getKey(inputWord[c])[1], (162, 162, 162), tolerance = 0.8):
            print(inputWord[c] + ' is Gray!')

            for txtWord in list(words):
                if inputWord[c] in txtWord:
                    words.remove(txtWord)
                    
        # Yellow or Orange
        if pau.pixelMatchesColor(getKey(inputWord[c])[0], getKey(inputWord[c])[1], (233, 198, 1), tolerance = 0.8) or pau.pixelMatchesColor(getKey(inputWord[c])[0], getKey(inputWord[c])[1], (233, 190, 1), tolerance = 0.8):
            print(inputWord[c] + ' is Yellow!')

            for txtWord in list(words):
                    
                if (inputWord[c] not in txtWord) or (inputWord[c] == txtWord[c]):
                    words.remove(txtWord)
            
        
    nf.writelines(words)
    nf.close()
    
    # Checks if won or loss, then continue solving
    checkState()
    
    pressKeys(words[0])
    print(words[0])
    checkKeys(words[0].strip('\n'), 'mutable_words.txt')



def checkState():
        
    time.sleep(1)
    # Checks if the location on screen is green or red. If not, continues with guessing. If so, restart the program and return win or loss accordingly
    if pau.pixelMatchesColor(1053, 683, (209, 231, 221), tolerance = 0.8):
        # f = open('wins_and_losses.txt', 'a')
        
        pau.press('enter')
        #wins += 1
        #print('Wins: '+ wins + '\nLosses: ' + losses)
        startSolve()


    if pau.pixelMatchesColor(1053, 683, (248, 215, 218), tolerance = 0.8):
        
        
        pau.press('enter')
        #losses +=1
        #print('Wins: '+ wins + '\nLosses: ' + losses)
        startSolve()
    

# Iterates through characters in a word then types them to screen, pressing enter at the end
def pressKeys(word):

    for ch in word:
        pau.press(ch)
    


# Types first word, which is always 'Heart'
def startSolve():
    
    pressKeys('heart')
    pau.press('enter')
    checkKeys('heart', 'new_five_letter_words.txt')
    
    

if __name__ == "__main__":

    confirmProgram()
    startSolve()
