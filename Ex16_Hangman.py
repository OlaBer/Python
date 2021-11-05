import random

class Hangman:
    def __init__(self):
        self.mistake = 0
        self.sentence = Sentence.draw_sentence()
        self.player_letters = []

    def get_secret_sentence(self):
        result = ""
        for letter in self.sentence:
            if letter in self.player_letters:
                result = result + letter
            elif letter == " ":
                result = result + " "
            else:
                result = result + "*"
        return result

class Sentence:
    @staticmethod
    def draw_sentence():
        _lst = ["Niebo gwieździste nade mną, prawo moralne we mnie",
                "Lody czekoladowe",
                "Telefon"]
        return random.choice(_lst).upper()
                         
obj = Hangman()

while True:
    print(obj.get_secret_sentence())
    print("Ilość popełnionych błędów wynosi: ", obj.mistake)
    if obj.mistake > 10:
        print("Niestety przegrałeś, przekroczyłeś liczbe dozwolonych blędów")
        break

    if "*" not in obj.get_secret_sentence():
        print("Brawo, odgadłeś hasło!")
        break
    
    letter = input("Podaj literę: ").upper()
    if len(letter) != 1:
        continue
    if letter.lower() not in "aąbcćdeęfghijklłmnńoópqrsśtuwyzżźv":
        continue
    if letter in obj.player_letters:
        print("Ta litesra została juz użyta, spróbuj ponownie")
    elif letter not in obj.player_letters and letter not in obj.sentence:
        obj.player_letters.append(letter)
        obj.mistake = obj.mistake + 1
    else:
        obj.player_letters.append(letter)


# losowanie wyrazów z internetu
# losuj wyraz z pliku
    
 







