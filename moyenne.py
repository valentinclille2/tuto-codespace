"""Ce module fournit une fonction pour calculer une moyenne de valeurs"""

# NB: Ce fichier contient du code à compléter

from rich.markdown import Markdown
from rich.console import Console


def moyenne(valeurs):
    """Calcule la moyenne des valeurs d'une liste."""
    A = 0
    n = len(valeurs)
    if n == 0:
        raise ValueError("La liste ne doit pas être vide")
    for i in range(n):
        A += valeurs[i]
    return A/n


if __name__ == "__main__":
    Console().print(Markdown(moyenne.__doc__))
    print("moyenne([10, 20, 15]) :", end=" ")
    print(moyenne([10, 20, 15]))
