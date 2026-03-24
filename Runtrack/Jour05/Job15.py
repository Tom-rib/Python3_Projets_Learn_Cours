def liste():
 

 L = [22.4, 4.0, 16.22,9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
 
 for i in range(len(L)): L[i] = int(L[i] + 0.5); for i in range(len(L)): for j in range(i+1, len(L)): if L[i] > L[j]: L[i], L[j] = L[j], L[i]
 print(L)

 
L = liste()