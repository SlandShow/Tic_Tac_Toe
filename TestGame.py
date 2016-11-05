""" Simple TIC TAC TOE game
    made by SlandShow  """

import random


class ValuesOfTheGame:
    def __init__(self):
        # VALUES:
        self.tic_tac_toe_l = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]  # playground map
        self.play = True
        self.first_AI_choice = False
        self.count_free_elements = 9


res = ValuesOfTheGame()


def make_choice(x, y, v):
    res.tic_tac_toe_l[x][y] = v
    res.count_free_elements -= 1


# when AI start to play, we also use random position
def get_first_position():
    return random.randint(0, 2)


def clearO():
    for i in range(3):
        for j in range(3):
            if res.tic_tac_toe_l[i][j] == "O_t":
                res.tic_tac_toe_l[i][j] = " "


def clearX():
    for i in range(3):
        for j in range(3):
            if res.tic_tac_toe_l[i][j] == "Xt":
                res.tic_tac_toe_l[i][j] = " "


def calc_position():
    l = res.tic_tac_toe_l
    for i in range(3):
        for j in range(3):
            if l[i][j] != "O" and l[i][j] != "X" and l[i][j] != "O_t" and l[i][j] != "Xt":
                return i, j


def is_player_win():
    l = res.tic_tac_toe_l
    if l[0][0] == "X" and l[1][1] == "X" and l[2][2] == "X":
        return -1  # diagonal1 win
    if l[0][2] == "X" and l[1][1] == "X" and l[2][0] == "X":
        return -1  # diagonal2 win

    if l[0][0] == "X" and l[1][0] == "X" and l[2][0] == "X":
        return -1
    if l[0][1] == "X" and l[1][1] == "X" and l[2][1] == "X":
        return -1
    if l[0][2] == "X" and l[1][2] == "X" and l[2][2] == "X":
        return -1

    if l[0][0] == "X" and l[0][1] == "X" and l[0][2] == "X":
        return -1  #
    if l[1][0] == "X" and l[1][1] == "X" and l[1][2] == "X":
        return -1
    if l[2][0] == "X" and l[2][1] == "X" and l[2][2] == "X":
        return -1

    return 0  # if player don`t win in current position


def try_to_predict_player(i, j):
    tx = i
    ty = j
    tmp = res.tic_tac_toe_l[tx][ty]
    res.tic_tac_toe_l[tx][ty] = "X"  # set new element
    return_result = is_player_win()
    if return_result == 0:
        res.tic_tac_toe_l[tx][ty] = "Xt"
    if return_result == -1:
        res.tic_tac_toe_l[tx][ty] = tmp
        clearX()

    return return_result


def calculate_AI():
    for i in range(3):
        for j in range(3):
            if res.tic_tac_toe_l[i][j] != "X" and res.tic_tac_toe_l[i][j] != "O" and res.count_free_elements != "O_t":
                res.tic_tac_toe_l[i][j] = "O"
                clearO()
                res.tic_tac_toe_l[i][j] = "O_t"
                calc = True
                count = 0
                while calc:

                    if count == res.count_free_elements - 1:
                        make_choice(i, j, "O")
                        clearX()
                        return
                        # display()
                        # print("--------------")
                    # print(res.count_free_elements, count)
                    a_b = calc_position()
                    result = try_to_predict_player(a_b[0], a_b[1])

                    if result == -1:
                        calc = False
                        break

                    if result == 0:
                        count += 1


def display():
    for i in res.tic_tac_toe_l:
        print(i)


# this main function in project
# here we control all processes

def game():
    while res.play:

        xp = int(input("Enter x of map "))
        yp = int(input("Enter y of map "))
        make_choice(xp, yp, "X")  # player plays as X

        if not res.first_AI_choice:
            res.first_AI_choice = True
            xAI = get_first_position()
            yAI = get_first_position()
            if xAI == xp and yAI == yp:
                yAI += 1
            make_choice(xAI, yAI, "O")  # AI plays as O

        else:
            calculate_AI()

        # show our new playground map
        display()


game()