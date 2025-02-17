import random
import pyttsx3
from colorama import Fore, Style
import os

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Function to speak the text
def speak(choices):
    engine.say(choices)
    engine.runAndWait()

# its dictionary
choices = ["rock","paper","scissor"]

# enter user and computer choice
user_choice = input(Fore.RED +"enter rock,paper,scissor:" + Style.RESET_ALL)

if user_choice not in choices:
    speak("you not enterd valid choice")
    print(Fore.CYAN + "you not entered valid choice " + Style.RESET_ALL)
    speak("enterd again choice")
    print("enter again")
    breakpoint

else:
    computer_choice = random.choice(choices)
    speak(f"user chose {user_choice} ")
    print(f"user chose: {user_choice} ")

    speak(f"computer chose {computer_choice} ")
    print(f"computer chose: {computer_choice}")


    if user_choice == computer_choice:
        speak("game is tie")
        print("game is tie")

    elif user_choice == "rock" and computer_choice == "paper":
        speak("computer wins ")
        print("computer wins ")

    elif user_choice == "rock" and computer_choice == "scissor":
        speak("you wins")
        print("you wins ")

    elif user_choice == "paper" and computer_choice == "rock":
        speak("you wins")
        print("you wins ")

    elif user_choice == "paper" and computer_choice == "scissor":
        speak("computer wins ")
        print("computer wins ")

    elif user_choice == "scissor" and  computer_choice == "rock":
        speak("computer wins")
        print("computer wins")

    elif user_choice == "scissor" and computer_choice == "paper":
        speak("you wins ")
        print("you wins ")

 # Clear the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')   