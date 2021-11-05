secret_number = 777

while True:
    my_number = input("Podaj numer: ")

    try:
        my_number = int(my_number)
    except:
        continue
   
    if my_number == secret_number:
        print("Brawo, odgadłeś")
        break
    else:
        print("Próbuj dalej")
    

   
