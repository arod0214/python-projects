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
