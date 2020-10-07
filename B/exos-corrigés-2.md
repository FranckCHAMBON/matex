> Une théorie mathématique ne doit être regardée comme parfaite que si elle a été rendue tellement claire qu’on peut la faire comprendre au premier individu rencontré dans la rue.  
> **David Hilbert** en 1900

# Feuille d'exercices 2

## Exercice 1

Démontrer les premières propriétés vues en cours ; à savoir : 

Soient $a,b,c$ trois entiers relatifs.
1. $1\mid a$ ; _( $1$ est toujours un diviseur, de tout entier. )_
2. Si $a\mid 1$, alors $a=\pm 1$ ; _( $\pm1$ sont les seuls inversibles de $\mathbb{Z}$. )_
3. Si $a\mid b$, alors $\pm a\mid \pm b$ ; _( Le signe n'a pas d'importance. )_
4.  $a\mid 0$ ; _( Zéro est multiple de tout entier ; tous les entiers divisent zéro. )_
5.  Si $0\mid a$, alors $a=0$ ; _( Autrement dit : zéro ne divise que zéro. )_
6. $a\mid a$ ; _(réflexivité)_
7. Si $a\mid b$ et $b\mid c$, alors $a\mid c$ ; _(transitivité)_
8. Si $a\mid b$ et $a\mid c$, alors $a\mid b+c$ ; 
9. Si $a\mid b$, alors $a\mid bc$ et $ac\mid bc$;
10. Si  $ac\mid bc$ avec $c\neq 0$, alors $a\mid b$ ;
11. Si  $a\mid b$ avec $b\neq 0$, alors $0<|a| \leqslant |b|$ ;
12. Si  $a\mid b$ et $b\mid a$ , alors $a=\pm b$.

### Corrigé
1. $\forall a \in \mathbb Z, a = a×1$, ainsi $1\mid a$.
2. Les solutions de l'équation sur $\mathbb Z$ : $a×b = 1$ sont $(a=1, b=1)$ et $(a=-1, b=-1)$, en effet ni $a$ ni $b$ ne peuvent être nuls, et ni de valeur absolue supérieure à $1$.
3. Si $a\mid b$, alors $b = a×k$ pour $k\in \mathbb Z$, on déduit $-b=-a×k$, mais aussi $-b=a×(-k)$, et encore $b=(-a)×k$, le tout avec $(-a)$ et $(-k)$ dans $\mathbb Z$ (*important à souligner*), ainsi $\pm a \mid \pm b$.
4. $\forall a\in\mathbb Z, 0=0×a$, ainsi $a\mid 0$.
> Remarque : $0\mid 0$, certes, mais $0$ divisé par $0$ n'est pas défini. C'est différent.
5. Si $0\mid a$, alors $a=0×k$, avec $k\in\mathbb Z$, donc $a=0$.
6. $a=a×1$, donc $a\mid a$.
7. Si $a\mid b$ et $b\mid c$, alors $c=b×k$ avec $k\in\mathbb Z$, et $b=a×l$ avec $l\in\mathbb Z$, d'où $c = (a×l)×k = a×(l×k)$ avec $(l×k)\in\mathbb Z$, ainsi $a\mid c$.
8. Si $a\mid b$ et $a\mid c$, alors $b=a×k$ avec $k\in\mathbb Z$, et $c=a×l$ avec $l\in\mathbb Z$, ainsi $b+c = a×k+a×l=a×(k+l)$, avec $(k+l)\in\mathbb Z$, ainsi $a\mid b+c$.
9. Si $a\mid b$, alors $b=a×k$ avec $k\in\mathbb Z$, donc $bc=a×(k×c)$ avec $(k×c)\in\mathbb Z$, et $bc = a×k×c = (ac)×k$ avec $(ac)\in\mathbb Z$, ainsi $a\mid bc$ et $ac\mid bc$. *On a utilisé ici la commutativité de la multiplication !.*
10. Si  $ac\mid bc$ avec $c\neq 0$, alors $bc=ac×k$ avec $k\in\mathbb Z$, d'où $b=a×k$, ainsi $a\mid b$.
11. Si  $a\mid b$ avec $b\neq 0$, alors $|a|\mid |b|$ et $|b| = |a| × k$ avec $k\in\mathbb Z$. Avec $b\neq 0$, on déduit $k\neq 0$ et $a\neq 0$, et enfin $0<|a| \leqslant |b|$ ;
12. Si  $a\mid b$ et $b\mid a$ , alors
* si $a=0$, alors $b=0$ d'après 5.
* si $b=0$, alors $a=0$ d'après 5.
* sinon, $0<|a| \leqslant |b|$ et $0<|b| \leqslant |a|$ d'après 11. d'où $|a|=|b|$, ainsi  $a=\pm b$.

## Exercice 2

Démontrer que $7 \mid 35\,042$, sans calculatrice.

## Exercice 3

Avec l'algorithme d'Euclide, calculer $\text{PGCD}(16191, 9252)$.

## Exercice 4

Calculer $A = \dfrac{21}{1535} + \dfrac{17}{2763}$

*Donner le résultat sous forme d'une fraction irréductible. Justifier cela de manière efficace !*

> **Indice** : penser à l'algorithme d'Euclide.

## Exercice 5

Calculer $B = \dfrac{15730}{25137} × \dfrac{45619}{112200}$

*Donner le résultat sous forme d'une fraction irréductible.*

> **Indice** : penser à la décomposition en facteurs premiers des numérateurs et des dénominateurs.

## Exercice 5

Calculer $C = \dfrac{1}{91} + \dfrac{2}{91} × \dfrac{5}{3}$

*Donner le résultat sous forme d'une fraction irréductible.*

## Exercice 6
> Pour les élèves aussi en NSI.

On rappelle que : 
* $\text{PGCD}(a, 0) = |a|$ pour tout $a\in \mathbb Z$
* Pour $b\neq 0$, $\text{PGCD}(a, b) = \text{PGCD}(b, r)$, où $r$ est le reste dans la division euclidienne de $a$ par $b$.

En déduire une fonction Python récursive de calcul de $\text{PGCD}$.
