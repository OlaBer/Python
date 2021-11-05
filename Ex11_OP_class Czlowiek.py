import random                       

class Czlowiek:
    
    def __init__(self,
                 f_name = None,
                 l_name = None,
                 id = None,
                 sex = None):

        self.f_name = f_name
        self.l_name = l_name
        self.id = id
        self.sex = sex

         
    def __str__(self):
        if self.sex == "F":
            sex = "kobietą"
        else:
            sex = "mężczyzną"
        result = f"Hej, jestem {sex} i nazywam się {self.f_name} {self.l_name}"
        return result
        
jan_kowalski = Czlowiek(f_name = "Jan",
                        l_name = "Kowalski",
                        id = "1234567890",
                        sex = "M")

anna_nowak = Czlowiek(f_name = "Anna",
                      l_name = "Nowak",
                      id = "0987654321",
                      sex = "F")
