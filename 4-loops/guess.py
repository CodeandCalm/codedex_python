# Guess the number and get the Loop ! 🌐
# -----------Guess if you can 📌 --------------------
guess = 0
tries = 0

while (guess != 6 and tries < 5):
    guess = int(input("Guess a number: "))
    tries += 1
if (guess == 6):
    print("Yoy got it!, Congrats!💡")
elif (tries == 5):
    print("you run out of tries!")
