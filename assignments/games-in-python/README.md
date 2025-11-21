
# 📘 Assignment: 🎮 Hangman Game Challenge

## 🎯 Objetivo

Build a console-based Hangman game in Python where students practice string manipulation, loops, conditionals and basic I/O by implementing the game loop, guess handling, and game state display.

## 📝 Tarefas

### 🛠️	Build the Hangman Game

#### Description
Create a playable Hangman game that runs in the terminal. The program should choose a secret word from a predefined list, accept single-letter guesses from the player, show progress using an underscore-style display, and keep track of incorrect guesses until the game is won or lost.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list embedded in the script.
- Accept single-letter guesses from the user and update the displayed progress in `_ _ _` format.
- Track and display remaining incorrect attempts (e.g., 6 attempts total).
- Keep and show a list of letters already guessed; repeated guesses should not further penalize the player.
- End when the word is fully guessed or when attempts are exhausted, displaying a clear win or lose message and revealing the correct word.
- Be robust to user input (ignore case and trim whitespace).

Example run (simplified):

```
Secret word: _ a _ _ _
Guessed letters: a
Attempts remaining: 5
Enter a letter: n
Good guess! Secret word: n a n _ _
```

### 🛠️	Stretch Goals (Optional)

#### Description
Add one or more optional enhancements to make the game more polished or configurable.

#### Requirements
Completed program may include one or more of the following:

- ASCII-art hangman that progresses with each incorrect guess.
- Load the word list from an external text file (e.g., `words.txt`).
- Difficulty levels that change allowed attempts or choose longer/shorter words.
- A simple scoring or replay option so the player can play multiple rounds without restarting the program.

