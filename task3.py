# You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.

# You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

def convertTemperature(celsius: float):
    k = celsius + 273.15
    f = celsius * 1.80 + 32.00
    return [round(k, 5), round(f,5)]

print(convertTemperature(36.50))
