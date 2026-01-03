
# $ uv run ./main.py
# Traceback (most recent call last):
#   File "C:\Users\russ\python-misc\pygame\misc\main.py", line 2, in <module>
#     from .pygame_handler import PygameHandler
# ImportError: attempted relative import with no known parent package
from .pygame_handler import PygameHandler

def main():
    print("Hello from misc!")


if __name__ == "__main__":
    main()
