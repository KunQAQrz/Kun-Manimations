from manim import *

class MySquare(Square):
    def __init__(self, color: ParsableManimColor = MAROON, opacity: float = 0.3, **kwargs):
        super().__init__(**kwargs)
        self.set_fill(color, opacity) # set the color and transparency
