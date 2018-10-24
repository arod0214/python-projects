# Pig Latin is a made-up language formed from English.

# Write a function called translateToPigLatin(...) that in takes one string representing a word and returns that word in Pig Latin. You can assume the word entered by the user is always all lower case, and falls into one of the 4 cases below.

# The rules for converting a word into Pig Latin are as follows:

# if the word begins with a vowel (a,e,i,o, or u), add "hay" to the end of the word.
# if the first letter in a word is a consonant (not including 'y') and the second letteris a vowel or 'y', move the first letter to the end of the word and add "ay".
# if the first two letters in a word are consonants (not including 'y') and the third letter is a vowel or 'y', move the first two letters to the end of the word and add "ay".
# if the first three letters in a word are consonants (not including 'y') and the fourth letter is a vowel or 'y', move the first three letters to the end of the word and add "ay".
 
# You should also write a main method to test your function by asking the user a word, calling (using) your function to find the Pig Latin translation, and printing it to the screen.

# Hint: You can save yourself some typing by making a second function to check if a character is a vowel.

def translateToPigLatin(word):
    if word[0] == "a" or "e" or "i" or "o" or "u":
        word = str(word+"hay")
    elif word[0] == "b"or "c"or"d"or"f"or"g"or"h"or"j"or"k"or"l"or"m"or"n"or"p"or"q"or"r"or"s"or"t"or"v"or"w"or"x"or"z":
        word = str(word[1:]+word[0]+"ay")
    elif word[1] == "a" or "e" or "i" or "o" or "u" or "y":
        word = str(word[1:]+word[0]+"ay")
    #elif word[:1] == 
    return word

def main():
    word = input("Enter a word:")
    print("Your word is", str(translateToPigLatin(word))+".")

if __name__ == "__main__":
    main()
