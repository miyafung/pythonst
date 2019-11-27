secret_word ="abc"
guess= ""
guess_count = 0
guess_limit = 3
# out_of_guesses = false


while guess != secret_word:
    guess = input("Enter guess: ")
    # guess_count +=1
print("you win!")