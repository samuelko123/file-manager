import tkinter as tk
from tkinter import ttk
from typing import Any


class Entry(ttk.Entry):
    def __init__(self, text: str, **kwargs: Any) -> None:
        self._text = tk.StringVar(value=text)
        ttk.Entry.__init__(self, textvariable=self._text, **kwargs)

    @property
    def text(self) -> str:
        return self._text.get()

    @text.setter
    def text(self, text: str) -> None:
        self._text.set(text)


class Label(ttk.Label):
    def __init__(self, text: str, **kwargs: Any) -> None:
        self._text = tk.StringVar(value=text)
        ttk.Label.__init__(self, textvariable=self._text, **kwargs)

    @property
    def text(self) -> str:
        return self._text.get()

    @text.setter
    def text(self, text: str) -> None:
        self._text.set(text)


class Treeview(ttk.Treeview):
    def __init__(self, columns: list[dict], **kwargs: Any) -> None:
        ttk.Treeview.__init__(self, **kwargs)
        self._fields: list[str] = [col["field"] for col in columns]
        self._items: list[dict] = []

        # vertical scroll
        vsb = ttk.Scrollbar(master=self, orient="vertical", command=self.yview)
        vsb.pack(side=tk.RIGHT, fill=tk.Y, padx=1, pady=1)
        self.configure(columns=self._fields, yscrollcommand=vsb.set)

        # configure columns
        for column in columns:
            anchor = tk.W if "anchor" not in column else column["anchor"]
            header = (
                column["header"] if "header" in column else column["field"].capitalize()
            )

            self.column(
                column=column["field"],
                width=column["width"],
                stretch=tk.NO,
                anchor=anchor,
            )
            self.heading(column=column["field"], text=header)

    @property
    def fields(self) -> list[str]:
        return self._fields

    @property
    def items(self) -> list[dict]:
        return self._items

    @items.setter
    def items(self, items: list[dict]) -> None:
        self._items = items
        self.delete(*self.get_children())
        for item in items:
            data = [item[field] for field in self._fields]
            self.insert(parent="", index=tk.END, values=data)

    def get_value(self, point_x: float, point_y: float, field: str) -> Any:
        item_id = self.identify("item", point_x, point_y)
        item = self.item(item=item_id)

        if not item:
            return None
        if "values" not in item:
            return None
        if field not in self._fields:
            return None

        index = self._fields.index(field)
        return item["values"][index]
