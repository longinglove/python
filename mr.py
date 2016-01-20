def str_handle(L):
    return L[0].upper()+L[1:].lower()

def is_odd(n):
    return n%2 == 1

def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return True 
    return False
N = [1,2,3,4,5,6,7,8,9,10]
L = ['adam', 'LISA', 'barT']
print map(str_handle, L)
print filter(is_odd, N)
print filter(is_prime, range(2, 101))
