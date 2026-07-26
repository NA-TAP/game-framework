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
        self.movement = parse_mvment(movement)
        
    def __eq__(self, value):
        if isinstance(value, Piece):
            return self.kind == value.kind and self.color == value.color
        elif isinstance(value, tuple):
            kind, color = value
            return self.kind == kind and self.color == color
        
    def parse_mvment(mvment):
        pass    
