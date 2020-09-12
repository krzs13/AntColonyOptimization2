from random import choice, choices
from typing import Union

import numpy as np

from logic.pheromone_logic import PheromoneLogic
from logic.utilities import Position


class AntLogic:
    def __init__(self, pheromone: PheromoneLogic):
        self._pheromone_matrix = pheromone.pheromone_matrix
        self._home_position = pheromone.home_position
        self._food_position = pheromone.food_position
        self._position = self._set_initial_position()
        self._mode = self._set_initial_mode()
        self._tabu_list = []
        self.current_solution = []
        self.last_solution = []
        self._possible_moves = [(-1, -1), (-1, 0), (-1, 1),
                                (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def _set_initial_position(self) -> Position:
        position = choice([self._home_position, self._food_position])

        return position

    def _set_initial_mode(self) -> int:
        mode = self._position == self._food_position

        return mode

    def _change_mode(self, mode: int, position: Position) -> None:
        self._mode = mode
        self._tabu_list.append(position)
        self.current_solution = self._tabu_list
        self._tabu_list = []

    @property
    def position(self) -> Position:
        return self._position

    @property
    def previous_position(self) -> Union[Position, int]:
        previous_position = self._tabu_list[-1] if self._tabu_list else 0 

        return previous_position

    def choose_path(self, alpha: int):
        self._tabu_list.append(self._position)
        possible_paths = []
        pheromone_values = []

        for row, column in self._possible_moves:
            possible_path = Position(
                self._position.row + row, self._position.column + column)
            row = possible_path.row
            column = possible_path.column

            if row < 0 or column < 0:
                continue

            try:
                pheromone_value = self._pheromone_matrix[row][column]

                if pheromone_value < 0:
                    continue

                if possible_path in self._tabu_list:
                    pheromone_values.append(0)
                else:
                    pheromone_values.append(pheromone_value ** alpha)

                possible_paths.append(possible_path)
            except IndexError:
                continue

            if sum(possible_paths) > 0:
                moves = []
                weights = []

                for i, pheromone_value in enumerate(pheromone_values):
                    if pheromone_value > 0:
                        moves.append(possible_paths[i])
                        weights.append(pheromone_value)

                choosen_path = choices(moves, weights)[0]
            else:
                choosen_path = choice(moves)

            if choosen_path == self._home_position and self._mode == 1:
                self._change_mode(0, choosen_path)
            elif choosen_path == self._food_position and self._mode == 0:
                self._change_mode(1, choosen_path)

            self._position = choosen_path
