# if and elif to add conditions
PH = int(input("Tell me the level of you ph from  0 to 14 "))
if (PH > 7):
    print("Basic")
elif(PH < 7):
    print("Acidic")
else:
    print ("Neutral")
