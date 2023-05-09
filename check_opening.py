import chess
import opening
import json
board = chess.Board()

with open("board_hashes.json", "r") as file:
    board_hashes = json.load(file)

print(board)

move = input("\nEnter a move: ")

board.push_san(move)

print(board)

h = opening.generate_hash(board)

print(board_hashes[h])

