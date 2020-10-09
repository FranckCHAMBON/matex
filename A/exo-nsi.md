# Décomposition en facteurs premiers
Pour les élèves en Maths expertes + NSI.
> L'exercice 6 de la feuille n°1. Partie 2

## Notion de complexité
* La notation $\mathcal O(f(n))$ pour un script signifie un coût en temps, **dans le pire des cas**, proportionnel à $f(n)$.
* Pour un coût qui serait proportionnel à $f(n)$, **dans tous les cas**, on note $\Theta(f(n)$).
* La notion de proportionnalité s'entend ici avec un coefficient qui n'est pas clairement défini, mais plutôt encadré. Il dépendra de la machine qui exécute le code... L'objectif étant de pouvoir anticiper un temps de calcul. 

### Exemple
Avec un algorithme en $\Theta(\sqrt(n))$, qui met $4\,s$ pour traiter le cas $n = 10^6$, on sait qu'il mettra $40\,s$ pour $n=10^8$. En effet, on complète le tableau de proportionnalité suivant.

|Entrée $n$|Temps (s)|
|----|----|
|$\sqrt{10^6}$|$4$|
|$\sqrt{10^8}$|   |

## Script en $\mathcal O(n)$

Nous avons reproduit ici notre script de la partie 1, en $\mathcal O(n)$ :

```python
def factor(n):
    """Renvoie une liste, la décomposition en facteurs premiers de n.
    >>> factor(6)
    [2, 3]
    >>> factor(8)
    [2, 2, 2]
    """
    assert n > 0
    Factor = []
    p = 2
    while n > 1:
        if n % p == 0:
            n //= p
            Factor.append(p)
            while n % p == 0:
                n //= p
                Factor.append(p)
        p += 1
    return Factor
```

La question est de faire un nouveau script qui donne une décomposition en facteurs premiers, en $\mathcal O(\sqrt n)$.

## Script en $\mathcal O(\sqrt n)$

C'était l'objet de l'exercice. Voici une solution.

```python
def factor(n):
    """ Renvoie la décomposition en facteurs premiers de n
    >>> factor(6)
    [2, 3]
    >>> factor(50)
    [2, 5, 5]
    """
    assert n > 0
    Factor = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            Factor.append(p)
            while n % p == 0:
                n //= p
                Factor.append(p)
        p += 1
    if n > 1:
        Factor.append(n)
    return Factor
```

### Commentaires

On sort de la boucle quand $p^2 > n$.

Dans ce cas, $n$ ne possède aucun facteur premier inférieur ou égal à $\sqrt n$.
On déduit que $n=1$, ou alors $n$ est premier.

Ce script permet d'obtenir très vite la décomposition en facteurs premiers de nombres tels que $2\,000\,000\,018$, en effet, le premier facteur $2$ amène $n$ à $1\,000\,000\,009$ qui est un nombre premier.