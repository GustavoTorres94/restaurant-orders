from models.dish import Dish
from models.ingredient import Ingredient
from csv import DictReader


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        with open(source_path, "r") as file:
            reader = DictReader(file)
            self._data = list(reader)
            for item in self._data:
                dish_name = item["dish"]
                price = float(item["price"])
                ingredient_name = item["ingredient"]
                recipe_amount = int(item["recipe_amount"])

                dish = next(
                    (d for d in self.dishes if d.name == dish_name), None
                )
                if dish is None:
                    dish = Dish(dish_name, price)
                    self.dishes.add(dish)

                ingredient = next(
                    (i for i in self.dishes if i.name == ingredient_name), None
                )
                if ingredient is None:
                    ingredient = Ingredient(ingredient_name)

                dish.add_ingredient_dependency(ingredient, recipe_amount)
