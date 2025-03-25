try:
    from Galaxy import Galaxy
    from Launcher import distance, create_stars, print_stars, determine_galaxy, calc_distances
except ImportError as e:
    print(f"Error importing modules: {e}")
    exit(1)

if __name__ == "__main__":
    # Crear estrellas y mostrarlas
    stars = create_stars()
    print_stars(stars)

    # Calcular y mostrar distancias entre estrellas
    distances = calc_distances(stars)
    for (star1, star2), d in distances.items():
        print(f"Distancia entre {star1} & {star2}: {d}")

    # Encontrar la estrella más lejana
    if stars:
        concrete_star = stars[0]
        galaxy_name = determine_galaxy(concrete_star)
        print(f"La galaxia que contiene a {concrete_star} es: {galaxy_name}")
    else:
        print("No hay estrellas disponibles para determinar la galaxia.")
    # Crear una galaxia y añadir estrellas
    galaxy = Galaxy()
    
    if stars:
        for star in stars:
            galaxy.add_star(star)
    else:
        print("No hay estrellas para añadir a la galaxia.")
    galaxy_name = determine_galaxy(concrete_star)
    print(f"La galaxia que contiene a {concrete_star} es: {galaxy_name}")

    print(f"Galaxia: {galaxy}")
    print(f"Estrellas en la galaxia: {galaxy.stars}")

    # Mostrar la galaxia de cada estrella
    for star in galaxy.stars:
        print(f"La galaxia de {star} es: {galaxy}")

    # Calcular la distancia entre dos estrellas específicas
    if len(stars) > 1:
        star1 = stars[0]
        star2 = stars[1]
        dist = distance(star1, star2)
        print(f"Distancia entre {star1} y {star2}: {dist}")
