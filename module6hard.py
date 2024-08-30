import math
class Figure:

    def __init__(self, __color, __sides, sides_count=0, filled=True):
        self.__color = __color
        self.__sides = __sides
        self.sides_count = sides_count
        self.filled = filled
        self.correct()


    def correct(self, *__sides):         # проверка на корректоность количества переданных сторон
        if len(self.__sides) != self.sides_count:
            sides = []
            if self.sides_count == 12 and len(self.__sides) == 1:
                for i in range(12):
                    sides.append(self.__sides[0])
            else:
                for i in range(self.sides_count):
                    sides.append(1)
            self.__sides = sides
        return self.__sides


    def rangle_in(self, a):   #проверяет корректность числового значения цвета
        f = True
        if ((a < 0) or (a > 255)):
            f = False
        return f

    def __is_valid_color__(self, __color):  #проверяет корректность переданных значений перед установкой нового цвета.
        f = False
        if ((self.rangle_in(__color[0])) and (self.rangle_in(__color[1]))
                and (self.rangle_in(__color[2]))):
            f = True
        return f

    def set_color(self, *new_color):      # меняет цвет, предварительно проверив на корректность
        if self.__is_valid_color__(new_color):
            self.__color = list(new_color)
        return self.__color

    def get_sides(self):    # возвращает список сторон
        self.__sides = list(self.__sides)
        return self.__sides

    def get_color(self):                  # возвращает список RGB цветов
        self.__color = list(self.__color)
        return self.__color

    def __is_valid_sides__(self, *args):   # проверка: все стороны целые положительные числа и кол-во новых сторон совпадает с текущим классом
        f = True
        if len(args) == self.sides_count:
            for i in range(len(args)):
                if args[i] < 0:
                    f = False
                continue
        else:
            f = False
        return f

    def __len__(self):       # возвращает периметр фигуры
        summ = 0
        if isinstance(self.__sides, int):
            summ = self.__sides
        else:
            for i in self.__sides:
                summ += i
        return summ

    def set_sides(self, *new_sides):  # меняет стороны
        if self.__is_valid_sides__(*new_sides):
            self.__sides = list(new_sides)
        return self.__sides

class Circle(Figure):
    def __init__(self, __color, *__sides, sides_count=1, filled=True):
        super().__init__(__color, __sides, sides_count=1, filled=True)
        self.radius()

    def radius(self): # возвращает радиус круга
         radius = round((self.__len__()/(2*(math.pi))), 3)
         return radius

    def get_square(self): #возвращает площадь круга
        s = round((self.__len__())**2/(4*(math.pi)), 3)
        return s


class Triangle(Figure):
    def __init__(self, __color, *__sides, sides_count=1, filled=True):
        super().__init__(__color, __sides, sides_count=3, filled=True)

    def triangle(self): # проверка на невырожденность треугольника
        sides = self.get_sides()
        f = False
        if ((sides[0]+sides[1]) > sides[2]) and ((sides[0]+sides[2]) > sides[1]) and ((sides[2]+sides[1]) > sides[0]):
            f = True
        return f

    def get_square(self):   #возвращает площадь треугольника
        if self.triangle():
            p = (self.__len__())*0.5
            sides = self.get_sides()
            s = p*(p-sides[0])*(p-sides[1])*(p-sides[2])
            s = round(s**0.5, 3)
        else:
            print('Треугольник является вырожденным, нельзя посчитать площадь')
            s = None
        return s

class Cube(Figure):
    def __init__(self, __color, *__sides, sides_count=1, filled=True):
        super().__init__(__color, __sides, sides_count=12, filled=True)


    def get_volume(self):    #возвращает объем куба
        a = self.get_sides()[0]
        v = round(a**3, 3)
        return v

c1 = Circle((200,15,16),12,12) # стороны переданы не корректно
print('sides', c1.get_sides())
print('S=',c1.get_square())
print('radius', c1.radius())
print('-'*37)

c2 = Cube((200, 200, 100), 10,10)
print(c2.get_sides())
print(c2.get_volume())
print(len(c2))
print('-'*30)

t2 = Triangle(100,10,20,30)
print('sides',t2.get_sides())
print('периметр', len(t2))
print('S=', t2.get_square())
t2.set_sides(3,4,5)
print('S=', t2.get_square())
print('-'*30)


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
#print(cube1.sides())
# print('tr'*27)
# t1 = Triangle((200,15,16),1,2,5)
# print(t1.sides_count)
# print('sides', t1.get_sides())
# print('color', t1.get_color())
# print('s', t1.get_square())
# print('new color',t1.set_color(100,120,200))
# print('new sides', c1.get_sides())
# print('P=', t1.__len__())
# print('new sides',t1.set_sides(3,4,5))
# print('P', t1.__len__())
# print('S=',t1.get_square())
# print('*'*27)

