import random
# Simulate the Infinite Monkey Theorem by generating letters of the alphabet
# knowing that eventually they will spell the given word.


def simulate_imt(word, logging):
    count = 0
    done = False
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    length = len(word)
    attempts = (26**length)

    if logging:
        print("\nestimated attempts: " + str(attempts))

    # Loop this until we find the result.
    while not done:
        result = ""

        # create a word from letters with same length as our target word.
        for _ in range(length):
            letter_index = random.randint(0, 25)
            result += alphabet[letter_index]

        count += 1
        if logging:
            print(result)

        # If our generated word is the same as our target, finish and print.
        if result == word:
            done = True

    print("\n\nWord has been found!")
    print("Estimated: " + str(attempts))
    print("Actual:    " + str(count))


