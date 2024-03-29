def jacobi(a, n):
    if n <= 0:
        print("'n' must be a positive integer.")
    if n % 2 == 0:
        print("'n' must be odd.")
    # a %= n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            n_mod_8 = n % 8
            if n_mod_8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    if n == 1:
        return result
    else:
        return 0

a = int(input("Enter a: "))
n = int(input("Enter n: "))

print("(a|n) :", jacobi(a, n))