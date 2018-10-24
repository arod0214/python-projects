def main():
    python = 0
    for i in range(10):
        word = input("Enter a word:")
        if word == "python":
            python = python + 1
    print("You entered the word python",python,"times.")

if __name__ == "__main__":
    main()
