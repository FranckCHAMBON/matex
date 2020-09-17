> _Die Mathematik ist die Königin der Wissenschaften und die Zahlentheorie ist die Königin der Mathematik._
> **Carl Friedrich Gauss**

# 1 - Décomposition en facteurs premiers

L'ensemble des entiers naturels non nuls se note $\mathbb{N}^*$, il s'agit de $\{1, 2, 3, 4, 5, \cdots\}$

Dans tout ce qui suit : $a, b, n \in \mathbb{N}^*$.

## I] Opérations élémentaires sur $\mathbb{N}^*$

### Addition, soustraction, multiplication et puissance avec Python

Python3 est capable de travailler avec des entiers aussi grands que la mémoire de l'ordinateur le permet. Les opérations élémentaires respectent les priorités. La puissance s'obtient avec ```**```.

> **Exemple**
> Calculer $A = (10^9+7)^4$
>
>```python
>>>> (10**9 + 7)**4
>1000000028000000294000001372000002401
>```



### La division euclidienne

* Le **dividende** étant la quantité à partager.
* Le **diviseur** étant le nombre de parts ; non nul.
* On souhaite un **quotient** entier et un **reste**.

On a bien $b \neq 0$, et :

> $a\div b \rightarrow (q, r)$,  
> où $a=b\times q + r$, avec $0\leqslant r<b$.

> $a$ est le dividende, $b$ est le diviseur.  
> $q$ est le quotient,  $r$ est le reste.

On parle de **division modulo** $b$, (*divmod* en abrégé).

> **Exemple**
> $410\div 30 \rightarrow$ quotient $= 13$, reste $= 20$,  
> on a bien $410 = 30\times 13 + 20$, et $0 \leqslant 20 < 30$.
>> On dit que $410$ modulo $30$ est égal à $20$.
>
> :warning: **Attention**
> $410\div 13 \rightarrow$ quotient $= 30$ , reste $= 20$ ; **est faux**,  
> on a bien $410 = 13\times 30 + 20$, mais pas $0 \leqslant 20 < 13$.

Test avec Python :
```python
>>> 13*30 + 20 == 410
True
>>> 20 < 30
True
```


Avec Python3, le quotient entier de $a$ par $b$ s'obtient avec ```a // b```,
et le reste dans cette division s'obtient avec ```a % b```.  
On peut aussi obtenir le quotient et le reste simultanément avec ```divmod(a, b)```.

**Exemple,**  avec la situation précédente :


```python
>>> 410 // 30
13
>>> 410 % 30
20
>>> divmod(410, 30)
(13, 20)
>>> divmod(410, 13)
(31, 7)
```


**Exercice** :

* Quels sont les 3 derniers chiffres de $42$ à la puissance $1337$ ?

> *Indice* : Une méthode est de calculer la puissance, puis son reste modulo $1000$.
>
>> **Solution** :
>>```python
>>>>> (42**1337) % 1000)
>>552
>>```
>>
>> Les trois derniers chiffres sont donc : 5, 5 et 2.

Ce genre de question est **réellement fondamental** pour les applications comme la cryptographie ; il existe des méthodes bien plus efficaces, nous les aborderons ! La sécurité  (informatique, bancaire, militaire), repose en partie sur ces méthodes.

### Factorielle d'un entier
Définition
: On note $n! = 1×2×3×...×n$, la factorielle de $n$.

Exemple
: $5! = 1×2×3×4×5 = 120$

Avec Python, on peut la calculer en important une fonction incluse dans le module `math` :
```python
>>> from math import factorial
>>> factorial(5)
120
```

Attention, sur la calculatrice NumWorks, la version de Python n'inclut pas `factorial`, on peut alors créer le script suivant :

