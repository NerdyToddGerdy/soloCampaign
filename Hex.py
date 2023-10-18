from typing import Tuple

from DiceRolls import roll_for_terrain_change, roll_for_new_terrain, roll_die
from Dungeon import Dungeon
from Exploration import Exploration


def set_terrain(last_terrain: str) -> str:
    if roll_for_terrain_change():
        terrain = roll_for_new_terrain(last_terrain)
    else:
        terrain = last_terrain
    return terrain


def set_weather_type() -> str:
    roll = roll_die(6)
    match roll:
        case 1, 2, 3, 4:
            return "no weather"
        case 5:
            return "Light Precipitation"
        case 6:
            return "Heavy Precipitation"


def set_water_feature() -> str:
    roll = roll_die(6)
    match roll:
        case 1, 2, 3, 4:
            return "nothing"
        case 5:
            return "river"
        case 6:
            return "lake"


class Hex:
    coordinates: Tuple[int, int]
    terrain: str
    weather_type: str
    water_feature: str
    exploration_result: Exploration
    dungeon: Dungeon

    def __init__(self, coordinates: Tuple[int, int], last_terrain: str, ):
        self.coordinates = coordinates
        self.terrain = set_terrain(last_terrain)
        self.weather_type = set_weather_type()
        self.water_feature = set_water_feature()
        # self.exploration_result = set_exploration_result()


if __name__ == '__main__':
    hexagon = Hex((0, 0), 'Woods')
    print(hexagon.coordinates)
    print(hexagon.terrain)
