from stockfish import Stockfish

stockfish = Stockfish(path="/Users/sidharthsandeep/Downloads/stockfish/stockfish-macos-m1-apple-silicon", depth=18, parameters={"Threads": 4,"Hash":2048, "Minimum Thinking Time": 30})
def besmove():
    #stockfish.set_fen_position(pos)
    return stockfish.get_best_move()
def make(move):
    stockfish.make_moves_from_current_position([move])
