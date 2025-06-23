from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, radius):
        super().__init__(radius)
        self.radius = SHOT_RADIUS
        