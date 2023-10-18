from consolemenu import *
from consolemenu.items import *


def hello_world(name=input):
    return f"Hello {name}"


def gameloop():
    # menu = ConsoleMenu("Title", "Subtitle")
    menu = ConsoleMenu("SoloCampaign", "A game for me.")

    # MenuItem is the base class for all items, it doesn't do anything when selected
    # menu_item = MenuItem("Create a character")

    # A FunctionItem runs a Python function when selected
    # function_item = FunctionItem("Create a character", hello_world)

    # A SelectionMenu constructs a menu from a list of strings
    selection_menu = SelectionMenu(["item1", "item2", "item3"])

    character_creation = SubmenuItem("Create a character", selection_menu, menu)

    # A CommandItem runs a console command
    # command_item = CommandItem("Run a console command", "touch hello.txt")


    # A SubmenuItem lets you add a menu (the selection_menu above, for example)
    # as a submenu of another menu
    # submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

    # Once we're done creating them, we just add the items to the menu
    # menu.append_item(menu_item)
    # menu.append_item(function_item)
    # menu.append_item(command_item)
    # menu.append_item(submenu_item)
    menu.append_item(character_creation)
    menu.show()
    print(selection_menu)
    # hello_world(function_item)

if __name__ == '__main__':
    gameloop()
