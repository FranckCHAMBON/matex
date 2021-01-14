> _Les mathématiques sont la seule science où on ne sait pas de quoi on parle ni si ce qu'on dit est vrai._  
**Bertrand Russell** (Mathématicien, philosophe, et … doué d'humour !)

---

## Exercice 1
Soient $a$, $b$, $c$ trois entiers non nuls. Valider (en écrivant une preuve) ou infirmer (par un contre-exemple) les affirmations suivantes :
1. Si $a \mid b$ et $b \mid c$, alors $a \mid c$.
2. Si $a \mid b$ et $a \mid c$, alors $a$ divise tous les entiers de la forme $pb + qc$ avec $p$, $q$ entiers.
3. Si $c$ divise $2a$ alors $c$ divise $a$.
4. Si $c$ divise $a$, ou si $c$ divise $b$, alors $c$ divise $ab$.
5. Si $c$ divise $ab$, alors $c$ divise $a$ ou $c$ divise $b$.
6. Si $c$ divise $3a + 1$ et $5a − 1$, alors $c$ divise $8$.

---
**Correction**

1. Si $a \mid b$ et $b \mid c$, alors $b=ka$ et $c=lb$, avec $k$ et $l$ entiers.  
D'où $c = lka$, avec $lk$ entier, ce qui donne $a\mid c$. **VRAIE.**

2. Si $a\mid b$ et $a \mid c$, alors $b=ka$ et $c=la$, avec $k$ et $l$ entiers.  
D'où, pour $p$ et $q$ entiers, $pb+qc = pka+qla = (pk+ql)a$, avec $pk+ql$ entier,
ce qui donne $a\mid pb+qc$. **VRAIE.** _(Rappel : propriété utile pour prouver l'algorithme d'Euclide)_

3. Avec $c=2$ et $a=1$, on a $c\mid 2a$, mais $c\nmid a$. **FAUSSE.**  
_(Autre exemple)_ Avec $c=22$ et $a=33$, on a $c\mid 2a$, mais $c\nmid a$.

4. On raisonne par disjonction des cas:  
    * Si $c\mid a$, alors $a=kc$ avec $k$ entier,
    ainsi $ab=kcb = (kb)c$ avec $kb$ entier, et donc $c\mid ab$.
    * L'autre cas est similaire, $a$ et $b$ jouant des rôles symétriques.  
    **VRAIE.**
    
5. Il s'agit d'étudier la réciproque.  
* Soit $p$ un nombre premier, on pose $c=p^2$, et $a=b=p$, on a $c\mid ab$, mais $c\nmid a$ et $c\nmid b$. **FAUSSE.**
* *Autre contre-exemple* : avec $c = 2×3, a = 2, b = 3$, on a $c\mid ab$, mais $c\nmid a$ et $c\nmid b$. **FAUSSE.**

6. Si $c$ divise $3a + 1$ et $5a − 1$, on utilise la propriété utile 2.  
$c$ divise $5(3a + 1)+(-3)(5a − 1)$, d'où $c\mid (15a +5 -15a +3)$, et enfin
$c$ divise $8$. **VRAIE.**

---

## Exercice 2
1. Quel est le dernier chiffre de $7^{1337}$ ?
   - Conseil 1 : Voir d'abord pour : $7^{0} ; 7^{1} ; 7^{2} ; 7^{3} ; \dots$
   - Conseil 2 : deviner une règle, et la justifier.
2. Quel est le dernier chiffre de $7^{(1337^{42})}$ ?

---

> Une réponse

Voyons d'abord ce que Python peut répondre directement.

```python
# 1.
a = 7
e = 1337

print(f"Le dernier chiffre de {a} exposant {e} est :", a**e % 10)
# Noter l'utilisation de : f"texte et {variable} mélangés"

print(f"Le dernier chiffre de {a} exposant {e} est :", pow(a, e, 10))
# Méthode plus rapide et efficace ; Python utilise ici du calcul modulaire... à suivre

#----

# 2.
a = 7
e = 1337**42

#print(a**e % 10) # <--- danger, ne pas essayer !!!
# Le calcul de a**e ne rentre pas en mémoire !!!
# Même pas pour un ordinateur de la taille de l'univers.

print("Question 2 ->", pow(a, e, 10))
# Cette méthode fonctionne.
```


    Le dernier chiffre de 7 exposant 1337 est : 7
    Le dernier chiffre de 7 exposant 1337 est : 7
    Question 2 -> 7



Étude mathématique.

* $7^0 = 1$, se termine par un $1$.  
* $7^1 = 7$, se termine par un $7$.  
* $7^2 = 49$, se termine par un $9$.  
* $7^3 = \dots3$, se termine par un $3$, tout comme $9\times 7=63$.  
* $7^4 = \dots1$, se termine par un $1$, tout comme $3\times 7=21$.  
* $7^5 = \dots7$, se termine par un $7$, tout comme $1\times 7=7$.  
* $7^6 = \dots9$, se termine par un $9$, tout comme $7\times 7=49$.  
* $7^7 = \dots3$, se termine par un $3$, tout comme $9\times 7=63$.  
* $7^8 = \dots1$, se termine par un $1$, tout comme $3\times 7=21$.  
* $\dots$

La suite est cyclique, d'ordre $4$.

* Les exposants $e$ conduisant à $7^e$ se finissant par $1$, sont : $\{0, 4, 8, 12, 16, 20, 24,\dots\}$. Ce sont les entiers dont le reste dans une division modulo $4$ est égale à $0$. On dit que ce sont les entiers congrus à $0$ modulo $4$, ils sont dans la même classe.
* Les exposants $e$ conduisant à $7^e$ se finissant par $7$, sont : $\{1, 5, 9, 13, 17, 21, 25,\dots\}$. Ce sont les entiers dont le reste dans une division modulo $4$ est égale à $1$. On dit que ce sont les entiers congrus à $1$ modulo $4$, ils sont dans la même classe.
* Les exposants $e$ conduisant à $7^e$ se finissant par $9$, sont : $\{2, 6, 10, 14, 18, 22, 26,\dots\}$. Ce sont les entiers dont le reste dans une division modulo $4$ est égale à $2$. On dit que ce sont les entiers congrus à $2$ modulo $4$, ils sont dans la même classe.
* Les exposants $e$ conduisant à $7^e$ se finissant par $3$, sont : $\{3, 7, 11, 15, 19, 23, 27,\dots\}$. Ce sont les entiers dont le reste dans une division modulo $4$ est égale à $3$. On dit que ce sont les entiers congrus à $3$ modulo $4$, ils sont dans la même classe.

Notre question 1. se résume donc à : « Quelle est la classe de $1337$, modulo $4$ ? »  
$1337 \div 4 \mapsto (q=334, r=1)$, on déduit que $1337$ est dans la classe de $1$, modulo $4$. On écrit : $1337 \equiv 1 \pmod 4$.

$1337$ étant dans la classe de $1$, modulo $4$, on déduit que $7^{1337}$ se termine par un $7$.

---

Notre question 2. se résume aussi à : « Quelle est la classe de $1337^{42}$, modulo $4$ ? »  

Nous verrons que $1337 \equiv 1 \pmod 4$ implique que $1337^{42} \equiv 1^{42} \equiv 1 \pmod 4$.

$1337^{42}$ étant dans la classe de $1$, modulo $4$, on déduit que $7^{(1337^{42})}$ se termine par un $7$.



---

## Exercice 3

Un **triplet Pythagoricien** est un triplet d'entiers $(a, b, c)$, avec $0 < a , b < c$ et $a^2 + b^2 = c^2$. Ce sont alors les trois côtés entiers d'un triangle rectangle. $(b,a,c)$ en est alors un aussi. On dit que le triplet est **primitif** si les entiers $a$ et $b$ sont premiers entre eux, c'est-à-dire que le $\text{PGCD}(a, b)=1$.

*Exemple :* $(3, 4, 5)$ est très connu des maçons. Mais aussi $(5, 12, 13)$ et $(6, 8, 10)$ ; des deux derniers exemples, le premier est primitif, pas le second.

1. Avec un script Python, afficher tous les triplets pythagoriciens $(a,b,c)$, avec $0 < a < b < c < M$.  
    1. Dans un premier temps, une méthode en $\Theta(M^3)$ suffira pour $M = 100$.
    2. Modifier votre script pour avoir une version en $\Theta(M^2)$ ; dans ce cas-là, l'utilisation de la racine carrée est conseillée ; on peut alors tester $M = 1000$.

2. Modifier vos scripts pour n'avoir que les triplets primitifs.

3. Démontrer que si $a$ et $b$ sont premiers entre eux, alors $a$ et $c$ le sont aussi. En déduire que un triplet est primitif si et seulement si deux côtés quelconques sont premiers entre eux.

---
**Correction**

1. Voici des scripts donnant des triplets pythagoriciens :
    1. Faisons une triple boucle : pour tout $a$, pour tout $b$, pour tout $c$ (ou dans l'autre ordre).  
Tirons parti de $0 < a < b < c < M$.

```python
M = 100
for a in range(1, M):
    for b in range(a+1, M):
        for c in range(b+1, M):
            if a*a + b*b == c*c:
                print(a, b, c)
```

    3 4 5
    5 12 13
    6 8 10
    7 24 25
    8 15 17
    9 12 15
    9 40 41
    10 24 26
    11 60 61
    12 16 20
    12 35 37
    13 84 85
    14 48 50
    15 20 25
    15 36 39
    16 30 34
    16 63 65
    18 24 30
    18 80 82
    20 21 29
    20 48 52
    21 28 35
    21 72 75
    24 32 40
    24 45 51
    24 70 74
    25 60 65
    27 36 45
    28 45 53
    30 40 50
    30 72 78
    32 60 68
    33 44 55
    33 56 65
    35 84 91
    36 48 60
    36 77 85
    39 52 65
    39 80 89
    40 42 58
    40 75 85
    42 56 70
    45 60 75
    48 55 73
    48 64 80
    51 68 85
    54 72 90
    57 76 95
    60 63 87
    65 72 97

> Critique du script :
* Le calcul de $a\times a$ se fait de nombreuses fois, pour la même valeur de $a$, de même que $b$.
* Quand $2a^2>M^2$, il n'y a plus de solutions, en effet, avec aussi $a < b$, on a $c^2 = a^2+b^2 > a^2+a^2 > M^2$. 


Version légèrement améliorée :
```python
from math import sqrt, floor
M = 100
aMax = floor(M/sqrt(2)) # floor(x) renvoie un entier, le plus grand inférieur ou égal à x.
for a in range(1, aMax + 1):
    a2 = a*a
    for b in range(a+1, M):
        b2 = b*b
        for c in range(b+1, M):
            if a2 + b2 == c*c:
                print(a, b, c)
```

Mais surtout, la triple boucle donne une complexité en $\Theta(M^3)$.  
$\Theta(M^3)$ signifie (un peu comme $\mathcal{O}(M^3)$) que le script fait un nombre d'opérations proportionnel à $M^3$, mais pas seulement dans le pire des cas ; toujours !

Pour passer en $\Theta(M^2)$, on remplace la dernière boucle par un calcul du seul candidat possible pour $c$ avec le théorème de Pythagore.


```python
for a in range(1, M):
    for b in range(1, M):
        c = round(sqrt(a*a + b*b))
        if (c < M) ans (a*a + b*b == c*c):
            print(a, b, c)
```

---

## Exercice 4
Écrire $\sqrt{511\;104}$ sous la forme $a\sqrt{b}$, avec $a$ et $b$ entiers, et $b$ le plus petit possible.

---

> Une réponse

On factorise $511\;104$, ici avec un appel de commande externe via `bash` dans la console Python de Jupyter.  
_Qui a dit tricheur ?_

La version `factor` incluse dans `bash` est très efficace ; bien plus que les méthodes qui vous sont accessibles. Pensez-y si votre méthode est trop lente.

```bash
$ factor 511104
511104: 2 2 2 2 2 2 2 3 11 11 11
```

On a : $511\;104 = 2^7\times3\times11^3 = (2^6\times11^2)\times(2\times3\times11)$, et donc :

$\sqrt{511\;104} = (2^3\times11)\times\sqrt{2\times3\times11} = 88\sqrt{66}$
