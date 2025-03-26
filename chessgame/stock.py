from stockfish import Stockfish
import chess
import os
stocky = Stockfish(path="/Users/sidharthsandeep/Chesbo/models/stockfish", depth=18, parameters={"Threads": 4,"Hash":2048, "Minimum Thinking Time": 30})
def setfen(fen):
    stocky.set_fen_position(fen)
def besmove(do=True):
    #stockfish.set_fen_position(pos)
    move = stocky.get_best_move()
    if (do): make(move)
    return move
def check():
    board = chess.Board(fenot())
    return board.is_check()
def make(move):
    stocky.make_moves_from_current_position([move])
    return move
def reboard():
    return stocky.get_board_visual()
def val(square):
    return (stocky.get_what_is_on_square(square))
def fenot():
    return stocky.get_fen_position()
def eva():
    mae = False
    if stocky.get_evaluation()['type'] == 'mate' and stocky.get_evaluation()['value'] == 0:
        mae = True
    return stocky.get_evaluation(), mae
if __name__ == '__main__':
    while True:
        make(input("move: "))
        print(besmove())
        print(reboard())
        print(stockfish.get_evaluation())
        if stockfish.get_evaluation()['type'] == 'mate' and stockfish.get_evaluation()['value'] == 0:
            print("Game Over")
            break
