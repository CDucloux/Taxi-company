# Taxi driver :taxi:______________________________________:taxi:

<img src="http://www.parisfaitsoncinema.com/cache/media/de-niro-590/cr%2C640%2C450-7f7085.jpg" width=40% height=40% align="right">

Shields à ajouter pour les tests qui sont passés, les test coverage, les dependencies et la version -> voir Shields.Io

- Il s'agit d'un problème de graphe **non-orienté et pondéré** 
- Le graphe est symétrique car pour chaque arrête $x - y$, il existe une arrête $y-x$ (on peut parcourir la route dans les deux sens)

## Présentation

La librairie `taxi_driver` permet de modéliser le problème suivant [(Lien vers le sujet)](https://github.com/CDucloux/Taxi-company/blob/main/Sujet.md) en termes de *graphe pondéré*.

Elle répondra aux exigeances suivantes :
- [x] Déterminer le chemin le plus court de la compagnie de taxi à l'aéroport
- [x] Déterminer les chemins les plus courts entre tous les points de la ville
- [x] Etudier l'impact d'un ralentissement ou d'une fluidification sur la route **9-13** $\Rightarrow$ Généralisation à tous les segments
- [ ] Les emplacements **(3,5,7,9,11)** sont en travaux $\Rightarrow$ Tout passage par un de ces lieux ajoute +1 minute au trajet

## Résolution



### Utilisation de la **Command Line Interface**

```python
py -m app emplacements
```

- Affiche la liste des emplacements disponibles de la ville.

```python
py -m app routes
```

- Affiche la liste des routes reliant des emplacements de la ville, et leur durée de parcours.

## Caractéristiques

- Module entièrement documenté sur l'interface publique et privée
- Formatage du code par `black` pour correspondre à la norme **PEP 8**
- Gestion des *dependencies* avec `poetry`
- Type checking avec `mypy`
- Création d'une `cli` avec `typer`
- Tests unitaires et tests d'intégrations avec `pytest` et couverture des tests avec `pytest-cov`
