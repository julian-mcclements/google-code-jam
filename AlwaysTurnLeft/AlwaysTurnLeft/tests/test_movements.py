import unittest
from maze import NORTH, EAST, SOUTH, WEST, EXITS, Maze, Room
from mazebuilder import Walker
from movements import MovementBase, TurnRight, TurnLeft, Walk, Enter, Exit, Reenter

# See http://stackoverflow.com/questions/644821/python-how-to-run-unittest-main-for-all-source-files-in-a-subdirectory on 
# how to run python unit tests from the command line.
# i.e. "python -m unittest discover --pattern=test_movements.py"

class TestTurnRight(unittest.TestCase):
    ''' Test fixture for the command object to turn right. '''

    def test_turn_right_ninety_degrees(self):

        test_cases = []
        test_cases.append((NORTH, EAST))
        test_cases.append((EAST, SOUTH))
        test_cases.append((SOUTH, WEST))
        test_cases.append((WEST, NORTH))

        for (original_direction, expected_direction) in test_cases:
            walker = Walker(None, original_direction)
            movement = TurnRight(walker)
            movement.move();
            self.assertEqual(walker.direction, expected_direction)

class TestTurnLeft(unittest.TestCase):
    ''' Test fixture for the command object to turn left. '''

    def test_turn_left_ninety_degrees(self):

        test_cases = []
        test_cases.append((NORTH, WEST))
        test_cases.append((WEST, SOUTH))
        test_cases.append((SOUTH, EAST))
        test_cases.append((EAST, NORTH))

        for (original_direction, expected_direction) in test_cases:
            walker = Walker(None, original_direction)
            movement = TurnLeft(walker)
            movement.move();
            self.assertEqual(walker.direction, expected_direction)

