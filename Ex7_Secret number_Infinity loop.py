from random import randint
secret_number = randint(0, 100)
#print(secret_number)

user_number = int(input("Podaj liczbę: "))

counter = 0

while secret_number != user_number:
    
    if user_number > secret_number:
        print("Podana liczba jest większa od Tajemniczego numeru. Spróbuj ponownie")
    if user_number < secret_number:
        print("Podana liczba jest mniejszaa od Tajemniczego numeru. Spróbuj ponownie")
    else:
        print("Brawo, to jest ta liczba!")

    counter +1
    
        
        
