import numpy as np

from logic.utilities import Position


class PheromoneLogic:
    def __init__(
        self,
        width: int,
        height: int,
        home_position: Position,
        food_position: Position,
        pheromone_matrix: np.ndarray,
    ):
        self._width = width
        self._height = height
        self._pheromone_matrix = pheromone_matrix
        self.home_position = home_position
        self.food_position = food_position
        self.fields_to_move = self._count_fields_to_move()

    def _count_fields_to_move(self) -> int:
        """Counts available fields where the ants can move.

        Returns:
            int: Number of fields where the ants can move.
        """

        result = (self._width * self._height) - \
            np.count_nonzero(self._pheromone_matrix)

        return result

    @property
    def pheromone_matrix(self):
        return self._pheromone_matrix

    def evaporate_pheromone(self, evaporate_coefficent: float) -> None:
        """Evaporates pheromone according to the evaporate coefficent.

        Formula: 
        `pheromone(t) = pheromone(t - 1) * evaporate_coefficent`

        Args:
            evaporate_coefficent (float): Coefficent of the pheromone evaporation. 
                Should be in the range `0 < evaporate_coefficent <  1`.
        """

        self._pheromone_matrix = np.where(
            self._pheromone_matrix >= 0,
            np.multiply(self._pheromone_matrix, evaporate_coefficent),
            self._pheromone_matrix,
        )

    def deposit_pheromone(self, position: Position,
                          deposit_coefficent: float) -> None:
        """Increases the amount of the pheromone in the given position 
        according to the deposit coefficent.

        Formula:
        `pheromone(row, column) = pheromone(row, column) + deposit_coefficent`

        Args:
            position (Tuple[int, int]): Position to deposit the pheromone.
            deposit_coefficent (float): Coefficent of the pheromone deposit. 
                Should be in the range `0 < deposit_coefficent < 1`.
        """

        row = position.row
        column = position.column

        self._pheromone_matrix[row][column] = np.add(
            self._pheromone_matrix[row][column], deposit_coefficent)
