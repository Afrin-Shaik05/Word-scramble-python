# =============================================
# WORD SCRAMBLE GAME - word_scramble.py
# Concepts: String manipulation, Randomization
# =============================================

import random   # built-in Python library for randomization


# --- STEP 1: Word list ---
word_list = [
    {"word": "APPLE",   "hint": "A common fruit"},
    {"word": "BRIDGE",  "hint": "Crosses a river"},
    {"word": "CAMERA",  "hint": "Takes photos"},
    {"word": "JUNGLE",  "hint": "Dense tropical forest"},
    {"word": "BUTTER",  "hint": "Goes on bread"},
    {"word": "CASTLE",  "hint": "Where kings live"},
    {"word": "OXYGEN",  "hint": "We breathe it"},
    {"word": "PENCIL",  "hint": "Used to write"},
    {"word": "WINTER",  "hint": "The cold season"},
    {"word": "SPIDER",  "hint": "An 8-legged creature"},
    {"word": "PLANET",  "hint": "Found in space"},
    {"word": "LAPTOP",  "hint": "A portable computer"},
]


# --- STEP 2: Shuffle the letters of a word ---
def shuffle_word(word):
    # String manipulation: convert word to a list of letters
    # "APPLE" → ["A", "P", "P", "L", "E"]
    letters = list(word)

    # Randomization: shuffle the list randomly
    random.shuffle(letters)

    # String manipulation: join letters back into a string
    scrambled = "".join(letters)

    # If it accidentally stayed the same, shuffle again
    if scrambled == word:
        return shuffle_word(word)

    return scrambled


# --- STEP 3: Display the scoreboard ---
def show_score(score, attempts, streak):
    print("\n" + "=" * 35)
    print(f"  Score: {score}   Tries: {attempts}   Streak: {streak}")
    print("=" * 35)


# --- STEP 4: Play one round ---
def play_round(current, score, attempts, streak):
    word    = current["word"]
    hint    = current["hint"]
    scrambled = shuffle_word(word)

    print(f"\n  Scrambled word:  {scrambled}")
    print("  (type HINT to see a clue, or QUIT to exit)\n")

    while True:
        guess = input("  Your answer: ").strip().upper()

        if guess == "QUIT":
            print(f"\n  The answer was: {word}")
            return score, attempts, streak, False   # False = quit game

        elif guess == "HINT":
            print(f"  Hint: {hint}")

        elif guess == word:
            score   += 10
            streak  += 1
            attempts += 1
            print("\n  ✅ Correct! +10 points 🎉")
            return score, attempts, streak, True

        else:
            streak   = 0
            attempts += 1
            print("  ❌ Wrong — try again!")


# --- STEP 5: Main game loop ---
def main():
    print("\n" + "#" * 35)
    print("#    WORD SCRAMBLE GAME           #")
    print("#    Unscramble the letters!      #")
    print("#" * 35)

    score    = 0
    attempts = 0
    streak   = 0

    # Make a copy so we don't repeat words
    remaining_words = word_list.copy()
    random.shuffle(remaining_words)

    for current in remaining_words:
        show_score(score, attempts, streak)

        score, attempts, streak, keep_playing = play_round(
            current, score, attempts, streak
        )

        if not keep_playing:
            break

        play_again = input("\n  Next word? (yes / no): ").strip().lower()
        if play_again != "yes":
            break

    # Game over
    print("\n" + "=" * 35)
    print("       GAME OVER!")
    print(f"  Final Score : {score}")
    print(f"  Total Tries : {attempts}")
    print(f"  Best Streak : {streak}")
    print("=" * 35 + "\n")


# --- Run the game ---
if __name__ == "__main__":
    main()