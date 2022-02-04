from collections import defaultdict
from typing import Any, Callable


class Publisher:
    def __init__(self) -> None:
        self._observers: defaultdict[str, list[Callable]] = defaultdict(lambda: [])

    def attach(self, topic: str, observer: Callable) -> None:
        self._observers[topic].append(observer)

    def detach(self, topic: str, observer: Callable) -> None:
        self._observers[topic].remove(observer)

    def notify(self, topic: str, **kwargs: Any) -> None:
        for observer in self._observers[topic]:
            observer(**kwargs)
