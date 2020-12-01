![Étoiles](stars.png)

> _Ils [les rationnels] sont parmi les nombres réels comme des étoiles dans le
ciel pour illuminer le mystère du continu._
> **Émile Borel**

# Arithmétique modulaire - congruences

**Introduction aux notations.**

* Le reste de $1337$ divisé par $100$ est $37$, on dit que $1337$ est congru à $37$ modulo $100$, on dit aussi que $1337$ modulo $100$ est égal à $37$.
* Le reste de $2037$ divisé par $100$ est aussi égal à $37$. On peut dire que $1337$ et $2037$ sont congrus modulo $100$ ; ils ont le même reste dans la division par $100$. On dit que $2037$ modulo $100$ est égal à $37$.
* La différence $2037-1337$ est égale à $700$ qui est divisible par $100$ ; c'est normal pour deux nombres qui sont congrus modulo $100$.

**Autres exemples**
* $12$ est congru à $5$, modulo $7$ ;
* $12$ est congru à $3$, modulo $9$ ;
* $27$ est congru à $12$, modulo $15$ ;
* $162$ est congru à $12$, modulo $15$ ;
* $162$ est congru à $27$, modulo $15$ ;
* $77$ est congru à $0$ modulo $7$.

**Exemple plus difficile**.

En étudiant le dernier chiffre de $7^n$, nous avons remarqué que le résultat était commun pour certaines classes d'entiers :
* la classe des entiers $n$ dont le reste dans une division par $4$ est égal à $0$, donnait un dernier chiffre pour $7^n$ égal à $1$.
* la classe des entiers $n$ dont le reste dans une division par $4$ est égal à $1$, donnait un dernier chiffre pour $7^n$ égal à $7$.
* la classe des entiers $n$ dont le reste dans une division par $4$ est égal à $2$, donnait un dernier chiffre pour $7^n$ égal à $9$.
* la classe des entiers $n$ dont le reste dans une division par $4$ est égal à $3$, donnait un dernier chiffre pour $7^n$ égal à $3$.

> Tous les entiers sont ainsi classés.

> Dire que le dernier chiffre de $M$ est $c$ revient à dire que $M$ modulo $10$ est égal à $c$.

On écrira de manière plus succincte :
* Si $n\equiv 0 \pmod 4$, alors $7^n \equiv 1 \pmod{10}$.
* Si $n\equiv 1 \pmod 4$, alors $7^n \equiv 7 \pmod{10}$.
* Si $n\equiv 2 \pmod 4$, alors $7^n \equiv 9 \pmod{10}$.
* Si $n\equiv 3 \pmod 4$, alors $7^n \equiv 3 \pmod{10}$.

## I] Définitions
### Congruence
Soit $m$, $a$, $b$ entiers dans $\mathbb{Z}$.
> On dit que $a$ est congru à $b$ modulo $m$, si $m$ divise $a - b$.

On dit aussi que :
* $a$ et $b$ sont congrus modulo $m$ ;
* $a$ et $b$ sont dans la même classe, modulo $m$.

On note avec l'une des deux notations :
* $a \equiv b \pmod m$ ;
* $a \equiv b \; [m]$ ;

Dans ce cas, on a :
* $m \mid a-b$ ;
* $\exists k \in \mathbb{Z}$, tel que $a-b = km$.

Dans le cas le plus fréquent $m> 0$, on a :
* $a$ et $b$ ont le même reste dans la division euclidienne par $m$.

Dans le cas contraire
: on écrit $a \not \equiv b \pmod m$, si $a$ et $b$ ne sont pas congrus modulo $m$.

**Image mentale**
* Il faut imaginer une roue avec les nombres de $0$ à $m-1$ ; il y a $m$ nombres.
* On fait tourner d'un certain nombre de crans en partant de $0$, la roue qui s'arrête sur un nombre, peut importe le nombre de tours effectués avant. Par exemple, avec $m=7$, faire tourner de 55 crans conduit à finir sur le $6$.
* Deux nombres congrus modulo $m$ conduisent au même résidu modulo $m$ ; au même point sur la roue.

