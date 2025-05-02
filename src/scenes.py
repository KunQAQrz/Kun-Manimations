from manim import *

from helper import *

from patterns.my_circle import MyCircle
from patterns.my_square import MySquare

class MyTransform(SubScene):
    def construct_for_other(scene:Scene):
        circle = MyCircle()  # create a circle
        square = MySquare()  # create a square
        scene.play(Create(square))  # animate the creation of the square
        scene.play(Transform(square, circle))  # interpolate the square into the circle
        scene.play(FadeOut(square))  # fade out animation

class MyRow(SubScene):
    def construct_for_other(scene:Scene):
        circle = MyCircle()  # create a circle
        square = MySquare(color=BLUE, opacity=0.5)  # create a square
        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        scene.play(Create(circle), Create(square))  # show the shapes on screen
        #scene.play(FadeOut(circle), FadeOut(square))  # fade out animation

class MyRotations(SubScene):
    def construct_for_other(scene:Scene):
        left_square = MySquare(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = MySquare(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        scene.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        scene.wait()
        #scene.play(FadeOut(left_square), FadeOut(right_square))  # fade out animation

class Main(Scene):
    def construct(self):
        MyTransform.construct_for_other(self)
        self.clear()
        self.wait(1)
        MyRow.construct_for_other(self)
        self.clear()
        self.wait(1)
        MyRotations.construct_for_other(self)
        self.clear()
        self.wait(1)
