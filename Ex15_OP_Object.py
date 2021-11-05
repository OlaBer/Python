class Person:
    
    age = 100
    
    def __init__(self):
        self.age = 44

obj1 = Person()
obj2 = Person()
obj3 = Person()

obj2.age = 33
obj3.age = 11

print(obj1.age, obj2.age, obj3.age)
print(Person.age)


my_lst = [1,2,3,4,5]

def my_sum(_lst):
    
    _sum = 0

    for element in _lst:
        _sum = _sum + element

    return _sum

print(my_sum(my_lst))
    
