class Human:
    def __str__(self):
        return 'I am human'

class Child(Human):
    pass
    
    
class Ex(Exception):
    def __init__(self, *msg):
        self.args = ("misio",)
        pass
try:
    raise Ex('Wywołuję wyjątek Ex', 'A to jest drugi parametr')
except Ex as e:
    print('Jestem w bloku except Ex')
    print(e.args)

Person = Child()
print(Person)




