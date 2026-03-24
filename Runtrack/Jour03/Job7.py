chaine = "abcdefghijklmnopqrstuvwxyz" * 10
index = 0
n = 1  # Nombre de caractères à afficher sur la ligne

while index + n <= len(chaine):
    print(chaine[index:index + n]) 
    index += n
    n += 2
       