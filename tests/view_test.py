from datetime import datetime
import tkinter as tk
from file_manager.view import View
from unittest import mock


def test_update_folder(mocker):
    # Arrange
    root = tk.Tk()
    v = View(master=root)

    # Action
    v.update_text_field("Test")

    # Assert
    assert v.text_field.text == "Test"


def test_update_items():
    # Arrange
    root = tk.Tk()
    v = View(master=root)
    items = [
        {
            "name": "test1.txt",
            "date": datetime(year=2000, month=1, day=1, hour=1, minute=1, second=1),
            "size": 5000,
            "type": "File",
        },
        {
            "name": "test2 folder",
            "date": datetime(year=2001, month=1, day=1, hour=1, minute=1, second=1),
            "size": 0,
            "type": "Folder",
        },
    ]

    # Action
    v.update_file_list(items)

    # Assert
    assert v.file_list.items == [
        {
            "date": "2000-01-01 01:01:01",
            "name": "test1.txt",
            "size": "5 KB",
            "type": "File",
        },
        {
            "date": "2001-01-01 01:01:01",
            "name": "test2 folder",
            "size": "",
            "type": "Folder",
        },
    ]
