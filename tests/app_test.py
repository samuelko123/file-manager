from unittest import mock
from file_manager.app import App


def test_report_callback_exception():
    # Arrange
    a = App()

    a._view.error_label = mock.MagicMock()
    p = mock.PropertyMock()
    type(a._view.error_label).text = p

    # Action
    a.report_callback_exception(Exception, "Test Error", None)

    # Assert
    p.assert_called_once_with("Test Error")
