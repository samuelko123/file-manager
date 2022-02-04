import tkinter as tk
from tkinter import ttk
from typing import Any
from .widgets import Entry, Label, Treeview


class View(tk.Frame):
    def __init__(self, master: tk.Tk, **kwargs: Any):
        super().__init__(master=master, **kwargs)
        ttk.Style().configure("Padding.TEntry", padding=1)
        ttk.Style().configure("Error.TLabel", foreground="#aa0000")

        self.up_button = ttk.Button(master=self, text="↑", width=5)
        self.text_field = Entry(master=self, text="", style="Padding.TEntry")
        self.error_label = Label(master=self, text="", style="Error.TLabel")

        columns = [
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
        ]

        self.file_list = Treeview(
            master=self,
            columns=columns,
            show="headings",
            height=5,
            padding=10,
            selectmode="browse",
        )
        self.up_button.grid(row=0, column=0)
        self.text_field.grid(row=0, column=1, sticky="ew")
        self.error_label.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.file_list.grid(row=2, column=0, columnspan=2, sticky="nsew")
        self.rowconfigure(index=0, weight=0, pad=10)
        self.rowconfigure(index=1, weight=0, pad=10)
        self.rowconfigure(index=2, weight=1, pad=10)
        self.columnconfigure(index=0, weight=0, pad=10)
        self.columnconfigure(index=1, weight=1, pad=10)

    def update_text_field(self, folder: str) -> None:
        self.text_field.text = folder

    def update_file_list(self, items: list[dict]) -> None:
        for item in items:
            item["date"] = item["date"].strftime("%Y-%m-%d %H:%M:%S")

            size = item["size"]
            item["size"] = f"{size / 1024.0:,.0f} KB" if size > 0 else ""

        self.file_list.items = items
