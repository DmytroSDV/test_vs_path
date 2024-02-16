import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a.a import a

print(sys.path)


def b():
    return "Hello from b func!"


if __name__ == "__main__":
    print(a())
