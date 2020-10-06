> _Un mathématicien ce n’est pas quelqu’un qui passe son temps à faire des calculs, c’est quelqu’un qui trouve des techniques pour ne pas avoir à les faire._
> **Anonyme**

# Divisibilité dans $\mathbb{Z}$

$\mathbb{Z} = \{\dots,-3, -2, -1, 0, 1, 2, 3,\dots \}$ est l'ensemble des entiers relatifs.

Dans ce cours, on généralise à $\mathbb{Z}$ les notions de divisibilité, de division euclidienne, de $\textrm{PGCD}$. On découvre l'algorithme d'Euclide.

## I] Définition, premières propriétés

### Définition
Soit $a, b \in \mathbb{Z}$, on dit que $a$ divise $b$, et on note $a\mid b$,  
s'il existe un entier $k \in \mathbb{Z}$ tel que $b=ak$.  
Dans ce cas, $b$ est un multiple de $a$.  
$a\nmid b$ signifie : $a$ ne divise pas $b$.

> La définition est similaire à celle vue pour $\mathbb N^*$.

### Propriétés
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

> **Remarque** : on a écrit que $0$ divise $0$, cependant $0$ divisé par $0$ n'est pas défini... Nuance.

**Une propriété très utile**
> Avec $a, b, c, u, v \in \mathbb{Z}$,
> * si $a\mid b$ et $a\mid c$,
> * alors $a\mid ub+vc$.
>
> On dit aussi que si $a$ divise $b$ et $c$, alors $a$ divise toute combinaison linéaire de $b$ et $c$.

> > **Preuve** : On a : $b = k_1 a$, et $c = k_2 a$, avec $k_1, k_2 \in \mathbb{Z}$, ainsi  
> > $ub+vc = uk_1 a + vk_2 a = (uk_1 + vk_2) a$,  avec $(uk_1 + vk_2) \in \mathbb{Z}$  
> > On conclut que : $a\mid ub+vc$

## II] Division euclidienne
### Théorème
Pour $a,b \in \mathbb{Z}$, avec $b\neq 0$, $\exists! \;q,r \in \mathbb{Z}$, tel que $a=bq+r$, et $0\leqslant r<|b|$.

**⚠️ Attention**, avec Python et <kbd>divmod</kbd> ou <kbd>%</kbd>, si $b<0$, le reste $r$ vérifie alors $b<r\leqslant 0$.  
Mais on a toujours $a=bq+r$.  
Avec d'autres langages de programmation, il faudra vérifier la règle !


```python
for b in [+3, -3]:
    for a in [-13, -12, +12, +13]:
        q, r = divmod(a, b)
        q, r = a//b, a%b # variante de la ligne précédente
        print(a, "divisé par", b, "=> quotient :", q, "; reste :", r)
        print("Vérification :", a, "=", str(b)+"*"+str(q), "+", r, end="  et  ")
        if b>0:
            print("0 <=", r, "<", b)
        else:
            print(b, "<", r, "<= 0")
        print()
```

    -13 divisé par 3 => quotient : -5 ; reste : 2
    Vérification : -13 = 3*-5 + 2  et  0 <= 2 < 3
    
    -12 divisé par 3 => quotient : -4 ; reste : 0
    Vérification : -12 = 3*-4 + 0  et  0 <= 0 < 3
    
    12 divisé par 3 => quotient : 4 ; reste : 0
    Vérification : 12 = 3*4 + 0  et  0 <= 0 < 3
    
    13 divisé par 3 => quotient : 4 ; reste : 1
    Vérification : 13 = 3*4 + 1  et  0 <= 1 < 3
    
    -13 divisé par -3 => quotient : 4 ; reste : -1
    Vérification : -13 = -3*4 + -1  et  -3 < -1 <= 0
    
    -12 divisé par -3 => quotient : 4 ; reste : 0
    Vérification : -12 = -3*4 + 0  et  -3 < 0 <= 0
    
    12 divisé par -3 => quotient : -4 ; reste : 0
    Vérification : 12 = -3*-4 + 0  et  -3 < 0 <= 0
    
    13 divisé par -3 => quotient : -5 ; reste : -2
    Vérification : 13 = -3*-5 + -2  et  -3 < -2 <= 0
    


### Propriété
$a \mid b$ si et seulement si $b=0$  **ou alors** $a\neq 0$ et le reste de la division euclidienne de $b$ par $a$ est $0$.


## III] PGCD de deux entiers
### Définition
Pour tout entier $a$, on note $\mathcal{D}(a)$ l'ensemble des diviseurs de $a$.
$$\mathcal{D}(a) =  \{k \in\mathbb{Z} \text{ tels que } k\mid a\}$$

