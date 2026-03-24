def liste():
 L = [1, 2, 3, 4, 5]

 print ("l'élement 1:",L[1])
 
 L[2]= L[1]+L[3]

 print(L)

 L[0],L[-1]=L[-1],L[0]
 print(L)

 

L = liste()