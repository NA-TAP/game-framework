import sys
from pathlib import Path

# Add the parent directory (my_project) to the Python path then imprting dependencies
sys.path.append(str(Path(__file__).resolve().parent.parent))
from boardandpieces import Board, Piece
from card import Card, Deck
