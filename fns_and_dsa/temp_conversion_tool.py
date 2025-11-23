FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return f"{fahrenheit}{chr(176)}F is {celcius}{chr(176)}C"


def convert_to_fahrenheit(celcius):
    fahrenheit = (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return f"{celcius}{chr(176)}C is {fahrenheit}{chr(176)}F"
    



temperature_unit = input("Enter the temperature to convert: ")
temperature = float(temperature_unit)
unit = input("Is this temperature in Celcius or Fahrenheit? (C/F): ")
if unit == "F":
    result = convert_to_celcius(temperature)
    print(result)
elif unit == "C":
    result = convert_to_fahrenheit(temperature)
    print(result)
else:
    print("Invalid unit. Please Enter C or F. ")