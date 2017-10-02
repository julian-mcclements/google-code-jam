(NORTH, EAST, SOUTH, WEST) = range(1, 5)

EXITS = { 1: 1, 2: 8, 3: 2, 4: 4 }

class Room():

    ''' A single room in the maze.'''

    def __init__(self, vector, exits):
        # Vector (expressed as a sum of row and column vectors) to reach the room from maze entrance.
        # Moving west and south is postive; north and east is negative.
        self.vector = vector    
        # Bit array that describes in what directions you can exit from the room.
        self.exits = exits     

    # If all you want to do is compare the equality of all attributes, you can do that succinctly by 
    # comparison of __dict__ in each object. See http://stackoverflow.com/questions/6423814/is-there-a-way-to-check-if-two-object-contain-the-same-values-in-each-of-their-v.
    def __eq__(self, other) : 
        return self.__dict__ == other.__dict__

class MazeEntrances():

        ''' Holds references for entrances in the maze'''

        def __init__(self):
            self.first = None
            self.second = None

class Maze():

    '''The maze.'''

    def __init__(self):
        self.rooms = {}
        # Vectors of entrances to maze
        self.entrances = MazeEntrances()
        self.__directions = { EAST: 0, SOUTH: 0, WEST: 0} 
        
    def add_room(self, new_room):
        (new_room_row_direction, new_room_column_direction) = new_room.vector
        self.rooms[new_room.vector] = new_room
        directions = self.__directions
        directions[SOUTH] = max([directions[SOUTH], new_room_row_direction])
        if (new_room_column_direction > 0):
            directions[WEST] = max([directions[WEST], new_room_column_direction])
        else:
            directions[EAST] = min([directions[EAST], new_room_column_direction])

    def has_room(self, vector):
        return vector in self.rooms

    def to_matrix(self):
        directions = self.__directions
        matrix = []
        row_index = 0

        while row_index <= directions[SOUTH]:
            row = []
            column_index = directions[WEST]
            while column_index >= directions[EAST]:
                exits = self.rooms[(row_index, column_index)].exits
                row.append(exits)
                column_index -= 1
            matrix.append(row)
            row_index += 1
        return matrix

