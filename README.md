# infinite-monkey-theorem
#### A small simulator of the Infinite Monkey Theorem.

The Infinite Monkey Theorem roughly states that, given an infinite amount of time and a keyboard, a monkey hitting keys at random would type any given text.

We don't really have infinite time on our hands, but the concept intrigued me enough to build a small python script that could emulate the probability of a "monkey" typing out a word that we give it, and allow us to see how many attempts it would take and what it typed instead.

A general summation of how the program works: 
* Takes a word input from user in console
* Notes the length of the word
* Makes strings of randomly-selected letters in the alphabet with the length of the word
* After each attempt, compares the strings and only stops if the attempt is the desired word

# Project Milestones
* Running imt.py script takes in a word input and estimates how many attempts it will take the "monkey" to generate that same word.
* Added the ability to log the attempts in the console, although this does increase wait time.

# Project Goals
* Export the attempts to a text file if the player wants it logged.
* Add capitalization and punctuation if the performance isn't completely unrealistic.





