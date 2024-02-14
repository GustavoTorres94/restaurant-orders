import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient


def test_dish():
    dish = Dish("Test", 10.0)
    ingredient = Ingredient("Test ingredient")
    assert dish.name == "Test"
    assert dish.price == 10.0
    assert dish.recipe == {}
    assert dish.__repr__() == "Dish('Test', R$10.00)"
    assert dish.__hash__() == hash("Dish('Test', R$10.00)")
    assert dish.__eq__(Dish("Test", 10.0))
    dish.add_ingredient_dependency(ingredient, 1)
    assert dish.recipe == {ingredient: 1}
    ingredient_with_restriction = Ingredient(
        "Test Ingredient With Restriction"
    )
    ingredient_with_restriction.restrictions.add("Test Restriction")
    dish.add_ingredient_dependency(ingredient_with_restriction, 1)
    assert dish.get_restrictions() == {"Test Restriction"}
    dish.get_ingredients()
    assert dish.get_ingredients() == {ingredient, ingredient_with_restriction}
    with pytest.raises(TypeError) as exc_info:
        Dish("Test", "10.0")
    assert str(exc_info.value) == "Dish price must be float."

    with pytest.raises(ValueError) as exc_info:
        Dish("Test", -10.0)
    assert str(exc_info.value) == "Dish price must be greater then zero."