### Résidu
Si $a\in\mathbb{Z}$, et $m\in\mathbb{N}^*$.  
On appelle résidu de $a$ modulo $m$, et on note $a$ mod $m$,   l'unique entier $r\in[\![0, m-1]\!]$ pour lequel $a\equiv r \pmod m$.

Pour $a, b \in \mathbb{Z}$, on a donc :
$$a\equiv b\pmod m \iff a \text{ mod } m = b \text{ mod } m$$

On a par exemple : 
* $17 \text{ mod } 5 = 2$

### Premières propriétés
Soit $m$, $a$, $b$ entiers dans $\mathbb{Z}$.
1. $a\equiv 0 \pmod m \iff m \mid a$ ;
2. $a\equiv b \pmod m \iff -a\equiv -b \pmod m$ ;
3. $a\equiv b \pmod 0 \iff a=b$ ;
3. $a\equiv b \pmod 1$ est toujours vrai.

### Exemple
* $2$ mis à part, un nombre premier est congru à $1$ modulo $2$.
* $2$ et $3$ mis à part, un nombre premier est congru à $1$ ou $-1$ modulo $6$.

## II] Propriétés
Soit $m\in\mathbb{Z}$, la congruence modulo $m$ est une relation d'équivalence, en effet :
* Réflexivité : $\forall a \in \mathbb{Z}, a\equiv a \pmod m$ ;
* Symétrie : $\forall a, b \in \mathbb{Z}, a\equiv b \pmod m \implies b\equiv a \pmod m$ ;
* Transitivité : $\forall a, b, c \in \mathbb{Z}$, $(a\equiv b \pmod m, \text{ et } b\equiv c \pmod m \implies a\equiv c \pmod m$.

La congruence modulo $m$ est compatible avec l'addition et la multiplication dans le sens suivant :

$\forall a, a', b, b', c, m \in \mathbb{Z}$ et $k \in \mathbb{N}$,   
avec $a\equiv a' \pmod m$ et $b\equiv b' \pmod m$, on a :  
* $a+b \equiv a'+b' \pmod m$ ;
* $ab \equiv a'b' \pmod m$ ;
* $ac \equiv a'c \pmod m$ ;
* $a^k \equiv a'^k \pmod m$.

Donc les règles de manipulation des congruences contiennent la plupart des règles de manipulations d’égalités entre entiers pour l’addition, la soustraction, et la multiplication.
> Mais pour la division (et la simplification des congruences), c’est plus compliqué.

De plus, on a:
* Si $d$ est un diviseur commun de $a$, $b$ et $m$, alors   

$a\equiv b \pmod m \implies \frac a d \equiv \frac b d \pmod {\frac m d}$

### Utilisations
* On peut faire de l'évaluation polynomiale modulaire de manière assez transparente. En effet, évaluer un polynôme se fait en enchaînant des additions et des multiplications.
* On utilise le calcul modulaire dans de nombreuses situations, en particulier lorsqu'on souhaite que le résultat d'un calcul reste contenu dans un intervalle, évitant donc les débordements. En effet, en informatique, avec certains langages, on ne peut pas travailler avec des entiers trop grands, il faut rester dans un intervalle !
* On verra comment reconstruire un entier lorsque l'on connaît plusieurs résidus avec des modulos variés. C'est un procédé très efficace.
* Les méthodes abordées ici avec les entiers seront généralisées plus tard dans vos études avec des polynômes ; le principe restera le même.


## III] Inversion modulaire
> Diviser par un nombre, c'est multiplier par son inverse.
> > Encore faut-il que l'inverse existe.

Soit $a, m\in\mathbb{Z}$, on dit que $a$ est inversible modulo $m$,   
s'il existe un entier $\tilde a\in \mathbb{Z}$ tel que :
$a\tilde a \equiv 1\pmod m$.
> On dit alors $\tilde a$ est un inverse modulo $m$ de $a$.

### Méthode élémentaire
Pour $a$ fixé, on construit la liste de tous les produits $ab$ et on cherche si un résultat est congru modulo $m$.

### Exemple
* Démontrer que $3$ est inversible modulo $5$.
* Démontrer que $4$ n'admet pas d'inverse modulo $6$.

### Exercice NSI+Matex
Faire un script qui trouve s'il existe un inverse de $a$ modulo $m$.
