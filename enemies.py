from person import Person


class Skeleton(Person):
    def __int__(self):
        self.health_value = 80
        self.attack_value = 20
        self.defence_value = 1

    def attack(self):
        return self.attack_value

    def defence(self):
        return self.defence_value


class Zombie(Person):

    def __int__(self):
        self.health_value = 150
        self.defence_value = 60
        self.attack_value = 50

    def attack(self):
        self.attack_value -= 5
        return self.attack_value

    def defence(self):
        self.defence_value -= 7
        return self.defence_value
