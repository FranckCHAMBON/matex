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


## Algorithme en Python

```python
def euclide(a, b):
    R, U, V, r, u, v = a, 1, 0, b, 0, 1
    while r:
        q = R//r
        R, U, V, r, u, v = r, u, v, R - q*r, U - q*u, V - q*v
    return R, U, V

```

Dans cet algorithme, $R$ est le résultat du calcul du $\text{PGCD}(a, b)$ par l'algorithme d'Euclide vu au cours précédent.  
D'autre part, à chaque tour, on a que $r$ est une combinaison linéaire de $a$ et $b$ : en effet $r = au + bv$ tient à chaque tour de boucle.
> $a(U-qu) + b(V-qv) =$  
> $aU + bV - q(au+bv) =$  
> $R - qr=$  
> $\text{La prochaine valeur de } r$

**Attention.** Si on a $au +bv = d$, cela ne signifie pas que $\text{PGCD}(a, b) = d$, mais plutôt que $d$ est un multiple de ce PGCD.

**Remarque.** Avec $\text{PGCD}(a, b) = d$.  
L'équation $au+bv = 0$ possède une solution évidente $a\times (-b) + b\times a = 0$,  
mais on a aussi $a\times \dfrac{-b}{d} + b\times \dfrac{a}{d} = 0$.  
Ainsi, par combinaison linéaire, on déduit que  
$a\times \left(u-k\dfrac{b}{d}\right) + b\times \left(v+k\dfrac{a}{d}\right) = d$ pour tout entier $k$, ce qui prouve qu'il y a une infinité de solutions à l'équation $au+bv=a\land b$.

## Nombres premiers entre eux
**Définition.** Deux nombres $a$ et $b$ sont dits premiers entre eux, si leur PGCD est égal à $1$.  
> Dans ce cas la fraction $\dfrac{a}{b}$ est irréductible.

**Proposition.** Pour tous entiers $(a, b)$, on a:

> $$a\land b = 1 \iff \exists\;u, v \in \mathbb{Z}, \, au+bv = 1$$

> *Preuve :* Un sens est donné directement par le théorème précédent.  
> Pour l'autre sens, on note $\text{PGCD}(a, b) = d$, $a=da'$, $b=db'$.  
> Si $au+bv = 1$, alors $da'u+db'v=1$, et donc $d\mid 1$,  
et ainsi $d=1$, ie $a$ et $b$ sont premiers entre eux.


**Lemme de Gauss.** Soit $a, b, c \in \mathbb{Z}$, alors
$$\left.
    \begin{array}{rr}
      a\mid bc \\
      a\land b = 1
    \end{array}
  \right\}
  \implies a\mid c$$


> *Preuve :* On a $bc=ka$ et $au+bv=1$, d'où  
> $acu+bcv=c$, et donc $acu+kav=c$, et enfin $a(cu+kv)=c$,  
> qui prouve que $a\mid c$.

**Proposition** Soit $a, b, c \in \mathbb{Z}$, alors
$$\left.
    \begin{array}{rr}
      a\mid c,\, b\mid c \\
      a\land b = 1
    \end{array}
  \right\}
  \implies ab\mid c$$


> *Preuve :* On a $c=ka$, $c=lb$ et $au+bv=1$, d'où  
> $auc+bvc=c$, et donc $aulb+bvka=c$, et enfin $ab(ul+vk)=c$,  
> qui prouve que $ab\mid c$.


**Remarque.** Chercher des contre-exemples !

## L'équation $ax+by=c$ dans $\mathbb{Z}$ 

Avec $a\neq 0$, $b\neq 0$ et $c$ fixés dans $\mathbb{Z}$, discutons des solutions de cette équation $(E)$.

* Si $a\land b \nmid c$, alors il n'y a pas de solutions.
* Si $a\land b \mid c$, alors on écrit $d = a\land b$, $a=a'd$, $b=b'd$ et $c=c'd$.  
On a $a'\land b' =1$, et les solutions de $(E)$ sont les mêmes que celles de :  
$$ (E') \quad a'x+b'y=c' $$
On s'inspire de la remarque au I] pour construire l'ensemble des solutions.  
Ce sera l'objet d'un problème, avec juge en ligne.

