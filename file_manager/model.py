import os
import datetime
import copy
from .publisher import Publisher


class Model:
    def __init__(self) -> None:
        self._folder: str = ""
        self._items: list[dict] = []
        self._publisher: Publisher = Publisher()

    @property
    def publisher(self) -> Publisher:
        return self._publisher

    @property
    def items(self) -> list[dict]:
        return self._items

    @property
    def folder(self) -> str:
        return self._folder

    @folder.setter
    def folder(self, folder: str) -> None:
        try:
            if not os.path.isdir(folder):
                raise NotADirectoryError(f"Invalid folder - {folder}")

            items = []
            fnames = os.listdir(folder)
            for fname in fnames:
                fpath = os.path.join(folder, fname)
                mdate = os.path.getmtime(fpath)

                if os.path.isdir(fpath):
                    ftype = "Folder"
                    size = 0
                else:
                    ftype = "File"
                    size = os.path.getsize(fpath)

                items.append(
                    {
                        "name": fname,
                        "size": size,
                        "date": datetime.datetime.fromtimestamp(mdate),
                        "type": ftype,
                    }
                )

            self._items = items
            self._publisher.notify(
                topic="items updated", items=copy.deepcopy(self._items)
            )

            self._folder = folder
            self._publisher.notify(topic="folder updated", folder=self._folder)

        except Exception as err:
            raise err

    def go_to_parent_folder(self) -> None:
        self.folder = os.path.dirname(self._folder)

    def open_item(self, fname: str) -> None:
        fpath = os.path.join(self._folder, fname)
        if os.path.isdir(fpath):
            self.folder = fpath
