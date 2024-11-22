class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    # Вывести 'name' атрибута
    def __str__(self):
        return (f'Название: {self.name} кол-во этажей: {self.number_of_floors}.')

    # Сравнить '=' кол. этажей и вывести bool значение
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    # Сравнить '<' кол. этажей и вывести bool значение
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    # Сравнить '<=' кол. этажей и вывести bool значение
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    # Сравнить '>' кол. этажей и вывести bool значение
    def __gt__(self, other):
        return  self.number_of_floors > other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)


    def __radd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)

h1 = House('ЖК "Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1) # __str__
print(h2)
#
# print(len(h1)) # __len__
# print(len(h2))

print(h1 == h2)

h1 = h1 + 10 # __add__
print(h1)

print(h1 == h2) # __eq__

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__