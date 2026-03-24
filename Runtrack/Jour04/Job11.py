def time_to_text(minute):
    heures = minute // 60  
    minutes = minute % 60   
    print(heures, "heures", minutes, "minutes")


minute = int(input("Veuillez entrer un nombre de minutes: "))
time_to_text(minute)  
