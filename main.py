# ============================================================
# Python Final Project 2026
# Name: jr
# Date: 
# Project Title: final
# Description: (Write 1-2 sentences explaining what your program does)
# ============================================================


# ---- SECTION 1: Setup / Variables ----
# Create your starting variables here.
# Example: player_name = ""
import random

# Generate a random number between 1 and 10 (inclusive)
secret_number = random.randint(1, 10)

# Loop until the guess is correct
while True:
    try:
        # Prompt user to input their guess
        guess = int(input("Guess a number between 1 and 10: "))
        
        # Compare guess to the target
        if guess == secret_number:
            print("You guessed it right!")
            break  # Exit the loop
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
            
    except ValueError:
        print("Please enter a valid integer.")
# ---- SECTION 2: Welcome Message ----
# Greet the user and explain what your program does.

print("Welcome!")
print("----------------------------")



# ---- SECTION 3: Get Input from User ----
# Use input() to ask the user for information.
# Remember: input() always returns a string.
# Use int() or float() if you need a number.

# Example:
# player_name = input("What is your name? ")
# score = int(input("Enter a number: "))



# ---- SECTION 4: Logic (if / elif / else) ----
# Use if/elif/else to make decisions based on user input or variables.

# Example:
# if score >= 90:
#     print("Great job!")
# elif score >= 70:
#     print("Good work!")
# else:
#     print("Keep practicing!")



# ---- SECTION 5: Final Output ----
# Print a final message, result, or summary to the user.

print("----------------------------")
print("Thanks for using my program!")
