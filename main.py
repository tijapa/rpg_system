class Entity:
    def __init__(self, health_points, strength, dexterity, physical_defense, speed):
        self.health_points = health_points
        self.strength = strength
        self.dexterity = dexterity
        self.physical_defense = physical_defense
        self.speed = speed


class Player(Entity):
    pass


class Enemy(Entity):
    pass
