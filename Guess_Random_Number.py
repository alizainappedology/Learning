import random;

secret_number = random.randint(1,10)
guess = None

while guess != secret_number:
    
    guess = int(input("Guess Secret Number: "))
    
    if guess < secret_number:
        print("Secret number is smaller then", guess)
        
    elif guess > secret_number:
        print("Secret Number is bigger than", guess)
        
    else:
        print("Great", guess, "is the Secret Number")