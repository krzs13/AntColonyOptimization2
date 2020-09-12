import tkinter as tk
from typing import List

from graphics.base_canvas import BaseCanvas
from logic.ant_logic import AntLogic
from logic.pheromone_logic import PheromoneLogic
from logic.utilities import Position


class DisplayCanvas(BaseCanvas):
    def __init__(self, width: int, height: int, field_size: int, master: tk.Tk,
                 pheromone: PheromoneLogic):
        super().__init__(width, height, field_size, master)
        self._pheromone_matrix = pheromone.pheromone_matrix
        self._home_position = pheromone.home_position
        self._food_position = pheromone.food_position
        self._home_food_tabu = [self._home_position, self._food_position]

    def _change_color(self, position: Position, color: str) -> None:
        row = position.row
        column = position.column

        self.canvas.itemconfig(self.canvas_matrix[row][column], fill=color)

    def display_map(self) -> None:
        for row in range(self._height):
            for column in range(self._width):
                x_1 = column * self._field_size
                y_1 = row * self._field_size
                x_2 = x_1 + self._field_size
                y_2 = y_1 + self._field_size

                if self._home_position.coordinates == (row, column):
                    color = 'blue'
                elif self._food_position.coordinates == (row, column):
                    color = 'green'
                elif self._pheromone_matrix >= 0:
                    color = 'white'
                else:
                    color = 'black'

                self.canvas_matrix[row][column] = self.canvas.create_rectangle(
                    (x_1, y_1, x_2, y_2), fill=color)

    def change_field_color(self, ant: AntLogic) -> None:
        current_position = ant.position
        previous_position = ant.previous_position

        if current_position not in self._home_food_tabu:
            self._change_color(current_position, 'red')

        if previous_position and previous_position not in self._home_food_tabu:
            self._change_color(previous_position, 'white')

    def draw_solution(self, solution: List[Position]) -> None:
        for position in solution:
            if position not in self._home_food_tabu:
                self._change_color(position, 'red')
