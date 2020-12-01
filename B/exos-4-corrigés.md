> _La mathématique est l'art de donner le même nom à des choses différentes._  
> **Poincaré**


# Exercices NSI & Maths expertes $-$ Algorithme d'Euclide

> Avec corrigé

>**Rappels de cours** :  
> * $\text{PGCD}(a, 0) = a$, pour $a \geqslant 0$  
> * Si $a = bq+r$, alors $\text{PGCD}(a, b) = \text{PGCD}(b, r)$

>**Exemple** : On souhaite calculer $\text{PGCD}(323, 187)$.  
> $\text{divmod}(323, 187) = (1, 136)$ ; _On continue avec $187$ et $136$_.  
> $\text{divmod}(187, 136) = (1, 51)$ ; _On continue avec $136$ et $51$_.  
> $\text{divmod}(136, 51) = (2, 34)$ ; _On continue avec $51$ et $34$_.  
> $\text{divmod}(51, 34) = (1, 17)$ ; _On continue avec $34$ et $17$_.  
> $\text{divmod}(34, 17) = (2, 0)$ ; _Le reste est nul, le dernier diviseur est $17$_.  
> D'après l'algorithme d'Euclide, $\text{PGCD}(323, 187) = 17$.

---

## Exercice 1
1. Vérifier que $\text{PGCD}(6699, 5313) = 231$. _Deux méthodes sont demandées : avec décomposition en facteurs premiers, ou sinon utiliser l'algorithme d'Euclide._

2. Faire un script qui définit une fonction <kbd>PGCD(a, b)</kbd>.

3. Calculer $\text{PGCD}(63245986, 102334155)$.  
_Quelle remarque peut-on faire pendant le calcul ?_

---

> Une réponse

1. Plusieurs méthodes
    1. Avec décomposition en facteurs premiers  
$6699 = 3\times7\times11\times29$  
$5313 = 3\times7\times11\times23$  
Ainsi $\text{PGCD}(6699, 5313) = 3\times7\times11 = 231$

    2. Avec l'algorithme d'Euclide :  
$\text{divmod}(6699, 5313) = (1, 1386)$ ; _On continue avec $5313$ et $1386$_.  
$\text{divmod}(5313, 1386) = (3, 1155)$ ; _On continue avec $1386$ et $1155$_.  
$\text{divmod}(1386, 1155) = (1, 231)$ ; _On continue avec $1155$ et $231$_.  
$\text{divmod}(1155, 231) = (5, 0)$ ; _Le reste est nul, le dernier diviseur est $231$_.  
Ainsi $\text{PGCD}(6699, 5313) = 231$

2. Voir ci-dessous plusieurs variantes.

3. Les nombres choisis sont des termes consécutifs de la suite de Fibonacci, dans ce cas, les quotients sont toujours égaux à $1$, et le $\text{PGCD}$ est aussi égal à $1$. C'est le pire des cas pour l'algorithme d'Euclide, il est plus rapide pour tous nombres inférieurs.

```python
a, b = 6699, 5313
while b != 0:
    q, r = divmod(a, b)
    print(a, "/", b, "-> quotient :", q, ", reste :", r)
    a, b = b, r

print("PGCD =", a)
```

```
6699 / 5313 -> quotient : 1 , reste : 1386
5313 / 1386 -> quotient : 3 , reste : 1155
1386 / 1155 -> quotient : 1 , reste : 231
1155 / 231 -> quotient : 5 , reste : 0
PGCD = 231
```

```python
# variante minimaliste
a, b = 6699, 5313
while b != 0:
    a, b = b, a%b
print(a)

# variante avec une fonction récursive
def gcd(a: int, b: int) -> int:
    """Renvoie le PGCD de a et b.
    >>> gcd(15, 35)
    5
    >>> gcd(18, 77)
    1
    """
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a%b)

# Variante avec une fonction non récursive
def gcd(a: int, b: int) -> int:
    """Renvoie le PGCD de a et b.
    >>> gcd(15, 35)
    5
    >>> gcd(18, 77)
    1
    """
    while b != 0:
        a, b = b, a%b
    return abs(a)
# on profite ici de l'affectation simultanée ; possible en Python


# variante fainéant
from math import gcd
gcd(6699, 5313)

# attention `gcd` est dans le module `math` depuis Python3.6
# avant, `gcd` était dans le module `fractions`
```



