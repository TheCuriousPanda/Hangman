import random
file=open("C:/Users/Trey Yu/Python Tests/words.txt", 'r')
s=file.read()
file.close()
letters=[]
words=s.split(" ")
rand_word = words[random.randrange(len(words))]
numberofattempts=0
attempts=10
print("\nWelcome to the game, Hangman!")
print("\nI am thinking of a {} letter word".format(len(rand_word)))
print("\nYour options are \nabcdefghijklmnopqrstuvwxyz")

def blankword(l,s):
    output=""
    for c in s:
        if c in l:
            output = output+c
        else:
            output = output+"_"
    return output
def userguess():
    global numberofattempts
    global a
    if c in rand_word:
        print("Good Guess!")
        letters.append(c)
        return blankword(letters,rand_word)
    else:
        numberofattempts = numberofattempts+1
        a=attempts-numberofattempts
        print("Sorry, that letter is not in the word\nYou have {} guesses left.".format(a))
        letters.append(c)
        print(blankword(letters,rand_word))
        return blankword(letters,rand_word)
        return a
while(True):
    c=input("\nPlease enter a letter... \n")
    if c in rand_word:
        print(userguess())
    if c == rand_word:
        print("Congratulations! You guessed the word!")
        break
    if userguess() == rand_word:
        print("Congratulations! You have figured out the word!")
        break
    if a == 0:
        print("Sorry, you have run out of guesses.")
        print("\nThe word was {}.".format(rand_word))
        break
