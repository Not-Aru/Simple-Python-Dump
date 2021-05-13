import random

play_again = 'Y'

while(play_again == 'Y'):
    random_integer = random.randint(1, 100)
    int(random_integer)
    print(random_integer)

    print("Guess an integer between One and 100: \n")

    guess = 0

    while(int(guess) != random_integer):
        guess = input("Enter Your Guess: ")
        if(int(guess) == random_integer):
            print("You are Correct!\n")
        else: 
            print("Incorrect!")
    
    play_again = input("Would you Like to Play Again? (Y/n) \n")


print("Thank you for Playing Guess the Number!\n")



