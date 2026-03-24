Nom = ("trousse")
prix_unitaire = 35
quantité_en_stock = 20


print("Nom du produit:" , Nom )
print("Prix du produit:" , prix_unitaire)
print("Quantités en stock" , quantité_en_stock)
voulu=int(input("Combien de Trousse voulez-vous?"))


stock= quantité_en_stock - voulu


print("Nom du produit:" , Nom )
print("Il reste en stock:" , stock )
nouveau_prix = prix_unitaire * 1.1
print ("Le prix du produit a subi une inflation le nouveau prix est:" , nouveau_prix )
