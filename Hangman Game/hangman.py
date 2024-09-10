# Hangman Game in Python
# The word to be guessed
word = "Nepal".lower()


# The number of lives
lives = 5

#The guessed letters
guessed = ["_"] * len(word)

# The Game loop
while lives > 0:
    # Print the current state of the word
    print(" ".join(guessed))
    print(f"Lives: {lives}")

    #Ask the user for a letter
    letter = input("Guess a letter: ")

    #Check if the letter is in the word
    if letter in word:
        #Reveal the correct letter
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        #Decrease the number of lives
        lives -= 1

    #check if the word has been fully guessed

    if "_" not in guessed:
        print("Congratulation you won!, the word is "+ word)
        break

#If user runs out of lives, they lose
if lives == 0:
    print("Game Over, You lose! the word was " + word)


