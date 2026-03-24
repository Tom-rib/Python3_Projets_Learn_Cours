def fonction(langage):
    langage = langage.lower()

    if langage=="javaScript":
         print("tu es un développeur web")

    elif langage=="python":
         print("tu es un développeur IA")

    elif langage=="java":  
        print("tu es un développeur logiciel")

    elif langage=="reactjs":
         print("tu es un développeur mobile")
    else :
        print ("langage non reconnu")      



langage_input = input("Ecrivé votre langage: ")
fonction(langage_input)