class SuperA:
    zm3 = 10
    def fun(self):
        return 11

class SuperB:
    zm1 = 20
    def fun1(self):
        return 22

class SuperC(SuperB):
    zm2 = 30
    def fun(self):
        return 33

class Sub(SuperC, SuperA):
    pass

obj = Sub()
print(obj.zm1, obj.fun1())
    
