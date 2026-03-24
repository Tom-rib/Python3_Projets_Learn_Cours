# 1. tests basiques d'égalité et de comparaison :

1 == 1            # => True
2 == 1            # => False  
2 != 5            # => True
6 < 9             # => True
5 >= 5            # => True
32 % 2 == 1       # => False
33 % 3 > 0        # => False
7 < 9 < 15        # => True
85 < 32 < 127     # => False
"abc" == "abc"    # => True
"abc" == "abd"    # => False
"2" == "2"        # => True 

# 2. tests avec des variables de type distinct :

2 == "2"                                # False
3 == 3.0                                # True
5 == 5.1                                # False
6 == False                              # False
"2" == "2.0"                            # False
3 + 0.000000000001 == 3                 # False
3 + 0.00000000000000001 == 3            # True
True != "True"                          # False
True == 1                               # True  
True != 2                               # True


# 3. tests entre littéraux booléens (True et False) :

True == True                    # True
False == False                  # True
False == True                   # False
False != True                   # True


# 4. expressions avec opérateurs not, and et or :
not True                    # False
not False                   # True
True and True               # True
False and False             # False
False or False              # False
True and not False          # True
False != (not False)        # True
False or True               # True

1 == 1 and 2 == 1           # False
not "test" == "test"        # False
2 == 1 or 2 != 1            # True


# 5. expressions avec l'opérateur booléen `in`
1 in [1, 2, 3, 4]            # True
1 in [2, 3, 4, 5]            # False
2.0 in [1, 2, 3]             # True
"n" in "anne"                # True
"test" == "testing"          # False
"test" in "testing"          # True
"testing" in "test"          # False 


# 6. tests avec des variables booléennes
A = True             
B = False

B or A                          # => True
B and A                         # => False
A and 1 == 1                    # => True
B or 0 != 1                     # => True
A or 1 == 2                     # => True
(A and B) or ((not B) and A)    # => True

# Faites une table de vérité de l'expression précédente : de quelle variable
# dépend-elle ? Comment pourrait-on la réécrire ?


