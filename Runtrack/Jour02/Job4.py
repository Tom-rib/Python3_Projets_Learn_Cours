N = int(input("Entre un nombre :"))
tour = 0
for i in range(N):
   tour += 1
   print( )
   print("Table de multiplication de", i+1)
   for i in range(11):
      print(tour, "x", i, "=", tour*i)