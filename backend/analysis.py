import chess.pgn
import io
def analyze_game(pgn_text):
        game = chess.pgn.read_game(io.StringIO(pgn_text))
        if game is None:
            return None
        for move in game.mainline_moves():
                print(move)
print(analyze_game("1. e4 e5 2. Nf3 Nc6"))

      
