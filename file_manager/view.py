from typing import Any
import tkinter as tk
from tkinter import ttk
from .widgets import Entry, Label, Treeview


class View(tk.Tk):
    def __init__(self) -> None:
        # root window settings
        super().__init__()
        self.title("File Manager")
        self.geometry("800x600+100+100")
        self.minsize(width=500, height=300)
        self.configure(padx=10, pady=10)
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        # style settings
        ttk.Style().configure("Padding.TEntry", padding=1)
        ttk.Style().configure("Error.TLabel", foreground="#aa0000")

        # create widgets
        self.up_button = ttk.Button(master=self, text="↑", width=5)
        self.text_field = Entry(master=self, text="", style="Padding.TEntry")
        self.error_label = Label(master=self, text="", style="Error.TLabel")
        self.file_list = Treeview(
            master=self,
            columns=[
                {
                    "field": "name",
                    "width": 200,
                },
                {
                    "field": "date",
                    "header": "Modified Date",
                    "width": 200,
                },
                {
                    "field": "type",
                    "width": 100,
                },
                {
                    "field": "size",
                    "width": 100,
                    "anchor": tk.E,
                },
            ],
            show="headings",
            height=5,
            padding=10,
            selectmode="browse",
        )

        # arrange layout
        self.rowconfigure(index=0, weight=0, pad=10)
        self.rowconfigure(index=1, weight=0, pad=10)
        self.rowconfigure(index=2, weight=1, pad=10)
        self.columnconfigure(index=0, weight=0, pad=10)
        self.columnconfigure(index=1, weight=1, pad=10)

        # arrange widgets
        self.up_button.grid(row=0, column=0)
        self.text_field.grid(row=0, column=1, sticky="ew")
        self.error_label.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.file_list.grid(row=2, column=0, columnspan=2, sticky="nsew")

    def report_callback_exception(self, *args: Any) -> None:  # type: ignore[override]
        self.error_label.text = args[1]

    def update_text_field(self, folder: str) -> None:
        self.text_field.text = folder

    def update_file_list(self, items: list[dict]) -> None:
        for item in items:
            item["date"] = item["date"].strftime("%Y-%m-%d %H:%M:%S")

            size = item["size"]
            item["size"] = f"{size / 1024.0:,.0f} KB" if size > 0 else ""

        self.file_list.items = items
