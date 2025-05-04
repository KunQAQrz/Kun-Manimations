from manim import *

from helper import *

from patterns.array import Array


class ArrayAndLinkedList(SubScene):
    def construct(self):
        arr = Array(size=0, capacity=10)
        self.play(FadeIn(arr))
        self.wait()

        for i in range(1, arr.capacity + 1):
            self.play(*arr.animate_set_size(i), run_time=0.1)
            self.wait(0.1)

        new_arr = Array(size=arr.capacity, capacity=16)

        self.play(AnimationGroup(FadeOut(arr, run_time=0.5), FadeIn(new_arr)))
        self.wait()

        self.play(*new_arr.animate_set_size(new_arr.size + 1), run_time=0.1)
        self.wait(0.1)


class Main(Scene):
    def construct(self):
        # todo: 这里可以添加多个子场景
        self.clear()
        self.wait(1)
