from manim import *


class Array(VGroup):
    def _create_label(self) -> Text:
        """创建容量标签"""
        return Text(
            f"{self.size}/{self.capacity}",
            font_size=24,
            color=RED if self.size == self.capacity else WHITE,
        ).next_to(self.elements, DOWN)

    def __init__(
        self,
        size: int,
        capacity: int,
        element_color: ParsableManimColor = BLUE,
        empty_color: ParsableManimColor = GREY,
        element_width: float = None,
        **kwargs,
    ):
        if size > capacity:
            raise ValueError("Size cannot exceed capacity")

        super().__init__(**kwargs)

        self.size = size
        self.capacity = capacity
        self.element_color = element_color
        self.empty_color = empty_color

        # 自动计算元素尺寸
        if element_width is None:
            max_total_width = config.frame_width * 0.9  # 最大总宽度
            element_width = max_total_width / max(capacity, 1)  # 防止除零
            element_width = min(element_width, 1.5)  # 最大宽度限制

        # 生成数组元素
        self.elements = VGroup()
        for i in range(capacity):
            rect = Rectangle(
                height=element_width,
                width=element_width,
                color=self.empty_color,
                fill_opacity=0.5,
            )

            if i < size:
                rect.set_color(self.element_color)
                rect.set_z_index(1)

            # 添加索引标签
            index_text = (
                Text(str(i), font_size=20).move_to(rect.get_center()).set_z_index(2)
            )

            """层级：索引标签 > 元素 > 空元素"""

            # 组合元素和索引
            element_group = VGroup(rect, index_text)
            self.elements.add(element_group)

        # 排列所有元素
        self.elements.arrange(RIGHT, buff=0)

        # 创建并排的容量标签
        self.label = self._create_label()

        # 组合所有组件
        self.add(self.elements, self.label)
        self.center()

    def animate_set_size(self, new_size: int, **anim_args) -> list[Animation]:
        if new_size == self.size:
            return []
        if new_size > self.capacity:
            raise ValueError(f"Size {new_size} exceeds capacity {self.capacity}")

        # 生成元素颜色变化动画
        elements_anim = []
        for i, element in enumerate(self.elements):
            rect = element[0]
            target_color = self.element_color if i < new_size else self.empty_color
            if rect.fill_color != target_color:
                elements_anim.append(
                    rect.animate().set_color(target_color).set_fill(opacity=0.5)
                )

        # 生成标签更新动画
        self.size = new_size

        new_label = self._create_label().move_to(self.label)
        label_anim = AnimationGroup(
            FadeOut(self.label, shift=UP * 0.1),
            FadeIn(new_label, shift=UP * 0.1),
        )

        self.remove(self.label)
        self.add(new_label)
        self.label = new_label

        return [AnimationGroup(*elements_anim, label_anim, **anim_args)]
