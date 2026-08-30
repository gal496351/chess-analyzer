# Chess Analyzer

A chess analysis tool that explains *why* moves are good or bad — not just how good they are.

## The Problem

Engines like Stockfish give you a number (e.g. "+1.5"), but they don't explain the reasoning behind it. This project fills that gap: upload a game, and get a clear, human explanation of its critical moments.

## How It Works

The tool is built around a deliberate separation between fact and explanation:

- **Truth layer** — Stockfish (with MultiPV) computes evaluations and candidate lines.
- **Explanation layer** — a language model narrates *only verified facts*; it never invents moves.
- **Validation** — every variation is checked before it is shown to the user.

## Tech Stack

- **Frontend:** React + TypeScript (`react-chessboard`, `chess.js`)
- **Backend:** Python + FastAPI (`python-chess`, Stockfish)

## Status

🚧 In development — building the MVP: PGN upload → critical-moment detection → explained analysis with interactive lines.