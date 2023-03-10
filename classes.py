from dataclasses import dataclass


@dataclass(frozen=True)
class Emplacement:
    """Représente un emplacement de la ville."""

    nom: int

@dataclass
class Itineraire:
    """Représente l'itinéraire qu'un client souhaite emprunter"""

    etapes: list[Emplacement]
      
      
@dataclass
class Carte:
    """Représentation de la carte de la ville."""

    emplacements: list[Emplacement]
    connexions: list[tuple[Emplacement, Emplacement, float]]

    def __post_init__(self):
        if any(poids <= 0 for _, _, poids in self.connexions):
            raise ValueError("Les durées des trajets sont forcément positives!")

        for depart, arrivee, _ in self.connexions:
            if depart not in self.emplacements:
                raise ValueError(f"L'emplacement {depart} n'existe pas dans la ville !")
            if arrivee not in self.emplacements:
                raise ValueError(f"L'emplacement {arrivee} n'existe pas dans la ville !")
