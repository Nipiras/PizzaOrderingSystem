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
class Margherita(Pizza):
  def __init__(self):
    super().__init__("Pizza Margherita", 6.5)

class QuattroFormaggi(Pizza):
  def __init__(self):
    super().__init__("Quattro Formaggi", 9)

class Capricciosa(Pizza):
  def __init__(self):
    super().__init__("Pizza Capricciosa", 8)

class Calzone(Pizza):
  def __init__(self):
    super().__init__("Calzone Pizza", 8)

# Objects of pizza options(Pizza)
p1 = Margherita()
p2 = QuattroFormaggi()
p3 = Capricciosa()
p4 = Calzone()


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
class Olive(Decorator):
  def __init__(self, component=None):
    super().__init__("Olive", 1.5, component=component)

class Mushroom(Decorator):
  def __init__(self, component=None):
    super().__init__("Mushroom", 1, component=component)

class Mozarella(Decorator):
  def __init__(self, component=None):
    super().__init__("Mozarella", 1, component=component)

class Oregano(Decorator):
  def __init__(self, component=None):
    super().__init__("Oregano", 0.5, component=component)

class SalameNapoli(Decorator):
  def __init__(self, component=None):
    super().__init__("Salame Napoli", 2, component=component)

class Tomato(Decorator):
  def __init__(self, component=None):
    super().__init__("Tomato", 0.5, component=component)

# Objects of pizza ingredient(Decorator)
s11 = Olive()
s12 = Mushroom()
s13 = Mozarella()
s14 = Oregano()
s15 = SalameNapoli()
s16 = Tomato()