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
            coordict[(x, y)] = None
    return coordict

class Board:
    def __init__(self, setup, metadata):
        self.setup = setup
        self.metadata = metadata
        
    def __getitem__(self, x, y):
        return self.setup[(x, y)]
    
    def render():
        pass # TODO: add board rendering in boardrender.py
