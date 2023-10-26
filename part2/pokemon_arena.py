import time
from abc import ABC

from pokemon_base import Pokemon, PokemonState
from constants import DELAY_GAME_START, DELAY_TURN, BURN_DAMAGE, POISON_DAMAGE


class PokemonArena(ABC):

    @staticmethod
    def fight(pokemon1: Pokemon, pokemon2: Pokemon) -> None:
        """
        Simule un combat tour par tour entre deux pokémons.

        @param pokemon1: Le premier pokémon
        @param pokemon2: Le deuxième pokémon
        """
        PokemonArena.display_intro(pokemon1, pokemon2)
        time.sleep(DELAY_GAME_START)
        turn = 0
        while not PokemonArena.is_game_over(pokemon1, pokemon2):
            print(f"====================== TOUR {turn} ======================")
            PokemonArena.handle_states(pokemon1, pokemon2)

            if not PokemonArena.is_game_over(pokemon1, pokemon2):
                for attacker, defender in [(pokemon1, pokemon2), (pokemon2, pokemon1)]:
                    PokemonArena.handle_turn(attacker, defender)

            PokemonArena.display_health(pokemon1, pokemon2)
            turn += 1
            time.sleep(DELAY_TURN)

        PokemonArena.display_winner(pokemon1, pokemon2)

    @staticmethod
    def handle_turn(attacker: Pokemon, defender: Pokemon) -> None:
        """
        Gère un tour de combat entre un pokémon attaquant et un pokémon défenseur.

        @param attacker: Le pokémon attaquant
        @param defender: Le pokémon défenseur
        """
        if attacker.state == PokemonState.FROZEN:
            print(
                f"{attacker.name} tente de bouger mais ses muscles ne répondent pas ! Il est gelé et ne peut pas attaquer !")
            return
        damage = PokemonArena.attack(attacker, defender)
        print(
            f"{attacker.name} attaque {defender.name} et lui inflige {damage} points de dégâts")
        PokemonArena.try_induce_state(attacker, defender)

    @staticmethod
    def is_game_over(pokemon1: Pokemon, pokemon2: Pokemon) -> bool:
        """
        Détermine si le combat est terminé.

        @param pokemon1: Le premier pokémon
        @param pokemon2: Le deuxième pokémon
        """
        return pokemon1.is_knocked_out() or pokemon2.is_knocked_out()

    # TODO: Implémenter la méthode suivante
    @staticmethod
    def attack(attacker: Pokemon, defender: Pokemon) -> int:
        """ 
        Calcule les dégâts infligés par l'attaquant au défenseur en fonction du multiplicateur de
        dégâts de l'attaquant, soustrait les dégâts aux points de vie du défenseur et retourne
        les dégâts infligés.

        @param attacker: Le pokémon attaquant
        @param defender: Le pokémon défenseur
        @return: Les dégâts infligés au défenseur
        """
        pass

    @staticmethod
    def apply_state_effect(pokemon: Pokemon) -> None:
        """
        Applique l'effet de l'état du pokémon.

        @param pokemon: Le pokémon dont l'état doit être appliqué
        """
        damage = 0
        match pokemon.state:
            case PokemonState.BURNED:
                damage = BURN_DAMAGE
            case PokemonState.POISONED:
                damage = POISON_DAMAGE
            case PokemonState.NORMAL | PokemonState.FROZEN:
                return

        pokemon - damage
        print(f"{pokemon.name} est {pokemon.state} et perd {damage} points de vie")

    @staticmethod
    def handle_states(*pokemons: Pokemon) -> None:
        """
        Gère les états de plusieurs pokémons en appliquant les effets des états et en décrémentant les compteurs.

        @param pokemons: Les pokémons dont les états doivent être gérés
        """
        for pokemon in pokemons:
            PokemonArena.apply_state_effect(pokemon)
            PokemonArena.decrement_state_counter(pokemon)

    @staticmethod
    def try_induce_state(attacker: Pokemon, defender: Pokemon) -> None:
        """
        Tente d'induire un nouvel état sur le pokémon défenseur en fonction de l'attaque du pokémon attaquant.

        @param attacker: Le pokémon attaquant
        @param defender: Le pokémon défenseur
        """
        if defender.state == PokemonState.NORMAL:
            newState, count = attacker.generate_random_induced_state()
            if newState is not PokemonState.NORMAL:
                defender.state = newState
                defender.state_counter = count
                print(f"{defender.name} est maintenant {newState} !")

    @staticmethod
    def decrement_state_counter(pokemon: Pokemon) -> None:
        """
        Décrémente le compteur de l'état du pokémon.

        @param pokemon: Le pokémon dont le compteur de l'état doit être décrémenté
        """
        pokemon.decrement_state_counter()

        if not pokemon.state_counter and pokemon.state != PokemonState.NORMAL:
            previousState = pokemon.state
            pokemon.state = PokemonState.NORMAL
            print(f"{pokemon.name} n'est plus {previousState}")

    @staticmethod
    def display_intro(pokemon1: Pokemon, pokemon2: Pokemon) -> None:
        """
        Affiche l'introduction du combat.

        @param pokemon1: Le premier pokémon
        @param pokemon2: Le deuxième pokémon
        """
        print(
            f"Un combat ÉPIQUE entre {pokemon1.name} et {pokemon2.name} est sur le point de commencer ! 🥊")
        print(pokemon1)
        print(pokemon2)
        print("Préparez-vous... 3... 2... 1... QUE LE MEILLEUR GAGNE ! 🎉")

    @staticmethod
    def display_health(pokemon1: Pokemon, pokemon2: Pokemon) -> None:
        """
        Affiche les points de vie des pokémons.

        @param pokemon1: Le premier pokémon
        @param pokemon2: Le deuxième pokémon
        """
        print(
            f"Points de vie: {pokemon1.name}: {pokemon1.health}, {pokemon2.name}: {pokemon2.health}\n")

    @staticmethod
    def display_winner(pokemon1: Pokemon, pokemon2: Pokemon) -> None:
        """
        Affiche le gagnant du combat.

        @param pokemon1: Le premier pokémon
        @param pokemon2: Le deuxième pokémon
        """
        if pokemon1.health == pokemon2.health:
            print("Quel retournement de situation ! C'est un match nul !")
            return

        winner = pokemon1 if pokemon2.is_knocked_out() else pokemon2
        print(f"{winner.name} a remporté le combat !🏆")
        print(winner.get_signature_sound())
