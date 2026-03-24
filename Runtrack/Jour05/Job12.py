def liste():
 L = [8,24, 48 , 2, 16]

 for i in range(len(L)): for j in range(i+1, len(L)): if L[i] > L[j]: L[i], L[j] = L[j], L[i]

 print(L)
 print()

 
L = liste()