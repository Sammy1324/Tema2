class Star:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    def mane(self):
        return f"Estrella: {self.x}, {self.y}, {self.z}"