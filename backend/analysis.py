import chess.pgn
import io
import chess.engine
def analyze_game(pgn_text):
        game = chess.pgn.read_game(io.StringIO(pgn_text))
        if game is None:
            return None
        engine = chess.engine.SimpleEngine.popen_uci("engines/stockfish-windows-x86-64-universal.exe")
        board = game.board()
        results = []
        previous_eval = 0
        for move in game.mainline_moves():
            player = "white" if board.turn == chess.WHITE else "black"
            board.push(move)
            info = engine.analyse(board, chess.engine.Limit(depth=15))
            score = info["score"].white()
            eval_cp = score.score(mate_score=10000)
            delta = eval_cp - previous_eval
            is_blunder = (player == "white" and delta <= -200) or (player == "black" and delta >= 200)
            results.append({"move": str(move), "player": player, "evaluation": str(score), "delta": delta, "is_blunder": is_blunder})
            previous_eval = eval_cp
        engine.quit()
        return results


      
