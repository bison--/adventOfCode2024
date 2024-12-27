from Maze import Maze
from MazeRunner import MazeRunner


class Cheater:
    CHEAT_DIRECTION_NONE = 0
    CHEAT_DIRECTION_X = 1
    CHEAT_DIRECTION_Y = 2

    class CheaterStats:
        def __init__(self, steps, base_steps):
            self.steps = steps
            self.base_steps = base_steps
            self.improvement = self.get_improvement()

        def get_improvement(self):
            return self.base_steps - self.steps

    def __init__(self, map_file="map1.txt"):
        self.maze: Maze = Maze(map_file)

        self.maze_runner = MazeRunner(self.maze)
        self.baseline_steps = 0
        self.stats: list[Cheater.CheaterStats] = []

    def run_cheater(self):
        self.maze_runner.run()
        self.baseline_steps = self.maze_runner.get_path_steps()

        if self.baseline_steps == -1:
            raise Exception("No path found")

        total_cheats = self.maze.get_height() * self.maze.get_width()
        current_index = 0

        for y in range(self.maze.get_height()):
            for x in range(self.maze.get_width()):
                current_index += 1
                print(f"Running cheater {current_index}/{total_cheats}")

                for cheat_direction in [self.CHEAT_DIRECTION_NONE]:
                    self.maze.reset_map_data()
                    if not self.cheat(x, y, cheat_direction):
                        continue

                    self.maze_runner.run()
                    steps = self.maze_runner.get_path_steps()

                    # the cheat itself cost 2 steps
                    steps += 2

                    if steps >= self.baseline_steps:
                        continue

                    if steps == 22:
                        self.maze_runner.print_path(True)

                    self.stats.append(
                        Cheater.CheaterStats(
                            steps,
                            self.baseline_steps
                    ))

    def cheat(self, cheat_position_x, cheat_position_y, cheat_direction):
        self.maze.reset_map_data()

        # borders do not affect the walk-cycle
        if self.maze.is_border(cheat_position_x, cheat_position_y):
            return False

        if not self._has_walkable_nearby(cheat_position_x, cheat_position_y):
            return False

        if cheat_direction == self.CHEAT_DIRECTION_X:
            if not self._has_walkable_nearby(cheat_position_x + 1, cheat_position_y):
                return False
        elif cheat_direction == self.CHEAT_DIRECTION_Y:
            if not self._has_walkable_nearby(cheat_position_x, cheat_position_y + 1):
                return False

        self.maze.remove_wall(cheat_position_x, cheat_position_y)

        if cheat_direction == self.CHEAT_DIRECTION_X:
            self.maze.remove_wall(cheat_position_x + 1, cheat_position_y)
        elif cheat_direction == self.CHEAT_DIRECTION_Y:
            self.maze.remove_wall(cheat_position_x, cheat_position_y + 1)

        return True

    def _has_walkable_nearby(self, x, y):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if self.maze.can_walk(nx, ny):
                return True

        return False

    def print_stats(self):
        print("Baseline steps:", self.baseline_steps)
        print("Stats:")

        self.stats.sort(key=lambda _stat: _stat.improvement)

        grouped = {}
        for stat in self.stats:
            print(f"Improvement: {stat.improvement}  Steps: {stat.steps}, count: -")
            if stat.improvement not in grouped:
                grouped[stat.improvement] = 0
            grouped[stat.improvement] += 1

        print("#" * 20)

        for steps in sorted(grouped.keys()):
            print(f"There are {grouped[steps]} cheats that save {steps} picoseconds")

