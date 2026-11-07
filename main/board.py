import re

def construct_dict(width, height):
    """Creates a dictionary of width and height

    Args:
        width (int): the width of the dict as a board
        height (int): the height of the dict as a board

    Returns:
        dict: Dictionary of tuple (x, y): None for every x and y in width and height
    """
    coordict = {}
    for x in range(width):
        for y in range(height):
            coordict[(x, y)] = Piece(None, None)
    return coordict

class Board:
    def __init__(self, setup, metadata, width, height):
        self.setup = setup
        self.metadata = metadata
        self.width = width
        self.height = height
        
    def __getitem__(self, x, y):
        return self.setup[(x, y)]
    
    def render(self, conversion):
        """renders the board. the conversions dictionary needs a Piece(None, None) case.

        Args:
            conversion (dict): converts pieces to characters
        """
        lines = []
        for y in range(self.height):
            line = []
            for x in range(self.height):
                line.append(conversion[self.setup[(x,y)]])
            lines.append(" ".join(line))
        print("\n".join(lines))
    
class Piece:
    def __init__(self, kind, color, movement):
        self.kind = kind
        self.color = color
        self.movement = self.parse_mvment(movement)
        
    def __eq__(self, value):
        if isinstance(value, Piece):
            return self.kind == value.kind and self.color == value.color
        elif isinstance(value, tuple):
            kind, color = value
            return self.kind == kind and self.color == color
        
    def parse_mvment(self, mvment):
        matches = re.fullmatch(r"^S\(([-0-9,|]+)\)/J\(([-0-9,|]+)\)$",mvment, re.IGNORECASE, re.MULTILINE, re.UNICODE)
        groups = matches.groups()
        slide = groups[1]
        jump = groups[2] 
        sl = [tuple(thing.split(",")) for thing in slide.split("|")]
        jmp = [tuple(thing.split(",")) for thing in jump.split("|")]
        return {
            "slide": sl,
            "jump": jmp
        }

    def is_move_legal(self, start, end, board):
        d_rank = start[1] - end[1]
        d_rank = abs(d_rank)
        d_file = start[0] - end[0]
        d_file = abs(d_file)
        move = (d_file, d_rank)
        slideflag = False
        for available_jump in self.movement["jump"]:
            if available_jump == move:
                return True
        for available_slide in self.movement["slide"]:
            slideflag = slide_movement_legal(start, end, available_slide) if not slideflag else True
        return slideflag

    def slide_movement_legal(start, end, slidedir, board):
        d_rank = start[1] - end[1]
        d_rank = abs(d_rank)
        d_file = start[0] - end[0]
        d_file = abs(d_file)
        move = (d_file, d_rank)
        if (slidedir[1]//d_rank) - (slidedir[1]/d_rank) == 0.0:
            if (slidedir[2]//d_file) - (slidedir[2]/d_file) == 0.0:
                pass
            else:
                return False
        else:
            return False
        return True
