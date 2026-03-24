def is_prime(n):
    """Vérifie si un nombre est premier."""
    if n <= 1:
        return False
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_up_to(limit):
    """Affiche tous les nombres premiers jusqu'à une limite donnée."""
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num)

# Appel de la fonction pour afficher les nombres premiers jusqu'à 100
print_primes_up_to(1000)
