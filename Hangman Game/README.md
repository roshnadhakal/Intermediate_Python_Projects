# Hangman Game in Python

Welcome to the Hangman Game! This is a simple text-based implementation of the classic word-guessing game. The objective is to guess the hidden word by suggesting letters within a certain number of guesses (lives).

## Requirements

- Python 3.12.4 or higher


## How to Play

1. The game will display the number of lives you have and the current state of the word to be guessed (with unguessed letters represented as underscores).
2. You will be prompted to guess a letter.
3. If the letter is in the word, it will be revealed in the correct positions. If not, you will lose a life.
4. The game continues until you either guess the word or run out of lives.

## Code Explanation

# The word to be guessed
word = \"Nepal\".lower()  
\`\`\`
- This line initializes the word to be guessed, converting it to lowercase for case-insensitive comparison.


# The number of lives
lives = 5
\`\`\`
- This sets the number of incorrect guesses (lives) a player can make before losing the game.


# The guessed letters
guessed = [\"_\"] * len(word)
\`\`\`
- Initializes a list to keep track of the correctly guessed letters. It starts with underscores representing unguessed letters.


# The Game loop
while lives > 0:  
\`\`\`
- This starts the main game loop, which continues until the player runs out of lives.

    # Print the current state of the word  
    print(\" \".join(guessed))  
    print(f\"Lives: {lives}\")  

- Displays the current state of the guessed word and the number of lives remaining.

\`\`\`python
    # Ask the user for a letter    
    letter = input(\"Guess a letter: \")   
\`\`\`
- Prompts the player to input a letter.

\`\`\`python
    # Check if the letter is in the word  
    if letter in word:  
\`\`\`
- Checks if the guessed letter is part of the word.

\`\`\`python
        # Reveal the correct letter    
        for i in range(len(word)):  
            if word[i] == letter:  
                guessed[i] = letter  
\`\`\`
- If the letter is correct, it updates the \`guessed\` list to reveal the letter in the correct position.

\`\`\`python
    else:
        # Decrease the number of lives  
        lives -= 1
\`\`\`
- If the letter is incorrect, the player loses a life.

\`\`\`python
    # Check if the word has been fully guessed  
    if \"_\" not in guessed:  
        print(\"Congratulations you won!, the word is \" + word)  
        break  
\`\`\`
- If there are no underscores left in the \`guessed\` list, the player has successfully guessed the word, and the game ends.

\`\`\`python
# If user runs out of lives, they lose
if lives == 0:  
    print(\"Game Over, You lose! the word was \" + word)  
\`\`\`
- If the player runs out of lives, the game ends with a loss message.

## Contributing

Feel free to fork this repository and submit pull requests for improvements or new features!
