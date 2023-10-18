import tkinter as tk
from math import sqrt, cos, sin, radians
from tkinter import *
from tkinter import ttk

from Character import Character


class Gui(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Game")
        self.character_stats = tk.Frame(self)
        self.character_stats.pack(side='right')
        self.main_label = tk.Label(self.character_stats, text='Hello')

        # Setup Notebook
        self.notebook = ttk.Notebook(self)

        self.map_tab = ttk.LabelFrame(self.notebook)
        self.dungeon_tab = LabelFrame(self.notebook)
        self.settings_tab = LabelFrame(self.notebook)

        self.notebook.add(self.map_tab, text="Map")
        self.notebook.add(self.dungeon_tab, text="Dungeon")
        self.notebook.add(self.settings_tab, text="Settings")
        self.notebook.pack(expand=1, fill='both')

        self.update()

        # Character Stats Section
        self.character_general_info = ttk.LabelFrame(self.character_stats)
        self.character_general_info.grid(column=0,
                                         row=0,
                                         sticky='N')
        self.stat_block = ttk.LabelFrame(self.character_stats)
        self.stat_block.grid(column=1,
                             row=0,
                             sticky='N')
        self.inventory = ttk.LabelFrame(self.character_stats)
        self.inventory.grid(column=0,
                            row=1,)


# ----- Map Tab -----
        self.hex_map_canvas = Canvas(self.map_tab,
                                     width=400,
                                     height=300,
                                     bg='#000000')
        self.hex_map_canvas.pack()

        self.hexagons: list = []
        self.init_grid(10, 7, 30, debug=True)
        self.hex_map_canvas.bind("<Button-1>", self.click)

# ----- Dungeon Tab -----
        # TODO: Create Dungeon logic
        ttk.Label(self.dungeon_tab,
                  text="Dungeon").grid()

# ----- Settings Page -----
        # TODO: Create Settings Page Logic
        ttk.Label(self.settings_tab,
                  text="Settings Page").grid()

    def init_grid(self, cols: int, rows: int, size: int, debug: bool):
        """
        2d grid of hexagons
        :param cols:
        :param rows:
        :param size:
        :param debug:
        :return:
        """
        # TODO: Why won't it select the proper hex.

        for c in range(cols):
            if c % 2 == 0:
                offset = size * sqrt(3) / 2
            else:
                offset = 0
            for r in range(rows):
                h = FillHexagon(self.hex_map_canvas,
                                c * (size * 1.5),
                                (r * (size * sqrt(3))) + offset,
                                size,
                                "#a1e2a1",
                                f"{r}.{c}")
                self.hexagons.append(h)

                if debug:
                    coords = f"{r}, {c}"
                    self.hex_map_canvas.create_text(c * (size * 1.5) + (size / 2),
                                                    (r * (size * sqrt(3))) + offset + (size / 2),
                                                    text=coords)

    def click(self, evt):
        """
        hexagon detection on mouse click
        :param evt:
        :return:
        """
        x, y = evt.x, evt.y
        print(x, y)
        for i in self.hexagons:
            i.selected = False
            i.isNeighbour = False
            self.hex_map_canvas.itemconfigure(i.tags, fill=i.color)
        clicked = self.hex_map_canvas.find_closest(x, y)[0]
        self.hexagons[int(clicked) - 1].selected = True
        for i in self.hexagons:
            if i.selected:
                self.hex_map_canvas.itemconfigure(i.tags, fill="#53ca53")
            if i.isNeighbour:
                self.hex_map_canvas.itemconfigure(i.tags, fill="#76d576")


class FillHexagon:
    def __init__(self, parent: Canvas, x, y, length, color, tags):
        self.parent = parent  # canvas
        self.x = x  # top left x
        self.y = y  # top left y
        self.length = length  # length of a side
        self.color = color  # fill color

        self.selected = False
        self.tags = tags

        self.draw()

    def draw(self):
        start_x = self.x
        start_y = self.y
        coords: list = []
        angle: int = 60
        for i in range(6):
            end_x = start_x + self.length * cos(radians(angle * i))
            end_y = start_y + self.length * sin(radians(angle * i))
            coords.append([start_x, start_y])
            # print(coords)
            start_y = end_y
            start_x = end_x
        self.parent.create_polygon(coords[0][0],
                                   coords[0][1],
                                   coords[1][0],
                                   coords[1][1],
                                   coords[2][0],
                                   coords[2][1],
                                   coords[3][0],
                                   coords[3][1],
                                   coords[4][0],
                                   coords[4][1],
                                   coords[5][0],
                                   coords[5][1],
                                   fill=self.color,
                                   outline="gray",
                                   tags=self.tags)


if __name__ == '__main__':
    # Start app
    app = Gui()

    # Create random fighter player
    player1 = Character(
        character_class='Fighter',
        gender='Male',
        race='Human',
    )

    player1.set_ability_scores()

    player1.view_character_gen_info(app.character_general_info)
    player1.view_character_stats(app.stat_block)
    player1.view_character_inventory(app.inventory)

    app.mainloop()
