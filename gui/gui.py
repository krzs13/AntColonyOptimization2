import tkinter as tk

from controller.aco_controller import ACOController
from graphics.display_map import DisplayMap
from graphics.draw_map import DrawMap
from logic.ant_logic import AntLogic
from logic.pheromone_logic import PheromoneLogic


class GraphicalUserInterface:
    def __init__(
        self,
        width: int,
        height: int,
        field_size: int,
        display_map: DisplayMap,
        draw_map: DrawMap,
        aco_controller: ACOController,
    ):
        self._width = width
        self._height = height
        self._field_size = field_size
        self._master = tk.Tk()
        self._frame = tk.Frame(self._master)
        self._display_map_object = display_map
        self._display_map = None
        self._draw_map_object = draw_map
        self._draw_map = None
        self._pheromone_matrix = None
        self._aco_controller_object = aco_controller
        self._aco_controller = None

    def _destroy_frame(self) -> None:
        self._frame.destroy()
        self._frame = tk.Frame(self._master)
        self._frame.grid()

    def run(self) -> None:
        self._destroy_frame()

        about = """The Ant Colony Optimization algorithm is a probabilistic 
        technique for searching the shortest path. Multi-agent system of 
        artificial ants is inspired by real ants and their 
        pheromone based behavior."""
        text = tk.Label(self._frame, text=about)
        text.grid(row=0)

        draw_button = tk.Button(
            self._frame, text='Draw Map', command=self._draw_map_canvas)
        draw_button.grid(row=1)

        self._master.mainloop()

    def _draw_map_canvas(self):
        self._destroy_frame()

        self._draw_map = self._draw_map_object(
            self._width, self._height, self._field_size, self._frame)
        self._draw_map.create_canvas()
        self._draw_map.canvas.grid(row=0)

        finish_button = tk.Button(
            self._frame, text='Finish', command=self._display_map_canvas)
        finish_button.grid(row=1)

        self._master.mainloop()

    def _display_map_canvas(self):
        pass
