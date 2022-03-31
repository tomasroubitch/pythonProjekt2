import textwrap
from random import shuffle
#win conditions
podminky_vyhry = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)
oddelovac = 50 * "="

#welcome
def uvitani():
    vitej = "Welcome to Tic Tac Toe"
    print(oddelovac)
    print(vitej)
    print(oddelovac)
#rules
def pravidla():
    pravidla = """\
            GAME RULES:
            Each player can place one mark (or stone)
            per turn on the 3x3 grid. The WINNER is
            who succeeds in placing three of their
            marks in a:
            * horizontal,
            * vertical or
            * diagonal row 
            """
    print(oddelovac)
    print(textwrap.dedent(pravidla))
    print("START THE GAME")
    print(oddelovac)
#gameboard
def hraci_plocha(board):
    print_board = f"""\
    ---------
    {board[6]} | {board[7]} | {board[8]}
    ---------
    {board[3]} | {board[4]} | {board[5]}
    ---------
    {board[0]} | {board[1]} | {board[2]}
    ---------"""
    print(textwrap.dedent(print_board))
#plazboard
def play_board(board, player, box):
    board[box] = player

def volne_pole(board, box):
    return board[box] == " "

def vystup_hrace(hrac):
    print(f"Player {hrac} |", end=" ")
    while True:

        try:
            box = int(input("Please enter your move number: "))

            if box in range(1, 10):
                return box - 1
            else:
                print("Choose number in range 1-9")
                continue
        except ValueError:
            print("Choose number")

def kontrola_vyhry(board, hrac):
    for x, y, z in podminky_vyhry:
        if hrac == board[x] == board[y] == board[z]:
            return True
    return False

def kontrola_remizy(board):
    return " " not in board

def hraci_kolo():
    board = [" " for i in range(9)]

    hracova_volba = ["X", "O"]
    hra = True

    shuffle(hracova_volba)

    uvitani()
    pravidla()
    hraci_plocha(board)
    while hra:

        for hrac in hracova_volba:

            while True:
                hracovo_pole = vystup_hrace(hrac)
                if not volne_pole(board, hracovo_pole):
                    print(oddelovac)
                    print("Select another box, this is busy")
                    continue
                break

            play_board(board, hrac, hracovo_pole)
            hraci_plocha(board)
            if kontrola_vyhry(board, hrac):
                print(oddelovac)
                print(f"Congratulations, the player {hrac} WIN!")
                hra = False
                break

            if kontrola_remizy(board):
                print(oddelovac)
                print("DRAW!")
                hea = False
                break

if __name__ == "__main__":
    hraci_kolo()