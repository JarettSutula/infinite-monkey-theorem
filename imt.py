from simulation import simulate_imt

# The Infinite Monkey Theorem states that "a monkey hitting keys at random on
# typewriter keyboard for an infinite amount of time will almost surely type
# any given text, such as the complete works of William Shakespeare.
#
# This is a small program that will take in a given word and output the
# predicted amount of times it will run before it prints out the word, and
# then try to generate it.

# Fair word of warning: If you are looking to go over 5 letter words, it will
# take a while. For now, we only do lowercase to reduce wait time.
# Written by Jarett Sutula

# Take inputs for word and logging to send to simulation file.
word = input("What word would you like to find today? ")
word = word.lower()

print("\nWould you like to log every attempt? NOTE: This will " +
      "drastically increase wait time. \nNot recommended for long words. ")
logging = input("Y/N: ")

if logging.lower() == "y":
    doLog = True
else:
    doLog = False

simulate_imt(word, doLog)
