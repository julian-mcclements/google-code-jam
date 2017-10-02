from maze import NORTH, EAST, SOUTH, WEST, Maze, Room
from movements import MovementBase, TurnRight, TurnLeft, Walk, Enter, Exit, Reenter

class Paths():
    ''' Holds the paths to take through the maze '''

    def __init__(self, entrance_to_exit, exit_to_entrance):
        self.entrance_to_exit = entrance_to_exit
        self.exit_to_entrance = exit_to_entrance

class Walker():
    ''' Follows the path through the maze and reveals its layout. '''

    def __init__(self, start_room, direction):
        self.direction = direction     # Direction that the walker currently faces.
        self.room = start_room
        
class MazeBuilder():

    command = { 'LEFT': 'L', 'RIGHT': 'R', 'FORWARD': 'W'}

    def __init__(self):
        self.maze = None
        self.walker = None

    def __walk_path(self, path, is_reentering = False):
        
        char_index = 0
        path_length = len(path)
        commands = MazeBuilder.command
                
        for character in list(path):
            movement = None
            if char_index == 0 and character == commands['FORWARD']:
                movement = Reenter(self.walker, self.maze) if is_reentering else Enter(self.walker, self.maze)
            elif char_index == (path_length - 1) and character == commands['FORWARD']:
                movement = Exit(self.walker, self.maze)
            elif character == commands['LEFT']:
                movement = TurnLeft(self.walker)
            elif character == commands['RIGHT']:
                movement = TurnRight(self.walker)
            elif character == commands['FORWARD']:
                movement = Walk(self.walker, self.maze)
            else:
                raise RuntimeError("Unexpected character found in path. Value is '{0}'.".format(character))
            movement.move()
            char_index += 1        
                
    def construct(self, paths):
        self.maze = Maze()
        self.walker = Walker(None, SOUTH)
        self.__walk_path(paths.entrance_to_exit)
        self.__walk_path(paths.exit_to_entrance, True)
        return self.maze


        