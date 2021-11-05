import random
import json

class Person:
    first_name = None
    last_name = None
    pesel = None
    sex = None

    def __init__(self, first_name = None, last_name = None, pesel = None, sex = None):
        if pesel == None:
            self.pesel = PatientData.draw_numbers_for_pesel()
        else:
            self.pesel = pesel
        if sex == None:
            gender_lst = ["F", "M"]
            self.sex = random.choice(gender_lst)
        else:
            self.sex = sex
        if self.sex == "M":
            if first_name == None:
                self.first_name = PatientData.draw_male_name()
            else:
                self.first_name = first_name
            if last_name == None:
                self.last_name = PatientData.draw_male_surname()
            else:
                self.last_name = last_name
        else:
            if first_name == None:
                self.first_name = PatientData.draw_female_name()
            else:
                self.first_name = first_name
            if last_name == None:
                self.last_name = PatientData.draw_female_surname()
            else:
                self.last_name = last_name
        #print(str(self.first_name) + "\n" + str(self.last_name) + "\nPESEL: " + str(self.pesel) + "\npłeć: " + str(self.sex) + "\n")

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name) + ", PESEL: " + str(self.pesel) + ", płeć: " + str(self.sex)

    def get_patient_data_to_csv(self):
        return str(self.first_name) + "," + str(self.last_name) + "," + str(self.pesel) + "," + str(self.sex)


class PatientData:

    @staticmethod
    def draw_male_name():
        male_names = ["John", "Jack", "Tom", "Ron"]
        result = random.choice(male_names)
        return result

    @staticmethod
    def draw_male_surname():
        male_surnames = ["Smith", "Jones", "Williams", "Thomas"]
        return random.choice(male_surnames)

    @staticmethod
    def draw_female_name():
        female_names = ["Ann", "Cindy", "Victoria", "Elisabeth"]
        return random.choice(female_names)

    @staticmethod
    def draw_female_surname():
        female_surnames = ["Davies", "Brown", "Evans", "Wilson"]
        return random.choice(female_surnames)

    @staticmethod
    def draw_numbers_for_pesel():
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        pesel = ""
        while len(pesel) < 11:
            number = random.choice(numbers)
            pesel = pesel + number
        return pesel

    @staticmethod
    def save_all_patients_to_csv(lst):
        with open("C:/Users/akne/OneDrive - Demant/Desktop/Python/Patients.csv", "w", encoding = "Utf - 8") as patients:
            for el in lst:
                patients.write(el + "\n")

    @staticmethod
    def save_all_patients_to_json(lst):
        with open("C:/Users/akne/OneDrive - Demant/Desktop/Python/Patients.json", "w", encoding = "Utf - 8") as patients:
            for el in lst:
                patients.write(json.dumps(el.__dict__, indent = 4))

p1 = Person()
print("\nPacjent 1: \nWszystkie parametry są losowane: ", p1)

p2 = Person(sex = "F")
print("\nPacjent 2: \nZostała podana płeć damska: ", p2)

p3 = Person(sex = "M")
print("\nPacjent 3: \nZostała podana płeć męska: ", p3)

p4 = Person(pesel = "23232323232")
print("\nPacjent 4: \nZostał podany PESEL: ", p4)

p5 = Person(sex = "F", first_name = "Andrzej")
print("\nPacjent 5: \nPłeć i imię zostały podane: ", p5)

p6 = Person(sex = "F", last_name = "Kowalski")
print("\nPacjent 6: \nPłeć i nazwisko zostały podane: ", p6)

patients_lst1 = [p1, p2, p3, p4, p5, p6]
PatientData.save_all_patients_to_json(patients_lst1)

patients_lst2 = [p1.get_patient_data_to_csv(), p2.get_patient_data_to_csv(), p3.get_patient_data_to_csv(), p4.get_patient_data_to_csv(), p5.get_patient_data_to_csv(), p6.get_patient_data_to_csv()]
PatientData.save_all_patients_to_csv(patients_lst2)
