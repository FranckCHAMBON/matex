> _Les mathématiques sont la seule science où on ne sait pas de quoi on parle ni si ce qu'on dit est vrai._  
**Bertrand Russell** (Mathématicien, philosophe, et … doué d'humour !)

---

## Exercice 1
Soient $a$, $b$, $c$ trois entiers non nuls. Valider (en écrivant une preuve) ou infirmer (par un contre-exemple) les affirmations suivantes :
1. Si $a \mid b$ et $b \mid c$, alors $a \mid c$.
2. Si $a \mid b$ et $a \mid c$, alors $a$ divise tous les entiers de la forme $pb + qc$ avec $p$, $q$ entiers.
2. Si $c$ divise $2a$ alors $c$ divise $a$.
3. Si $c$ divise $a$, ou si $c$ divise $b$, alors $c$ divise $ab$.
4. Si $c$ divise $ab$, alors $c$ divise $a$ ou $c$ divise $b$.
5. Si $c$ divise $3a + 1$ et $5a − 1$, alors $c$ divise $8$.


---

## Exercice 2
1. Quel est le dernier chiffre de $7^{1337}$ ?
   - Conseil 1 : Voir d'abord pour : $7^{0} ; 7^{1} ; 7^{2} ; 7^{3} ; \dots$
   - Conseil 2 : deviner une règle, et la justifier.
2. Quel est le dernier chiffre de $7^{(1337^{42})}$ ?

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

## Exercice 4
Écrire $\sqrt{511\;104}$ sous la forme $a\sqrt{b}$, avec $a$ et $b$ entiers, et $b$ le plus petit possible.
