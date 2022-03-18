from enum import Enum

class FoodCategory(Enum):
    VEGETABLE = 0
    FRUIT = 1
    GRAIN = 2
    PROTEIN = 3
    DAIRY = 4
    OIL = 5
    OTHER = 6

class FoodItem(object):
    def __init__(self, name, category, calories):
        try:
            self.category = FoodCategory(category)
            self.calories = int(calories)
        except:
            print("Invalid!")
        self.name = self
    
    def getName(self):
        return self.name

    def getCategory(self):
        return self.category

    def getCalories(self):
        return self.calories

    def __str__(self):
        return f'{self.name} ({self.category}) {self.calories}cal/100g'
    




class FoodServing(object):
    pass

class Meal(object):
    pass




