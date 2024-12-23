from Maze import Maze
from MazeRunner import MazeRunner
from Cheater import Cheater

"""
maze = Maze("map1.txt")
maze.print_stats()
runner = MazeRunner(maze)

runner.run()
#runner.walk_symbol = ' '
#runner.clear_symbol = '#'
runner.print_path(True)
"""

cheater = Cheater("map1.txt")
cheater.run_cheater()
cheater.print_stats()