```python
def factorial(n):
    ans = 1
    for x in range(1, n+1):
        ans = ans * x
    return ans

def factorial(n: int)->int:
    """ Renvoie la factorielle de n
    n doit être un entier positif.
    Version récursive pour les NSI
    >>> factorial(0)
    1
    >>> factorial(5)
    120
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

**Exercice**
: * Avec Python, calculer $A = 1000!$
: * montrer que $ 10^{300} < A < 10^{3000}$ (avec et sans Python).
> *Indice* : on pourra utiliser que $2^{10} = 1024 > 10^3$.

**Réponse** :
Avec Python
```python
>>> A = 1
>>> for x in range(1, 1001):
...     A = A * x
>>> 10**300 < A < 10**3000
True
```
Sans Python,
* on obtient une majoration de $1000!$ en remplaçant tous les facteurs par $1000$, de sorte que :
    * $A < 1000^{1000}$
    * $A < (10^3)^{1000}$
    * $A < 10^{3000}$
* on obtient une minoration de $1000!$ en remplaçant tous les facteurs par $2$, sauf $1$ et $4$ que l'on conserve. On a donc une minoration avec $998$ facteurs égaux à $2$, le tout fois $4$.
    * $A = 1×2×3×4×5×6×...×1000$
    * $A > 1×2×2×4×2×2×...×2$
    * $A > 2^{998}×4$
    * $A > 2^{1000}$
    * $A > (2^{10})^{100}$
    * $A > 1024^{100}$
    * $A > 1000^{100}$
    * $A > (10^3)^{100}$
    * $A > 10^{300}$

Obtenir des majorations et des minorations est une activité importante des mathématiques, cela permet d'obtenir des encadrements. Il existe de nombreuses méthodes...
    
## II] Diviseurs et multiples
Dans $\mathbb{N}^*$, les **multiples** de $a$ sont : $a, 2a, 3a, 4a, \cdots$

> $an$ est un multiple de $a$, mais aussi de $n$.

> $11 \times 13 = 143$, donc $143$ est un multiple de $11$ et de $13$.

> Les multiples de $7$ sont : $7, 14, 21, 28, \cdots$

« $k$ est un **diviseur** de $a$ » équivaut à « $a$ est un multiple de $k$ ».

On note dans ce cas « $k \mid a$ », et on peut dire « $k$ divise $a$ ».

Dans le cas contraire, on note « $k \nmid a$ », et on peut dire « $k$ ne divise pas $a$ ».

> **Exemples** :  
> Avec $1 \times 143 = 143$ et $11 \times 13 = 143$, on a :
>
> $143$ est un multiple de $1$, et donc $1$ est un diviseur de $143$.
>
> $143$ est un multiple de $11$, et donc $11$ est un diviseur de $143$.
>
> $143$ est un multiple de $13$, et donc $13$ est un diviseur de $143$.
>
> $143$ est un multiple de $143$, et donc $143$ est un diviseur de $143$.
>
> $1, 11, 13, 143$ sont des diviseurs de $143$.  
Y en a-t-il d'autres ? Cf III]

**Propriété :** $a \mid n \iff $ le reste dans la division de $n$ par $a$ est nul.

> **Exemple,** avec Python3, on calcule ce reste avec ```n % a```.

```python
>>> 143 % 13
0
>>> 17 % 3
2
```

```python
# Exemple pour les élèves aussi en NSI
for n, a in ((143, 13), (17, 3)):
    if n % a == 0:
        print(f"{n} est divisible par {a}")
    else:
        print(f"{n} n'est pas divisible par {a}")
```

    143 est divisible par 13
    17 n'est pas divisible par 3


## III] Liste des diviseurs

On rappelle que $a$, $b$ et $n$ sont des entiers non nuls.

**Propriété** : si $a$ est un diviseur de $n$, alors $\dfrac{n}{a}$ est entier et aussi un diviseur de $n$.

> *Preuve* : Si $a$ est un diviseur de $n$, alors $\exists\ b \in \mathbb{N}^*$ tel que $a \times b = n$, ainsi $b = \dfrac{n}{a}$ est entier et un diviseur de $n$.

**Propriété** : Si $a\times b=n$, avec $a < b$, alors $a < \sqrt{n}$.

> *Preuve 1* : $a\times a < a\times b = n$, avec $\sqrt{\cdot}$ croissante sur $\mathbb{R}^+$, on a: $\sqrt{a×a} < \sqrt{n}$, donc $a<\sqrt{n}$.

> *Preuve 2* : Si $\sqrt{n} \leqslant a < b$, alors $a\times b > (\sqrt{n})^2 = n$ ; absurde.

**Utilisation** : Pour obtenir la liste des diviseurs de $n$ non nul, il suffit de trouver ceux inférieurs à $\sqrt{n}$, d'y adjoindre leur 'binôme', et de tester éventuellement $\sqrt{n}$.

> **Exemple 1** : Trouver la liste des diviseurs de $345$.  
> On va tester tous les diviseurs de $1$ jusqu'à $18$. En effet,  $18<\sqrt{345} < 19$.  
> $345 = 1\times 345$  
> $345 = 3\times 115$  
> $345 = 5\times 69$  
> $345 = 15\times 23$  
> La liste des diviseurs de $345$ est $\{1, 3, 5, 15, 23, 69, 115, 345\}$ , il y en a $8$.  

Il faut ne compter qu'une fois les diviseurs d'un carré, comme $36 \dots$ 

> **Exemple 2** : Trouver la liste des diviseurs de $36$.  
> On va tester tous les diviseurs de $1$ jusqu'à $\sqrt{36} = 6$.  
> $36 = 1\times 36$  
> $36 = 2\times 18$  
> $36 = 3\times 12$  
> $36 = 4\times 9$  
> $36 = 6\times 6$  
> La liste des diviseurs de $36$ est $\{1, 2, 3, 4, 6, 9,  12, 18, 36 \}$ , il y en a $9$.  

**Remarques** :   
$1$ ne possède qu'un seul diviseur : lui-même. _C'est le seul tel nombre._  
$2$ possède exactement deux diviseurs : $1$ et lui-même.  
$3$ possède exactement deux diviseurs : $1$ et lui-même.  
$4$ possède exactement trois diviseurs : $1$, lui-même, et $2$.  
$5$ possède exactement deux diviseurs : $1$ et lui-même.  

> **Exercice** : Créer un script qui donne la somme des diviseurs d'un entier.

```python
def somme_diviseurs(n):
    S = 0
    for d in range(1, n+1):
        if n % d == 0:
            S = S + d

