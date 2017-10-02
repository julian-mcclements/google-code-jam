import unittest
from maze import Maze
from mazebuilder import Paths, MazeBuilder

# See http://stackoverflow.com/questions/644821/python-how-to-run-unittest-main-for-all-source-files-in-a-subdirectory on 
# how to run python unit tests from the command line.
# i.e. "python -m unittest discover --pattern=test_mazebuilder.py"

class TestBuildMaze(unittest.TestCase):
    ''' Test a MazeBuilder instance can build mazes correctly '''

    def test_first_maze(self):
        paths = Paths('WW', 'WW')
        builder = MazeBuilder()
        maze = builder.construct(paths)

        maze_as_matrix = maze.to_matrix()
        self.assertEqual(len(maze_as_matrix), 1)
        self.assertEqual(len(maze_as_matrix[0]), 1)
        self.assertEqual(maze_as_matrix[0][0], 3)

    def test_second_maze(self):
        paths = Paths('WRWWLWWLWWLWLWRRWRWWWRWWRWLW', 'WWRRWLWLWWLWWLWWRWWRWWLW')
        builder = MazeBuilder()
        maze = builder.construct(paths)

        self.assertEqual(len(maze.rooms), 15)

        maze_as_matrix = maze.to_matrix()
        self.assertEqual(len(maze_as_matrix), 5)
        self.assertEqual(len(maze_as_matrix[0]), 3)
        self.assertEqual(len(maze_as_matrix[1]), 3)
        self.assertEqual(len(maze_as_matrix[2]), 3)
        self.assertEqual(len(maze_as_matrix[3]), 3)
        self.assertEqual(len(maze_as_matrix[4]), 3)

        self.assertEqual(maze_as_matrix[0][0], 10)
        self.assertEqual(maze_as_matrix[0][1], 12)
        self.assertEqual(maze_as_matrix[0][2], 5)

        self.assertEqual(maze_as_matrix[1][0], 3)
        self.assertEqual(maze_as_matrix[1][1], 8)
        self.assertEqual(maze_as_matrix[1][2], 6)

        self.assertEqual(maze_as_matrix[2][0], 9)
        self.assertEqual(maze_as_matrix[2][1], 12)
        self.assertEqual(maze_as_matrix[2][2], 7)

        self.assertEqual(maze_as_matrix[3][0], 14)
        self.assertEqual(maze_as_matrix[3][1], 4)
        self.assertEqual(maze_as_matrix[3][2], 3)
  
        self.assertEqual(maze_as_matrix[4][0], 9)
        self.assertEqual(maze_as_matrix[4][1], 12)
        self.assertEqual(maze_as_matrix[4][2], 5)
