Mathématiques expertes, Terminales, Lycée Lucie Aubrac
# Devoir surveillé n°2

Calculatrice autorisée, durée 50 minutes.

## Ex 1 : Nombres premiers jumeaux (3 pts)
Nombres premiers jumeaux
: On dit que $p$ et $p'$ sont des nombres premiers jumeaux, si $p$ et $p'$ sont des nombres premiers et $p' = p+2$. Par exemple $5$ et $7$ sont des nombres premiers jumeaux.

1. Donner la liste des couples de nombres premiers jumeaux $(p, p')$ avec $p < 30$.
2. $(101, 103)$ est-il un couple de nombres premiers jumeaux ?
3. $(839, 841)$ est-il un couple de nombres premiers jumeaux ?


## Ex2 : Je sais travailler avec des fractions (8 pts)
Calculer et donner le résultat sous forme d'une fraction irréductible. Il faut donner toutes les étapes de calcul, et justifier que votre réponse est bien irréductible.
Pour la présentation, on ne mettra qu'un seul signe égal à chaque ligne, et on répétera la lettre juste avant à chaque fois.

**Indices** :
* Pour le $A$, penser à la décomposition en facteurs premiers des dénominateurs.
* Pour le $B$ penser au $\text{PGCD}$ des dénominateurs.
* Pour le $C$, la calculatrice est inutile.
* Pour le $D$, bien justifier que votre résultat est irréductible.

$$A = \frac{2}{323} + \frac{13}{323} \times \frac{5}{91}$$

$$B = \frac 1 {11009} - \frac 1 {11227}$$

$$C = \frac{2^3×3^5×7}{11^2×13^5}×\frac{13^2×17^2}{2^2×7^3×11}$$

$$D = \frac 1 p - \frac 1 {p'}\text{ , où } p < p' \text{ sont des nombres premiers jumeaux.}$$

# Ex 3 : Je sais faire des démonstrations (4 pts)
Pour chaque proposition, si elle est vraie donner une démonstration, si elle est fausse donner un contre-exemple.

**Proposition 1**
: Si $p$ est un nombre premier, alors $p+1$ n'est pas un nombre premier.

**Proposition 2**
: Avec $a, b, c$ trois entiers relatifs, si $a\mid c$ et $b \mid c$, alors $ab \mid c$.

**Proposition 3**
: Avec $a, b, c$ trois entiers relatifs, si $a\mid c$ et $b \mid c$, alors $ab \mid c^2$.

**Proposition 4**
: Avec $a, b, c$ trois entiers relatifs, si $a\mid c$ et $a \mid b$, alors $a \mid b + bc + c$.

# Ex 4 : Je sais lire un script Python simple (2 pts)

Que fait le script suivant ? *On cherchera d'abord ce que fait la fonction `mystère`, puis comment elle est utilisée.*


```python
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
```


# Ex 5 : *Prime or not prime?* (3 pts)

1. On sait que $10\,403$ n'est divisible par aucun nombre premier inférieur à $100$.
$10\,403$ est-il premier ?

2. On sait que $39\,989$ n'est divisible par aucun nombre premier inférieur à $200$.
$39\,989$ est-il premier ?

3. $p>3$, et $(p, p+2)$ sont des nombres premiers jumeaux.
$p+4$ est-il un nombre premier ? (On pourra tester les trois cas de $p$ modulo $3$.)