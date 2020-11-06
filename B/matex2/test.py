def mystère(n, b):
    for d in range(2, b):
        if n%d == 0:
            return False
    return True

for p in range(2, 1000):
    if mystère(p, p) and mystère(p+2, 20) and (not mystère(p+2, p+2)):
        print(p, p+2, "pas le 2")
    if mystère(p, 20) and mystère(p+2, p+2) and (not mystère(p, p)):
        print(p, p+2, "pas le 1")
        
