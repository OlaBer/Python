class Instrument:
    def __init__(self):
        self.label = "Instrument"

    def play(self):
        return (self.label+ " plays")

    def __str__(self):
        return self.play()


class Guitar(Instrument):
    def __init__(self):
        self.label = "Guitar"

    def __str__(self):
        return self.play()+" very loud !!!"


class Trumpet(Instrument):

    def __init__(self):
        super().__init__()
        self.label = "Trumpet"

    def __str__(self):
        return self.play()+" very nice"


print(Guitar())
print(Trumpet())

