from colorama import Fore, Style, init
init(autoreset=True)
import random

print(Fore.CYAN + "🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

best_score = None
while True:
    secret_number = random.randint(1,100)
    attempts = 0
    wrong_attempts = 0
    
    # let the user guess
    while True:
        user_input = input("Take a guess: ")
        if not user_input.isdigit() : 
            print(Fore.RED + "❌ Please enter a valid number!")
            continue
        guess = int(user_input)
        attempts += 1
        

    # Check the guess 
        if guess < secret_number: 
            print(Fore.YELLOW + "📉 Too low! Try again.")
            wrong_attempts += 1
        elif guess > secret_number:
            print(Fore.YELLOW + "📈 Too high! Try again.")
            wrong_attempts += 1

        else: 
            print(Fore.GREEN + f"🎉 Correct! You guessed it in {attempts} attempts!")
        
            
            if best_score is None or attempts < best_score :
                best_score = attempts
                print(Fore.MAGENTA + "🏆 New Best Score! You're improving!")
            else:
                print(Fore.CYAN + f"🎖️ Your best score: {best_score} attempts!")

            break

        if wrong_attempts > 0 and wrong_attempts % 3 == 0 :
            print("Hint: ", end=" ")
            if secret_number % 5 ==0 : 
                print("The number is divisible by 5.")
            elif secret_number % 2 == 0 : 
                print("The number is even.")
            else : 
                print("The number is odd.")


    play_again = input(Fore.GREEN + "Do you want to play again (yes / no)").lower()
    if play_again != 'yes' :
        print("Thanks for Playing! Goodbye ")
        break