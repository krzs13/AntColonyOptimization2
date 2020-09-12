from math import sqrt
from typing import List


class Position:
    def __init__(self, row: int, column: int):
        self._row = row
        self._column = column

    def __eq__(self, position: Position):
        return self._row == position.row and self._column == position.column

    @property
    def row(self):
        return self._row

    @property
    def column(self):
        return self._column


def calculate_distance(solution: List[Position]) -> float:
    """Calculates the length of the solution.

    Due to the fact that the ants move on the map where the unit is 1, there is 
    no need to square the subtraction of two coordinates as in the Euclidean 
    distance. The rest of the formula for calculating the distance between two 
    points remains the same.

    Args:
        solution (List[Position]): List of the positions that creates solution.

    Returns:
        float: The length of the solution.
    """

    distance = 0

    for position_1, position_2 in zip(solution[:-1], solution[1:]):
        x_1 = position_1.row
        y_1 = position_1.column
        x_2 = position_2.row
        y_2 = position_2.column

        distance += sqrt(abs(x_1 - x_2) + abs(y_1 - y_2))

    return distance
