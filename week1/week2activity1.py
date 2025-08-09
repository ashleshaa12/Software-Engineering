import random

#random words
words = ["apple", "banana", "grape", "mango", "peach"]

#  Pick a random word
word = random.choice(words)

# Generate blanks (underscores)
blanks = ["_"] * len(word)

#  number of lives
lives = 5

# loop
while True:
    print("Word:", " ".join(blanks))
    print("Lives left:", lives)
    
    # Ask user to guess a letter
    guess = input("Guess a letter: ").lower()
    
    # Check if guess is in word
    if guess in word:
        print("Yes! The letter is in the word.")
        # Replace blanks with the correct letter
        for i in range(len(word)):
            if word[i] == guess:
                blanks[i] = guess
    else:
        print("No! The letter is not in the word.")
        lives = 1  
        # Lose a life
    
    # Check if all blanks are filled
    if "_" not in blanks:
        print("Congratulations! You guessed the word:", word)
        break  # Game over (win)

    # Check if out of lives
    if lives == 0:
        print("Game over! You ran out of lives.")
        print("The word was:", word)
        break  # Game over (loss)
