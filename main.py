import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
chosen_word = random.choice(word_list)

print(logo[0])

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += " _ "
print(placeholder)

game_over = False

correct_letters = []

guesses = ""

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess not in guesses:
        guesses += guess + " / "
        print(f"Guesses: {guesses}\n")
    else:
        print(f"YOU HAVE ALREADY GUESSED {guess}")
        print(f"Guesses: {guesses}\n")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += guess + " "
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter + " "
        else:
            display += " _ "

    print(f"{display}\n")

    if guess not in chosen_word:
        lives -= 1

    if lives > 0 and "_" in display:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    elif lives == 0 and "_" in display:
        print("YOU ARE DEAD !")
    else:
        print("YOU WIN !")

    print(f"{lives * ' ♥ '}")
    print(f"{stages[lives]}\n\n")

    if lives == 0:
        game_over = True
        print(f"The word was {chosen_word}")
        print("You lose!")

    if "_" not in display:
        game_over = True
        print("You win!")
