from tkinter import ttk
from typing import List, Dict, Tuple
from random import randint

from DiceRolls import roll_die

races: List[str] = ["Human", "Dwarf", "Hafling"]





class AbilityScores:
    class_score_order: Dict[str, dict] = {
        "Fighter": {
            'strength': 0,
            'constitution': 0,
            'dexterity': 0,
            'wisdom': 0,
            'charisma': 0,
            'intelligence': 0,
        },
        "Wizard": {
            'intelligence': 0,
            'constitution': 0,
            'dexterity': 0,
            'wisdom': 0,
            'charisma': 0,
            'strength': 0,
        },
        "Rogue": {
            'dexterity': 0,
            'constitution': 0,
            'wisdom': 0,
            'charisma': 0,
            'intelligence': 0,
            'strength': 0,
        }
    }

    def __init__(self):
        self._charisma = None
        self._strength = None
        self._dexterity = None
        self._constitution = None
        self._intelligence = None
        self._wisdom = None

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        self._strength = value

    @property
    def dexterity(self):
        return self._dexterity

    @dexterity.setter
    def dexterity(self, value):
        self._dexterity = value

    @property
    def constitution(self):
        return self._constitution

    @constitution.setter
    def constitution(self, value):
        self._constitution = value

    @property
    def intelligence(self):
        return self._intelligence

    @intelligence.setter
    def intelligence(self, value):
        self._intelligence = value

    @property
    def wisdom(self):
        return self._wisdom

    @wisdom.setter
    def wisdom(self, value):
        self._wisdom = value

    @property
    def charisma(self):
        return self._charisma

    @charisma.setter
    def charisma(self, value):
        self._charisma = value



genders: List[str] = ["Male", "Female", "Other"]


def __get_random_name__(race) -> str:
    human_first_names = ['Liam', 'Thicken', 'Will', 'Kat', 'Sophia', 'Holly']
    human_last_names = ['Smith', 'Brown', 'Green']
    dwarf_first_names = ['Kurzan', 'Gimli', 'Damien', 'Amber', 'Artin', 'Audhild']
    dwarf_last_names = ['Battlehammer', 'Bonetank', 'Ironhand']
    halfling_first_names = ['Frodo', 'Samwise', 'Pippin', 'Andry', 'Callie', 'Jillian']
    halfling_last_names = ['Baggins', 'Gamgie', 'Took']
    match race:
        case "Human":
            return f'{human_first_names[randint(0, len(human_first_names) - 1)]} {human_last_names[randint(0, len(human_last_names) - 1)]}'
        case "Dwarf":
            return f'{dwarf_first_names[randint(0, len(dwarf_first_names) - 1)]} {dwarf_last_names[randint(0, len(dwarf_last_names) - 1)]}'
        case "Halfling":
            return f'{halfling_first_names[randint(0, len(halfling_first_names) - 1)]} {halfling_last_names[randint(0, len(halfling_last_names) - 1)]}'


class Character:
    name: str
    race: str
    character_class: str
    gender: str
    ability_scores: AbilityScores
    level: int

    def __init__(
            self,
            race: str,
            character_class: str,
            gender: str
    ):
        self.name = __get_random_name__(race)
        self.race = race
        self.character_class = character_class
        self.gender = gender
        self.level = 1
        self.ability_scores = AbilityScores()
        self.inventory = ['Test Inventory Item']

    def view_character_gen_info(self, location: ttk.LabelFrame):
        gen_info = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__") and not attr.startswith("ability") and not attr.startswith('inv')]
        for info in gen_info:
            ttk.Label(location, text=f'{info.replace("_", " ").title()}: {getattr(self, info)}').grid(
                column=0, sticky='W')

    def view_character_stats(self, location: ttk.LabelFrame):
        for key, value in AbilityScores.class_score_order.get('Fighter').items():
            ttk.Label(location,
                      text=f'{key.title()}: {getattr(self.ability_scores, key)}').grid(
                column=3, sticky='W'
            )

    def set_ability_scores(self):
        ability_scores = ['strength',
                          'constitution',
                          'dexterity',
                          'wisdom',
                          'charisma',
                          'intelligence']
        # ability_score_order: tuple = class_score_order.get(self.character_class)
        die_roll_results = []

        for score in ability_scores:
            die_roll_results.append(roll_die(20))
        sorted_rolls = die_roll_results.sort(reverse=True)
        roll_num = 0
        for key, value in self.ability_scores.class_score_order.get(self.character_class).items():
            die = roll_die(20)
            setattr(self.ability_scores, key, sorted(die_roll_results, reverse=True)[roll_num])
            roll_num = roll_num + 1
            # self.ability_scores.__setattr__(key, roll_die(20))

    def view_character_inventory(self, location: ttk.LabelFrame):
        # Inventory Section
        # TODO: Create the inventory section
        ttk.Label(location, text='Here is the future Inventory').grid()
        for item in self.inventory:
            ttk.Label(location, text=f'{item}').grid(column=0,
                                                     sticky='W')
