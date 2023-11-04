from person import Person


class Skeleton(Person):
    def __int__(self, name):
        self.health_value = 80
        self.attack_value = 20
        self.defence_value = 1
    def attack(self):
        self.attack_value = 20
        return self.attack_value

    def defence(self):
        if Warrior.attack and self.attack():
            self.health_value =
        pass

