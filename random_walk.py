from random import choice

class RandomWalk():
    """Generate random walks"""

    def __init__(self, num_points=5000):
        """Init attr of a walk"""
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in a walk"""

        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            x_next = self.x_values[-1] + x_step
            y_next = self.y_values[-1] + y_step

            self.x_values.append(x_next)
            self.y_values.append(y_next)

    def get_step(self):
        """Decide which direction to go and how far to go in that direction"""
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        return distance * direction
