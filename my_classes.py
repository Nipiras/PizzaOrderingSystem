# -*- coding: utf-8 -*-

#@title Component Class
# Pizza class
class Pizza:
  def __init__(self, description, cost):
    self.description = description
    self.cost = cost
  
  def get_description(self):
    return self.description

  def get_cost(self):
    return self.cost

# Pizza options(Pizza)
class Klasik(Pizza):
  def __init__(self):
    super().__init__("Klasik Pizza", 140)

class Margarita(Pizza):
  def __init__(self):
    super().__init__("Margarita Pizza", 120)

class TurkPizza(Pizza):
  def __init__(self):
    super().__init__("Türk Pizza", 180)

class SadePizza(Pizza):
  def __init__(self):
    super().__init__("Sade Pizza", 100)

# Objects of pizza options(Pizza)
p1 = Klasik()
p2 = Margarita()
p3 = TurkPizza()
p4 = SadePizza()

#@title Decorator Class
# Decorator(Pizza) class
class Decorator(Pizza):
  def __init__(self, description, cost, component):
    super().__init__(description, cost)
    self.component = component or Pizza("", 0)

  def get_description(self):
    return self.component.get_description() + ' ' + Pizza.get_description(self)

  def get_cost(self):
    return self.component.get_cost() + Pizza.get_cost(self)

# Pizza ingredient(Decorator)
class Zeytin(Decorator):
  def __init__(self, component=None):
    super().__init__("Zeytin", 5, component=component)

class Mantar(Decorator):
  def __init__(self, component=None):
    super().__init__("Mantar", 10, component=component)

class Peynir(Decorator):
  def __init__(self, component=None):
    super().__init__("Keçi Peyniri", 10, component=component)

class Et(Decorator):
  def __init__(self, component=None):
    super().__init__("Et", 20, component=component)

class Sogan(Decorator):
  def __init__(self, component=None):
    super().__init__("Soğan", 5, component=component)

class Misir(Decorator):
  def __init__(self, component=None):
    super().__init__("Mısır", 5, component=component)

# Objects of pizza ingredient(Decorator)
s11 = Zeytin()
s12 = Mantar()
s13 = Peynir()
s14 = Et()
s15 = Sogan()
s16 = Misir()