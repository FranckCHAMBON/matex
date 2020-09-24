# Exercices corrigés - 1

## Exercice 1
Par quel chiffre doit-on remplacer les zéros de $120450$ pour qu'il soit divisible par $99$ ?

**Réponse** :

Pour le chiffre $c$, $12c45c = 120450 + 1000c + c$. On teste les 10 chiffres...

```python
for c in range(10):
    n = 120450 + c*1000 + c
    if n % 99 == 0:
        print("Le chiffre", c, "convient.")
```

    Le chiffre 3 convient.

> On apprendra bientôt comment répondre à cette question sans faire de boucle.

---
## Exercice 2
Les nombres de la forme $F_n = 2^{2^n}+1$ où $n \in \mathbb{N}$, sont-ils tous premiers ?

**Réponse** :

Premiers exemples :
* $F_0 = 2^{2^0}+1 = 2^1+1 = 3$, est premier.
* $F_1 = 2^{2^1}+1 = 2^2+1 = 5$, est premier.
* $F_2 = 2^{2^2}+1 = 2^4+1 = 17$, est premier.
* $F_3 = 2^{2^3}+1 = 2^8+1 = 257$, est premier.

Pour vérifier que $257$ est premier, avec notre méthode, on utilise $\sqrt{257}\approx 16$ divisions. Une amélioration serait juste de vérifier que $257$ n'est divisible par aucun nombre premier inférieur ou égal à $16$, à savoir : $[2, 3, 5, 7, 11, 13]$ ; ainsi en $6$ divisions on peut prouver que $257$ est premier.

* $F_4 = 2^{2^4}+1 = 2^{16}+1 = 65\,537$, est premier.

Pour vérifier que $65\,537$ est premier, avec notre méthode, on utilise $\sqrt{65\,357}\approx 256$ divisions. Une amélioration serait juste de vérifier que $65\,537$ n'est divisible par aucun nombre premier inférieur ou égal à $256$, à savoir une liste de $54$ nombres $[2, 3, 5, 7, ..., 239, 241, 251]$. Ce qui peut se faire sans calculatrice, et a été prouvé par Pierre de Fermat.



$F_n$ : [**Les nombres de Fermat**](https://fr.wikipedia.org/wiki/Nombre_de_Fermat)  
Ces nombres doivent leur nom à Pierre de Fermat, qui émit la conjecture en 1640 que tous ces nombres étaient premiers.

* $F_5 = 2^{2^5}+1 = 2^{32}+1 = 4\,294\,967\,297$. Ce nombre n'est divisible par aucun nombre premier inférieurs à $256$ ; cependant il faudrait tester jusqu'à $65\,536$ pour prouver sa primalité avec notre méthode. En 1732, Euler utilise une autre méthode et trouve que $641$ est un facteur de $F_5$.

Aujourd'hui l'outil informatique permet une réponse rapide :

```python
def is_prime(n):
    """ Test de primalité
    Version améliorée ; O(√(n))
    """
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
        if d * d > n:
            return True
    return True

def F(n):
    """Renvoie le nombre de Fermat F_n"""
    return 2**(2**n) + 1

def vérifie_conjecture():
    """Vérifie la primalité des nombres de Fermat.
    S'arrête au premier nombre composé."""
    n = 0
    while True:
        Fn = F(n) # le nième nombre de Fermat
        if is_prime(Fn):
            print("F"+str(n)+" =", Fn, ", est premier.")
        else:
            print("F"+str(n)+" =", Fn, ", est composé.")
            print("Conjecture fausse.")
            return
        n = n + 1


>>> vérifie_conjecture()
```

    F0 = 3 , est premier.
    F1 = 5 , est premier.
    F2 = 17 , est premier.
    F3 = 257 , est premier.
    F4 = 65537 , est premier.
    F5 = 4294967297 , est composé.
    Conjecture fausse.

```python
def plus_petit_diviseur_premier(n):
    """Renvoie le plus petit diviseur premier de n > 1"""
    assert n > 1
    for d in range(2, n+1):
        if n % d == 0:
            return d

>>> plus_petit_diviseur_premier(F(5))
```

    641


---
## Exercice 3
Vérifier que pour tout $n \in [\![0..100]\!]$, et $p \in [\![0..50]\!]$ avec $p$ premier, on a : $n^p-n$ est divisible par $p$.

**Réponse** :

On va faire une double boucle qui fait le test demandé pour chaque cas :

```python
nb_échec = 0
for p in range(51):
    if is_prime(p):
        for n in range(101):
            if (n**p - n)%p != 0:
                nb_échec = nb_échec + 1
print(nb_échec, "échecs")
```

    0 échecs


Nous prouverons bientôt que cela est vrai pour tout $n \in \mathbb{N}$, et tout $p \in \mathbb{P}$.

---
## Exercice 4
Quel est le plus petit entier divisible par tous les entiers de $1$ à $15$ ? _Sans script_.  

**Réponse** :
Donnons la décomposition en facteurs premiers de chaque entier entre $2$ et $15$.
* $2 = 2$
* $3 = 3$
* $4 = 2^2$
* $5 = 5$
* $6 = 2×3$
* $7 = 7$
* $8 = 2^3$
* $9 = 3^2$
* $10 = 2×5$
* $11 = 11$
* $12 = 2^2×3$
* $13 = 13$
* $14 = 2×7$
* $15 = 3×5$

Le plus petit commun multiple s'obtient en trouvant le maximum des exposants associés à chaque nombre premier. On obtient :

$$m = 2^3×3^2×5×7×11×13 = 360\,360$$

---

## Exercice 5
$p$, $q$, $r$ sont des nombres premiers distincts.
1. Quelle est la décomposition en facteurs premiers de $(p^5q^7r)\times(p^2q)$ ?
2. Quels sont les diviseurs de $p^5$ ?
3. Quels sont les diviseurs de $p^2q$ ?
4. Quels sont les diviseurs de $pqr$ ?
5. Quel est le PGCD de $pq$ et $qr$ ?


**Réponse :**
1. $A = (p^5q^7r)\times(p^2q)$  
$A = (p^5\times p^2)\times(q^7\times q)\times r$  
$A = p^7q^8r$, est décomposé en facteurs premiers.

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


## Exercice 6 : Décomposition en facteurs premiers
La question est de faire un premier script qui donne une décomposition en facteurs premiers.


```python
def factor(n):
    """Renvoie une liste, la décomposition en facteurs premiers de n.
    >>> factor(6)
    [2, 3]
    >>> factor(8)
    [2, 2, 2]
    """
    assert n > 0
    Factor = []
    p = 2
    while n > 1:
        if n % p == 0:
            n //= p
            Factor.append(p)
            while n % p == 0:
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
    assert n > 0
    Factor = []
    p = 2
    while n > 1:
        if n % p == 0:
            n //= p
            e = 1
            while n % p == 0:
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

>**Devoirs pour la semaine suivante, pour les NSI+MATEX** :
>> Modifier ce script pour le rendre en $\mathcal{O}\left(\sqrt{n}\right)$.    
Il doit être rapide pour un nombre comme $n=2\;000\;000\;018$.  
Pour cela, s'inspirer du cours, et des deux versions incluses de ```is_prime```. Ici, une légère modification suffit !  

