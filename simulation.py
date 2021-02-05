import random


# Simulate the Infinite Monkey Theorem by generating letters of the alphabet
# knowing that eventually they will spell the given word.


def simulate_imt(word, logging):
    count = 0
    done = False
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    length = len(word)
    attempts = (26 ** length)

    if logging:
        output_file = open("imt_result.txt", "w")
        output_file.write("--Infinite Monkey Theorem--" +
                          "\nWe are looking for the word " + word + "!" +
                          "\nThe monkey's probability of generating " + word +
                          " is 1 / " + str(attempts) + "." +
                          "\n\nThe monkey is hard at work...\n")

    # Loop this until we find the result.
    while not done:
        result = ""

        # create a word from letters with same length as our target word.
        for _ in range(length):
            letter_index = random.randint(0, 25)
            result += alphabet[letter_index]

        count += 1
        if logging:
            output_file.write("\n" + result)
        # If our generated word is the same as our target, finish and print.
        if result == word:
            done = True

    over_under = attempts - count
    if logging:
        print("\n\nWord has been found!")
        print("\nCheck imt_result.txt for details.")
        output_file.write("\n\n Estimated: " + str(attempts))
        output_file.write("\n Actual:    " + str(count))
        if over_under > 0:
            output_file.write("\nThe monkey was " + str(over_under) +
                              " attempts under its estimation.")
        else:
            over_under *= -1
            output_file.write("\nThe monkey was " + str(over_under) +
                              " attempts over its estimation.")

    else:
        print("Estimated: " + str(attempts))
        print("Actual:    " + str(count))
        if over_under > 0:
            print("\nThe monkey was " + str(over_under) +
                  " attempts under its estimation.")
        else:
            over_under *= -1
            print("\nThe monkey was " + str(over_under) +
                  " attempts over its estimation.")

    if logging:
        output_file.close()
