import random;

def guess(x):
    random_number = random.randint(1, x)
    #Random int is between 1 and x so 0 will never be the 
    #answer. Setting guess to 0
    guess = 0
    while guess != random_number:
        #F-strings provide a concise and convenient way to embed 
        #Python expressions inside string literals for formatting. 
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Guess a higher number!')
        elif guess > random_number:
            print('Guess a lower number!')
    
    print('Congrats! You guessed the correct number!')

guess(50)