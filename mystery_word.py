from random import choice

# Global constants
NUM_TURNS = 8
CURRENT_USER_TURN = 0
WORDS_FILE = "words.txt"

# Create an output string by assigning from word_to_guess
def show_guessed_so_far(word_to_guess, letters_to_guess, letters_guessed):
    pass

# Initialize the game state based on word_to_guess
# Print the length of the word to be guessed
# Enter the game loop
# Show the user what they've guessed so far
# While the number of guesses used is less than `NUM_TURNS`, get a new user guess
# Check whether the new user guess is an element of word to be guessed
def play_game(word_to_guess):
    letters_to_guess = set(word_to_guess)
    letters_guessed = set()
    guesses_used = 0

    print(word_to_guess)
    print(f"Your word has {len(word_to_guess)} letters.")

    while guesses_used < NUM_TURNS:
        show_guessed_so_far(word_to_guess, letters_to_guess, letters_guessed)

        new_guess = get_guess(letters_guessed)
        letters_guessed.add(new_guess)

        if new_guess in letters_to_guess:
            print("Correct!")

        else:
            print("Incorrect!")
            guesses_used += 1

        user_has_won = check_victory(letters_guessed, letters_to_guess)

        if user_has_won:
            print("Congratulations, you win!")
            print(f"You finished in {guesses_used} turns!")
            return

        # Assert guesses_used == NUM_TURNS
        print("You lose!")
        print(f"Your word was {word_to_guess}")
        return

# Open the file for reading
# Read in all content as a string
# Use .split() method to break the content into newline characters
def read_words(filename):
    f = open(filename, 'r+')
    words = [word for word in f.readlines()]
    f.close()
    return words

# Check value of desired difficulty
def filtered_by_difficulty(words, desired_difficulty):
    print(words)
    easy_words = [word for word in words if len(word) >= 4 and len(word) <= 6]
    normal_words = [word for word in words if len(word) >= 6 and len(word) <= 8]
    hard_words = [word for word in words if len(word) > 8]

    if desired_difficulty == "easy":
        return easy_words

    if desired_diffulty == "normal":
        return normal_words

    if desired_difficulty == "hard":
        return hard_words

# Read all words from words.txt
def get_word_to_guess(desired_difficulty):
    words = read_words(WORDS_FILE)
    filtered = filtered_by_difficulty(words, desired_difficulty)
    return choice(filtered)

# Setup an input validation
def get_user_difficulty():
    return "easy"

# Get desired user difficulty
# Get a word for the player to guess
# Play the game
# Ask if the user wants to play again
# Run game again or exit game
def run_game_loop():
    desired_difficulty = get_user_difficulty()
    word_to_guess = get_word_to_guess(desired_difficulty)
    play_game(word_to_guess)

    play_again = prompt_play_again()

    if play_again:
        run_game_loop()

    else:
        print("Goodbye!")
        exit(0)

# Run the game loop
def main():
    print("Welcome to Mystery Word!")
    run_game_loop()

if __name__ == "__main__":
    main()