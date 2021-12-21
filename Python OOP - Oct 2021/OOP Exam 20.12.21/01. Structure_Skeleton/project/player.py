class Player:
    __STAMINA_MIN_VALUE = 0
    __STAMINA_MAX_VALUE = 100

    def __init__(self, name, age, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.need_sustenance = True if self.stamina < 100 else False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < self.__STAMINA_MIN_VALUE or value > self.__STAMINA_MAX_VALUE:
            raise ValueError("Stamina not valid!")
        self.__stamina = value