nombres = 0
exclusions = {26, 37, 88}

while  nombres <= 99 :
   nombres = nombres + 1
   if nombres not in exclusions :
      print(nombres)
   