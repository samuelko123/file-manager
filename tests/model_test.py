import os
import pytest
from unittest import mock
from file_manager.model import Model
from file_manager.publisher import Publisher


def test_publisher():
    # Arrange
    m = Model()

    # Assert
    assert isinstance(m.publisher, Publisher)


def test_folder(mocker, tmp_path):
    # Arrange
    m = Model()
    m._publisher.notify = mocker.Mock()

    tmp_folder = os.path.join(tmp_path, "Temp Folder")
    os.mkdir(path=tmp_folder)

    tmp_file = os.path.join(tmp_path, "temp.txt")
    with open(file=tmp_file, mode="w") as f:
        f.write("it is a temp file")

    # Action
    m.folder = tmp_path

    # Assert
    assert m.folder == tmp_path
    assert len(m.items) == 2
    assert m.items[0]["name"] == "Temp Folder"
    assert m.items[0]["type"] == "Folder"
    assert m.items[1]["name"] == "temp.txt"
    assert m.items[1]["type"] == "File"
    m._publisher.notify.assert_has_calls(
        [
            mock.call(topic="items updated", items=mock.ANY),
            mock.call(topic="folder updated", folder=tmp_path),
        ]
    )


def test_folder_not_exists(mocker, tmp_path):
    # Arrange
    m = Model()
    m._publisher.notify = mocker.Mock()

    # Action
    with pytest.raises(NotADirectoryError) as err:
        m.folder = os.path.join(tmp_path, "no such folder")

    # Assert
    assert str(err.value).startswith("Invalid folder")


def test_folder_invalid(mocker, tmp_path):
    # Arrange
    m = Model()
    m._publisher.notify = mocker.Mock()

    tmp_file = os.path.join(tmp_path, "temp.txt")
    with open(file=tmp_file, mode="w") as f:
        f.write("it is a temp file")

    # Action
    with pytest.raises(NotADirectoryError) as err:
        m.folder = tmp_file

    # Assert
    assert str(err.value).startswith("Invalid folder")


def test_go_to_parent(mocker, tmp_path):
    # Arrange
    m = Model()
    m._publisher.notify = mocker.Mock()
    m.folder = tmp_path

    # Action
    m.go_to_parent_folder()

    # Assert
    assert m.folder == os.path.dirname(tmp_path)


def test_open_item(mocker, tmp_path):
    # Arrange
    m = Model()
    m._publisher.notify = mocker.Mock()
    m.folder = tmp_path

    tmp_folder = os.path.join(tmp_path, "Temp Folder")
    os.mkdir(path=tmp_folder)

    # Action
    m.open_item("Temp Folder")

    # Assert
    assert m.folder == tmp_folder
