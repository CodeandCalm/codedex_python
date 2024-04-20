# Boleans 🎢

height = int(input("🧙 What's your height in cm? "))
credit = int(input("💵 What's your credit? "))
if(height >= 137 and credit >= 10):
    print("Enjoy the ride😎!")
elif height < 137 and credit >=10:
    print("You are not tall enough to ride.")
elif (height >= 137 and credit < 10):
    print("You don't have enough credits..💸")
elif (height < 137 and credit < 10):
    print("💔You have not met either requirement🎮")