class TestWalk(unittest.TestCase):
    ''' Test fixture for the command object to walk straight ahead. '''
    
    def test_walk_south_into_new_room(self):
        
        maze = Maze()
        start_room = Room((0,0), EXITS[NORTH])
        maze.add_room(start_room)
        end_room = Room((1,0), EXITS[NORTH])
        walker = Walker(start_room, SOUTH)

        walk = Walk(walker, maze)
        walk.move();
        
        self.assertEqual(walker.direction, SOUTH)
        self.assertEqual(walker.room, end_room)
        self.assertEqual(maze.has_room(end_room.vector), True)
        self.assertEqual(maze.rooms[end_room.vector], end_room)
        self.assertEqual(maze.rooms[start_room.vector].exits, 3)

    def test_walk_east_into_new_room(self):
        
        maze = Maze()
        start_room = Room((0,0), EXITS[NORTH])
        maze.add_room(start_room)
        end_room = Room((0, -1), EXITS[WEST])
        walker = Walker(start_room, EAST)

        walk = Walk(walker, maze)
        walk.move();
        
        self.assertEqual(walker.direction, EAST)
        self.assertEqual(walker.room, end_room)
        self.assertEqual(maze.has_room(end_room.vector), True)
        self.assertEqual(maze.rooms[end_room.vector], end_room)
        self.assertEqual(maze.rooms[start_room.vector].exits, 9)

    def test_walk_west_into_new_room(self):
        
        maze = Maze()
        start_room = Room((0,0), EXITS[NORTH])
        maze.add_room(start_room)
        end_room = Room((0, 1), EXITS[EAST])
        walker = Walker(start_room, WEST)

        walk = Walk(walker, maze)
        walk.move();
        
        self.assertEqual(walker.direction, WEST)
        self.assertEqual(walker.room, end_room)
        self.assertEqual(maze.has_room(end_room.vector), True)
        self.assertEqual(maze.rooms[end_room.vector], end_room)
        self.assertEqual(maze.rooms[start_room.vector].exits, 5)

    def test_walk_north_into_new_room(self):
        
        maze = Maze()
        start_room = Room((1,2), EXITS[SOUTH])
        maze.add_room(start_room)
        end_room = Room((0,2), EXITS[SOUTH])
        walker = Walker(start_room, NORTH)

        walk = Walk(walker, maze)
        walk.move();
        
        self.assertEqual(walker.direction, NORTH)
        self.assertEqual(walker.room, end_room)
        self.assertEqual(maze.has_room(end_room.vector), True)
        self.assertEqual(maze.rooms[end_room.vector], end_room)
        self.assertEqual(maze.rooms[start_room.vector].exits, 3)

    def test_walk_back_north_into_known_room_through_known_entrance(self):
        known_exits = 3
        start_room = Room((1,0), EXITS[NORTH])
        end_room = Room((0,0), known_exits)
        maze = Maze()
        maze.add_room(start_room)
        maze.add_room(end_room)
        walker = Walker(start_room, NORTH)
        
        walk = Walk(walker, maze)
        walk.move()         
        
        self.assertEqual(walker.direction, NORTH)
        self.assertEqual(walker.room, end_room)
        self.assertEqual(maze.rooms[start_room.vector].exits, EXITS[NORTH])
        self.assertEqual(maze.rooms[end_room.vector].exits, known_exits)

    def test_walk_back_south_into_known_room_through_known_entrance(self):
        known_exits = 3
        start_room = Room((1,1), EXITS[SOUTH])
        end_room = Room((2,1), known_exits)
        maze = Maze()
        maze.add_room(start_room)
        maze.add_room(end_room)
        walker = Walker(start_room, SOUTH)
        
        walk = Walk(walker, maze)
        walk.move()         
        
        self.assertEqual(walker.direction, SOUTH)
        self.assertEqual(walker.room, end_room)
        self.assertEqual(maze.rooms[start_room.vector].exits, EXITS[SOUTH])
        self.assertEqual(maze.rooms[end_room.vector].exits, known_exits)

    def test_walk_back_east_into_known_room_through_known_entrance(self):
        known_exits = 12
        start_room = Room((1,1), EXITS[EAST])
        end_room = Room((1,0), known_exits)
        maze = Maze()
        maze.add_room(start_room)
        maze.add_room(end_room)
        walker = Walker(start_room, EAST)
        
        walk = Walk(walker, maze)
        walk.move()         
        
        self.assertEqual(walker.direction, EAST)
        self.assertEqual(walker.room, end_room)
        self.assertEqual(maze.rooms[start_room.vector].exits, EXITS[EAST])
        self.assertEqual(maze.rooms[end_room.vector].exits, known_exits)

    def test_walk_back_west_into_known_room_through_known_entrance(self):
        known_exits = 12
        start_room = Room((1,1), EXITS[WEST])
        end_room = Room((1,2), known_exits)
        maze = Maze()
        maze.add_room(start_room)
        maze.add_room(end_room)
        walker = Walker(start_room, WEST)
        
        walk = Walk(walker, maze)
        walk.move()         
        
        self.assertEqual(walker.direction, WEST)
        self.assertEqual(walker.room, end_room)
        self.assertEqual(maze.rooms[start_room.vector].exits, EXITS[WEST])
        self.assertEqual(maze.rooms[end_room.vector].exits, known_exits)

    def test_walk_back_north_into_known_room_through_new_entrance(self):
        previously_known_exits = EXITS[NORTH]
        now_known_exits = 3
        start_room = Room((1,0), EXITS[NORTH])
        end_room = Room((0,0), previously_known_exits)
        maze = Maze()
        maze.add_room(start_room)
        maze.add_room(end_room)
        walker = Walker(start_room, NORTH)
        
        walk = Walk(walker, maze)
        walk.move()         
        
        self.assertEqual(walker.direction, NORTH)
        self.assertEqual(walker.room, end_room)
        self.assertEqual(maze.rooms[start_room.vector].exits, EXITS[NORTH])
        self.assertEqual(maze.rooms[end_room.vector].exits, now_known_exits)

    def test_walk_back_south_into_known_room_through_new_entrance(self):
        previously_known_exits = EXITS[SOUTH]
        now_known_exits = 3
        start_room = Room((1,1), EXITS[SOUTH])
        end_room = Room((2,1), previously_known_exits)
        maze = Maze()
        maze.add_room(start_room)
        maze.add_room(end_room)
        walker = Walker(start_room, SOUTH)
        
        walk = Walk(walker, maze)
        walk.move()         
        
        self.assertEqual(walker.direction, SOUTH)
        self.assertEqual(walker.room, end_room)
        self.assertEqual(maze.rooms[start_room.vector].exits, EXITS[SOUTH])
        self.assertEqual(maze.rooms[end_room.vector].exits, now_known_exits)

    def test_walk_back_east_into_known_room_through_new_entrance(self):
        previously_known_exits = EXITS[EAST]
        now_known_exits = 12
        start_room = Room((1,1), EXITS[EAST])
        end_room = Room((1,0), previously_known_exits)
        maze = Maze()
        maze.add_room(start_room)
        maze.add_room(end_room)
        walker = Walker(start_room, EAST)
        
        walk = Walk(walker, maze)
        walk.move()         
        
        self.assertEqual(walker.direction, EAST)
        self.assertEqual(walker.room, end_room)
        self.assertEqual(maze.rooms[start_room.vector].exits, EXITS[EAST])
        self.assertEqual(maze.rooms[end_room.vector].exits, now_known_exits)

    def test_walk_back_west_into_known_room_through_new_entrance(self):
        previously_known_exits = EXITS[WEST]
        now_known_exits = 12
        start_room = Room((1,1), EXITS[WEST])
        end_room = Room((1,2), previously_known_exits)
        maze = Maze()
        maze.add_room(start_room)
        maze.add_room(end_room)
        walker = Walker(start_room, WEST)
        
        walk = Walk(walker, maze)
        walk.move()         
        
        self.assertEqual(walker.direction, WEST)
        self.assertEqual(walker.room, end_room)
        self.assertEqual(maze.rooms[start_room.vector].exits, EXITS[WEST])
        self.assertEqual(maze.rooms[end_room.vector].exits, now_known_exits)

