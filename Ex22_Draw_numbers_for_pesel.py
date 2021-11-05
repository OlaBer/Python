import random

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def draw_numbers_for_pesel(numbers):
    
    pesel = ""
    while len(pesel) < 11:
        number = random.choice(numbers)
        pesel = pesel + number          
    return pesel

print(draw_numbers_for_pesel(numbers))

    
