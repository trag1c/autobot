"""...without object inheritance."""


class Foo(Bar):
    def __init__(self, x: int) -> None:
        self.x = x
