from stockfish import Stockfish
import os
stockfish = Stockfish(path="/Users/sidharthsandeep/Chesbo/stockfish", depth=18, parameters={"Threads": 4,"Hash":2048, "Minimum Thinking Time": 30})
def setfen(fen):
    stockfish.set_fen_position(fen)
def besmove(do=True):
    #stockfish.set_fen_position(pos)
    move = stockfish.get_best_move()
    if (do): make(move)
    return move
def make(move):
    
    stockfish.make_moves_from_current_position([move])
def reboard():
    return stockfish.get_board_visual()
def val(square):
    return (stockfish.get_what_is_on_square(square))
def fenot():
    return stockfish.get_fen_position()
def eva():
    mae = False
    if stockfish.get_evaluation()['type'] == 'mate' and stockfish.get_evaluation()['value'] == 0:
        mae = True
    return stockfish.get_evaluation(), mae
if __name__ == '__main__':
    while True:
        make(input("move: "))
        print(besmove())
        print(reboard())
        print(stockfish.get_evaluation())
        if stockfish.get_evaluation()['type'] == 'mate' and stockfish.get_evaluation()['value'] == 0:
            print("Game Over")
            break
