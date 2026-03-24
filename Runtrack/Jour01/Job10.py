class Investissement:
    def __initself , montant_initial, taux_rendement:
        self.montant_initial = montant_initial
        self.taux_rendement = taux_rendement

    def calculer_gain_annuel(self):
        return self.montant_initial * (self.taux_rendement / 100)

    def ajouter_capital(self, montant_ajoute, nouveau_taux):
        self.montant_initial += montant_ajoute
        self.taux_rendement += nouveau_taux

    def retirer_capital(self, pourcentage_retrait, diminution_rendement):
        retrait = self.montant_initial * (pourcentage_retrait / 100)
        self.montant_initial -= retrait
        self.taux_rendement -= diminution_rendement
        
def main():
    # Initialisation des variables
    montant_initial = 10000  # Montant initial de l'investissement
    taux_rendement = 5  # Taux de rendement annuel en pourcentage

    # Création d'une instance de Investissement
    investissement = Investissement(montant_initial, taux_rendement)

    # Affichez le gain annuel initial
    gain_annuel = investissement.calculer_gainuel()
    print(f"Gain annuel initial: {gain_annuel:.2f} €")

    # L'investisseur augmente son capital de 5000 euros et le taux augmente de 2%
    investissement.ajouter_capital(5000, 2)
    gain_annuel = investissement.calculer_gain_annuel()
    print(f"Gain annuel après ajout de capital: {gain_annuel:.2f} €")

    # L'investisseur retire 10% du montant total et le diminue de 1%
    investissement.retirer_capital(10, 1)
    gain_annuel = investissement.calculer_gain_annuel()
   (f"Gain annuel après retrait et diminution du rendement: {gain_annuel:.2f} €")

if __name__ == "__main__":
    main()
