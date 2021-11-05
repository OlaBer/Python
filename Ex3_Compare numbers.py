import random

def get_number(min,max):
    return random.randint(min,max)

def compare_numbers(num_1, num_2):
    if num_1 == num_2:
        return True
    else:
        return False

counter = 1
while not compare_numbers(get_number(min = 1,max = 5),
                          get_number(min = 3,max = 7)
    ):
    print(counter)
    counter +=1
