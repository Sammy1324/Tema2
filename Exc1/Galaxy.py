from Star import Star

class Galaxy(Star):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z)
        self.stars = []
    def str(self):
        return f"Galaxia en coordenadas: {self.x}, {self.y}, {self.z}"
    def mane(self):
        return f"Galaxia: {self.x}, {self.y}, {self.z}"
    def add_star(self, star):
        self.stars.append(star) #kinda, revisar