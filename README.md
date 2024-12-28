A python script to quickly guess the secret code in the game Mastermind. Usually gets the right answer in 4-6 guesses

The script works by generating a list of all possible colour combinations, and slowly eliminating them based on previous guesses. Each guess left will give more information, thus the function to determine the next guess tries to find the guess most similar to the other remaining possibilities, in order to differentiate between them. 
