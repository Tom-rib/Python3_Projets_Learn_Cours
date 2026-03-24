# Entrée des longueurs
a = int(input("Entrez une longueur a : "))
b = int(input("Entrez une longueur b : "))
c = int(input("Entrez une longueur c : "))

triangle = False

# Vérifier le théorème de l'inégalité triangulaire
if a + b > c or a + c > b or b + c > a:
    triangle = True

# Vérifier le type de triangle
if triangle:
    if a == b == c:
        print("Le triangle est équilatéral.")
    elif a == b or a == c or b == c:
        if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
            print("Le triangle est un triangle rectangle isocèle.")
        else:
            print("Le triangle est isocèle.")
    elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print("Le triangle est un triangle rectangle.")
    else:
        print("Le triangle est un triangle quelconque.")
else:
    print("Ceci n'est pas un triangle.")
