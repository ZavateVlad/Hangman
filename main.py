#Import random module and art and words
import random
from hangman_words import word_list
from hangman_art import logo, stages

#Choose word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Create conditions to end the game
end_of_game = False
lives = 6

#Print logo
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#Guess words as long as the game continues
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check if the word is already guessed
    if guess in display:
        print(f"This word was already guessed! {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"Your letter, {guess}, it's not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Show guessed words
    print(f"{' '.join(display)}")

    #Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Print the hangman
    print(stages[lives])

#If the player losses, print the word
print(f"The word was: {chosen_word}")
