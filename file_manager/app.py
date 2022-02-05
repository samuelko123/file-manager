import os

from .controller import Controller
from .model import Model
from .view import View


class App:
    def __init__(self) -> None:
        self.model = Model()
        self.view = View()
        self.controller = Controller(model=self.model, view=self.view)

        # set default values
        self.model.folder = os.path.expanduser("~")
