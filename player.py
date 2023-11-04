from person import Person
class Warrior(Person):
    def __init__(self,name):
        self.defence_value = 100
        self.attack_value= 200
        self.health_value= 200

    def attack(self):
        damage=self.attack_value-self.defence_value
        self.health_value-damage
    def defence(self):
        pass

class Wizzard(Person):
    def __init__(self,name):
        self.defence_value = 100
        self.attack_value= 300
        self.health_value= 300

    def attack(self):
        pass

    def defence(self):
        pass

a=Warrior('Zorro')
print(a.defence_value)