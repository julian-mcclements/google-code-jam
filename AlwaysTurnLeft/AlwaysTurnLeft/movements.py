from abc import ABCMeta, abstractmethod
from maze import NORTH, EAST, SOUTH, WEST, EXITS, Room

class MovementBase(metaclass=ABCMeta):
    '''
    Abstract base class for the different types of moves available when traversing a maze.
    '''
       
    @abstractmethod
    def move(self): 
        pass

class TurnRight(MovementBase):
    '''
    Turn right (or clockwise) 90 degrees.
    '''
    new_direction = { NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH }

    def __init__(self, walker):
        self.__walker = walker

    def move(self):
        original_direction = self.__walker.direction
        self.__walker.direction = TurnRight.new_direction[original_direction]
        
class TurnLeft(MovementBase):
    '''
    Turn left (or anti-clockwise) 90 degrees.
    '''
    new_direction = { NORTH: WEST, EAST: NORTH, SOUTH: EAST, WEST: SOUTH }

    def __init__(self, walker):
        self.__walker = walker

    def move(self):
        original_direction = self.__walker.direction
        self.__walker.direction = TurnLeft.new_direction[original_direction]

class Walk(MovementBase):
    '''
    Walk forward into the next room.
    '''
    vector = { NORTH: (-1, 0), EAST: (0, -1), SOUTH: (1, 0), WEST: (0, 1)}

    # The keys for the exit_defaults match the possible directions a walker can move.
    # Since a walker will move into the room through the entrance on the wall opposite
    # her current direction each key will set to the opposite direction (forex a walker
    # facing south will move through the north-facing entrance\exit of the new room).
    entrance_exit_map = { NORTH: EXITS[SOUTH], 
        EAST: EXITS[WEST], 
        SOUTH: EXITS[NORTH], 
        WEST: EXITS[EAST]
        }

    def __init__(self, walker, maze):
        self.__walker = walker
        self.__maze = maze

    def __hasDiscoveredExit(self, room_exits, exit_direction):
        return (room_exits & exit_direction) == 0

    def move(self):
        start_room = self.__walker.room
        (row, col) = start_room.vector
        (delta_row, delta_col) = Walk.vector[self.__walker.direction]
        next_room_vector = (row + delta_row, col + delta_col)
        next_room_entrance = Walk.entrance_exit_map[self.__walker.direction]
        if self.__maze.has_room(next_room_vector):
            # Walker has returned to a known room.
            next_room = self.__maze.rooms[next_room_vector]
            if self.__hasDiscoveredExit(next_room.exits, next_room_entrance):
                # Walker has found a new entrance\exit to the room
                next_room.exits = next_room.exits | next_room_entrance
        else:
            # Walker has moved into a newly-discovered room.
            new_room = Room(next_room_vector, next_room_entrance) 
            self.__maze.add_room(new_room)
            # Update exits of room that walker has just left to show newly
            # discovered exit.
            start_room.exits = start_room.exits | EXITS[self.__walker.direction]

        self.__walker.room = self.__maze.rooms[next_room_vector]

class Enter(MovementBase):

    def __init__(self, walker, maze):
        self.__walker = walker
        self.__maze = maze

    def move(self):
        entrance_room = Room((0,0), EXITS[NORTH])
        self.__maze.add_room(entrance_room)
        self.__maze.entrances.first = (0,0)
        self.__walker.room = entrance_room

class Exit(MovementBase):

    def __init__(self, walker, maze):
        self.__walker = walker
        self.__maze = maze

    def move(self):
        exit_room = self.__walker.room
        self.__walker.room = None
        exit_room.exits = exit_room.exits | EXITS[self.__walker.direction]
        self.__maze.entrances.second = exit_room.vector

class Reenter(MovementBase):

    new_direction = { NORTH: SOUTH, EAST: WEST, SOUTH: NORTH, WEST: EAST }

    def __init__(self, walker, maze):
        self.__walker = walker
        self.__maze = maze

    def move(self):
        self.__walker.direction = Reenter.new_direction[self.__walker.direction]
        self.__walker.room = self.__maze.rooms[self.__maze.entrances.second]