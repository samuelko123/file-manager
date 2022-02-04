from subprocess import check_call
from file_manager.app import App


def start() -> None:
    app = App()
    app.mainloop()


def lint() -> None:
    check_call(["black", "*/*.py"])
    check_call(["pylint", "file_manager"])
    check_call(["mypy"])


def test() -> None:
    check_call(["pytest", "-s", "-vv"])
