

from controllers.base import Controller
from controllers.menu import Menu
from views.base import Views


def main():
    view = Views()
    menu = Menu(view)
    logiciel = Controller(view, menu)
    logiciel.run()


def test():
    view = Views()
    menu = Menu(view)
    logiciel = Controller(view, menu)
    logiciel.test()


if __name__ == "__main__":
    main()
