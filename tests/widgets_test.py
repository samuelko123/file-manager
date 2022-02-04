import tkinter as tk
from file_manager.widgets import Label, Entry, Treeview


def test_entry():
    # Arrange
    root = tk.Tk()
    e = Entry(master=root, text="")

    # Action
    e.text = "Test Entry"

    # Assert
    assert e.text == "Test Entry"


def test_label():
    # Arrange
    root = tk.Tk()
    l = Label(master=root, text="")

    # Action
    l.text = "Test Label"

    # Assert
    assert l.text == "Test Label"


def test_tree_view():
    # Arrange
    columns = [
        {"field": "a", "width": 200},
        {"field": "b", "width": 200},
        {"field": "c", "width": 200},
    ]

    data = [
        {"a": 1, "b": 2, "c": 3},
        {"a": None, "b": False, "c": "Test"},
    ]

    root = tk.Tk()
    t = Treeview(master=root, columns=columns)

    # Action
    t.items = data

    # Assert
    assert t.items == data
    assert t.fields == ["a", "b", "c"]


def test_tree_view_get_value(mocker):
    # Arrange
    root = tk.Tk()
    t = Treeview(master=root, columns=[])
    t._fields = ["test1", "test2", "test3"]

    # Action
    t.item = mocker.Mock(return_value={"values": ["Value 1", "Value 2", "Value 3"]})
    v1 = t.get_value(0, 0, "test2")
    v2 = t.get_value(0, 0, "no such field")

    t.item = mocker.Mock(return_value=None)
    v3 = t.get_value(0, 0, "test2")

    t.item = mocker.Mock(return_value={"invalid": "dict"})
    v4 = t.get_value(0, 0, "test2")

    # Assert
    assert v1 == "Value 2"
    assert v2 == None
    assert v3 == None
    assert v4 == None
