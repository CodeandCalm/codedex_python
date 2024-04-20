# ----------------FIZZ BUZZ GAME ----------------------------

# The player designated to go first says the number "one",
# and the players then count upwards in turn. 
# However, any number divisible by three is replaced by the word fizz 
# and any number divisible by five by the word buzz. 
# Numbers divisible by both three and five (i.e. divisible by fifteen) become fizz buzz. 
#A player who hesitates or makes a mistake is eliminated.

for i in range (1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print('Fizz Buzz')
    elif (i % 3 == 0):
        print('Fizz')
    elif (i % 5 == 0):
        print('Buzz')
    else:
        print(i)
