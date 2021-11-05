class Stack:

    def __init__(self):
        self.stack_lst = []

    def push(self, val):
        self.stack_lst.append(val)

    def pop(self):
        val = self.stack_lst[-1]
        del self.stack_lst[-1]
        return val

stack_obj = Stack()

stack_obj.push(9)
stack_obj.push(11)
stack_obj.push(555)

print(stack_obj.stack_lst)

stack_obj.stack_lst = 98765

print(stack_obj.stack_lst)

print(stack_obj.__dict__)
    
    

    
