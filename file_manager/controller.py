import tkinter as tk
from .model import Model
from .view import View


class Controller:
    def __init__(self, model: Model, view: View):
        self._model = model
        self._view = view

        # attach listeners to model changes
        self._model.publisher.attach("folder updated", self._view.update_text_field)
        self._model.publisher.attach("items updated", self._view.update_file_list)

        # attach event handlers to view widgets
        self._view.bind(sequence="<Control-l>", func=self._view.focus_text_field)
        self._view.bind(
            sequence="<Alt-Up>", func=lambda event: self.go_to_parent_folder()
        )
        self._view.up_button.configure(command=self.go_to_parent_folder)
        self._view.text_field.bind(sequence="<Return>", func=self.set_folder)
        self._view.text_field.bind(
            sequence="<Escape>", func=lambda event: self._view.focus()
        )
        self._view.file_list.bind(sequence="<Double-1>", func=self.open_item)

    def dismiss_error(self) -> None:
        self._view.error_label.text = ""

    def go_to_parent_folder(self) -> None:
        self.dismiss_error()
        self._model.go_to_parent_folder()

    def set_folder(self, event: tk.Event) -> None:
        self.dismiss_error()
        self._model.folder = self._view.text_field.text
        self._view.focus()

    def open_item(self, event: tk.Event) -> None:
        self.dismiss_error()
        fname = self._view.file_list.get_value(
            point_x=event.x, point_y=event.y, field="name"
        )
        if not fname:
            return
        self._model.open_item(fname=fname)
