import os
import tkinter as tk
from typing import Any

from .controller import Controller
from .model import Model
from .view import View


class App(tk.Tk):
    def __init__(self) -> None:
        # root window settings
        super().__init__()
        self.title("File Manager")
        self.geometry("800x600+100+100")
        self.minsize(width=500, height=300)
        self.configure(padx=10, pady=10)
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        # model
        self._model = Model()

        # view
        self._view = View(master=self)
        self._view.grid(row=0, column=0, stick="nsew")

        # controller
        self._controller = Controller(model=self._model, view=self._view)

        # set default values
        self._model.folder = os.path.expanduser("~")

    def report_callback_exception(self, *args: Any) -> None:  # type: ignore[override]
        self._view.error_label.text = args[1]
