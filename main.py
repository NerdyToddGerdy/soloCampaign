# This is a sample Python script.
from typing import Tuple, List

from Quest import Quest


# Press ⇧⌘F11 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⇧⌘B to toggle the breakpoint.


def add_quest(quests: List[Quest], old_coordinates: Tuple[int, int]):
    quests.append(Quest(old_coordinates))


def main():
    starting_location: Tuple[int, int] = (0, 0)
    quests: List[Quest] = []
    add_quest(quests, starting_location)
    add_quest(quests, quests[-1].get_direction_coordinates())
    add_quest(quests, quests[-1].get_direction_coordinates())
    for quest in quests:
        quest.print_results()
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    print_hi('PyCharm')
    #
    main()
    # options = ["entry1", "entry2", "entry3"]
    # terminal_menu = TerminalMenu(options)
    # menu_entry_index = terminal_menu.show()
    # print(f'You have selected {options[menu_entry_index]}!')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
