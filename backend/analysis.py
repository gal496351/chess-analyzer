import chess.pgn
import io
import chess.engine
def analyze_game(pgn_text):
        game = chess.pgn.read_game(io.StringIO(pgn_text))
        if game is None:
            return None
        engine = chess.engine.SimpleEngine.popen_uci("engines/stockfish-windows-x86-64-universal.exe")
        board = game.board()
        for move in game.mainline_moves():
         board.push(move)
         info = engine.analyse(board, chess.engine.Limit(depth=15))
         print(move, info)
        engine.quit()
print(analyze_game("1. e4 e5 2. Nf3 Nc6"))

      
