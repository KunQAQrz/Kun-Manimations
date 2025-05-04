from manim import *


class LinkedListNode(VGroup):
    """链表节点可视化组件"""

    def __init__(
        self,
        data: str,
        node_size: float = 0.8,
        node_color: ParsableManimColor = BLUE,
        arrow_color: ParsableManimColor = WHITE,
        **kwargs,
    ):
        super().__init__(**kwargs)
        # 节点主体（矩形框 + 数据）
        self.box = Rectangle(
            height=node_size, width=node_size, color=node_color, fill_opacity=0.5
        )
        self.data_text = Text(data).scale(0.6).move_to(self.box)

        # 指向自身的指针
        self.arrow = Arrow(
            start=self.box.get_left() + LEFT * 0.38,
            end=self.box.get_left(),
            color=arrow_color,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=3,
        )

        self.add(self.box, self.data_text, self.arrow)


class LinkedList(VGroup):
    """单链表可视化组件"""

    arrow_length = 0.38  # 根据实际箭头长度调整

    def __init__(self, max_node=None, **kwargs):
        super().__init__(**kwargs)

        if max_node == None:
            self.node_size = None
        else:
            max_total_width = config.frame_width * 0.9
            # 每个节点的有效宽度 = 节点宽度 + 箭头长度
            self.node_size = (
                max_total_width - self.arrow_length * (max_node - 1)
            ) / max_node
            self.node_size = min(self.node_size, 1.5)  # 最大宽度限制

        self.nodes = VGroup()

        self.add(self.nodes)
        self.center()

    def animate_append(self, data: str, **anim_args) -> list[Animation]:
        """动态追加节点的动画"""
        new_node = LinkedListNode(data, self.node_size)

        if self.nodes:
            new_node.next_to(self.nodes[-1], RIGHT, buff=0)
        else:
            new_node.arrow.set_opacity(0)
            new_node.to_edge(LEFT)

        self.nodes.add(new_node)
        return [FadeIn(new_node, **anim_args, shift=LEFT * 0.1)]
