from manim import *

from helper import *

from patterns.array import Array


class ArrayAndLinkedList(SubScene):
    def __array_push_element(self, arr: Array, size: int = None):
        if size is None:
            size = arr.capacity
        for i in range(arr.size + 1, size + 1):
            self.play(*arr.animate_set_size(i, run_time=0.1))

    def __array(self):

        # 生成数组
        arr = Array(size=0, capacity=10)
        self.play(FadeIn(arr))

        # 填满数组
        self.__array_push_element(arr)

        new_arr = Array(size=arr.capacity, capacity=16)

        # 扩容数组
        self.play(AnimationGroup(FadeOut(arr, run_time=0.5), FadeIn(new_arr)))

        # 数组添加元素
        self.__array_push_element(new_arr, size=15)

    def construct(self):
        self.__array()

        self.wait()


class Main(Scene):
    def construct(self):
        # todo: 这里可以添加多个子场景
        ArrayAndLinkedList.construct_for_other(self)
        self.clear()
        self.wait()
