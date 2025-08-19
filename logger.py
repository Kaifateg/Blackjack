def logger(message):
    print(message)
    with open("blackjacklog.txt", "a") as file:
        file.write(message+"\n")
