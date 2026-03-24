def generer_toit(rang: int) -> str:
    result = ""
    for i in range(rang + 2):
        nb_stars = 2 * i + 1
        spaces = rang + 1 - i
        result += " " * spaces + "/" + "*" * nb_stars + "\\" + "\n"
    return result


def generer_porte(rang: int) -> str:
    result = ""
    nb_pipes = rang + 1
    
    for i in range(rang + 1):
        nb_stars_total = 4 * rang + 5 + 2 * i
        nb_stars_side = (nb_stars_total - nb_pipes) // 2
        spaces = rang + 1 - i
        
        result += " " * spaces + "/" + "*" * nb_stars_side + "|" * nb_pipes + "*" * nb_stars_side + "\\" + "\n"
    
    return result


def pyramide(rang: int) -> str:
    if rang < 0:
        return ""
    if rang == 0:
        return ""
    
    return generer_toit(rang) + generer_porte(rang)


def main() -> None:
    try:
        rang = int(input("Entrez le nombre de rang en un entier possitif de la pyramide : "))
        if rang < 0:
            print("Le rang doit être positif")
            return
        
        result = pyramide(rang)
        print(result)


if __name__ == "__main__":
    main()