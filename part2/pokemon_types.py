from abc import ABC
import random

from pokemon_base import Pokemon
from pokemon_enums import PokemonType, PokemonState
from constants import BURN_PROBABILITY, FREEZE_PROBABILITY, POISON_PROBABILITY


# TODO: Héritez de la classe Pokemon de base et rendez cette classe abstraite.
class PokemonFireType():

    # TODO: Utilisez le constructeur de la classe parent pour initialiser les attributs en spécifiant le
    # type de Pokémon à PokemonType.FIRE.
    # Important: Il est nécessaire d'utiliser le constructeur de la classe PARENT.
    def __init__(self, name: str, attack: int, defense: int) -> None:
        pass

    # TODO: "Override" la méthode abstraite du parent "get_attack_multiplier", qui prend en paramètre le type
    # du Pokémon attaqué (PokemonType) et qui retourne un nombre à virgule (float) représentant le multiplicateur.
    # Le multiplicateur est de 1.25 si le Pokémon attaqué est de type PLANTE, 0.75 si le Pokémon attaqué est de type
    # EAU et 1.0 dans tous les autres cas.

    def generate_random_induced_state(self) -> (PokemonState, int):
        """
        Induit un état "brûlé" pour 2 tours avec une probabilité de 20%.

        @return: Un tuple contenant l'état induit et le nombre de tours de cet état
        """
        burned = random.random() <= BURN_PROBABILITY
        return (PokemonState.BURNED, 2) if burned else (PokemonState.NORMAL, 0)


# TODO: Héritez de la classe Pokemon de base et rendez cette classe abstraite.
class PokemonWaterType():

    # TODO: Utilisez le constructeur de la classe parent pour initialiser les attributs en spécifiant le
    # type de Pokémon à PokemonType.WATER.
    # Important: Il est nécessaire d'utiliser le constructeur de la classe PARENT.
    def __init__(self, name: str, attack: int, defense: int) -> None:
        pass

    # TODO: "Override" la méthode abstraite du parent "get_attack_multiplier", qui prend en paramètre le type
    # du Pokémon attaqué (PokemonType) et qui retourne un nombre à virgule (float) représentant le multiplicateur.
    # Le multiplicateur est de 1.25 si le Pokémon attaqué est de type FEU, 0.75 si le Pokémon attaqué est de type
    # PLANTE et 1.0 dans tous les autres cas.

    def generate_random_induced_state(self) -> (PokemonState, int):
        """
        Induit un état "gelé" pour 3 tours avec une probabilité de 15%.

        @return: Un tuple contenant l'état induit et le nombre de tours de cet état
        """
        frozen = random.random() <= FREEZE_PROBABILITY
        return (PokemonState.FROZEN, 3) if frozen else (PokemonState.NORMAL, 0)


# TODO: Héritez de la classe Pokemon de base et rendez cette classe abstraite.
class PokemonGrassType():

    # TODO: Utilisez le constructeur de la classe parent pour initialiser les attributs en spécifiant le
    # type de Pokémon à PokemonType.GRASS.
    # Important: Il est nécessaire d'utiliser le constructeur de la classe PARENT.
    def __init__(self, name: str, attack: int, defense: int) -> None:
        pass

    # TODO: "Override" la méthode abstraite du parent "get_attack_multiplier", qui prend en paramètre le type
    # du Pokémon attaqué (PokemonType) et qui retourne un nombre à virgule (float) représentant le multiplicateur.
    # Le multiplicateur est de 1.25 si le Pokémon attaqué est de type EAU, 0.75 si le Pokémon attaqué est de type
    # FEU et 1.0 dans tous les autres cas.

    def generate_random_induced_state(self) -> (PokemonState, int):
        """
        Induit un état "empoisonné" pour 3 tours avec une probabilité de 20%.

        @return: Un tuple contenant l'état induit et le nombre de tours de cet état
        """
        poisoned = random.random() <= POISON_PROBABILITY
        return (PokemonState.POISONED, 3) if poisoned else (PokemonState.NORMAL, 0)
