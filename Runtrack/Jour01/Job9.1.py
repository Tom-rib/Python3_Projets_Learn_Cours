class Produit:
    def __init__(self, nom, prix_unitaire, quantite_stock):
        self.nom = nom
        self.prix_unitaire = prix_unitaire
        self.quantite_stock = quantite_stock

    def afficher_informations(self):
        print(f"Nom du produit: {self.nom}")
        print(f"Prix unitaire: {self.prix_unitaire:.2f} €")
        print(f"Quantité en stock: {self.quantite_stock}")

    def acheter(self, quantite):
        if quantite > self.quantite_stock:
            print("Quantité demandée supérieure à la quantité en stock.")
        else:
            self.quantite_stock -= quantite
            total = quantite * self.prix_unitaire
            print(f"Achat réussi! Total à payer: {total:.2f} €")
            print(f"Quantité restante en stock: {self.quantite_stock}")

    def appliquer_inflation(self, pourcentage):
        self.prix_unitaire += self.prix_unitaire * (pourcentage / 100)

def main():
    # Création d'un produit
    produit = Produit("T-shirt", 19.99, 50)

    # Affichage des informations du produit
    print("Informations sur le produit avant l'achat:")
    produit.afficher_informations()

    # Demander à l'utilisateur la quantité à acheter
    quantite_a_acheter = int(input("Combien de T-shirts souhaitez-vous acheter? "))

    # Mettre à jour le stock du produit
    produit.acheter(quantite_a_acheter)

    # Appliquer l'inflation de 10%
    produit.appliquer_inflation(10)

    # Afficher les informations mises à jour du produit
    print("\nInformations sur le produit après l'inflation:")
    produit.afficher_informations()

if __name__ == "__main__":
    main()
