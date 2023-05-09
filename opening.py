import hashlib
import chess

class Opening:

    def __init__(self, eco, name, pgn):
        self.eco = eco
        self.name = name
        self.pgn = pgn
    
    def _generate_opening_hashes(self):
        # generate a hash for each possible board configuration reachable
        # from the starting position.
        pass

def parse_sequence(opening_sequence: str):
    moves = []

    opening_sequence = opening_sequence.split(" ")

    for value in opening_sequence:
        if value[-1] == ".":
            continue
        moves.append(value)
    
    return moves

def generate_hash(board):
    return hashlib.sha256(str(board).encode('utf-8')).hexdigest()