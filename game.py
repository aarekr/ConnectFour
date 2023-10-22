""" Connect Four Game """

from ui import UI

def main():
    """ This function calls the game_loop method in UI class that starts the game """
    ui = UI()
    ui.who_starts()

if __name__ == "__main__":
    main()
