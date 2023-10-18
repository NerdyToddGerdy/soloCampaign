import random
from typing import List, Tuple, Dict


def roll_die(sides: int):
    return random.randint(1, sides)


def roll_for_strings(roll: int, return_string: str, values: List[str]):
    return f"{return_string} {values[roll - 1]}"


def roll_for_direction(
        roll: int, values: List[str], return_string: str,
        distance: int, coordinates: Tuple[int, int]
) -> Dict:
    return_value: dict = {}
    coordinate_a = coordinates[0]
    coordinate_b = coordinates[1]
    match roll:
        case 1:
            # north
            coordinate_b = coordinate_b + distance
        case 2:
            # northeast
            coordinate_a = coordinate_a + distance
        case 3:
            # southeast
            coordinate_a = coordinate_a + distance
            coordinate_b = coordinate_b - distance
        case 4:
            # south
            coordinate_b = coordinate_b - distance
        case 5:
            # southwest
            coordinate_a = coordinate_a - distance
        case 6:
            # northwest
            coordinate_a = coordinate_a - distance
            coordinate_b = coordinate_b + distance

    return_value['coordinates']: Tuple[int, int] = (
        coordinate_a,
        coordinate_b
    )
    return_value['message'] = f"{return_string} {values[roll - 1]}"
    return return_value


def roll_for_action(roll: int):
    match roll:
        case 1:
            return roll_for_strings(
                roll=roll_die(6),
                values=[
                    "a Powerful Person",
                    "an Organization",
                    "a Culture",
                    "an Artifact",
                    "an Old God",
                    "a Location",
                ],
                return_string='You must attack kill or destroy'
            )
        case 2:
            return roll_for_strings(
                roll=roll_die(6),
                values=[
                    "A way to another world",
                    "an individual",
                    "a hidden location",
                    "an artifact",
                    "a treasure",
                    "a magical location"
                ],
                return_string="You must find and/or recover"
            )
        case 3:
            return roll_for_strings(
                roll=roll_die(6),
                values=[
                    'an enemy',
                    'magical energy',
                    'knowledge',
                    'a powerful creature',
                    'a document',
                    'a message or a messenger'
                ],
                return_string='You need to either steal or capture'
            )
        case 4:
            return roll_for_strings(
                roll=roll_die(6),
                values=[
                    'an item',
                    'a prisoner',
                    'a message',
                    'an artifact',
                    'a merchant',
                    'a creature'
                ],
                return_string='You need to deliver'
            )
        case 5:
            return roll_for_strings(
                roll=roll_die(6),
                values=[
                    "an enemy's weakness",
                    "a rare resource",
                    "a new path",
                    "a temple",
                    "a truth about a plot",
                    "a new region"
                ],
                return_string="You need to explore or discover"
            )
        case 6:
            return roll_for_strings(
                roll=roll_die(6),
                values=[
                    'a cruel tyrant',
                    'a prison',
                    'hunters',
                    'a cult',
                    'a large creature',
                    'a battle'
                ],
                return_string='You need to survive or escape'
            )
        case _:
            return "That didn't work"


def roll_for_terrain_change() -> bool:
    roll = roll_die(6)
    if roll > 4:
        return True
    return False


def roll_for_new_terrain(last_terrain: str) -> str:
    new_terrain: str = ''
    roll = roll_die(6)
    match roll:
        case 1:
            new_terrain = "Grasslands"
        case 2:
            new_terrain = "Woods"
        case 3:
            new_terrain = "Hills"
        case 4:
            new_terrain = "Mountains"
        case 5:
            new_terrain = "Swamp"
        case 6:
            new_terrain = "Wasteland"
    if last_terrain == new_terrain:
        roll_for_new_terrain(last_terrain)
    return new_terrain


def roll_for_omen() -> str:
    roll = roll_die(6)
    match roll:
        case 1:
            return "sky"
        case 2:
            return "weather"
        case 3:
            return "animal"
        case 4:
            return "fire"
        case 5:
            return "voice"
        case 6:
            return "NPC"


def roll_for_discovery_type() -> str:
    roll = roll_die(6)
    match roll:
        case 1:
            return "unnatural"
        case 2:
            return "natural"
        case 3:
            return "ruin"
        case 4:
            return "settlement"
        case 5:
            return "evidence"
        case 6:
            return "passive"


discovery_dict: dict = {
    "unnatural": (
        "portal",
        "glowing",
        "residue",
        "cursed",
        "burn",
        "mutation"
    ),
    "natural": (
        "cave",
        "landmark",
        "nest",
        "water",
        "resource",
        "ravine"
    ),
    "ruin": (
        "abbey",
        "tower",
        "estate",
        "lair",
        "burial",
        "dungeon"
    ),
    "settlement": (
        "village",
        "village",
        "village",
        "town",
        "outpost",
        "city"
    ),
    "evidence": (
        "tracks",
        "camp",
        "bones",
        "tools",
        "supplies",
        "violence"
    ),
    "passive": (
        "wounded",
        "traveler",
        "merchant",
        "camp",
        "cleric",
        "animal"
    )
}


def roll_for_discovery(discovery_type: str) -> str:
    roll: int = roll_die(6)
    return discovery_dict.get(discovery_type)[roll - 1]


def roll_for_danger_type() -> str:
    roll: int = roll_die(3)
    match roll:
        case 1:
            return "unnatural"
        case 2:
            return "hazard"
        case 3:
            return "hostile"


encounter_type_tuple: tuple = (
    "human",
    "animal",
    "humanoid",
    "monster (s)",
    "monster (l)",
    "unnatural"
)

danger_dict: dict = {
    "unnatural": (
        "ghoul",
        "zombie",
        "skeleton",
        "demon",
        "elemental",
        "wraith"
    ),
    "hazard": (
        "bog",
        "landslide",
        "sinkhole",
        "poison",
        "resources",
        "ambush"
    ),
    "hostile": {
        "grasslands": (
            0,
            0,
            1,
            1,
            2,
            3
        ),
        "woods": (
            0,
            1,
            2,
            2,
            3,
            4
        ),
        "hills": (
            0,
            1,
            2,
            3,
            4,
            4
        ),
        "mountains": (
            0,
            1,
            2,
            2,
            4,
            4
        ),
        "swamps": (
            0,
            1,
            2,
            5,
            5,
            3
        ),
        "wastelands": (
            0,
            2,
            2,
            5,
            3,
            4
        )
    }
}


def roll_for_danger(danger_type: str, terrain: str) -> str:
    roll: int = roll_die(6)
    match danger_type:
        case "unnatural":
            return danger_dict.get(danger_type)[roll]
        case "hazard":
            return danger_dict.get(danger_type)[roll]
        case "hostile":
            return danger_dict.get(danger_type).get(terrain)[roll]


