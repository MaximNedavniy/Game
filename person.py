class Person:
    defence_value = 100
    attack_value = 1
    health_value = 1

    def __init__(self, name):
        self.name = name
        self.defence_value = self.defence_value
        self.attack_value = self.attack_value
        self.health_value = self.attack_value

    def attack(self):
        pass

    def defence(self):
        pass
