"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    for row in board:
        for col in row:
            if col==X: x += 1
            elif col==O: o += 1
    return X if x==o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    Actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY: Actions.add((i,j))
    return Actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    i,j = action
    if new_board[i][j]!=EMPTY: raise Exception("Not a valid action")
    new_board[i][j] = player(new_board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    Winner = None
    for i in range(3):
        if board[i][0]==X and board[i][1]==X and board[i][2]==X: Winner = X
        if board[i][0]==O and board[i][1]==O and board[i][2]==O: Winner = O
    
    for j in range(3):
        if board[0][j]==X and board[1][j]==X and board[2][j]==X: Winner = X
        if board[0][j]==O and board[1][j]==O and board[2][j]==O: Winner = O
    
    if board[0][0]==X and board[1][1]==X and board[2][2]==X: Winner = X
    if board[0][0]==O and board[1][1]==O and board[2][2]==O: Winner = O
    if board[0][2]==X and board[1][1]==X and board[2][0]==X: Winner = X
    if board[0][2]==O and board[1][1]==O and board[2][0]==O: Winner = O

    return Winner

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None: return True
    for row in board:
        for col in row:
            if col==EMPTY: return False
    return True
            


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    Winner = winner(board)
    if Winner==X: return 1
    elif Winner==O: return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """ 
    def minimax_helper(board):
        if terminal(board): return [utility(board),None,None]
        Player = player(board)
        Actions = actions(board)
        if Player==X:
            eval = [-2,None,None]
            for i,j in Actions:
                new_board = copy.deepcopy(board)
                new_board[i][j] = X
                new_eval = minimax_helper(new_board)
                if new_eval[0] > eval[0]:
                    eval[0] = new_eval[0]
                    eval[1] = i
                    eval[2] = j
            return eval
        else:
            eval = [2,None,None]
            for i,j in Actions:
                new_board = copy.deepcopy(board)
                new_board[i][j] = O
                new_eval = minimax_helper(new_board)
                if new_eval[0] < eval[0]:
                    eval[0] = new_eval[0]
                    eval[1] = i
                    eval[2] = j
            return eval

    if terminal(board): return None
    action = minimax_helper(board)
    return (action[1],action[2])


