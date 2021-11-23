class Astronaunt:
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if value in ["", " "]:
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        else:
            self.name = value


a = Astronaunt("george", 3)
print(a.name)