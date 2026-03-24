exclusions = {3 , 6  , 9 , 12 , 18 , 21 , 24 , 27 , 33 , 36 , 39 , 42 , 48 , 51 , 54 , 57 , 63 , 66 , 69 , 72 , 78 , 81 , 84 , 87 , 93 , 96 , 99}
exclusions2 = { 5 , 10 , 20 , 25 , 35 , 40 , 50 , 55 , 65 , 70 , 80 , 85 , 95 , 100}
exclusions3 = { 15 , 30 , 45 , 60 , 75 , 90 }

for i in range(1, 101):
        if i in exclusions :
            print("Fizz")
        elif i in exclusions2 :
            print("Buzz")
        elif i in exclusions3 :
            print("FizzBuzz")
        else:
            print(i)
