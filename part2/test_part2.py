import unittest
from abc import ABC
import inspect

from pokemon_enums import PokemonType, PokemonState
from pokemon_base import Pokemon
from pokemon_types import PokemonFireType, PokemonWaterType, PokemonGrassType
from pokemons import Squirtle, Charmander, Bulbasaur
from pokemon_arena import PokemonArena
from constants import MAX_HEALTH
from testing_constants import Stubs


class ConcreteTypePokemonImpl:
    def get_signature_sound(self) -> str:
        return "No sound"

    def evolve(self) -> None:
        pass


class ConcreteBasePokemonImpl(ConcreteTypePokemonImpl):
    def get_attack_multiplier(self, pokemon_type: PokemonType) -> float:
        super().get_attack_multiplier(pokemon_type)

    def generate_random_induced_state(self) -> (PokemonState, int):
        return (None, None)


class TestUtils:
    @staticmethod
    def is_constructor_one_liner(pokemon_class: Pokemon):
        constructor_source = inspect.getsource(pokemon_class.__init__)
        line_count = constructor_source.count('\n')

        if '@' in constructor_source:
            line_count -= constructor_source.count('@')

        return line_count == 2  # One line for signature, one line for parent constructor call


class TestPokemonBase(unittest.TestCase):

    class PokemonBaseMock(ConcreteBasePokemonImpl, Pokemon):
        def __init__(self, name: str, attack: int, defense: int, type: PokemonType) -> None:
            super().__init__(name, attack, defense, type)

    def setUp(self):
        self.pokemon_base = self.PokemonBaseMock(Stubs.SQUIRTLE.NAME, Stubs.SQUIRTLE.ATTACK,
                                                 Stubs.SQUIRTLE.DEFENSE, Stubs.SQUIRTLE.TYPE)

    def test_abstract_class(self):
        self.assertTrue(issubclass(Pokemon, ABC))

    def test_private_attributes(self):
        self.assertEqual(self.pokemon_base._Pokemon__name,
                         Stubs.SQUIRTLE.NAME)
        self.assertEqual(self.pokemon_base._Pokemon__attack,
                         Stubs.SQUIRTLE.ATTACK)
        self.assertEqual(self.pokemon_base._Pokemon__defense,
                         Stubs.SQUIRTLE.DEFENSE)
        self.assertEqual(self.pokemon_base._Pokemon__type,
                         Stubs.SQUIRTLE.TYPE)
        self.assertEqual(self.pokemon_base._Pokemon__health,
                         MAX_HEALTH)
        self.assertEqual(self.pokemon_base._Pokemon__state,
                         PokemonState.NORMAL)
        self.assertEqual(self.pokemon_base._Pokemon__state_counter, 0)
        self.assertEqual(self.pokemon_base._Pokemon__evolved, False)

    def test_properties_name(self):
        self.assertEqual(self.pokemon_base.name,
                         self.pokemon_base._Pokemon__name)

    def test_properties_attack(self):
        self.assertEqual(self.pokemon_base.attack,
                         self.pokemon_base._Pokemon__attack)

    def test_properties_defense(self):
        self.assertEqual(self.pokemon_base.defense,
                         self.pokemon_base._Pokemon__defense)

    def test_properties_type(self):
        self.assertEqual(self.pokemon_base.type,
                         self.pokemon_base._Pokemon__type)

    def test_properties_health(self):
        self.assertEqual(self.pokemon_base.health,
                         self.pokemon_base._Pokemon__health)

    def test_properties_state(self):
        self.assertEqual(self.pokemon_base.state,
                         self.pokemon_base._Pokemon__state)

    def test_properties_state_counter(self):
        self.assertEqual(self.pokemon_base.state_counter,
                         self.pokemon_base._Pokemon__state_counter)

    def test_properties_evolved(self):
        self.assertEqual(self.pokemon_base.evolved,
                         self.pokemon_base._Pokemon__evolved)

    def test_name_setter(self):
        self.pokemon_base.name = "NewName"
        self.assertEqual(self.pokemon_base._Pokemon__name, "NewName")
        self.pokemon_base.name = ""
        self.assertEqual(self.pokemon_base._Pokemon__name, "NewName",
                         "Le nom ne devrait pas être modifié si il est vide")

    def test_attack_setter(self):
        self.pokemon_base.attack = 200
        self.assertEqual(self.pokemon_base._Pokemon__attack, 200)
        self.pokemon_base.attack = -10
        self.assertEqual(self.pokemon_base._Pokemon__attack, 0,
                         "L'attaque ne devrait jamais avoir une valeur négative")

    def test_defense_setter(self):
        self.pokemon_base.defense = 200
        self.assertEqual(self.pokemon_base._Pokemon__defense, 200)
        self.pokemon_base.defense = -10
        self.assertEqual(self.pokemon_base._Pokemon__defense, 0,
                         "La défense ne devrait jamais avoir une valeur négative")

    def test_state_setter(self):
        self.pokemon_base.state = PokemonState.FROZEN
        self.assertEqual(self.pokemon_base._Pokemon__state,
                         PokemonState.FROZEN)
        self.pokemon_base.state = "INVALID_STATE"
        self.assertEqual(self.pokemon_base._Pokemon__state, PokemonState.FROZEN,
                         "L'état ne devrait pas être modifié si il est invalide")

    def test_state_counter_setter(self):
        self.pokemon_base.state_counter = 5
        self.assertEqual(self.pokemon_base._Pokemon__state_counter, 5)
        self.pokemon_base.state_counter = -1
        self.assertEqual(self.pokemon_base._Pokemon__state_counter, 0,
                         "Le compteur d'état ne devrait jamais avoir une valeur négative")

    def test_decrement_state_counter(self):
        self.pokemon_base._Pokemon__state_counter = 5
        self.pokemon_base.decrement_state_counter()
        self.assertEqual(self.pokemon_base._Pokemon__state_counter, 4)

        self.pokemon_base._Pokemon__state_counter = 0
        self.pokemon_base.decrement_state_counter()
        self.assertEqual(self.pokemon_base._Pokemon__state_counter, 0)

    def test_is_knocked_out(self):
        self.pokemon_base._Pokemon__health = 0
        self.assertTrue(self.pokemon_base.is_knocked_out())

        self.pokemon_base._Pokemon__health = 10
        self.assertFalse(self.pokemon_base.is_knocked_out())

    def test_heal(self):
        self.pokemon_base._Pokemon__health = 0
        self.pokemon_base.heal()
        self.assertEqual(self.pokemon_base._Pokemon__health, MAX_HEALTH)

    def test_get_attack_multiplier_implementation(self):
        self._assert_is_method_abstract("get_attack_multiplier")

    def test_generate_random_induced_state_implementation(self):
        self._assert_is_method_abstract("generate_random_induced_state")

    def test_get_signature_sound_implementation(self):
        self._assert_is_method_abstract("get_signature_sound")

    def test_evolve_implementation(self):
        self._assert_is_method_abstract("evolve")

    def test_str(self):
        expected_str = f"Squirtle est de type EAU. Il a 48 points d'attaque et 65 points de défense."
        self.assertEqual(str(self.pokemon_base), expected_str)

    def test_add(self):
        self.pokemon_base._Pokemon__health = MAX_HEALTH // 2
        initial_health = self.pokemon_base._Pokemon__health
        self.pokemon_base + 20
        self.assertEqual(self.pokemon_base._Pokemon__health,
                         initial_health + 20)

        self.pokemon_base._Pokemon__health = MAX_HEALTH
        self.pokemon_base + 20
        self.assertEqual(self.pokemon_base._Pokemon__health,
                         MAX_HEALTH, "La vie ne devrait pas dépasser la valeur maximale")

    def test_sub(self):
        self.pokemon_base._Pokemon__health = MAX_HEALTH // 2
        initial_health = self.pokemon_base._Pokemon__health
        self.pokemon_base - 20
        self.assertEqual(self.pokemon_base._Pokemon__health,
                         initial_health - 20)

        self.pokemon_base._Pokemon__health = 0
        self.pokemon_base - 20
        self.assertEqual(self.pokemon_base._Pokemon__health,
                         0, "La vie ne devrait pas être négative")

    def _assert_is_method_abstract(self, method_name: str):
        method_exists = method_name in dir(Pokemon)
        self.assertTrue(method_exists,
                        f"La méthode {method_name} doit être implémentée")

        is_abstract = method_name in Pokemon.__abstractmethods__
        self.assertTrue(is_abstract,
                        f"La méthode {method_name} doit être abstraite")


