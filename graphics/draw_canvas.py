import tkinter as tk

from graphics.base_canvas import BaseCanvas
from logic.utilities import Position


class DrawCanvas(BaseCanvas):
    def __init__(self, width: int, height: int, field_size: int, master: tk.Tk):
        super().__init__(width, height, field_size, master)
        self.canvas.bind('<Button-1>', self._draw_wall)
        self.canvas.bind('<B1-Motion>', self._draw_wall)
        self.canvas.bind('<Button-3>', self._erease_wall)
        self.canvas.bind('<B3-Motion>', self._erease_wall)
        self.canvas.bind('<Double-Button-1>', self._set_home_position)
        self.canvas.bind('<Double-Button-3>', self._set_food_position)
        self._pheromone_matrix = self._create_matrix()
        self._home_position = None
        self._food_position = None

    def _draw_wall(self, event) -> None:
        row = event.y // self._field_size
        column = event.x // self._field_size

        try:
            self.canvas.itemconfig(
                self.canvas_matrix[row][column], fill='black')
            self._pheromone_matrix[row][column] = -1
        except IndexError:
            pass

    def _erease_wall(self, event) -> None:
        row = event.y // self._field_size
        column = event.x // self._field_size

        try:
            self.canvas.itemconfig(
                self.canvas_matrix[row][column], fill='white')
            self._pheromone_matrix[row][column] = 0
        except IndexError:
            pass

    def _base_set_position(self, event: tk.Event, prior_position: Position,
                           later_position: Position, color: str) -> None:
        row = event.y // self._field_size
        column = event.x // self._field_size

        try:
            if prior_position:
                prior_row = prior_position.row
                prior_column = prior_position.column

                self.canvas.itemconfig(
                    self.canvas_matrix[prior_row][prior_column], fill='white')

            self.canvas.itemconfig(
                self.canvas_matrix[row][column], fill=color)
            prior_position = Position(row, column)

            if prior_position == later_position:
                later_position = None
        except IndexError:
            pass

    def _set_home_position(self, event) -> None:
        self._base_set_position(
            event, self._home_position, self._food_position, 'blue')

    def _set_food_position(self, event) -> None:
        self._base_set_position(
            event, self._food_position, self._home_position, 'green')

    def display_map(self) -> None:
        for row in range(self._height):
            for column in range(self._width):
                x_1 = column * self._field_size
                y_1 = row * self._field_size
                x_2 = x_1 + self._field_size
                y_2 = y_1 + self._field_size

                self.canvas_matrix[row][column] = self.canvas.create_rectangle(
                    (x_1, y_1, x_2, y_2), fill='white')
