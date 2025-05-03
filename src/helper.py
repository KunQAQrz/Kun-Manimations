from manim import *


class SubScene(Scene):
    @staticmethod
    def construct_for_other(scene: Scene):
        pass

    def construct(self):
        self.construct_for_other(self)
