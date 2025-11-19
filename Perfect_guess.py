import random
comp = random.randint(1, 100)

guesses= 0

while True:
    try:
        a = int(input("Guess a number (1 to 100): "))
        guesses += 1
    except ValueError:
        print("Please enter a valid number!")
        continue

    if(a > comp):
        print("Try Lower no. Pls")
    elif(a < comp):
        print("Try Higher no. Pls")
    else:
        print(f"you guessed the no. {a} in {guesses} guesses")
        break 
