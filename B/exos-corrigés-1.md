# Devoirs et exercices corrigés - 1

## Exercice 1 : Devoirs
La question était de faire un premier script qui donne une décomposition en facteurs premiers.


```python
def factor(n):
    assert n>0
    Factor = []
    p = 2
    while n>1:
        if n%p == 0:
            n //= p
            Factor.append(p)
            while n%p == 0:
                n //= p
                Factor.append(p)
        p += 1
    return Factor

for n in range(7, 13):
    print(n, "donne", factor(n))

for n in [4953851, 600851475143, 14837457737]:
    print(n, "donne", factor(n))

```

    7 donne [7]
    8 donne [2, 2, 2]
    9 donne [3, 3]
    10 donne [2, 5]
    11 donne [11]
    12 donne [2, 2, 3]
    4953851 donne [7, 7, 17, 19, 313]
    600851475143 donne [71, 839, 1471, 6857]
    14837457737 donne [1471, 1471, 6857]



```python
def factor(n):
    # variante qui sort une liste de couples (p, e)
    assert n>0
    Factor = []
    p = 2
    while n>1:
        if n%p == 0:
            n //= p
            e = 1
            while n%p == 0:
                n //= p
                e += 1
            Factor.append((p, e))
        p += 1
    return Factor

for n in range(7, 13):
    print(n, "donne", factor(n))

for n in [4953851, 600851475143, 14837457737]:
    print(n, "donne", factor(n))

```

    7 donne [(7, 1)]
    8 donne [(2, 3)]
    9 donne [(3, 2)]
    10 donne [(2, 1), (5, 1)]
    11 donne [(11, 1)]
    12 donne [(2, 2), (3, 1)]
    4953851 donne [(7, 2), (17, 1), (19, 1), (313, 1)]
    600851475143 donne [(71, 1), (839, 1), (1471, 1), (6857, 1)]
    14837457737 donne [(1471, 2), (6857, 1)]


Critique du script : dans le pire des cas (quand $n$ est un nombre premier), la boucle <kbd>while</kbd> fait presque $n$ tours ; on dit alors que l'algorithme est en $\mathcal{O}(n)$.

**Devoirs pour la semaine suivante** :
* Modifier ce script pour le rendre en $\mathcal{O}\left(\sqrt{n}\right)$.    
Il doit être rapide pour un nombre comme $n=2\;000\;000\;018$.  
Pour cela, s'inspirer du CM1, et des deux versions incluses de ```is_prime```. Ici, une légère modification suffit !  

* S'inscrire sur https://projecteuler.net/ et résoudre les trois premiers problèmes de l'archive https://projecteuler.net/archives

---
## Exercice 2
Par quel chiffre doit-on remplacer les zéros de $120450$ pour qu'il soit divisible par $99$ ?


```python
for c in range(10):
    n = 120450 + c*1000 + c
    if n%99 == 0:
        print("Le chiffre", c, "convient.")
```

    Le chiffre 3 convient.


On apprendra bientôt comment répondre à cette question sans faire de boucle.

---
## Exercice 3
Les nombres de la forme $2^{2^n}+1$ où $n \in \mathbb{N}$, sont-ils tous premiers ?

[**Les nombres de Fermat**](https://fr.wikipedia.org/wiki/Nombre_de_Fermat)  
Ces nombres doivent leur nom à Pierre de Fermat, qui émit la conjecture que tous ces nombres étaient premiers.


```python
def is_prime(n):
    if n<2: return False
    for d in range(2, n):
        if n%d==0: return False
        if d*d>n: return True
    return True

def F(n):
    return 2**(2**n) + 1

n = 0
while True:
    Fn = F(n)
    if is_prime(Fn):
        print("F"+str(n)+" =", Fn, ", est premier.")
    else:
        print("F"+str(n)+" =", Fn, ", est composé.")
        print("Conjecture fausse.")
        break
    n += 1
```

    F0 = 3 , est premier.
    F1 = 5 , est premier.
    F2 = 17 , est premier.
    F3 = 257 , est premier.
    F4 = 65537 , est premier.
    F5 = 4294967297 , est composé.
    Conjecture fausse.


---
## Exercice 4
Vérifier que pour tout $n \in [\![0..100]\!]$, et $p \in [\![0..50]\!]$ avec $p$ premier, on a : $n^p-n$ est divisible par $p$.


```python
for p in range(51):
    if is_prime(p):
        for n in range(101):
            assert (n**p - n)%p == 0, ("échec", n, p)
print("Succès")
```

    Succès


Nous prouverons que cela est vrai pour tout $n \in \mathbb{N}$, et tout $p \in \mathbb{P}$.

---
## Exercice 5
Quel est le plus petit entier divisible par tous les entiers de $1$ à $15$ ? _Sans script_.  
(Et de $1$ à $150$ ? _Avec script_)


```python
from math import gcd as PGCD
# gcd est dans 'math' à partir de Python3.6,
# avant, il était dans 'fractions'.

def PPCM(a, b): return a // PGCD(a, b) * b

N = int(input())
ans = 1
for n in range(2, N+1):
    ans = PPCM(ans, n)
print(ans)
```

    150
    4963595372164418730243844250278933730416682962970482173955824000


## Exercice 6
$p$, $q$, $r$ sont des nombres premiers distincts.
1. Quelle est la décomposition en facteurs premiers de $(p^5q^7r)\times(p^2q)$ ?
2. Quels sont les diviseurs de $p^5$ ?
3. Quels sont les diviseurs de $p^2q$ ?
4. Quels sont les diviseurs de $pqr$ ?
5. Quel est le PGCD de $pq$ et $qr$ ?

---
**Réponse :**
1. $A = (p^5q^7r)\times(p^2q)$  
$A = (p^5\times p^2)\times(q^7\times q)\times r$  
$A = p^7q^8r$, est décomposé facteurs premiers.

2. Les diviseurs de $p^5$ sont $(1, p, p^2, p^3, p^4, p^5)$, ils sont agencés en une structure unidimensionnelle dont la somme est :  
$S = 1+ p+ p^2+ p^3+ p^4+ p^5 = \dfrac{p^6-1}{p-1}$  
*Remarque :* $5$ est un exposant moyen, plus petit la formule de gauche est très rapide, plus grand la formule de droite devient intéressante.

3. Les diviseurs de $p^2q$ ont une structure bidimensionelle :  
$1, p, p^2,$  
$q, pq, p^2q$  
dont la somme est $S = (1+ p+ p^2) + q(1+ p+ p^2)$  
$S= (1+q)(1+ p+ p^2)$.  
On donnera une formule générale pour la somme.

4. Les diviseurs de $pqr$ se placent au sommet d'un cube : 
$1, p, q, r, pq, pr, qr, pqr$, dont la somme est $(1+p)(1+q)(1+r)$

5. Le PGCD de $pq$ et $qr$ est $q$.
