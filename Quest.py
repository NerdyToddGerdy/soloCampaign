from typing import Tuple

from DiceRolls import roll_die, roll_for_direction, roll_for_action


def direction(roll: int, current_coordinates: Tuple[int, int], distance: int) -> dict:
    return roll_for_direction(
        roll=roll,
        values=[
            'north',
            'north east',
            'south east',
            'south',
            'south west',
            'north_west'
        ],
        return_string='Your objective is in the direction of',
        distance=distance,
        coordinates=current_coordinates
    )


class Quest:
    action: str
    distance: int
    direction: dict
    location: Tuple[int, int]

    def __init__(self, current_location: Tuple[int, int]):
        """
        Creates a new quest for the adventure
        :param current_location: Tuple[int, int] Input the location the player is currently
        """
        self.action = roll_for_action(roll_die(6))
        self.distance = roll_die(4)
        self.direction = direction(
            roll_die(6),
            current_coordinates=current_location,
            distance=self.distance
        )

    def get_action(self) -> str:
        """
        Get the action for the quest
        :return: str: the current quest
        """
        return self.action

    def get_distance(self):
        return f'distance is {self.distance} hexes away'

    def get_direction_message(self):
        return self.direction['message']

    def get_direction_coordinates(self):
        return self.direction['coordinates']

    def print_results(self):
        print(self.get_action())
        print(self.get_direction_message())
        print(self.get_direction_coordinates())
        print(self.get_distance())


if __name__ == '__main__':
    first_location = (0, 0)
    first_quest = Quest(first_location)
    first_quest.print_results()
