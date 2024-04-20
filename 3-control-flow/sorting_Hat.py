# questionare using int
#sorting HAT
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
# ----------------------Question 1 --------------------

print("Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
q1 = int(input("Answer number: "))
if (q1 == 1):
    gryffindor += 1
    Ravenclaw += 1
elif (q1 == 2):
    Slytherin += 1
    Hufflepuff += 1
else:
    print("Wrong input")
# ----------------------Question 2 --------------------
print("When I’m dead, I want people to remember me as: ")
print("( 1) The Good")
print("(2) The Great")
print("(3) The Wise")
print("(4) The Bold")
q2 = int(input("Answer number: "))
if (q2 == 1):
    Hufflepuff += 2
elif (q2 == 2):
    Slytherin += 2
elif (q2 == 3):
    Ravenclaw += 2
elif (q2 == 4):
    Gryffindor += 2
else:
    print("Wrong input")
# ----------------------Question 3 --------------------
print("Which kind of instrument most pleases your ear? ")
print("(1) The violin")
print("(2) The trumpet")
print("(3) The piano")
print("(4) The drum")
q3 = int(input("Answer number: "))

if (q3 == 1):
    Slytherin += 4
elif (q3 == 2):
    Hufflepuff += 4
elif (q3 == 3):
    Ravenclaw += 4
elif (q3 == 4):
    Gryffindor += 4
else:
    print("Wrong input")

max_score = max(Gryffindor, Ravenclaw, Slytherin, Hufflepuff)

print("Highest score:")
if Gryffindor == max_score:
    print("🦁 Gryffindor")
if Ravenclaw == max_score:
    print("🦅 Ravenclaw")
if Hufflepuff == max_score:
    print("🦡 Hufflepuff")
if Slytherin == max_score:
    print("🐍 Slytherin")

