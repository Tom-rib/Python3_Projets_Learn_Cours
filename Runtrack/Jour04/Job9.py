def moyenne(a,b,c):
    moyenne_etudiant= (a+b+c)/3

    if moyenne_etudiant >= 15:
      print("Très bon élève")
    elif moyenne_etudiant >=11 and moyenne_etudiant<=14:
       print("Bon élève")
    elif moyenne_etudiant >=8 and moyenne_etudiant<= 10:
       print("Eleve moyen")
    elif moyenne_etudiant >=0 and moyenne_etudiant <=7:
       print("Elève devant faire des efforts")
    else:
       print("L'eleve est probablement décédé!")    


a=int(input("Veuillez rentree une première note sur 20: "))
b=int(input("Veuillez rentree une deuxième note sur 20: "))
c=int(input("Veuillez rentree une troisième note sur 20: "))

            
moyenne(a,b,c)
