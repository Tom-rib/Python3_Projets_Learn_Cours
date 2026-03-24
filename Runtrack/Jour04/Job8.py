def saisonnier(type,saison):
    if type == "fruits" and saison=="hiver":
      print("orange, mandarine et kiwi")
    elif type == "fruits" and saison=="été" :
       print("Poire,fraise,cassis")
    elif type=="légume" and saison=="légume":
       print("carotte,topinambour,endive")    
    elif type=="légume" and saison=="été":
        print("artichaut,aubergine,navet")   
    else:
       print("Pas de fruits, ni de légume de saison")

type_input=input("entre un type fruits ou legumes")
saison_input=input("entre une saison")
saisonnier(type_input,saison_input)