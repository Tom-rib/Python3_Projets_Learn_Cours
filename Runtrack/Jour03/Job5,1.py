i=0
is_prime= True


while i<1001:
    for j in range (1,i):
      if i%j == 0:
          print("pas premier")
          is_prime == False
            break  
    
      if is_prime == True :   
           print(i)   

 i=i+1 
 is_prime = False 
    

