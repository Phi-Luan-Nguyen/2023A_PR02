from enum import Enum


class PokemonType(str, Enum):
    """
    Enumération des types de pokémons.
    """
    WATER = "EAU"
    FIRE = "FEU"
    GRASS = "PLANTE"

    def __str__(self):
        return self.value


class PokemonState(str, Enum):
    """
    Enumération des états de pokémons pouvant être induits par une attaque.
    """
    NORMAL = "NORMAL"
    FROZEN = "GELÉ"
    BURNED = "BRULÉ"
    POISONED = "EMPOISONNÉ"

    def __str__(self):
        return self.value
