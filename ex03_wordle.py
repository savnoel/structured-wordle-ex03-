"""Structured Wordle"""

__author__ = "730604481"

def contains_char(str_searched: str, str_character: str) -> bool:
    """Returns True if the single character of 2nd string is anywhere in 1st string. Returns False otherwise"""
    exist: bool = False
    ind: int = 0
    assert len(str_character) == 1

    while ind  < len(str_searched) and not exist:
        if str_character == str_searched[ind]:
            exist = True
        ind = ind + 1
    return exist

def emojified(guess_word: str, secret_word: str) -> str:
    """ Returns string of emojis using contains_char function"""
    assert len(guess_word) == len(secret_word) # Since we can expect anyone using this function will provide two strings == in length
    store: str = ""
    word_idx: int = 0
    GREEN_BOX: str = "\U0001F7E9"
    WHITE_BOX: str = "\U00002B1C"
    YELLOW_BOX: str = "\U0001F7E8"

    while  word_idx < len(secret_word):
        if guess_word[word_idx] == secret_word[word_idx]: # When the character is  in the correct location
            store = store + GREEN_BOX
        else:
            if contains_char(secret_word, guess_word[word_idx]):
                store += YELLOW_BOX # When the character is in string, just not the correct location
            else:
                store += WHITE_BOX
        word_idx = word_idx +1
    return store

def input_guess(expected_length: int) -> str:
    """ Given an int "expected length", will prompt user for a guess """
    inputted_guess: str = input(f"Enter a {expected_length} character word:") # the users inputted guess

    while len(inputted_guess) != expected_length: # while the length of the inputted guess is not equal to the expected length
        inputted_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return inputted_guess # what is being returned back into as user_input

def main() -> None:
    """ Implementing the high level logic of the wordle game loop """
    SECRET: str = "codes" # secret word
    game_completed: bool = False
    number_of_turns: int = 0

    while  not game_completed and number_of_turns < 6: # While the game is still ongoing and the number of turns is less than 6
        number_of_turns += 1
        print(f"=== Turn {number_of_turns}/6 ===")
        user_input: str = input_guess(len(SECRET))
        if user_input == SECRET:
            game_completed = True
        print(emojified(user_input, SECRET))      
    if game_completed: print(f"You won in {number_of_turns}/6 turns!") # game is completed and user wins
    else:
        print("X/6 - Sorry, try again tomorrow!") # game is over and user lost

if __name__ == "__main__":
    main()