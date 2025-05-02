from manim import *

class MyCircle(Circle):
    def __init__(self, color: ParsableManimColor = PINK, opacity: float = 0.5, **kwargs):
        super().__init__(**kwargs)
        self.set_fill(color, opacity) # set the color and transparency
