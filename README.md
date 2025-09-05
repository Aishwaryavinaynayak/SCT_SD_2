# Number Guessing Game 

This is a simple Number Guessing Game built in Python as part of my SkillCraft Technology Internship – Task 2.
The program allows the user to set a number range, and then try to guess the randomly chosen number.

## Features

User can set a custom range for the game.

Program generates a random number within that range.

Provides hints (Too high / Too low) for each guess.

Tracks the number of attempts taken.

Handles invalid inputs gracefully.

## How It Works

The user enters a starting and ending number.

The program selects a random number within that range.

The user guesses until the correct number is found.

The program displays the total attempts made.

## Technologies Used

Python 3, Random module

## Sample Output
Welcome to the Number Guessing Game

Enter the starting number of the range: 1

Enter the ending number of the range: 50

I have chosen a number between 1 and 50. Can you guess it?

Enter your guess: 25

Too low! Try again.

Enter your guess: 40

Too high! Try again.

Enter your guess: 33

Congratulations! You guessed the number in 3 attempts.

