import random




def start():
    
    name = input("Enter your name: ")
    
    wordsFile = open("list.txt", "r")
    wordsList = wordsFile.readlines()
    wordsFile.close()

    random.seed()
    word = random.choice(wordsList)
    
    hidden = ["-"]*(len(word)-1)
    tries = len(word) + 7

    print(f"Good luck {name}\n")

    
    while(tries > 0):
        print(f"You have {tries} turns left goodluck")
        print("".join(hidden))

        while(True):
            guess = input("Guess a character: ")
            if(len(guess) == 1): break
            
        tries -= 1
        if guess in word:
            for i,letter in enumerate(word):
                if guess == letter:
                    hidden[i] = guess
            if("-" not in hidden):
                print(f"Great you guessed the word\n{word}")
                break
    else:
        print(f"Better luck next time the word was {word}")
                










if __name__ == "__main__":
    start()
