word = "candyman"

secret_word = {n: letter for n, letter in enumerate(word)}
empty_word = {n: "_" for n in range(len(word))}

game = True
lives = 5

print("Computer made a word...\n")

while game:
    print(f"{list(empty_word.values())}\n")
    letter = input("Please guess the one letter: ").lower()

    if len(letter) != 1:
        print("\nPlease enter ONE letter!\n")
    else:
        if letter in word:
            print(f"\nThis word has '{letter}' letter.\n")
            for i in range(len(word)):
                if secret_word[i] == letter:
                    empty_word[i] = letter
        else:
            print(f"\nThis word doesn't have '{letter}' letter.\n")
            lives -= 1

    if lives == 0:
        print("You are lost!")
        game = False
    elif "_" not in empty_word.values():
        print(f"You are won!\nThe word is '{word}'")
        game = False
