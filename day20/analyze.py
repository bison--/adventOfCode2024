from Maze import Maze
from MazeRunner import MazeRunner


maze = Maze("map1.txt")
maze.print_stats()
runner = MazeRunner(maze)

runner.run()
#runner.walk_symbol = ' '
#runner.clear_symbol = '#'
runner.print_path(True)
