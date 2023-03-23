def convertTemperature(celsius):
    Kelvin = celsius + 273.15
    Fahrenheit = celsius * 1.80 + 32.00
    return [Kelvin, Fahrenheit]
print(convertTemperature(36.50))
print(convertTemperature(122.11))