from maze import Maze
from mazebuilder import Paths, MazeBuilder
from movements import TurnRight, TurnLeft, Walk, Enter, Exit, Reenter

if __name__ == '__main__':

    test_cases = []
    firstLineRead = False
    with open("B-large-practice.in") as f:
        for line in f:
            if firstLineRead:
                entrance_to_exit, exit_to_entrance = line.strip().split(" ")
                test_cases.append(Paths(entrance_to_exit, exit_to_entrance))
            else:
                case_count = int(line.strip())
                firstLineRead = True
    
    print("There should be {0} test cases.".format(case_count));

    builder = MazeBuilder()
    output = []
    for test_case in test_cases:
        maze = builder.construct(test_case)
        output.append(maze.to_matrix()) 

    count = 1
    with open('B-large-practice-output.txt', 'a') as output_file:
        for maze_matrix in output:
            output_file.write("Case #{0}:\n".format(count))
            for row in maze_matrix:
                output_file.write(''.join('%x'%column for column in row) + "\n")
            count += 1