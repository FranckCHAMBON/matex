# Mathématiques expertes
## DS1 d'arithmétique - 25 minutes

On travaille dans $\mathbb N^*$ dans tout le devoir. **La calculatrice est autorisée.**

### Exercice 1 (8 pts)
> Application directe du cours
1. Comment calculer avec Python, le reste de la division euclidienne de $5^{2020}$ par $1337$ ? *Donner une instruction.*
2. Donner la liste des diviseurs de $280$. *Justifier.*
3. $42! + 9$ est-il un nombre premier ? *Justifier.*
4. À quoi sert la fonction Python ci-dessous ? *On demande juste ce qu'elle permet de calculer.*
```python
def mystère(n):
    ans = 0
    for d in range(1, n+1):
        if n % d == 0:
            ans = ans + 1
    return ans
```

### Exercice 2 (6 pts)
> Brevet (Asie juin 2007)
1) Déterminer par la méthode de votre choix et en détaillant les différentes étapes le $\textrm{PGCD}$ de $144$ et $252$.
2) Une association organise une compétition sportive ; $144$ filles et $252$ garçons se sont inscrits. L’association désire répartir les inscrits en équipes mixtes. Le nombre de filles doit être le même dans chaque équipe, le nombre de garçons doit être le même dans chaque équipe. Tous les inscrits doivent être dans une des équipes.
    1. Quel est le nombre maximum d’équipes que cette association peut former ?
    2. Quelle est alors la composition de chaque équipe ?

### Exercice 3 (6 pts)
> Sans fin...

On considère les nombres de la forme $M_n = 2^n-1$, pour $n\in\mathbb N^*$.

En partant de $n=1$, et aussi loin que vous pouvez, calculer $M_n$ et justifier brièvement si c'est un nombre premier.