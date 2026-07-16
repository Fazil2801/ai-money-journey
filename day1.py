answer = input("What's your name? ")
with open("answers.txt", "a") as file:
    file.write(answer + "\n")

with open("answers.txt", "r") as file:
    print(file.read())
