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
