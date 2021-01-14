# Théorème de Bachet-Bezout

## Théorème

Avec $a$ et $b$ dans $\mathbb Z$, et $d = \text{PGCD}(a, b)$, on a:
* $d$ peut s'écrire comme combinaison linéaire de $a$ et $b$.

## Exemples

### Exemple 1

1. Montrer que le $\text{PGCD}(26, 39)$ est $13$.

2. Montrer qu'il existe $i$ et $j$ entiers relatifs tels que
* $26i + 39j = 13$

---

> Réponse

1. $26 = 2\times 13$, et $39 = 3 \times 13$, donc $\text{PGCD}(26, 39)=13$.
2. Avec $i=-1$ et $j=1$, on a ce qui est demandé.

### Exemple 2

Montrer qu'il existe $i$ et $j$ entiers relatifs tels que
* $13i + 17j = 1$

---

> Réponse

$i=4$ et $j=-3$ conviennent.

### Exemple 3

> Rappel, avec $a \in \mathbb Z$, on a : $\text{PGCD}(a, 0) = a$.

Démontrer le théorème de Bachet-Bezout dans le cas particulier où $b = 0$.

---

> Réponse

On a :
$$1\times a + 0\times 0 = a$$

### Exemple 4

On regarde la dernière étape de l'algorithme d'Euclide.

$\text{divmod}(a, b) = (q, 0)$, et $b$ est le $\text{PGCD}(a, b)$.

Montrer qu'il existe $i$ et $j$ tels que
$$a\times i + b\times j = b$$

---

> Réponse

$i=0$ et $j = 1$ conviennent.

### Exemple 5

* On sait que $13\times 4 + 17\times(-3) = 1$

* Trouver une combinaison linéaire de $17$ et $47$ égale à $1$.
 Indice : $\text{divmod}(47, 17) = (2, 13)$, ainsi $47 = 2\times 17 + 13$

---

> Réponse

On a $1\times 47 + (-2)\times 17 = 13$

On multiplie cette ligne par $4$.

On a $4\times 1\times 47 + 4\times (-2)\times 17 = 4\times 13$

On déduit

$4\times 1\times 47 + 4\times (-2)\times 17 = 1 - 17\times(-3)$

Ainsi

$4\times 47 -8\times 17 + (-3)\times 17= 1$

Et enfin

$4\times 47 -11\times 17 = 1$

## Démonstration du théorème

L'idée est par récurrence, de montrer qu'il est vrai à la dernière étape de l'algorithme d'Euclide, et qu'on peut remonter chaque étape...

* On a déjà prouvé que le théorème est vrai à la dernière étape de l'algorithme d'Euclide.

* On suppose que $\text{divmod}(a, b) = (q, r)$ est une étape de l'algorithme d'Euclide, et qu'il existe une combinaison linéaire de $b$ et $r$ égale à $d$. Montrons qu'il existe une combinaison linéaire de $a$ et $b$ égale à $d$.

    * Il existe $u, v \in \mathbb Z$ tel que $bu + rv = d$, d'où $rv = d - bu$.
    * D'autre part $a = bq +r$, que l'on multiplie par $v$.
    * Ainsi $av = bqv + rv$, et avec le premier point, on a :
    * $av = bqv + (d - bu)$ qui se réécrit
    * $av + b(u - qv) = d$.
    * Ce qui prouve que $d$ est une combinaison linéaire de $a$ et $b$.

## À retenir

Ce théorème doit être retenu et compris sous ses deux aspects **importants**.
* L'aspect théorique qui dit qu'il existe une telle combinaison linéaire.
* L'aspect pratique qui permet de déterminer concrètement cette combinaison linéaire.

> Les deux sont très utilisés !


## Exercices

### Exercice 1

Donner une combinaison linéaire de $91$ et $35$ égale à $\text{PGCD}(91, 35)$.

> Correction
* On utilise l'algorithme d'Euclide pour déterminer le $\text{PGCD}(91, 35)$.
    * $\text{divmod}(91, 35) = (2, 21)$
    * $\text{divmod}(35, 21) = (1, 14)$
    * $\text{divmod}(21, 14) = (1, 7)$
    * $\text{divmod}(14, 7) = (2, 0)$
    * Ainsi $\text{PGCD}(91, 35) = 7$.

* On remonte les étapes.
    * $0×14 + 1×7 = 7$, donc $1×7 = 0×14 + 7$
    * $21 = 1×14 + 7$, donc $1×14 = 1×21 - 7$
    * $35 = 1×21 + 14$, donc $35 = 1×21 + (1×21 - 7)$ d'où $2×21 = 1×35 + 7$
    * $91 = 2×35 + 21$, donc $2×91 = 4×35 + 2×21$, puis $2×91 = 4×35 + (1×35 + 7)$ et enfin
    * $\boxed{2×91 - 5×35 = 7}$

### Exercice 2

Donner une combinaison linéaire de $16$ et $52$ égale à $\text{PGCD}(16, 52)$.

### Exercice 3

Donner une combinaison linéaire de $13$ et $15$ égale à $1$. En déduire un inverse de $15$ modulo $13$.
