This program solves Wordle puzzles with 0 inputs from the user.

I grabbed all of the words used in scrabble, and through prune.py, I removed all elements that were not five letters long, and set them into lowercase. That information was saved in new_five_letter_words.txt. Then, upon starting the solve.py file, the program uses a base input 'heart' and based on the color of the letters in the word, adds the word to mutable_words.txt. The program then pulls the first word from this file and uses it as the next guess. This elemination continues until either the word is guessed or the program fails. 

It has a success rate of about 95% at the moment, which, while not great, still solves the program most of the time. There are a few edge case bugs that need to be fixed, but it is at a place where I am happy with it.

Feel free to steal this code, and fix it, or rework it to your heart's content!
And below is a few examples of it in action!

![Wordle Solver Example](WordleSolverEx.gif)
