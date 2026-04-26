from manim import *
import numpy as np

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920



class ArchimedeanSpiral(Scene):
    def construct(self):
        title = Tex(r"Polar Sketch of")
        title.to_edge(UP)
        polar_curve = Tex(r"Archimedean Spiral")
        polar_curve.next_to(title, DOWN, buff=0.3)

        formula = MathTex(r"r = a + b\theta").scale(1.2)
        formula.next_to(polar_curve, DOWN, buff=0.5)

        self.play(Write(title), Write(polar_curve))
        self.play(Write(formula))

        plane = PolarPlane(
            azimuth_units="PI radians",
            size=30,
            radius_step=2,
            azimuth_label_font_size=210,
            azimuth_step=12,
            radius_max=20,
        )
        plane.add_coordinates()
        plane.scale(1.8)

        self.play(Create(plane), run_time=2)
        angle = ValueTracker(0.01)

        Sprial = always_redraw(lambda: plane.plot_polar_graph(lambda theta:1+theta,theta_range=[0,angle.get_value()],color=ORANGE))
        label1 = MathTex(r"\theta=")
        number1 = DecimalNumber(
            angle.get_value(),
            num_decimal_places=2,
            color=ORANGE
        )
        number1.add_updater(lambda d: d.set_value(angle.get_value()))
        value_group1 = VGroup(label1, number1).arrange(RIGHT, buff=0.15)
        value_group1.to_edge(DOWN)
        value_group1.shift(UP * 2 )
        self.add(Sprial)
        self.play(FadeIn(value_group1))

        self.play(AnimationGroup(plane.animate.scale(0.12).move_to([0,0,0]),angle.animate.set_value(6 * PI),lag_ratio=0.1),run_time=4,rate_func=linear)
        self.wait(2)
        self.play(FadeOut(*self.mobjects))