class TestPokemonTypes(unittest.TestCase):

    def setUp(self):
        self.pokemon_fire = self._pokemon_type_mock_generator(PokemonFireType, Stubs.CHARMANDER.NAME, Stubs.CHARMANDER.ATTACK,
                                                              Stubs.CHARMANDER.DEFENSE)
        self.pokemon_water = self._pokemon_type_mock_generator(PokemonWaterType, Stubs.SQUIRTLE.NAME, Stubs.SQUIRTLE.ATTACK,
                                                               Stubs.SQUIRTLE.DEFENSE)
        self.pokemon_grass = self._pokemon_type_mock_generator(PokemonGrassType, Stubs.BULBASAUR.NAME, Stubs.BULBASAUR.ATTACK,
                                                               Stubs.BULBASAUR.DEFENSE)

    def test_pokemon_fire_inheritance(self):
        self._test_inheritance(PokemonFireType)

    def test_pokemon_water_inheritance(self):
        self._test_inheritance(PokemonWaterType)

    def test_pokemon_grass_inheritance(self):
        self._test_inheritance(PokemonGrassType)

    def test_pokemon_fire_constructor(self):
        self._test_constructor(self.pokemon_fire, Stubs.CHARMANDER)
        self.assertTrue(TestUtils.is_constructor_one_liner(
            PokemonFireType), "Le constructeur de PokemonFireType doit être sur une seule ligne")

    def test_pokemon_water_constructor(self):
        self._test_constructor(self.pokemon_water, Stubs.SQUIRTLE)
        self.assertTrue(TestUtils.is_constructor_one_liner(
            PokemonWaterType), "Le constructeur de PokemonWaterType doit être sur une seule ligne")

    def test_pokemon_grass_constructor(self):
        self._test_constructor(self.pokemon_grass, Stubs.BULBASAUR)
        self.assertTrue(TestUtils.is_constructor_one_liner(
            PokemonGrassType), "Le constructeur de PokemonGrassType doit être sur une seule ligne")

    def test_get_attack_multiplier_fire(self):
        self.pokemon_fire = self._pokemon_type_mock_generator(PokemonFireType, Stubs.CHARMANDER.NAME, Stubs.CHARMANDER.ATTACK,
                                                              Stubs.CHARMANDER.DEFENSE, False)
        self.assertEqual(self.pokemon_fire.get_attack_multiplier(
            PokemonType.FIRE), 1.0)
        self.assertEqual(self.pokemon_fire.get_attack_multiplier(
            PokemonType.WATER), 0.75)
        self.assertEqual(self.pokemon_fire.get_attack_multiplier(
            PokemonType.GRASS), 1.25)

    def test_get_attack_multiplier_water(self):
        self.pokemon_water = self._pokemon_type_mock_generator(PokemonWaterType, Stubs.SQUIRTLE.NAME, Stubs.SQUIRTLE.ATTACK,
                                                               Stubs.SQUIRTLE.DEFENSE, False)

        self.assertEqual(self.pokemon_water.get_attack_multiplier(
            PokemonType.FIRE), 1.25)
        self.assertEqual(self.pokemon_water.get_attack_multiplier(
            PokemonType.WATER), 1.0)
        self.assertEqual(self.pokemon_water.get_attack_multiplier(
            PokemonType.GRASS), 0.75)

    def test_get_attack_multiplier_grass(self):
        self.pokemon_grass = self._pokemon_type_mock_generator(PokemonGrassType, Stubs.BULBASAUR.NAME, Stubs.BULBASAUR.ATTACK,
                                                               Stubs.BULBASAUR.DEFENSE, False)
        self.assertEqual(self.pokemon_grass.get_attack_multiplier(
            PokemonType.FIRE), 0.75)
        self.assertEqual(self.pokemon_grass.get_attack_multiplier(
            PokemonType.WATER), 1.25)
        self.assertEqual(self.pokemon_grass.get_attack_multiplier(
            PokemonType.GRASS), 1.0)

    def _test_constructor(self, pokemon: Pokemon, stub: Stubs):
        self.assertEqual(pokemon.name, stub.NAME)
        self.assertEqual(pokemon.attack, stub.ATTACK)
        self.assertEqual(pokemon.defense, stub.DEFENSE)
        self.assertEqual(pokemon.type, stub.TYPE)

    def _pokemon_type_mock_generator(self, type_class, name: str, attack: int, defense: int, with_get_attack_multiplier: bool = True):
        base_class = ConcreteBasePokemonImpl if with_get_attack_multiplier else ConcreteTypePokemonImpl

        class PokemonTypeMock(base_class, type_class):
            def __init__(self, name: str, attack: int, defense: int) -> None:
                super().__init__(name, attack, defense)

        return PokemonTypeMock(name, attack, defense)

    def _test_inheritance(self, pokemon_class):
        self.assertTrue(issubclass(pokemon_class, Pokemon),
                        f"{pokemon_class.__name__} doit hériter de Pokemon")

        second_base = pokemon_class.__bases__[1] if len(
            pokemon_class.__bases__) > 1 else None
        self.assertEqual(second_base, ABC,
                         f"{pokemon_class.__name__} doit être une classe abstraite")


