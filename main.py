

from controllers.base import Controller
from views.base import Views


def main():
    view = Views()
    logiciel = Controller(view)
    logiciel.test()


if __name__ == "__main__":
    main()
