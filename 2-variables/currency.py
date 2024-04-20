# Calculate currency
a = int(input("What do you have left in pesos? "))
b = int(input("What do you have left in soles? "))
c = int(input("What do you have left in reais? "))

usd = (a * 0.00035626) + (b * 0.26667) + (c * 0.19110)
print(usd)
