from manim import *
import numpy as np 

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920

class LogarathmicSpiral(Scene):
    def construct(self):
        title = Tex(r"Polar Sketch of")
        title.to_edge(UP)
        polar_curve=Tex(r"Logarathmic Spiral")
        polar_curve.next_to(title,DOWN,buff = 0.3)
        formula = MathTex(r"r=ae^{k\theta}")
        formula.next_to(polar_curve,DOWN,buff=0.5).scale(1.2)
        self.play(Write(title),Write(polar_curve))
        self.play(Write(formula))
        plane = PolarPlane(
            azimuth_units="PI radians",
            size=120,
            radius_max=40,
            radius_step=4,
            azimuth_step=16,
            azimuth_label_font_size=560
        )
        plane.add_coordinates()
        plane.scale(1.8)

        self.play(Create(plane), run_time=2)
        a = ValueTracker(1)
        k = ValueTracker(0.3)
        angle = ValueTracker(0.01)
        Spiral = always_redraw(lambda: plane.plot_polar_graph(lambda theta: a.get_value()*np.exp(k.get_value()*theta),theta_range=[0,angle.get_value()],color=ORANGE))

        Thetavalues = MathTex(r"\theta=")
        Avalues = MathTex(r"a = ")
        Kvalues = MathTex(r"k=")
        value1=DecimalNumber(angle.get_value(),num_decimal_places=2,color=ORANGE)
        value2=DecimalNumber(a.get_value(),num_decimal_places=2,color=RED)
        value3=DecimalNumber(k.get_value(),num_decimal_places=2,color=GREEN)
        value1.add_updater(lambda d: d.set_value(angle.get_value()))
        value2.add_updater(lambda d:d.set_value(a.get_value()))
        value3.add_updater(lambda d: d.set_value(k.get_value()))
        value_group_1 = VGroup(Thetavalues,value1).arrange(RIGHT,buff = 0.15)
        value_group_1.to_edge(DOWN)
        value_group_1.shift(UP*2+LEFT*2)
        value_group_2=VGroup(Avalues,value2).arrange(RIGHT,buff=0.15)
        value_group_2.next_to(value_group_1,RIGHT*2)
        value_group_3 = VGroup(Kvalues,value3).arrange(RIGHT,buff = 0.15)
        value_group_3.next_to(value_group_2,RIGHT*2)
        self.play(AnimationGroup(FadeIn(value_group_1),FadeIn(value_group_2),FadeIn(value_group_3),lag_ratio=0),run_time=0.3,rate_func=linear)
        self.add(Spiral)
        self.play(AnimationGroup(plane.animate.scale(0.03).move_to([0,0,0]),angle.animate.set_value(3.955 * PI),lag_ratio=0.1),run_time=8,rate_func=linear)
        self.wait(2)
        self.play(AnimationGroup(a.animate.set_value(15),lag_ratio=0.1),run_time=5,rate_func=linear)
        self.wait()
        self.play(AnimationGroup(a.animate.set_value(1),lag_ratio=0.1),run_time=5,rate_func=linear)
        self.wait()
        self.play(AnimationGroup(k.animate.set_value(1.1),lag_ratio=0.1),run_time=5,rate_func=linear)
        self.wait()
        self.play(AnimationGroup(k.animate.set_value(0.3),lag_ratio=0.1),run_time=5,rate_func=linear)
        self.wait()
        self.play(FadeOut(*self.mobjects))