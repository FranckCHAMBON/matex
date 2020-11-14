> _La mathématique est l'art de donner le même nom à des choses différentes._  
> **Poincaré**


# Exercices NSI & Maths expertes $-$ Algorithme d'Euclide

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

## Exercice 2
Sachant que l'on a $96842 = 256\times 375 + 842$, déterminer avec le moins de calculs possibles les restes et quotients des divisions euclidiennes de $96842$ par $256$ et par $375$.

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
