class Grass:
    def __init__(self, nutritional_value: int = 4):
        self.nutritional_value = nutritional_value


class Herbivore:
    def __init__(self, hunger_degree: int = -10):
        self.hunger_degree = hunger_degree

    def satisfy_hunger(self, grass: Grass):
        if self.hunger_degree > 0:
            print('Нет, спасибо, я не голодный.')
        else:
            self.hunger_degree += grass.nutritional_value
