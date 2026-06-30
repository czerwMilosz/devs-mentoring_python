import math

class CircleArea:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


print(CircleArea(100).area())
assert True, "asercja testowa"
print(CircleArea(100).area())

assert CircleArea(100).area() == 0, "test"
# zlapac asercje za pomoca try

# co chce zrobic, dac readme
# jak uruchomic projekt
# stosowac git flow
# poczytac o ruff
# pre-commit
#pytest - unit testy

# CO ZROBIC
#feature konfiguracyjny
#skonfigurowac ruff, unittesty
# precommit
# zrobic pull request
# 1 etap projektu, wymagania funkcjonalne