class A:
    def sum_list(self):
        print("class A")
        return 10

class B(A):
     def sum_list(self):
        super().sum_list()
        print("class B")
        return 20 

class C(B):
     def sum_list(self):
        super().sum_list()
        return 30

o = C()

print(o.sum_list())


