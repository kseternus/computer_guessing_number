import random
guess = guesses = 0
low = 1
high = 100

my_number = int(input("Enter a number from 1 to 100 then I will try to guess it ok? "))
computer_choice = random.randint(low, high)

while my_number != computer_choice:
    print(f"My total guesses is {guesses}")
    print(f"Hmm ok i choose {computer_choice}, higher or lower?")
    guess = input(": ").capitalize()
    if guess == "Higher":
        low = computer_choice
        computer_choice = random.randint(low, high-1)   # -1 because there is a chance to roll same number two or more in a row
        guesses += 1
    elif guess == "Lower":
        high = computer_choice
        computer_choice = random.randint(low+1, high)   # +1 same as above
        guesses += 1

print(f"Yes! It was {my_number}! I guessed after {guesses} tries!")
