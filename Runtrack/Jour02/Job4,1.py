def afficher_tables_multiplication(n):
    for i in range(1, n + 1):
        print(f"\nTable de {i}:")
        for j in range(1, 11):  # Affiche les multiplications de 1 à 10
            print(f"{i} x {j} = {i * j}")

def main():
    # Demander à l'utilisateur de saisir un entier supérieur à zéro
    while True:
        try:
            N = int(input("Veuillez saisir un entier supérieur à zéro (N): "))
            if N > 0 :
                break
            else:
                print("Veuillez entrer un nombre supérieur à zéro.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un entier.")

    afficher_tables_multiplication(N)

if __name__ == "__main__":
    main()
