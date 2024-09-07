import random

easy = 10
hard = 5


def easy_hard_choice(decide):
    if decide == 'easy':
        return easy
    else:
        return hard


def guess_random(guess, random_number, easy_hard):
    if guess < random_number:
        print('Too low.')
        return easy_hard - 1
    elif guess > random_number:
        print('Too high.')
        return easy_hard - 1
    else:
        print(f"You got it! The answer was {random_number}")


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100)
    print(f"Pssst, the correct answer is {random_number}")

    decision = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    easy_hard = easy_hard_choice(decision)

    guess = 0
    while guess != random_number:
        print(f'You have {easy_hard} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))
        easy_hard = guess_random(guess, random_number, easy_hard)

        if easy_hard == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != random_number:
            print("Guess again.")


game()
