from Maze import Maze
from AStar import AStar


class MazeRunner:
    def __init__(self, maze: Maze):
        self.walk_symbol = 'X'
        self.clear_symbol = ' '
        self.maze: Maze = maze
        self.astar = AStar(maze)
        self.current_position = maze.start_position
        self.target_position = maze.end_position
        self.found_path = []

    def get_path_steps(self):
        if not self.found_path:
            return -1

        return len(self.found_path) - 1  # start should not count as a step

    def run(self):
        self.found_path = self.astar.search(self.current_position, self.target_position)
        if self.found_path:
            #print("Path found:", path)
            print("Path Steps:", self.get_path_steps())
        else:
            print("No path found")

    def print_path(self, clear_path=False):
        maze_walk_map = self.maze.data_rows.copy()
        for y in range(len(maze_walk_map)):
            for x in range(len(maze_walk_map[y])):
                if (x, y) in self.found_path:
                    maze_walk_map[y][x] = self.walk_symbol
                elif clear_path:
                    maze_walk_map[y][x] = self.clear_symbol
                else:
                    maze_walk_map[y][x] = self.maze.data_rows[y][x]

        for row in maze_walk_map:
            print(''.join(row))
