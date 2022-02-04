import tkinter as tk
from unittest import mock
from file_manager.controller import Controller


@mock.patch("file_manager.controller.View")
@mock.patch("file_manager.controller.Model")
def test_dismiss_error(model, view):
    # Arrange
    c = Controller(model, view)

    c._view.error_label = mock.MagicMock()
    p = mock.PropertyMock()
    type(c._view.error_label).text = p

    # Action
    c.dismiss_error()

    # Assert
    p.assert_called_once_with("")


@mock.patch("file_manager.controller.View")
@mock.patch("file_manager.controller.Model")
def test_go_to_parent(model, view, mocker):
    # Arrange
    c = Controller(model, view)
    c.dismiss_error = mocker.Mock()
    c._model.go_to_parent_folder = mocker.Mock()

    # Action
    c.go_to_parent_folder()

    # Assert
    c.dismiss_error.assert_called_once()
    c._model.go_to_parent_folder.assert_called_once()


@mock.patch("file_manager.controller.View")
@mock.patch("file_manager.controller.Model")
def test_set_folder(model, view, mocker):
    # Arrange
    c = Controller(model, view)
    c._view.text_field.text = "Testing"

    c.dismiss_error = mocker.Mock()
    c._model = mock.MagicMock()
    p = mock.PropertyMock()
    type(c._model).folder = p

    # Action
    c.set_folder(event=None)

    # Assert
    c.dismiss_error.assert_called_once()
    p.assert_called_once_with("Testing")


@mock.patch("file_manager.controller.View")
@mock.patch("file_manager.controller.Model")
def test_open_item(model, view, mocker):
    # Arrange
    c = Controller(model, view)
    c._view.text_field.text = "Testing"

    c.dismiss_error = mocker.Mock()
    c._model.open_item = mocker.Mock()

    event = tk.Event()
    event.x = 0
    event.y = 0

    # Action
    c._view.file_list.get_value = mocker.Mock(return_value="Testing")
    c.open_item(event=event)

    # Assert
    c.dismiss_error.assert_called_once()
    c._model.open_item.assert_called_once_with(fname="Testing")


@mock.patch("file_manager.controller.View")
@mock.patch("file_manager.controller.Model")
def test_open_item_empty(model, view, mocker):
    # Arrange
    c = Controller(model, view)
    c._view.text_field.text = "Testing"

    c.dismiss_error = mocker.Mock()
    c._model.open_item = mocker.Mock()

    event = tk.Event()
    event.x = 0
    event.y = 0

    # Action
    c._view.file_list.get_value = mocker.Mock(return_value="")
    c.open_item(event=event)

    # Assert
    c.dismiss_error.assert_called_once()
    c._model.open_item.assert_not_called()
