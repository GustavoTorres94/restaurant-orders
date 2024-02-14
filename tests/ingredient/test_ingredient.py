from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


def test_ingredient():
    ingredient = Ingredient("Tomato")
    assert ingredient.name == "Tomato"
    assert ingredient.__str__() == "Tomato"
    assert ingredient.__repr__() == "Tomato"
    assert ingredient.restrictions == set()
    assert ingredient.__hash__() == hash("Tomato")
    assert ingredient.__eq__("Tomato") is True
    assert ingredient.__eq__("Onion") is False
    assert ingredient.__eq__(Ingredient("Tomato")) is True
    assert ingredient.__eq__(Ingredient("Onion")) is False