class TestConcretePokemons(unittest.TestCase):
    def test_squirtle_inheritance(self):
        self.assertTrue(issubclass(Squirtle, PokemonWaterType))

    def test_charmander_inheritance(self):
        self.assertTrue(issubclass(Charmander, PokemonFireType))

    def test_bulbasaur_inheritance(self):
        self.assertTrue(issubclass(Bulbasaur, PokemonGrassType))

    def test_squirtle_constructor(self):
        self._manual_set_up_squirtle()
        self._test_constructor(self.squirtle, Stubs.SQUIRTLE, Squirtle)

    def test_charmander_constructor(self):
        self._manual_set_up_charmander()
        self._test_constructor(self.charmander, Stubs.CHARMANDER, Charmander)

    def test_bulbasaur_constructor(self):
        self._manual_set_up_bulbasaur()
        self._test_constructor(self.bulbasaur, Stubs.BULBASAUR, Bulbasaur)

    def test_squirtle_evolve(self):
        self._manual_set_up_squirtle()
        self._test_evolve(self.squirtle, Stubs.WARTORTLE)

    def test_charmander_evolve(self):
        self._manual_set_up_charmander()
        self._test_evolve(self.charmander, Stubs.CHARMELEON)

    def test_bulbasaur_evolve(self):
        self._manual_set_up_bulbasaur()
        self._test_evolve(self.bulbasaur, Stubs.IVYSAUR)

    def test_squirtle_get_signature_sound(self):
        self._manual_set_up_squirtle()
        self.assertEqual(self.squirtle.get_signature_sound(),
                         "Squirtle-squirtle")

    def test_charmander_get_signature_sound(self):
        self._manual_set_up_charmander()
        self.assertEqual(self.charmander.get_signature_sound(),
                         "Char-char")

    def test_bulbasaur_get_signature_sound(self):
        self._manual_set_up_bulbasaur()
        self.assertEqual(self.bulbasaur.get_signature_sound(),
                         "Bulba-bulba")

    def _test_evolve(self, pokemon, results_stub):
        pokemon.evolve()
        self.assertEqual(pokemon.name, results_stub.NAME)
        self.assertEqual(pokemon.attack, results_stub.ATTACK)
        self.assertEqual(pokemon.defense, results_stub.DEFENSE)

    def _test_constructor(self, pokemon: Pokemon, stub: Stubs, pokemon_class):
        self.assertEqual(pokemon.name, stub.NAME)
        self.assertEqual(pokemon.attack, stub.ATTACK)
        self.assertEqual(pokemon.defense, stub.DEFENSE)
        self.assertEqual(pokemon.type, stub.TYPE)
        self.assertTrue(TestUtils.is_constructor_one_liner(
            pokemon_class), f"Le constructeur de {pokemon_class.__name__} doit être sur une seule ligne")

    def _generate_mock_pokemon(self, pokemon_class):
        class MockConcretePokemon(ConcreteTypePokemonImpl, pokemon_class):
            def __init__(self) -> None:
                pokemon_class.__init__(self)

            def evolve(self) -> None:
                if hasattr(pokemon_class, "evolve"):
                    pokemon_class.evolve(self)

            def get_signature_sound(self) -> str:
                if hasattr(pokemon_class, "get_signature_sound"):
                    return pokemon_class.get_signature_sound(self)
                return "No sound"

        return MockConcretePokemon()

    def _manual_set_up_squirtle(self):
        self.squirtle = self._generate_mock_pokemon(Squirtle)

    def _manual_set_up_charmander(self):
        self.charmander = self._generate_mock_pokemon(Charmander)

    def _manual_set_up_bulbasaur(self):
        self.bulbasaur = self._generate_mock_pokemon(Bulbasaur)


class TestPokemonArena(unittest.TestCase):

    def setUp(self):
        self.charmander = Charmander()
        self.squirtle = Squirtle()

    def test_attack_correct_damage(self):
        health = self.squirtle.health
        PokemonArena.attack(self.charmander, self.squirtle)
        self.assertEqual(self.squirtle.health, health - 39)

        health = self.charmander.health
        PokemonArena.attack(self.squirtle, self.charmander)
        self.assertEqual(self.charmander.health, health - 60)

    def test_attack_return_value(self):
        self.assertEqual(PokemonArena.attack(self.charmander, self.squirtle), 39)
        self.assertEqual(PokemonArena.attack(self.squirtle, self.charmander), 60)

if __name__ == '__main__':
    unittest.main()
