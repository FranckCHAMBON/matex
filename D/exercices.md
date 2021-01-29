
# Exercices

## I] [Fonction indicatrice d'Euler](https://fr.wikipedia.org/wiki/Indicatrice_d%27Euler)
Soit $n\in\mathbb{N}^*$, on appelle _indicatrice d'Euler_ de $n$, et on note $\varphi(n)$, le nombre d'entiers entre $1$ et $n$ qui sont premiers avec $n$.

> $\forall p\in\mathbb{P}, \varphi(p)=p-1$

On voit en exercice comment calculer $\varphi(n)$ à l'aide de la décomposition en facteurs premiers ; $\varphi$ fait partie des [fonctions multiplicatives](https://fr.wikipedia.org/wiki/Fonction_multiplicative).

## II] Un théorème d'Euler
> **Théorème (Euler) :** (admis) Soit $a\in\mathbb{Z}$, et $n\in\mathbb{N}^*$, alors :  
> $$\text{PGCD}(a, n) = 1 \iff a^{\varphi(n)}\equiv 1 \pmod n$$

En particulier, si $a$ est inversible modulo $n$, un inverse modulo $n$ de $a$ est $a^{\varphi(n)-1}$. Ce qui fournit une nouvelle méthode pour l'inversion modulaire. Avec `Python` on utilisera la fonction `pow` pour avoir un résultat rapidement.

> **Théorème (Fermat) :** (Cas particulier du théorème d'Euler) Soit $a\in\mathbb{Z}$, et $p\in\mathbb{P}$, alors :  
> $$\text{PGCD}(a, p) = 1 \iff a^{p-1}\equiv 1 \pmod p$$

### Remarque 1
Si $p\in\mathbb{P}$ et $\text{PGCD}(a, p) \neq 1$, alors $p$ divise $a$, on a $a\equiv 0 \pmod p$, et donc :
$$a^n\equiv a \pmod p$$
Cette égalité est valable pour tout nombre premier $p$ et tout entier $a$ inversible ou non modulo $p$.

### Remarque 2
Ce théorème de Fermat est à la base d'un test de primalité.

## Exercices


### Exercice 0
1. Prouver que pour tout entier $k$, $2k+1$ et $9k+4$ sont premiers entre eux.
2. En est-il de même avec $2k-1$ et $9k+4$.



### Exercice 1 - [L'indicatrice d'Euler](https://fr.wikipedia.org/wiki/Indicatrice_d%27Euler)
La fonction $\varphi$ d'Euler est définie sur $\mathbb{N}^*$ par :  
$\varphi(n)$ est égal au nombre de d'entier $m$ premiers avec $n$ pour $m\in [1..n]$

**Par exemple :** $\varphi(8) = 4$ car parmi les nombres de $1$ à $8$, seuls les quatre nombres $1$, $3$, $5$ et $7$ sont premiers avec $8$.

1. Faire un premier script avec une fonction `totient` pour l'indicatrice d'Euler.
2. Vérifier que pour $1<u<v<100$, avec $u\land v = 1$, on a $\varphi(u)\times \varphi(v) = \varphi(uv)$
> **Remarque :** Cette propriété est vraie au-delà de 100, et de telles fonctions sont dites multiplicatives.
3. Prouver cette propriété pour $u$ et $v$ des nombres premiers distincts.
4. Quelle est la valeur de $\varphi(p)$ pour $p$ premier ?
4. Montrer que $\varphi(p^n) = p^{n-1}(p-1)$ pour $p$ premier et $n>0$ ?
6. Faire un nouveau script pour `totient` qui utilise la décomposition en facteurs premiers.



### Exercice 2
1. Si $n = p^e$, avec $p\in \mathbb{P}$, et $e\in \mathbb{N}$, alors :
    1. Les diviseurs de $n$ sont : $(1,p, p^2, \cdots, p^e)$, il y en a $e+1$.
    2. La somme de ces diviseurs est $1+p+p^2+\cdots+p^e$.   
> Faire un script avec une fonction `sommeDivPE(p, e)` qui renvoie la somme des diviseurs de $n=p^e$ quand $p$ est premier.

2. 
    1. Si $n = p_{1}^{e_1} \times p_{2}^{e_2} \times \cdots \times p_{k}^{e_k}$ est la décomposition en facteurs premiers de $n>1$, alors la somme des diviseurs de $n$ est égale au produit de la somme des diviseurs de chaque $p_{i}^{e_i}$.
    3. $1$ est le seul diviseur de $1$.
    4. Tous les entiers sont diviseurs de $0$, mais on dira que leur somme est nulle (même si c'est faux).
> Faire un script avec une fonction `sumDiv(n)` qui renvoie la somme des diviseurs de $n\geqslant 0$. _Commencer par une version en force brute._
5. On sait que $n=p^aq^b$, avec $p$ et $q$ premiers distincts, et $a>0$, $b>0$.   
On sait que $n^2$ possède $81$ diviseurs. Combien $n^3$ a-t-il de diviseurs ?
6. Soit $p$ un nombre premier tel que $2^p-1$ soit premier. On pose $n = (2^p-1)\times2^{p-1}$.  
Prouver que la somme des diviseurs de $n$ est égale à $2n$.