def somme_diviseurs(n: int)->int:
    """Renvoie la somme des diviseurs de l'entier n
    Version NSI, en une ligne !
    >>> somme_diviseurs(2)
    3
    >>> somme_diviseurs(6)
    12
    """
    return sum(d for d in range(1, n+1) if n%d == 0)

```

### IV] Nombres premiers
Pour tout entier $n>1$, on a $1\times n = n$, donc $n$ possède au moins deux diviseurs : $1$ et lui-même.

**Définition** : Un nombre premier est un entier qui a exactement deux diviseurs : $1$ et lui-même.

> Les nombres premiers inférieurs à $20$ sont : $2, 3, 5, 7, 11, 13, 17, 19$.

**Remarque** : Un entier $n>1$ est soit premier, soit **composé**.  
Son plus petit diviseur, excepté $1$, est premier.  
> $1$ est à part, il n'est ni premier, ni composé. 


**Théorème** : Il y a une infinité de nombres premiers.
> _Preuve 1_ : Soit $n \in \mathbb{N}^*$, on considère $N = 1 + n!$, qui n'a aucun diviseur entre $2$ et $n$, donc son plus petit diviseur est supérieur à $n$, il est premier. On déduit qu'il y a des nombres premiers aussi grands que l'on veut, une infinité donc.

> _Preuve 2_ : Par l'absurde, supposons qu'il y ait un nombre fini de nombres premiers notés $p_i$ (pour $i$ de $1$ à $k$). On considère $N = 1+p_1\times p_2\times \dots p_i \dots\times p_k$. On sait que $2$ est premier, donc $k>0$ et $N>1$ qui possède alors un plus petit diviseur (hors $1$) qui est un nombre premier $p_j$. Cependant le reste de la division de $N$ par $p_j$ est $1$ qui n'est donc pas un diviseur. Contradiction.


```python
def is_prime(n):
    "Renvoie True si n est premier, False sinon"
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True
```

```python
>>> [n for n in range(20) if is_prime(n)]
[2, 3, 5, 7, 11, 13, 17, 19]
```

Cette méthode est lente avec des nombres $n$ trop grands, (comme un milliard ou plus).  
Dans le pire des cas, la boucle de *is_prime* fait presque $n$ tours, donc un nombre d'opérations proportionnel à $n$. On dit alors que sa compléxité temporelle est en $\mathcal{O}(n)$.


```python
def is_prime(n):
    "Version améliorée"
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
        if d * d > n:
            return True
    return True
