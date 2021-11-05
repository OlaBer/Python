secret_number = 777

print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")

#my_number = int(input("Wprowadź numer: "))

while not int(input("Wprowadź numer: "))== secret_number:
    print("To nie ten numer, spróbuj ponownie")

print("Brawo, odgadłeś")





