def mM_to_inches(mm_value):
    return mm_value / 25.4

def celsius_to_fahrenheit(celsius_value):
    return (celsius_value * 9 / 5) + 32

def hpa_to_mmhg(hpa_value):
    return hpa_value * 0.750062

def kmh_to_mph(kmh_value):
    return kmh_value / 1.609344

def fahrenheit_to_celsius(fahrenheit_value):
    return (fahrenheit_value - 32) * 5 / 9

def kelvin_to_celsius(kelvin_value):
    return kelvin_value - 273.15


def celsius_to_kelvin(celsius_value):
    return celsius_value + 273.15


def fahrenheit_to_kelvin(fahrenheit_value):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit_value))

    