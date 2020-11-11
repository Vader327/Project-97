import random

print("==========GUESS THE NUMBER==========")

def game():
    guesses = 4
    no = random.randint(1, 9)
    print("\nA number is randomly generated from 0-9. Can you guess it?\n\n")
    
    while True:
        guess = int(input("Guess the Number: "))    
        if guess > no and guesses > 0:
            print("Too High!\nYou have " + str(guesses) + " guesses left.\n")
            
        elif guess < no and guesses > 0:
            print("Too Low!\nYou have " + str(guesses) + " guesses left.\n")
            
        elif guess == no:
            print("\nCorrect! You Won!")
            break
        
        elif guesses==0:
            print("\nYou Lose!")
            break
        
        guesses-=1

    print("The number was " + str(no) + "!")

while True:
    game()
    choice = input("\n\nWould you like to play again? (Yes/No): ")
    if choice == "Yes":
        continue
    elif choice=="No":
        print("OK. Bye!")
        break
    else:
        print("Invalid option.")
        break