## Exercice 2
Sachant que l'on a $96842 = 256\times 375 + 842$, déterminer avec le moins de calculs possibles les restes et quotients des divisions euclidiennes de $96842$ par $256$ et par $375$.

---
*Une réponse*
 * $842 = 3\times 256 + 74$, donc $96842 = 256\times375 + 3\times 256 + 74 = 378\times 256 + 74$, et ainsi :  
$96842$ divisé par $256$ donne un quotient de $378$ et un reste de $74$.

 * $842 = 2\times 375 + 92$, donc $96842 = 256\times375 + 2\times 375 + 92 = 258\times 375 + 92$, et ainsi :  
$96842$ divisé par $256$ donne un quotient de $258$ et un reste de $92$.



---

## Exercice 3
1. Faire un script qui calcule la somme $\frac{a}{b}+\frac{c}{d}$ et donne la réponse sous forme d'une fraction irréductible. (Contrainte : $a$, $b$, $c$, $d$ sont entiers, et $b\neq 0$, $d\neq 0$.)
2. Faire une version qui affiche les étapes intermédiaires comme dans l'exemple :

$A = \dfrac{1}{20}+\dfrac{-1}{28}$

$A = \dfrac{1}{4\times 5}+\dfrac{-1}{4\times 7}$

$A = \dfrac{1\times 7}{4\times 5 \times 7}+\dfrac{-1 \times 5}{4\times 7 \times 5}$

$A = \dfrac{7+(-5)}{4\times 5 \times 7}$

$A = \dfrac{2\times 1}{2\times 2\times 5 \times 7}$

$A = \dfrac{1}{2\times 5 \times 7}$

$A = \dfrac{1}{70}$  

---

> Une réponse

```python
from math import gcd
def ajoute_fractions(a, b, c, d):
    """Ajoute (détaille et simplifie) les fractions a/b et c/d"""
    assert b != 0 and d != 0, ("Dénominateur(s) nul(s) !", b, d)

    print(f"A = {a}/{b} + {c}/{d}")
    
    # peut-on simplifier les fractions dès le départ ?
    k1 = gcd(a, b); k2 = gcd(c, d)
    if k1>1 or k2>1:
        a //= k1; b //= k1
        c //= k2; d //= k2
        print(f"A = {a}/{b} + {c}/{d}")
    
    # on trouve alors le ppcm des dénominateurs
    k = gcd(b, d)
    if k == 1:
        # méthode brutale
        print("Les dénominateurs sont premiers entre eux.")
        print(f"A = ({a}*{d})/({b}*{d}) + ({c}*{b})/({d}*{b})")
        a, b, c, d = a*d, b*d, c*b, d*b
    else:
        # méthode élaborée
        print(f"{k} est un diviseur commun aux dénominateurs.")
        b //= k ; d //= k
        print(f"A = {a}/({b}*{k}) + {c}/({d}*{k})")
        print(f"A = ({a}*{d})/({b}*{k}*{d}) + ({c}*{b})/({d}*{k}*{b})")
        a, b, c, d = a*d, b*k*d, c*b, d*k*b

    assert b == d
    # nos dénominateurs sont bien égaux
    print(f"A = {a}/{b} + {c}/{b}")
    print(f"A = ({a}+{c})/{b}")
    a += c
    print(f"A = {a}/{b}")
    k = gcd(a, b)
    if k>1:
        print(f"On peut encore simplifier par {k}.")
        a //= k ; b //= k
        print(f"A = {a}/{b}")
    print("Le résultat est une fraction irréductible !")
    
    # TODO1 : faire uen version POO.
    # TODO2 : faire une version qui sort du code LaTeX !!!


# exemples
ajoute_fractions(1,2, 1,3)
ajoute_fractions(1,20, -1,28)
```

```
A = 1/2 + 1/3
Les dénominateurs sont premiers entre eux.
A = (1*3)/(2*3) + (1*2)/(3*2)
A = 3/6 + 2/6
A = (3+2)/6
A = 5/6
Le résultat est une fraction irréductible !

A = 1/20 + -1/28
4 est un diviseur commun aux dénominateurs.
A = 1/(5*4) + -1/(7*4)
A = (1*7)/(5*4*7) + (-1*5)/(7*4*5)
A = 7/140 + -5/140
A = (7+-5)/140
A = 2/140
On peut encore simplifier par 2.
A = 1/70
Le résultat est une fraction irréductible !
```