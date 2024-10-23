class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, (House, int)):
            return self.number_of_floors < (other.number_of_floors if isinstance(other, House) else other)
        return NotImplemented

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

# Пример использования класса
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)                # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)                # Название: ЖК Акация, кол-во этажей: 20

print(h1 == h2)         # False

h1 = h1 + 10            # Увеличение этажей на 10
print(h1)                # Название: ЖК Эльбрус, кол-во этажей: 20
print(h1 == h2)         # True

h1 += 10                # Увеличение этажей еще на 10
print(h1)                # Название: ЖК Эльбрус, кол-во этажей: 30

h2 = 10 + h2            # Увеличение этажей у h2 на 10
print(h2)                # Название: ЖК Акация, кол-во этажей: 30

print(h1 > h2)          # False
print(h1 >= h2)         # True
print(h1 < h2)          # False
print(h1 <= h2)         # False
print(h1 != h2)         # False