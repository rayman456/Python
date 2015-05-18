#I like input checking
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

tempC = input('Enter Temperature in Celsius:')
while is_number(tempC) is False:
	print('Invalid.')
	tempC = input('Enter Temperature in Celsius:')

kph = input('Enter Wind Speed in Kilometers per Hour:')
while is_number(kph) is False:
	print('Invalid.')
	kph = input('Enter Wind Speed in Kilometers per Hour:')

tempC = float(tempC)
kph = float(kph)

tempF = ((9 / 5) * tempC) + 32
mph = kph / 1.609344

chillF = 35.74 + (0.6215 * tempF) - (35.75 * (mph ** 0.16)) + ((0.4275 * tempF) * (mph ** 0.16))
chillC = (5 / 9) * (chillF - 32)

print("It feels like " + str(round(chillF)) + " in Fahrenheit and " + str(round(chillC)) + " in Celsius.")


