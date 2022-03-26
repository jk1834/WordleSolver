
lines = []

with open('scrabble_words.txt') as f:
    lines = f.readlines()

    newF = open('new_five_letter_words.txt','w')
    for line in lines:

        if len(line) == 6:
            newF.write(line.lower())
    newF.close()
