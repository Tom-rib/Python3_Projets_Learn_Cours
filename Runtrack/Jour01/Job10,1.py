
# initialiser les variable

montant_initial_investissement = 5000
taux_rendement = 1.02

#premier rendement

gain_annuel = montant_initial_investissement * taux_rendement - montant_initial_investissement 

portefeuille1 = montant_initial_investissement + gain_annuel

print(f"le gain annuel est de : , { gain_annuel} €")

# Ajout de capital et augmentation du rendement

taux_rendement= 1.04

nouveau_montant = montant_initial_investissement + 5000

gain_annuel = nouveau_montant * taux_rendement - nouveau_montant 

portefeuille2 = nouveau_montant  + gain_annuel

print(f"le gain annuel est de : , { gain_annuel} €")


# retrait d'une partie de l'investisement et perte de rendement
taux_rendement = 1.03

montant_après_retrait = portefeuille2 - portefeuille2 * 0.1 

gain_annuel = montant_après_retrait * taux_rendement - montant_après_retrait

portefeuille3 = montant_après_retrait + gain_annuel

print(f"le gain annuel est de : , { round(gain_annuel,2)} €")
print(f"Votre portefeuilles est de:, {round(portefeuille3,2)} €")



