def calcule(num1,operator, num2):

    result = 0
    if operator == "*" :
        result = num1*num2
        return result
    
    elif operator == "+" :
        result = num1+num2
        return result
    
    elif operator == "-" :
        result = num1-num2
        return result
    
    elif operator == "/" :
        result = num1/num2 
        return result
    
    elif operator == "%" :
        result = num1%num2
        return result
    
    else :
        print("Impossible ?")


