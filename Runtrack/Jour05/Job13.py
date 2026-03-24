def liste():
 

 L =[10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
 
 L = [x for i, x in enumerate(L) if x not in L[:i]]
 print(L)

 
L = liste()