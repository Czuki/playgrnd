import random

class Robot:
    names_taken = []

    def reset(self):
        self.name = ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 2) + random.sample('0123456789', 3))
        while self.name in self.names_taken:
            self.name = ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 2) + random.sample('0123456789', 3))
        self.names_taken.append(self.name)

    def __init__(self):
        Robot.reset(self)
