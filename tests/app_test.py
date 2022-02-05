from file_manager.app import App, View, Controller, Model


def test_app():
    # Arrange
    a = App()

    # Assert
    assert isinstance(a.view, View)
    assert isinstance(a.model, Model)
    assert isinstance(a.controller, Controller)
