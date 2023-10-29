from dataclasses import dataclass
from pokemon_enums import PokemonType


@dataclass
class SquirtleStub:
    NAME = "Squirtle"
    ATTACK = 48
    DEFENSE = 65
    TYPE = PokemonType.WATER


@dataclass
class CharmanderStub:
    NAME = "Charmander"
    ATTACK = 52
    DEFENSE = 43
    TYPE = PokemonType.FIRE


@dataclass
class BulbasaurStub:
    NAME = "Bulbasaur"
    ATTACK = 49
    DEFENSE = 49
    TYPE = PokemonType.GRASS


@dataclass
class WarTortleStub:
    NAME = "Wartortle"
    ATTACK = 63
    DEFENSE = 80
    TYPE = PokemonType.WATER


@dataclass
class CharmeleonStub:
    NAME = "Charmeleon"
    ATTACK = 64
    DEFENSE = 58
    TYPE = PokemonType.FIRE


@dataclass
class IvysaurStub:
    NAME = "Ivysaur"
    ATTACK = 62
    DEFENSE = 63
    TYPE = PokemonType.GRASS


@dataclass
class Stubs:
    SQUIRTLE = SquirtleStub
    CHARMANDER = CharmanderStub
    BULBASAUR = BulbasaurStub
    WARTORTLE = WarTortleStub
    CHARMELEON = CharmeleonStub
    IVYSAUR = IvysaurStub
