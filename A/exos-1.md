# Feuille d'exercices 1

## Exercice 1
Par quel chiffre doit-on remplacer les zéros de $120450$ pour qu'il soit divisible par $99$ ?

> **Indice** : faire une boucle Python pour tester tous les chiffres.

## Exercice 2
Les nombres de la forme $F_n = 2^{2^n}+1$ où $n \in \mathbb{N}$, sont-ils tous premiers ?

> **Indice** : Utiliser la fonction `is_prime` vue en cours et tester les premières valeurs de la suite.

## Exercice 3
Vérifier que pour tout $n \in [\![0..100]\!]$, et $p \in [\![0..50]\!]$ avec $p$ premier, on a : $n^p-n$ est divisible par $p$.

> **Indice** : Faire le test avec une double boucle.

## Exercice 4
Quel est le plus petit entier divisible par tous les entiers de $1$ à $15$ ? _Sans script_.

> **Indice** : Penser à la décomposition en facteurs premiers.

### Exercice 5
$p$, $q$, $r$ sont des nombres premiers distincts.
1. Quelle est la décomposition en facteurs premiers de $(p^5q^7r)\times(p^2q)$ ?
2. Quels sont les diviseurs de $p^5$ ?
3. Quels sont les diviseurs de $p^2q$ ?
4. Quels sont les diviseurs de $pqr$ ?
5. Quel est le PGCD de $pq$ et $qr$ ?

## Exercice 6 : Décomposition en facteurs premiers
> Pour les élèves aussi en NSI.

La question est de faire un premier script qui donne une décomposition en facteurs premiers.

```python
def factor(n):
    """ Renvoie la décomposition en facteurs premiers de n
    >>> factor(6)
    [2, 3]
    >>> factor(50)
    [2, 5, 5]
    """
    # À compléter
```
