import math
from Star import Star
# Removed unused import

def create_stars():
    stars = []
    starA = Star(2, 3, 1)
    starB = Star(4, 4, 4)
    starC = Star(-3, -1, 0)
    stars.append(starA)
    stars.append(starB)
    stars.append(starC)
    print(stars)
    return stars

def distance(star1, star2):
    x1, y1, z1 = star1.x, star1.y, star1.z
    x2, y2, z2 = star2.x, star2.y, star2.z

    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

def galaxy(star):
    if star.x > 0 and star.y > 0 and star.z > 0:
        return "Galaxy A"
    elif star.x < 0 and star.y < 0 and star.z < 0:
        return "Galaxy B"
    else:
        return "Galaxy C"
    
def farthest_star(stars):
    origin = (0, 0, 0)
    distances = {star: distance(star, Star(x=0, y=0, z=0)) for star in stars}
    farthest_star = max(distances, key=distances.get)
    return farthest_star

def print_stars(stars):
    for star in stars:
        print(star)

def determine_galaxy(stars):
    stars = create_stars()
    for star in stars:
        print(f"Star at ({star.x}, {star.y}, {star.z}) en la {galaxy(star)}")

def calc_distances(stars):
    distances = {}
    for i, star1 in enumerate(stars):
        for star2 in stars[i+1:]:    
            d = distance(star1, star2)
            distances[(star1, star2)] = d
    return distances