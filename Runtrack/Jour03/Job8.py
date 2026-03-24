a = int(input("entrée une longueur a : "))
b = int(input("entrée une longueur b : "))
c = int(input("entrée une longueur c : "))

triangle = False
# verifier le théorème de l'inégalité triangulaire
if a + b > c and a + c > b and b + c > a:
         triangle = True



# qu'elle type de triangle
if triangle:
  if a == b == c:
          print("Le triangle est Equilatéral.")
  
  elif a == b or a == c or b == c and  a*a + b*b == c*c or a*a + c*c == b*b  or b*b + c*c == a*a:
         print("Le triangle est un triangle Rectangle isocèle")
  elif a == b or a == c or b==c:
         print("Le triangle est Isocèle.")
  
  elif a*a + b*b == c*c or a*a + c*c == b*b  or b*b + c*c == a*a:
         print("Le triangle est un triangle Rectangle.")
  
  elif a + b > c or a + c > b or b + c > a:
         print("Le triangle est un triangle quelconque.")         
else :
        print("Ceci n'est pas un triangle") 

    


