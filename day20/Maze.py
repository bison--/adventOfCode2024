class Maze:
    WALL = '#'
    PATH = '.'
    START = 'S'
    END = 'E'

    def __init__(self, map_file="map1.txt"):
        self.map_file = map_file
        self.file_rows = []
        self.data_rows = []
        self.start_position = (-1, -1)
        self.end_position = (-1, -1)

        self.load_map(self.map_file)

    def get_width(self):
        return len(self.data_rows[0])

    def get_height(self):
        return len(self.data_rows)

    def load_map(self, map_file):
        self.data_rows = []

        with open(map_file, 'r') as f:
            for line in f.readlines():
                line_clean = line.strip()
                self.file_rows.append(line_clean)

        self.reset_map_data()

    def reset_map_data(self):
        # TODO: maybe a simple "copy" would be sufficient

        row_index = -1
        for line in self.file_rows:
            row_index += 1

            start_index = line.find(self.START)
            end_index = line.find(self.END)

            if start_index != -1:
                self.start_position = (start_index, row_index)

            if end_index != -1:
                self.end_position = (end_index, row_index)

            row_blocks = list(line)
            self.data_rows.append(row_blocks)

    def can_walk(self, x, y):
        if not self.is_on_map(x, y):
            return False

        if self.data_rows[y][x] != self.WALL:
            return True

        return False

    def is_type(self, x, y, map_type):
        if not self.is_on_map(x, y):
            return False

        if self.data_rows[y][x] == map_type:
            return True

        return False

    def is_on_map(self, x, y):
        if x < 0 or y < 0:
            return False

        if x >= len(self.data_rows[0]) or y >= len(self.data_rows):
            return False

        return True

    def remove_wall(self, x, y):
        if not self.is_type(x, y, self.WALL):
            return False

        self.data_rows[y][x] = self.PATH
        return True

    def print_stats(self):
        print("Start:", self.start_position)
        print("End:", self.end_position)
        for row in self.data_rows:
            print(''.join(row))
