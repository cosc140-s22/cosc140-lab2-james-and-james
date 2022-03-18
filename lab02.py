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
        if FoodCategory(category):
            self._category = category
        self._calories = int(calories)
        self._name = name
    
    def name(self):
        return self._name

    def category(self):
        return self._category

    def calories_per_100g(self):
        return self._calories

    def __str__(self):
        return f'{self._name} ({self._category}) {self._calories}cal/100g'
    


class FoodServing(object):
    def __init__(self, FoodItem, amount):
        self._FoodItem = FoodItem
        self._amount = amount
    
    def food(self):
        return self._FoodItem
    
    def amount(self):
        return self._amount
    
    def calories(self):
        return int((( self._amount / 100) * self._FoodItem.calories_per_100g()))
    
    def __str__(self):
        return f'{self._amount}g of {self._FoodItem}'



class Meal(object):
    def __init__(self):
        self.servingsList = []
    
    def addFood(self, FoodServing):
        self.servingsList.append(FoodServing)

    def calories(self):
        sum = 0
        if len(self.servingsList) == 0:
            return 0
        else:
            for serving in self.servingsList:
                sum += serving.calories()
        return sum
    
    def __str__(self) -> str:
        newStr = ""
        for serving in self.servingsList:
            newStr+= (str(serving) + "\n")
        newStr = newStr[:len(newStr)-1]
        return newStr








