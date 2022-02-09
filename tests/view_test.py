from datetime import datetime
import tkinter as tk
from file_manager.view import View
from unittest import mock


def test_focus_text_field(mocker):
    # Arrange
    v = View()
    v.text_field.focus = mocker.Mock()

    # Action
    evt = tk.Event()
    v.focus_text_field(evt)

    # Assert
    v.text_field.focus.assert_called_once()


def test_update_folder():
    # Arrange
    v = View()

    # Action
    v.update_text_field("Test")

    # Assert
    assert v.text_field.text == "Test"


def test_update_items():
    # Arrange
    v = View()
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


def test_report_callback_exception():
    # Arrange
    v = View()

    v.error_label = mock.MagicMock()
    p = mock.PropertyMock()
    type(v.error_label).text = p

    # Action
    v.report_callback_exception(Exception, "Test Error", None)

    # Assert
    p.assert_called_once_with("Test Error")
