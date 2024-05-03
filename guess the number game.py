import random    
def guess_the_number():
    secret_number=random.randint(1,10)
    # Above I have used module called random and used randint to generate a random integer between given values for the secret number.
    
    # allows the user to guess until he guess correctly or all the attempts are over.
    attempts=0
    max_attempts=3
    while(attempts<max_attempts):
        guess=int(input("Guess the secret number between (1 to 10): "))
        attempts+=1
        # to check the guess is correct or not i have used conditional statements.
        if(guess==secret_number):
            print("Congrats you guess is correct")
            return
        elif(guess<secret_number):
            print("The number is higher")
        else:
            print("The number is lower")        
    print("Your all attempts are over the secret number was:", secret_number)
guess_the_number()

    
    