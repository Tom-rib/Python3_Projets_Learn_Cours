class Produit :
  
  #créé un moule type de produit
  def __init__( self , nom , prix_unitaire , quantités_en_stock ) :
    self.nom = nom
    self.prix_unitaire = prix_unitaire
    self.quantités_en_stock = quantités_en_stock
  

  # Faire un fonction d'affichage
   def affichage_information(self) :
      print(f"nom du produit:  {self.nom}")
      print(f"le prix est de: {self.prix_unitaire}€")
      print(self.quantités_en_stock)


  # faire un fonction d'acheteur 
    
   def acheteur ( self , quantités ) :
     if quantités > self.quantités_en_stock :
        print("La quantité est supérieur a celle en stock.")
     else:
          self.quantités_en_stock -=  quantités 
          total = self.prix_unitaire * quantités
          print("Achat réussi Total a payer: {total:.2f} €")
          print(self.quantités_en_stock)

          
    



# programme

print(nom) 
print ("prix unitaire=" , prix_unitaire)
print("quantités en stock=", quantités_en_stock)

# Nouvelle quantités après une achat

print(nom) 
print ("prix unitaire=" , prix_unitaire)
Print(Newquantités_en_stock)




