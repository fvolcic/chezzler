import chess
from data_reader import read_openings
from opening import *
import hashlib
import json

openings = read_openings()

opening = openings["E93"]
sequence = opening[2] 

board_hashes = {} 


def hash_opening(opening):
    board = chess.Board()
    for move in parse_sequence(opening[2]):
        board.push_san(move)
        h = generate_hash(board) #hashlib.sha256(str(board).encode('utf-8')).hexdigest()
        
        if h in board_hashes:
            board_hashes[h].append(opening[0])
        else:
            board_hashes[h] = [opening[0]]

del openings["eco"]

for opening in openings:
    hash_opening(openings[opening])

with open("board_hashes.json", "w") as file:
    json.dump(board_hashes, file)




