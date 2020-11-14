> Une théorie mathématique ne doit être regardée comme parfaite que si elle a été rendue tellement claire qu’on peut la faire comprendre au premier individu rencontré dans la rue.  
> **David Hilbert** en 1900

# Feuille d'exercices 2

> **Rappel** : La notation $|x|$ signifie valeur absolue de $x$, c'est le maximum entre $x$ et $-x$. On a $|x| = x$ si $x\geqslant 0$. On a $|x| = -x$ si $x\leqslant 0$.
Exemples : $|+7| = +7$, et $|-11|=+11$.

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
2. Les solutions de l'équation sur $\mathbb Z$ : $a×b = 1$ sont $(a=1, b=1)$ et $(a=-1, b=-1)$, en effet ni $a$ ni $b$ ne peuvent être nuls, et ni de valeur absolue supérieure à $1$. $a$ et $b$ étant de même signe, on a :
* Si $a>1$, alors $b\geqslant 1$, et $a×b>1$ ; *impossible*.
* Si $a<-1$, alors $b\leqslant -1$, et $a×b>1$ ; *impossible*.
* $a$ et $b$ jouent des rôles symétriques, donc on a de même $b>1$ et $b<-1$ impossibles.
* Et $a$ ou $b$ nul, implique $a×b = 0$ ; *impossible*.
* Il ne reste que les cas $a=b=1$, et $a=b=-1$.
3. Si $a\mid b$, alors $b = a×k$ pour $k\in \mathbb Z$, on déduit $-b=-a×k$, mais aussi $-b=a×(-k)$, et encore $b=(-a)×k$, le tout avec $(-a)$ et $(-k)$ dans $\mathbb Z$ (*important à souligner*), ainsi $\pm a \mid \pm b$.
4. $\forall a\in\mathbb Z, 0=0×a$, ainsi $a\mid 0$.
> Remarque : $0\mid 0$, certes, mais $0$ divisé par $0$ n'est pas défini. C'est différent.
5. Si $0\mid a$, alors $a=0×k$, avec $k\in\mathbb Z$, donc $a=0$.
6. $a=a×1$, donc $a\mid a$.
7. Si $a\mid b$ et $b\mid c$, alors $c=b×k$ avec $k\in\mathbb Z$, et $b=a×l$ avec $l\in\mathbb Z$, d'où $c = (a×l)×k = a×(l×k)$ avec $(l×k)\in\mathbb Z$, ainsi $a\mid c$. *On a utilisé l'associativité de la multiplication.*
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

---

* $35 = 5×7$, donc $7 \mid 35$, et donc $7 \mid 35×1000$. (prop. 9)
* D'autre part $42 = 6×7$, donc $7 \mid 42$.
* Ainsi $7 \mid 35\,000 +42$. (prop. 8)

## Exercice 3

Avec l'algorithme d'Euclide, calculer $\text{PGCD}(16191, 9252)$.

---

* $(16191÷9252) \rightarrow (q=1, r=6939)$
* $(9252÷6939) \rightarrow (q=1, r=2313)$
* $(6939÷2313) \rightarrow (q=3, r=0)$
Le dernier diviseur est $2313$, c'est le $\text{PGCD}(16191, 9252)$.


## Exercice 4

Calculer $A = \dfrac{21}{1535} + \dfrac{17}{2763}$

*Donner le résultat sous forme d'une fraction irréductible. Justifier cela de manière efficace !*

---

Calculons $\text{PGCD}(1535, 2763)$ avec l'algorithme d'Euclide.
* $(1535÷2763) \rightarrow (q=0, r=1535)$
* $(2763÷1535) \rightarrow (q=1, r=1228)$
* $(1535÷1228) \rightarrow (q=1, r=307)$
* $(1228÷307) \rightarrow (q=4, r=0)$
Le dernier diviseur est $307$, c'est le $\text{PGCD}(1535, 2763)$.

