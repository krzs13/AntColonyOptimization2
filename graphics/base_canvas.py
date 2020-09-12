import tkinter as tk
from abc import ABC

import numpy as np


class BaseCanvas(ABC):
    def __init__(self, width: int, height: int, field_size: int,
                 master: tk.Tk):
        self._width = width
        self._height = height
        self._field_size = field_size
        self._master = master
        self.canvas = self._create_canvas_object()
        self.canvas_matrix = self._create_matrix()

    def _create_canvas_object(self) -> tk.Canvas:
        canvas_width = self._width * self._field_size
        canvas_height = self._height * self._field_size

        canvas_object = tk.Canvas(
            self._master, width=canvas_width, height=canvas_height)

        return canvas_object

    def _create_matrix(self) -> np.ndarray:
        matrix = np.zeros((self._width, self._height))

        return matrix
