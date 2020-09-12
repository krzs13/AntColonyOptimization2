from controller.aco_controller import ACOController
from graphics.display_map import DisplayMap
from graphics.draw_map import DrawMap
from gui.gui import GraphicalUserInterface


if __name__ == "__main__":
    gui = GraphicalUserInterface(
        width=20,
        height=20,
        field_size=20,
        display_map=DisplayMap,
        draw_map=DrawMap,
        aco_controller=ACOController,
    )
    gui.run()