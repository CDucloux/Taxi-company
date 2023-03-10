# Taxi driver :taxi:

Shields à ajouter pour les tests qui sont passés, les test coverage, les dependencies et la version -> voir Shields.Io

- Il s'agit d'un problème de graphe **non-orienté** 

## Présentation

La librairie `taxi_driver` permet de modéliser le problème suivant [(Lien vers le sujet)](https://github.com/CDucloux/Taxi-company/blob/main/Sujet.md) en termes de *graphe pondéré*.

Elle répondra aux exigeances suivantes :
- Déterminer le chemin le plus court de la compagnie de taxi à l'aéroport
- Déterminer les chemins les plus courts entre tous les points de la ville
- Etudier l'impact d'un ralentissement ou d'une fluidification sur la route **9-13** $\Rightarrow$ Généralisation à tous les segments
- Les emplacements **(3,5,7,9,11)** sont en travaux $\Rightarrow$ Tout passage par un de ces lieux ajoute +1 minute au trajet

## Résolution

TODO

### Exemples

```python
Code pas encore implémenté
```

## Caractéristiques

- Module entièrement documenté sur l'interface publique et privée
- Formatage du code par `black` pour correspondre à la norme **PEP 8**
- Gestion des *dependencies* avec `poetry`
- Type checking avec `mypy`
- Tests unitaires et tests d'intégrations avec `pytest` et couverture des tests avec `pytest-cov`
