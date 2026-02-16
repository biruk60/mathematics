from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle), run_time=1)  # show the circle on screen


# manim -pqh main.py CreateCircle

class Addition(Scene):
    def construct(self):
        # Load the flamingo SVG from assets/svgs
        # Assuming the file is named "flamingo.svg"
        flamingo = SVGMobject("assets/svgs/flamingo.svg")
        flamingo.set(height=2)          # Resize if needed
        # flamingo.set_fill(PINK, 1.0)    # Optional styling
        # flamingo.set_stroke(BLACK, 1.5)

        # Create 4 copies
        flamingos = VGroup(*[flamingo.copy() for _ in range(4)])

        # Arrange them in a 2x2 grid
        flamingos.arrange_in_grid(rows=2, cols=2, buff=1.0)

        # Optionally center and scale
        flamingos.move_to(ORIGIN)
        flamingos.scale(0.8)

        # Animate them in
        self.play(LaggedStartMap(FadeIn, flamingos, lag_ratio=0.15))
        self.wait(2)