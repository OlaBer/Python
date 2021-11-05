class A:
    zmienna = 5
    
    def metoda(self):
        print("Zwykła metoda wymaga obiektu. Ma dostęp do zmiennych klasy.")
        print(self.zmienna)
        print()

class B:
    zmienna = 4
    
    @staticmethod
    def metoda(): # Nie przyjmuje atrybutu 'self', ponieważ działa bez obiektu
        print("Statyczna metoda nie wymaga obiektu. Nie ma dostępu do zmiennych klasy.")
        # print(self.zmienna) # Wyrzuci error: name 'self' is not defined
        print()

class C:
    zmienna = 3

    @classmethod
    def metoda(self):
        print("Klasowa metoda nie wymaga obiektu. Ma dostęp do zmiennych klasy.")
        print(self.zmienna)
        print()

obiekt_a = A()
obiekt_a.metoda()

B.metoda()

C.metoda()
