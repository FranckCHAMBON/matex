def is_prime(n):
    if n<2: return False
    for d in range(2, n):
        if n%d==0: return False
        if d*d>n: return True
    return True

ans = 0
for n in range(2, 256):
    if is_prime(n):
        ans += 1
        print(n)

print(ans)
