from abc import ABC, abstractmethod
from pokemon_enums import PokemonState, PokemonType
from constants import MAX_HEALTH


class Pokemon():  # TODO: Rendez la classe Pokemon abstraite

    # TODO: Sauvegarder les paramètres dans des attributs privés (préfixés par __)
    # Initialisez l'attribut __health à MAX_HEALTH, l'attribut __state à PokemonState.NORMAL et l'attribut
    # __evolved à False.
    def __init__(self, name: str, attack: int, defense: int, type: PokemonType) -> None:
        pass

    # TODO: Ajouter "getters" pour les attributs privés en utilisant les décorateurs @property
    # Voici les noms des getters à utiliser: name, attack, defense, type, health, state, state_counter et evolved

    # Pour les setters suivant, vous devez vous assurer d'utiliser le décorateur "@nom_de_l_attribut.setter"
    # pour chaque attribut, ainsi que de valider les valeurs reçues avant de les affecter à l'attribut privé.

    # TODO: Ajouter le "setter" name, s'assurant de mettre à jour l'attribut uniquement si le nom n'est pas vide

    # TODO: Ajouter le "setter" attack, s'assurant de mettre à jour l'attribut uniquement si la valeur est positive

    # TODO: Ajouter le "setter" defense, s'assurant de mettre à jour l'attribut uniquement si la valeur est positive

    # TODO: Ajouter le "setter" state, s'assurant de mettre à jour l'attribut uniquement si la valeur est un state valide

    # TODO: Ajouter le "setter" state_counter, s'assurant de mettre à jour l'attribut uniquement si la valeur est positive

    # Pour les méthodes abstraites suivantes, vous devez vous assurer d'utiliser le décorateur "@abstractmethod".

    # TODO: Déclarer la signature de la méthode abstraite "get_attack_multiplier", qui prend en paramètre le type
    # du Pokémon attaqué (PokemonType) et qui retourne un nombre à virgule (float) représentant le multiplicateur

    # TODO: Déclarer la signature de la méthode abstraite "generate_random_induced_state", qui ne prend aucun
    # paramètre et qui retourne un tuple contenant un état (PokemonState) et un compteur d'état (int).

    # TODO: Déclarer la signature de la méthode abstraite "get_signature_sound", qui ne prend aucun paramètre et
    # qui retourne un string représentant le son caractéristique du Pokémon.

    # TODO: Déclarer la signature de la méthode abstraite "evolve", qui ne prend aucun paramètre et qui ne retourne
    # rien.

    # TODO: Implémenter la méthode non-abstraite decrement_state_counter, qui décrémente l'attribut __state_counter de 1, à moins que
    # sa valeur soit déjà à 0.

    # TODO: Implémenter la méthode non-abstraite "is_knocked_out", qui ne prend aucun paramètre et qui retourne un booléen indiquant si le Pokémon est
    # KO, c'est-à-dire si son attribut __health est à 0.)

    # TODO: Implémenter la méthode non-abstraite "heal" qui ne prend aucun paramètre et qui ne retourne rien. Cette méthode
    # met à jour l'attribut __health à MAX_HEALTH.
    
    # TODO: Implémenter la méthode spéciale __str__ qui retourne une chaîne de caractères décrivant le Pokémon, par
    # exemple: "Pikachu est de type ELECTRIC. Il a 112 points d'attaque et 96 points de défense."
    def __str__(self) -> str:
        pass

    # TODO: Implémenter la méthode spéciale __add__ qui surcharge l'opérateur "+", qui prend en paramètre un nombre
    # entier (int) représentant les points de vie à ajouter au Pokémon et qui ne retourne rien. Cette méthode doit
    # mettre à jour l'attribut __health en ajoutant les points de vie reçus à la santé actuelle du Pokémon. Si les
    # points de vie sont négatifs, ne faites rien.
    def __add__(self, health: int) -> None:
        pass

    # TODO: Implémenter la méthode spéciale __sub__ qui surcharge l'opérateur "-", qui prend en paramètre un nombre
    # entier (int) représentant les dégâts subis par le Pokémon et qui ne retourne rien. Cette méthode doit mettre à
    # jour l'attribut __health en soustrayant les dégâts reçus à la santé actuelle du Pokémon. Si les dégâts sont
    # négatifs, ne faites rien.
    def __sub__(self, damage: int) -> None:
        pass
