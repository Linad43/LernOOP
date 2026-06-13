from typing import Any


class MixinLog:

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        print(self.__repr__())
