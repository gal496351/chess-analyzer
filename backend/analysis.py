import chess.pgn
import io
import chess.engine

ENGINE_PATH = "engines/stockfish-windows-x86-64-universal.exe"

def analyze_game(pgn_text):
    game = chess.pgn.read_game(io.StringIO(pgn_text))
    if game is None:
        return None
    board = game.board()
    results = []
    previous_eval = 0
    previous_best = None
    with chess.engine.SimpleEngine.popen_uci(ENGINE_PATH) as engine:
        info = engine.analyse(board, chess.engine.Limit(depth=15))
        previous_eval = info["score"].white().score(mate_score=10000)
        pv = info.get("pv", [])
        previous_best = pv[0] if pv else None
        for move in game.mainline_moves():
            player = "white" if board.turn == chess.WHITE else "black"
            best_move_san = board.san(previous_best) if previous_best else None
            played_best = (move == previous_best)
            board.push(move)
            info = engine.analyse(board, chess.engine.Limit(depth=15))
            score = info["score"].white()
            eval_cp = score.score(mate_score=10000)
            delta = eval_cp - previous_eval
            is_blunder = (player == "white" and delta <= -200) or (player == "black" and delta >= 200)
            results.append({"move": str(move), "player": player, "evaluation": str(score), "delta": delta, "is_blunder": is_blunder, "best_move": best_move_san, "played_best": played_best})
            pv = info.get("pv", [])
            previous_best = pv[0] if pv else None
            previous_eval = eval_cp
    return results