# Loop: iterate

print('BANK OF CODE')
pin = int(input('Enter your pin: '))
while pin != 1234:
    pin = int(input('Incorrect PIN. Enter your PIN again: '))
if pin == 1234:
    print('Pin accepted!')

