
from .pygame_handler import PygameHandler

from .spelling import spelling
from .technologic import technologic


def main() -> None:
    print("Hello from misc!")


__all__ = [
    spelling, technologic
]