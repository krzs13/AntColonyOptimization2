from typing import List

import numpy as np

from logic.ant_logic import AntLogic
from logic.pheromone_logic import PheromoneLogic
from logic.utilities import Position, calculate_distance


class ACOController:
    def __init__(
        self,
        width: int,
        height: int,
        home_position: Position,
        food_position: Position,
        pheromone_matrix: np.ndarray,
        pheromone: PheromoneLogic,
        ant: AntLogic,
    ):
        self.pheromone = pheromone(
            width, height, home_position, food_position, pheromone_matrix)
        self._ant_object = ant
        self.ants = self._create_ants()
        self.iterations = 0

    def _create_ants(self) -> List[AntLogic]:
        ants = [self._ant_object(self.pheromone)
                for _ in self.pheromone.fields_to_move]

        return ants

    def choose_path_of_an_ant(self, ant: AntLogic, alpha: int) -> None:
        ant.choose_path(alpha)

    def evaporate_pheromone(self, evaporate_coefficient: float) -> None:
        self.pheromone.evaporate_pheromone(evaporate_coefficient)

    def deposit_pheromone(self, deposit_coefficent: float) -> None:
        for ant in self.ants:
            if ant.current_solution:
                deposit_value = deposit_coefficent / \
                    calculate_distance(ant.current_solution)

                for position in set(ant.current_solution):
                    self.pheromone.deposit_pheromone(position, deposit_value)

                ant.last_solution = ant.current_solution
                ant.current_solution = []

        self.iterations += 1

    def get_best_solution(self):
        all_solutions = []

        for ant in self.ants:
            if ant.current_solution:
                for position in ant.current_solution:
                    all_solutions.append(position.coordinates)
            else:
                for position in ant.last_solution:
                    all_solutions.append(position.coordinates)

        sorted_all_solutions = [sorted(solution) for solution in all_solutions]
        unique_solutions = [list(solution) for solution in set(
            tuple(solution) for solution in all_solutions)]

        for i, solution in enumerate(unique_solutions):
            unique_solutions[i] = (
                solution, sorted_all_solutions.count(sorted(solution)))

        best_solution = max(unique_solutions, key=lambda x: x[1])[0]
        best_solution = [Position(row, column)
                         for row, column in best_solution]

        best_solution_length = calculate_distance(best_solution)

        return best_solution, best_solution_length
