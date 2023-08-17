

from controllers.base import Controller
from views.base import View


def main():
    view = View()
    logiciel = Controller(view)
    logiciel.run()


if __name__ == "__main__":
    main()
