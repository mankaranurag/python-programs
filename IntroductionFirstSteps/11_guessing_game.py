secret_word = "bridge"
guess = ""

guess_counter = 0
guess_limit = 4
out_of_guesses = False

while guess != secret_word and guess != 'q' and not out_of_guesses:
    if guess_counter < guess_limit:
        guess = input("Guess the word or press q to quit: ")
        guess_counter += 1
    else:
        out_of_guesses = True

if guess == 'q':
    print("you quit")
elif out_of_guesses:
    print("you lose")
else:
    print("you win")
