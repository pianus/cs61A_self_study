class Bear:
    def __init__(self):
        self.__repr__ = lambda : 'oski'

    def __repr__(self):
        return 'Bear()'
    def __str__(self):
        return 'a bear'
oski = Bear()
print(oski)
print(str(oski))
print(repr(oski))
print(oski.__str__())
print()

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)

Storrs = Celsius(-10)
