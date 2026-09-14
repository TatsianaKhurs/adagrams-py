from random import randint

LETTER_POOL = {
    'A': 9,
    'B': 2,
    'C': 2,
    'D': 4,
    'E': 12,
    'F': 2,
    'G': 3,
    'H': 2,
    'I': 9,
    'J': 1,
    'K': 1,
    'L': 4,
    'M': 2,
    'N': 6,
    'O': 8,
    'P': 2,
    'Q': 1,
    'R': 6,
    'S': 4,
    'T': 6,
    'U': 4,
    'V': 2,
    'W': 2,
    'X': 1,
    'Y': 2,
    'Z': 1
}


def draw_letters():
    letters = []

    for letter in LETTER_POOL:
        count = LETTER_POOL[letter]
        for letter_index in range(count):
            letters = letters + [letter]

    hand = []

    for letter_index in range(10):
        random_index = randint(0, len(letters) - 1)

        random_letter = letters[random_index]

        new_letters = []

        for index in range(len(letters)):
            if index != random_index:
                new_letters = new_letters + [letters[index]]

        letters = new_letters

        hand = hand + [random_letter]

    return hand

def uses_available_letters(word, letter_bank):
    available_letters = []

    for letter in letter_bank:
        available_letters = available_letters + [letter]

    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in word:
        current_letter = letter

        for letter_index in range(len(lowercase)):
            if letter == lowercase[letter_index]:
                current_letter = uppercase[letter_index]

        found_letter = False
        found_index = -1

        for letter_index in range(len(available_letters)):
            if available_letters[letter_index] == current_letter:
                found_letter = True
                found_index = letter_index
                break

        if found_letter == False:
            return False

        new_letters = []

        for letter_index in range(len(available_letters)):
            if letter_index != found_index:
                new_letters = new_letters + [available_letters[letter_index]]

        available_letters = new_letters

    return True



def score_word(word):
    score = 0
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in word:
        current_letter = letter

        for letter_index in range(len(lowercase)):
            if letter == lowercase[letter_index]:
                current_letter = uppercase[letter_index]

        if current_letter in "AEIOULNRST":
            score += 1

        elif current_letter in "DG":
            score += 2

        elif current_letter in "BCMP":
            score += 3

        elif current_letter in "FHVWY":
            score += 4

        elif current_letter in "K":
            score += 5

        elif current_letter in "JX":
            score += 8

        elif current_letter in "QZ":
            score += 10

    if len(word) >= 7 and len(word) <= 10:
        score += 8

    return score

def get_highest_word_score(word_list):
    best_word = word_list[0]
    best_score = score_word(best_word)

    for word in word_list:
        current_score = score_word(word)

        if current_score > best_score:
            best_word = word
            best_score = current_score

        elif current_score == best_score:
            if len(word) == 10 and len(best_word) != 10:
                best_word = word
                best_score = current_score

            elif len(word) != 10 and len(best_word) != 10:
                if len(word) < len(best_word):
                    best_word = word
                    best_score = current_score

    return (best_word, best_score)