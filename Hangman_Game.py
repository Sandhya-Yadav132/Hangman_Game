import time
import random
import os


categories = {
    "Programming_Language": ["python", "java", "php", "c", "cpp"],
    "Operating_System": ["windows", "linux", "macos", "android", "ubuntu"],
    "Laptop_Brands": ["hp", "lenovo", "asus", "dell", "acer"],
    "Python_Datatypes": ["int", "float", "list", "tuple", "set", "dict", "bool", "complex"],
    "Web_Browsers": ["chrome", "firefox", "edge", "safari", "opera"],
    "Social_Media": ["facebook", "instagram", "twitter", "linkedin", "youtube"],
    "Programming_Tools": ["git", "docker", "postman", "github", "vscode"],
    "Databases": ["mysql", "sqlite", "mongodb", "oracle", "postgresql"]
}


def show_welcome_message():
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("\n                  Welcome To HANGMAN\n")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    time.sleep(2)


def list_categories():
    print("\nAvailable Categories:\n")

    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")


def choose_category():
    category_names = list(categories.keys())

    while True:
        choice = input("\nEnter category number: ").strip()

        if choice == "":
            return random.choice(category_names)

        try:
            choice = int(choice)

            if 1 <= choice <= len(category_names):
                return category_names[choice - 1]

            print("Invalid Choice. Please choose a valid category.")

        except ValueError:
            print("Invalid Input. Please enter a number.")


def pick_word(chosen_category):
    return random.choice(categories[chosen_category])


def display_initial_state(word_length, category):
    os.system("cls" if os.name == "nt" else "clear")

    print("\nCategory:", category)
    print("\nWord:", end=" ")

    for _ in range(word_length):
        print("_", end=" ")

    print()


def guess_letter():
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter only one letter.")
            continue

        if not guess.isalpha():
            print("Please enter a valid letter.")
            continue

        return guess


def update_word_state(word, guesses):
    word_state = ""

    for letter in word:
        if letter in guesses:
            word_state += letter
        else:
            word_state += "_"

    return word_state


def check_win(word_state):
    return "_" not in word_state


def check_lose(incorrect_guesses):
    return incorrect_guesses >= 6


def draw_hangman(incorrect_guesses):

    if incorrect_guesses == 1:
        print(" O")

    elif incorrect_guesses == 2:
        print(" O")
        print(" |")

    elif incorrect_guesses == 3:
        print(" O")
        print("/|")

    elif incorrect_guesses == 4:
        print(" O")
        print("/|\\")

    elif incorrect_guesses == 5:
        print(" O")
        print("/|\\")
        print("/")

    elif incorrect_guesses == 6:
        print(" O")
        print("/|\\")
        print("/ \\")


def game_setup():
    show_welcome_message()
    list_categories()

    category = choose_category()
    word = pick_word(category)
    word_length = len(word)

    display_initial_state(word_length, category)

    return word, word_length, category


def play_again():
    while True:
        choose = input("\nDo you want to play again [y/n]: ").lower().strip()

        if choose == "y":
            return True

        elif choose == "n":
            print("Thanks for playing!")
            return False

        else:
            print("Please enter 'y' or 'n'.")


# Main Game
while True:

    word, word_length, category = game_setup()

    incorrect_guesses = 0
    guesses = []

    word_state = update_word_state(word, guesses)

    while True:

        print("\nPrevious guesses:", guesses)

        guess = guess_letter()

        if guess in guesses:
            print("You already guessed that letter.")
            continue

        guesses.append(guess)

        if guess not in word:
            incorrect_guesses += 1
            print("\nIncorrect guess!")
            draw_hangman(incorrect_guesses)

        word_state = update_word_state(word, guesses)

        print("\nWord:", " ".join(word_state))

        # Check Win
        if check_win(word_state):
            print("\nCongratulations! You won!")
            print("The word was:", word)
            break

        # Check Lose
        if check_lose(incorrect_guesses):
            print("\nGame Over!")
            print("The word was:", word)
            break

    # Ask whether to play again
    if not play_again():
        break