On peut alors écrire : $1535 = 307×5$ et $2763=307×9$, de sorte que :

* $A = \dfrac{21}{307×5} + \dfrac{17}{307×9}$, *on veut obtenir le même dénominateur.*

* $A = \dfrac{21×9}{307×5×9} + \dfrac{17×5}{307×9×5}$, *inutile de calculer le dénominateur.*

* $A = \dfrac{21×9+17×5}{307×5×9}$, *mais on doit calculer le numérateur.*

* $A = \dfrac{274}{307×5×9}$, *pour simplifier, on peut penser à la décomposition en facteurs premiers.*

* $A = \dfrac{2×137}{307×5×3^2}$, *on ne peut donc pas simplifier cette fraction.*

* $A = \dfrac{274}{13815}$ est irréductible.

> On peut aussi vérifier que $\text{PGCD}(274, 13815) = 1$. C'est une excellente méthode, pour simplifier, ou justifier qu'une fraction est irréductible.


## Exercice 5

Calculer $B = \dfrac{15730}{25137} × \dfrac{45619}{112200}$

*Donner le résultat sous forme d'une fraction irréductible.*

---
On a les décompositions en facteurs premiers :
* $15730 = 2× 5× 11× 11× 13$
* $25137 = 3^3× 7^2× 19$
* $45619 = 7^4× 19$
* $112200 = 2^3× 3× 5^2× 11× 17$

On en déduit :
* $B = \dfrac{2× 5× 11× 11× 13}{3^3× 7^2× 19} × \dfrac{7^4× 19}{2^3× 3× 5^2× 11× 17}$

* $B = \dfrac{2× 5× 11× 11× 13× 7^4× 19}{3^3× 7^2× 19× 2^3× 3× 5^2× 11× 17}$, *simplifions par $2$, $5$, $11$, $7^2$ et $19$.*

* $B = \dfrac{11× 13× 7^2}{3^3× 2^2× 3× 5× 17}$, *enfin rangeons.*

* $B = \dfrac{7^2×11×13}{2^2× 3^4× 5× 17}$, *le résultat demandé.*

## Exercice 5

Calculer $C = \dfrac{1}{91} + \dfrac{2}{91} × \dfrac{5}{3}$

*Donner le résultat sous forme d'une fraction irréductible.*

---

> :warning: L'opération prioritaire n'est pas l'addition, mais la multiplication.

* $C = \dfrac{1}{91} + \dfrac{2×5}{91×3}$

* $C = \dfrac{1×3}{91×3} + \dfrac{2×5}{91×3}$

* $C = \dfrac{1×3+2×5}{91×3}$, *on n'évalue pas le dénominateur !*

* $C = \dfrac{13}{91×3}$, *on cherche à simplifier*.

Si une fraction possède un petit numérateur, ou un petit dénominateur, on décompose ce petit nombre en facteurs premiers, et seules les simplifications possibles sont issues de ces facteurs. Ici, $13$ seul candidat, or $91=7×13$, donc on peut simplifier.

* $C = \dfrac{1}{7×3}$, le résultat attendu.


## Exercice 6
> Pour les élèves aussi en NSI.

On rappelle que : 
* $\text{PGCD}(a, 0) = |a|$ pour tout $a\in \mathbb Z$
* Pour $b\neq 0$, $\text{PGCD}(a, b) = \text{PGCD}(b, r)$, où $r$ est le reste dans la division euclidienne de $a$ par $b$.

En déduire une fonction Python récursive de calcul de $\text{PGCD}$.

---

```python
def pgcd(a: int, b: int) -> int:
    """Renvoie PGCD(a, b) pour a et b relatifs.
    >>> pgcd(15, 49)
    1
    >>> pgcd(-12, 18)
    6
    """
    if b == 0:
        return abs(a)
    else:
        return pgcd(b, a%b)
    
    # variante en une ligne
    return abs(a) if b == 0 else pgcd(b, a%b)
```

