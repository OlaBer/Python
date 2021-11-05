from random import randint

secret_number = 88

#sectre_number = randint(0, 100)
user_number = int(input("Podaj liczbę: "))

counter = 1

while user_number != secret_number:
    print("Próba ", counter)

    if counter > 1:
        user_number = int(input("Podaj liczbę: "))
    
    print(user_number)

    if user_number > secret_number:
        print("Podana liczba jest większa od Tajemniczego numeru. Spróbuj ponownie")
                
    elif user_number < secret_number:
        print("Podana liczba jest mniejszaa od Tajemniczego numeru. Spróbuj ponownie")
    else:
        print("Brawo, to jest ta liczba!")
        break

    counter = counter +1
    
        
        
