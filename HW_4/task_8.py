class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Water):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()


class Air:
    def __str__(self) -> str:
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()

        elif isinstance(other, Fire):
            return Lighting()

        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Fire:
    def __str__(self) -> str:
        return 'Огноь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Dirt()

        elif isinstance(other, Air):
            return Lighting()


class Earth:
    def __str__(self) -> str:
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Dirt()


class Storm():
    def __str__(self) -> str:
        return 'Шторм'

class Dust():
    def __str__(self) -> str:
        return 'Пыль'

class Lighting():
    def __str__(self) -> str:
        return 'Молния'


class Vapor():
    def __str__(self) -> str:
        return 'Пар'


class Dirt():
    def __str__(self) -> str:
        return 'Грязь'

class Glass:
    def __str__(self):
        return 'Стекло'

 def __add__(self, other):
     if isinstance(other, Lighting):
            return LightBulb()
     else:
        return None

class LightBulb:
     def __str__(self):
         return 'Лампочка'
