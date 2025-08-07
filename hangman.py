import random

word_list = ["apple", "tiger", "house", "smart", "phone"]
chosen_word = random.choice(word_list)
guessed_word = ["_"] * len(chosen_word)

max_incorrect_guesses = 6
incorrect_guesses = 0
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("\nWord: " + " ".join(guessed_word))

while incorrect_guesses < max_incorrect_guesses and "_" in guessed_word:
    print("\nIncorrect guesses left:", max_incorrect_guesses - incorrect_guesses)
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                guessed_word[i] = guess
        print("Good guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess.")

    print("\nWord: " + " ".join(guessed_word))

print("\n- Game Over -")
if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", chosen_word)
else:
    print("You ran out of guesses. The word was:", chosen_word)