class TestEnter(unittest.TestCase):
    '''Test fixture for command object to enter a maze'''

    def test_enter_maze(self):

        maze = Maze()
        start_room = Room((0,0), EXITS[NORTH])
        walker = Walker(None, SOUTH)
        enter = Enter(walker, maze)
        enter.move();

        self.assertEqual(walker.direction, SOUTH)
        self.assertEqual(walker.room, start_room)
        self.assertEqual(maze.has_room(start_room.vector), True)
        self.assertEqual(maze.rooms[start_room.vector], start_room)
        self.assertEqual(maze.entrances.first, (0,0))

class TestExit(unittest.TestCase):
    '''Test fixture for command object to exit a maze'''

    def test_exit_maze(self):

        maze = Maze()
        exit_room = Room((2,2), 0)
        maze.add_room(exit_room)
        walker = Walker(exit_room, WEST)
        movement = Exit(walker, maze)
        movement.move()

        self.assertEqual(walker.room, None)
        self.assertEqual(maze.rooms[exit_room.vector].exits, WEST)
        self.assertEqual(maze.entrances.second, (2,2))

class TestReenter(unittest.TestCase):
    '''Test fixture for command object to reenter a maze'''

    def test_reenter_maze(self):

        test_cases = []
        test_cases.append((NORTH, SOUTH))
        test_cases.append((EAST, WEST))
        test_cases.append((SOUTH, NORTH))
        test_cases.append((WEST, EAST))

        test_case_second_entrances = { 
            NORTH: Room((0,2), EXITS[NORTH]), 
            EAST: Room((1, -2), EXITS[EAST]),
            SOUTH: Room((2, 2), EXITS[SOUTH]),
            WEST: Room((1, 2), EXITS[WEST])
        }

        for (original_direction, expected_direction) in test_cases:
            maze = Maze()
            second_entrance = test_case_second_entrances[original_direction]
            maze.add_room(second_entrance)
            maze.entrances.second = second_entrance.vector
            walker = Walker(None, original_direction)
            movement = Reenter(walker, maze)
            movement.move()

            self.assertEqual(walker.direction, expected_direction)
            self.assertEqual(walker.room, second_entrance)

if __name__ == '__main__':
    unittest.main()