Par exemple :
$$\mathcal{D}(24) =  \{\pm1,\pm2,\pm3,\pm4,\pm6,\pm8,\pm12,\pm24\}$$

On a toujours :
1. $\pm1, \pm a \in \mathcal{D}(a)$ ;
2. $\mathcal{D}(0) = \mathbb{Z}$ ;
3. Si $a\neq 0$, alors $\mathcal{D}(a) \subseteq [\![-|a|..|a|]\!]$.

Soient $a, b \in \mathbb{Z}$, dont un non nul au moins, on appelle **PGCD** de $a$ et $b$ _(**P**lus **G**rand **C**ommun **D**iviseur)_, et on note $a \land b$, le plus grand entier divisant à la fois $a$ et $b$.

**⚠️ Attention :** On étend cette définition en posant $0 \land 0 = 0$ ; mais cela traduit toujours que tous les entiers divisent $0$. Dans ce cas seul, cela ne traduit pas que $0$ est le plus grand diviseur commun à $0$ et $0$ !!!

### Propriétés
Pour $a, b \in \mathbb{Z}$, on a :
1. $a\land b = b\land a$ ;
2. $a\land b = \pm a\land \pm b$ ;
3. $a\land 0 = 0\land a = |a|$ ;
4. $a\land b = 0 \iff a=b=0$ ;
5. $a\land 1 = 1$.

On peut bien évidemment utiliser les méthodes étudiées sur $\mathbb{N}^*$.


## IV] Algorithme d'Euclide
On a vu comment calculer le $\text{PGCD}$ de deux entiers ayant connaissance de leur décomposition en facteurs premiers, mais cette méthode est lente pour de grands entiers. L'algorithme d'Euclide est une méthode efficace.

### Un exemple
On souhaite calculer $\text{PGCD}(323, 187)$.
> $\text{divmod}(323, 187) = (1, 136)$ ; _On continue avec $187$ et $136$_.  
> $\text{divmod}(187, 136) = (1, 51)$ ; _On continue avec $136$ et $51$_.  
> $\text{divmod}(136, 51) = (2, 34)$ ; _On continue avec $51$ et $34$_.  
> $\text{divmod}(51, 34) = (1, 17)$ ; _On continue avec $34$ et $17$_.  
> $\text{divmod}(34, 17) = (2, 0)$ ; _Le reste est nul, le dernier diviseur est $17$_.  
> D'après l'algorithme d'Euclide, $\text{PGCD}(323, 187) = 17$.


**Preuve :** 
1. *L'algorithme termine.*
Le diviseur suivant à la prochaine étape est le reste de la division actuelle, or on sait que le reste est strictement inférieur au diviseur, ce qui nous donne une suite strictement décroissante d'entiers naturels. Nécessairement elle arrive à zéro en un nombre fini d'étapes.
2. *L'algorithme est correct.*
Soit $a\geqslant b$.  
Si $b=0$, alors $\text{PGCD}(a, b) = a$. C'est fini.  
Sinon, on fait la division euclidienne de $a$ par $b$.  
$a = bq+r$, ainsi $r = a-bq$, et d'après la dernière propriété (utile) de I],  
on déduit que si $d \mid a$ et $d \mid b$, alors $d \mid r$,   
mais aussi que si $d \mid b$ et $d \mid r$, alors $d \mid a$.   
Dit autrement : les diviseurs communs à $a$ et $b$ sont les mêmes que ceux à $b$ et $r$.  
En particulier ils ont le même PGCD. Ce qui justifie l'algorithme et prouve même un peu plus :

> **Les diviseurs communs à $a$ et $b$, sont les diviseurs de leur PGCD.**


## V] Applications
* Une fraction $\dfrac a b$ peut être simplifiée au maximum par le $\text{PGCD}(a, b)$, elle devient alors irréductible. C'est la bonne méthode à utiliser.
* Pour additionner deux fractions, on doit les mettre au même dénominateur. Une méthode consiste à utiliser le $\text{PPCM}$. 
* Pour résoudre des problèmes du genre :
> Un philatéliste possède 1631 timbres français et 932 timbres étrangers. Il souhaite vendre toute sa collection en réalisant des lots identiques, c'est à dire comportant le même nombre de timbres français et le même nombre de timbres étrangers.
> 1. Calculer le nombre maximum de lots qu'il pourra réaliser.
> 2. Combien y-aura-t-il, dans ce cas, de timbres français et étrangers par lot ? 
> > **Réponse :** Les lots sont identiques, donc le nombre de lot est un diviseur de 1631, mais aussi de 932, il en veut le maximum, donc le nombre de lots est le PGCD(1631, 932)... 
* $\cdots$
