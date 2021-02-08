class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth = 31557600
        self.mercury = self.earth * 0.2408467
        self.venus = self.earth * 0.61519726
        self.mars = self.earth * 1.8808158
        self.jupiter = self.earth * 11.862615
        self.saturn = self.earth * 29.447498
        self.uranus = self.earth * 84.016846
        self.neptune = self.earth * 164.79132

    def on_earth(self):
        return round(self.seconds / self.earth, 2)


    def on_mercury(self):
        return round(self.seconds / self.mercury, 2)

    def on_venus(self):
        return round(self.seconds / self.venus, 2)

    def on_mars(self):
        return round(self.seconds / self.mars, 2)

    def on_jupiter(self):
        return round(self.seconds / self.jupiter, 2)

    def on_saturn(self):
        return round(self.seconds / self.saturn, 2)

    def on_uranus(self):
        return round(self.seconds / self.uranus, 2)

    def on_neptune(self):
        return round(self.seconds / self.neptune, 2)

print(SpaceAge(1210123456).on_uranus())

print(SpaceAge(1821023456).on_neptune())
print(SpaceAge(1000000000).on_earth())

print(SpaceAge(2134835688).on_mercury())