```
```python
>>> [n for n in range(10**9, 10**9+100) if is_prime(n)]
1000000007, 1000000009, 1000000021, 1000000033, 1000000087, 1000000093, 1000000097, 
```

Cette méthode fait, dans le pire des cas, $\sqrt{n}$ tours de boucle pour savoir si $n$ est premier. On dit alors que sa complexité temporelle est en $\mathcal{O}(\sqrt{n})$.

Elle sera lente pour des entiers premiers de $18$ chiffres ou plus, ou composés avec le plus petit facteur premier à $9$ chiffres ou plus. Dans ces cas, elle fera plus d'un milliard d'opérations, ce qui n'est pas instantané. Elle restera rapide pour des nombres très grands qui possèdent un petit facteur premier.

**Exercice**
* Démontrer que $101!+17$ est divisible par $17$.
* Calculer avec Python ce nombre ; est-il plus grand que $10^{18}$ ?
* Justifier que la fonction `is_prime` précédente sera pourtant très rapide pour répondre avec cette entrée.
* Proposer un nombre très grand pour lequel la fonction pourrait être lente.


**Propriété** : Tout entier supérieur à $1$ est produit de nombres premiers. On parle de **décomposition en facteurs premiers**. Elle est unique, à l'ordre près des facteurs.

**Exercice** : Donner la décomposition en facteurs premiers de $2325$.
> On commence par chercher les petits facteurs premiers :  
> $2$ n'est pas facteur ; $3$, oui. $2325 = 3 \times  775$  
> On continue avec $775$ à décomposer, et on reprend par $3$, puis $5$, $7$, $11$, ...  
> $775 = 5 \times  155$, donc $2325 = 3 \times  5 \times  155$  
> $155 = 5 \times  31$, et on reconnait $31$ comme nombre premier. Ainsi :  
> $2325 = 3 \times  5 \times  5 \times  31$ est la décomposition en facteurs premiers.

Pour en lire davantage : [https://fr.wikipedia.org/wiki/Nombre_premier](https://fr.wikipedia.org/wiki/Nombre_premier)

## V] PGCD, PPCM
On rappelle que $a$, $b$ et $n$ sont des entiers non nuls.

On note $\mathcal{D}(a)$ l'ensemble des diviseurs de $a$, c'est un ensemble non vide et fini, $a$ étant le plus grand élément.

**Propriété :** $1$ appartient à $\mathcal{D}(a)$ et $\mathcal{D}(b)$, ainsi leur intersection est non vide, qui est de plus une partie finie. Cette intersection possède donc un plus grand élément.

**Définitions :**
* $\textrm{PGCD}(a, b)$ est le plus grand élément de $\mathcal{D}(a) \cap \mathcal{D}(b)$.  
C'est le **P**lus **G**rand **C**ommun **D**iviseur, ([*gcd*](https://en.wikipedia.org/wiki/Greatest_common_divisor) : greatest common divisor ; in english).

* $\textrm{PPCM}(a, b)$ est le **P**lus **P**etit **C**ommun **M**ultiple à $a$ et $b$, ([*lcm*](https://en.wikipedia.org/wiki/Least_common_multiple) : least common multiple ; in english). C'est un entier inférieur ou égal à $ab$ qui est un multiple commun trivial.

> **Exemple 1**  
> $\mathcal{D}(9) = \{1, 3, 9\}$ et
> $\mathcal{D}(14) = \{1, 2, 7, 14\}$, donc  
> $\mathcal{D}(9) \cap \mathcal{D}(14) = \{1\}$.
> Enfin $\textrm{PGCD}(9, 14) = 1$.
>
> **Exemple 2**  
> Les multiples de $12$ sont : $12, 24, 36, 48, 60, 72\dots$  
> Les multiples de $15$ sont : $15, 30, 45, 60, 75, \dots$  
> > Ainsi $\textrm{PPCM}(12, 15) = 60$.

**Exercice**
: Avec cette définition,
    * Déterminer $\textrm{PGCD}(25, 35)$.
    * Déterminer $\textrm{PPCM}(24, 36)$.

:warning: Attention, avec ces définitions, le calcul peut être très laborieux, nous verrons d'autres méthodes.

> Avec la réforme des collèges, une nouvelle méthode est enseignée en classe de troisième, mais elle est peu utilisée par les élèves... Voici donc un rappel, ou une découverte pour certains :

**Méthode :** avec la décomposition en facteurs premiers.
* On peut calculer le **PGCD** ; on prend le **minimum** des exposants correspondants.
* On peut calculer le **PPCM** ; on prend le **maximum** des exposants correspondants.

> **Exemple**  
> Avec $a = 2^7 \times  3^2 \times  7 \times  11$, et $b = 2^5 \times  3^4 \times  7^3 \times  13$, on a :

> * $ab = 2^{7+5} \times  3^{2+4} \times  7^{1+3} \times  11 \times  13 = 2^{12} \times  3^6 \times  7^4 \times  11 \times  13$  

> * $\textrm{PGCD}(a, b) = 2^{\textrm{min}(7, 5)} \times  3^{\textrm{min}(2, 4)} \times  7^{\textrm{min}(1, 3)} = 2^5\times 3^2\times 7$.

> * $\textrm{PPCM}(a, b) = 2^{\textrm{max}(7, 5)} \times  3^{\textrm{max}(2, 4)} \times  7^{\textrm{max}(1, 3)} \times  11 \times  13$  
>$\textrm{PPCM}(a, b) = 2^7\times 3^4\times 7^3\times 11\times 13$.

**Propriété :** $\textrm{PGCD}(a, b) \times  \textrm{PPCM}(a, b) = ab$
> **Exemple**  
> $(2^5\times 3^2\times 7)\times (2^7\times 3^4\times 7^3\times 11\times 13) = 2^{12} \times  3^6 \times  7^4 \times  11 \times  13$  

> **Preuve**  
> Pour tous entiers $i$ et $j$, on a : $\textrm{min}(i, j) + \textrm{max}(i, j) = i+j$

**Exercice**
: Avec cette méthode, calculer :
    * $\textrm{PGCD}(62, 93)$
    * $\textrm{PPCM}(55, 121)$