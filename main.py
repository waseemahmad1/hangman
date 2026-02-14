import random
import string

def show_progress(word, guessed):

    res = []

    for ch in word:
        if ch in guessed:
            res.append(ch)
        else:
            res.append("_")
    
    return " ".join(res)

def get_valid_guess(guessed):
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1:
            print("\nPlease guess only a single character")
            continue
        elif guess not in string.ascii_lowercase:
            print("\nPlease guess a lowercase letter (a-z)")
            continue
        elif guess in guessed:
            print("\nYou have already guessed this letter, please guess something else")
            continue
        else:
            return guess

def main():
    user_input = input("Would you like to provide a word or generate a random word? (1 = provide, 2 = random): ").strip()

    word_bank = ["barbie", "giant", "funny", "police", "rangoon", "crabs", "mermaid", "brownie", "skating", "mcdonalds", "rooster"
                 "fish", "tuba", "trombone", "ozone", "jupiter", "uranus", "sirius", "starlight", "amazon", "forest", "tropical",
                 "monkey", "dolphin", "helium", "hydrogen", "mercury", "gold", "boron", "stapler", "paper", "clipboard", "computer"]

    while user_input != "1" and user_input != "2": 
        user_input = input("Please provide a valid number: ").strip()

    if user_input == "1":
        word = input("Great, please provide the word: ").strip().lower()
    else:
        word = random.choice(word_bank)

    lives = 5
    guessed = set()
    letters_remaining = len(set(word))

    while lives > 0 and letters_remaining > 0:

        print("\nWord:", show_progress(word, guessed))
        print("Guessed:", " ".join(sorted(guessed)) if guessed else "(none)")
        print("Lives remaining:", lives)

        guess = get_valid_guess(guessed)
        guessed.add(guess)

        if guess not in word:
            lives -= 1
            print(f"\n{guess} was not in the word!")
        else:
            letters_remaining -= 1
            print(f"\n{guess} was in the word! There is/are {letters_remaining} letter(s) remaining")

    if lives == 0:
        print(f"\nYou lost! The word was: {word}")
    elif letters_remaining == 0:
        print(f"\nYou won! The word was: {word}")

if __name__ == "__main__":
    main()













