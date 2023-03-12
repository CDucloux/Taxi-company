from dataclasses import dataclass
import networkx as nx
import matplotlib.pyplot as plt


@dataclass(frozen=True)
class Emplacement:
    """Représente un emplacement de la ville."""

    nom: int

    def __str__(self):
        return str(self.nom)


@dataclass
class Itineraire:
    """Représente l'itinéraire qu'un client souhaite emprunter"""

    etapes: list[Emplacement]


@dataclass
class Ville:
    """Représentation de la carte de la ville."""

    emplacements: list[Emplacement]
    arretes: list[tuple[Emplacement, Emplacement, float]]

    def __post_init__(self):
        if any(poids <= 0 for _, _, poids in self.arretes):
            raise ValueError("Les durées des trajets sont forcément positives!")

        for depart, arrivee, _ in self.arretes:
            if depart not in self.emplacements:
                raise ValueError(f"L'emplacement {depart} n'existe pas dans la ville !")
            if arrivee not in self.emplacements:
                raise ValueError(
                    f"L'emplacement {arrivee} n'existe pas dans la ville !"
                )


def _convertit_en_nx(ville: Ville) -> nx.Graph:
    """Crée un graphe symmétrique à partir de la carte de la ville"""
    resultat = nx.Graph()
    resultat.add_nodes_from(ville.emplacements)
    resultat.add_edges_from(
        (depart, arrivee, {"duree": poids}) for depart, arrivee, poids in ville.arretes
    )
    return resultat


def carte_graphe(ville: Ville) -> nx.Graph:
    """Crée la représentation graphique d'une carte avec des points donnés"""
    resultat = _convertit_en_nx(ville)
    positions = nx.spring_layout(resultat)
    edge_labels = {(a, b): p["duree"] for a, b, p in resultat.edges(data=True)}
    nx.draw_networkx_nodes(resultat, positions, node_color="green", node_size=500)
    nx.draw_networkx_labels(resultat, positions)
    nx.draw_networkx_edges(resultat, positions, edge_color="gray")
    nx.draw_networkx_edge_labels(resultat, positions, edge_labels=edge_labels)
    plt.title("Carte de la ville")
    plt.show()

    return resultat


class PasDeChemin(Exception):
    pass


class EmplacementInconnu(Exception):
    pass


class MemeEmplacement(Exception):
    pass


class DureeNegative(Exception):
    pass


class ArreteInexistante(Exception):
    pass


def determine_trajet(
    depart: Emplacement, arrivee: Emplacement, ville: Ville
) -> Itineraire:
    """Détermine le trajet le plus court possible d'un emplacement à un autre."""
    if all(depart != emplacement for emplacement in ville.emplacements):
        raise EmplacementInconnu(
            f"Attention, {depart} n'est pas un emplacement valide !"
        )
    if all(arrivee != emplacement for emplacement in ville.emplacements):
        raise EmplacementInconnu(
            f"Attention, {arrivee} n'est pas un emplacement valide !"
        )
    if depart == arrivee:
        raise MemeEmplacement(
            "Attention, le point de départ et le point d'arrivée du trajet sont les mêmes !"
        )

    G = _convertit_en_nx(ville)
    try:
        resultat_nx = nx.shortest_path(
            G, source=depart, target=arrivee, weight="duree", method="bellman-ford"
        )
    except nx.exception.NetworkXNoPath:  # remarque : ne sert à rien (pour l'instant) car tous les nodes sont interconnectés
        raise PasDeChemin(f"{depart} et {arrivee} ne sont pas connectées !")
    return Itineraire(etapes=resultat_nx)


def genere_bouchons(
    depart: Emplacement, arrivee: Emplacement, duree: float, ville: Ville
) -> Ville:
    """Génère des bouchons à partir d'une arrête et d'une durée spécifiée."""
    if all(depart != emplacement for emplacement in ville.emplacements):
        raise EmplacementInconnu(
            f"Attention, {depart} n'est pas un emplacement valide !"
        )
    if all(arrivee != emplacement for emplacement in ville.emplacements):
        raise EmplacementInconnu(
            f"Attention, {arrivee} n'est pas un emplacement valide !"
        )
    if depart == arrivee:
        raise MemeEmplacement(
            "Attention, vous n'avez pas sélectionné une route, mais un emplacement de la ville!"
        )
    try:
        i = next(
            i
            for i, (u, v, d) in enumerate(ville.arretes)
            if (u.nom == depart.nom and v.nom == arrivee.nom)
            or (v.nom == depart.nom and u.nom == arrivee.nom)
        )
    except StopIteration as e:
        raise ArreteInexistante(
            f"La route spécifiée entre les emplacements {depart} et {arrivee} n'existe pas !"
        )
    else:
        u, v, d = ville.arretes[i]

        if (d + duree) <= 0:
            raise DureeNegative(
                "Attention, la durée de la fluidification spécifiée ne respecte pas les durées de trajets réels !"
            )
        ville.arretes[i] = (u, v, d + duree)
    return ville


def _constructeur_ville():
    (
        e_1,
        e_2,
        e_3,
        e_4,
        e_5,
        e_6,
        e_7,
        e_8,
        e_9,
        e_10,
        e_11,
        e_12,
        e_13,
        e_14,
        e_15,
        e_16,
    ) = emplacements = [
        Emplacement(nom=1),
        Emplacement(nom=2),
        Emplacement(nom=3),
        Emplacement(nom=4),
        Emplacement(nom=5),
        Emplacement(nom=6),
        Emplacement(nom=7),
        Emplacement(nom=8),
        Emplacement(nom=9),
        Emplacement(nom=10),
        Emplacement(nom=11),
        Emplacement(nom=12),
        Emplacement(nom=13),
        Emplacement(nom=14),
        Emplacement(nom=15),
        Emplacement(nom=16),
    ]
    return Ville(
        emplacements=emplacements,
        arretes=[
            (e_1, e_2, 5.0),
            (e_1, e_3, 9.0),
            (e_1, e_4, 4.0),
            (e_2, e_5, 3.0),
            (e_2, e_6, 2.0),
            (e_3, e_4, 4.0),
            (e_3, e_6, 1.0),
            (e_4, e_7, 7.0),
            (e_5, e_8, 4.0),
            (e_5, e_9, 2.0),
            (e_5, e_10, 9.0),
            (e_6, e_7, 3.0),
            (e_6, e_10, 9.0),
            (e_6, e_11, 6.0),
            (e_7, e_11, 8.0),
            (e_7, e_15, 5.0),
            (e_8, e_12, 5.0),
            (e_9, e_8, 3.0),
            (e_9, e_13, 10.0),
            (e_10, e_9, 6.0),
            (e_10, e_13, 5.0),
            (e_10, e_14, 1.0),
            (e_11, e_14, 2.0),
            (e_12, e_16, 9.0),
            (e_13, e_12, 4.0),
            (e_13, e_14, 3.0),
            (e_14, e_16, 4.0),
            (e_15, e_14, 4.0),
            (e_15, e_16, 3.0),
        ],
    )


CARTE_VILLE = _constructeur_ville()
