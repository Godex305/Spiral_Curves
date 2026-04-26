from manim import *
import numpy as np

class ZoomGraphExample(MovingCameraScene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            x_length=8,
            y_length=8,
        )
        graph = plane.plot(lambda x: 0.1*x**3, x_range=[-8, 8], color=YELLOW)

        self.add(plane, graph)
        self.wait()

        # Zoom in
        self.play(
            self.camera.frame.animate.scale(0.5),
            run_time=2
        )

        # Move camera to a part of the graph
        point = plane.c2p(6, 0.1*6**3)
        self.play(
            self.camera.frame.animate.move_to(point),
            run_time=2
        )

        # Zoom out
        self.play(
            self.camera.frame.animate.scale(3).move_to(ORIGIN),
            run_time=2
        )

        self.wait()