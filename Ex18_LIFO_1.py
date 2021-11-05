class Stack:
    def __init__(self):
        self.__stack_lst = []

    def printObj(self):
        print(self.__stack_lst)
        
    def push(self, val):
        self.__stack_lst.append(val)

    def pop(self):
        val = self.__Stack__lst[-1]
        del self.__Stack_lst[-1]
        return val
    
obj = Stack()

print(obj)

obj.push(9)
obj.push(11)
obj.push(555)

print(obj)

print(obj.__dict__)
print(obj._Stack__stack_lst)

obj._Stack__stack_lst = 1

print(obj._Stack__stack_lst)





        





    
