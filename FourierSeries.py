from manimlib import *

def fourierSeries(x, size):
    sum = 0
    for i in range(0, size):
        if i % 2 == 1:
            sum += math.sin(i * x) / i
    return 4 / math.pi * sum

def func(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1

class FourierSeries(Scene):
    def construct(self):
        axes = Axes(
            x_range = (-math.pi, math.pi),
            y_range = (-1, 1.1),
        )
        axes.add_coordinate_labels()

        self.play(Write(axes), lag_ratio = 0.01)

        x_graph = axes.get_graph(
            lambda x: func(x),
            color = GREEN,
            discontinuity=[0],
            use_smoothing = False
        )
        x_graph.set_stroke(width = 5, color = RED)

        self.play(
            ShowCreation(x_graph),
        )

        self.wait()

        size = 25
        f = [0] * size
        for i in range(size):
            f[i] = axes.get_graph(
                lambda x: fourierSeries(x, i),
                color =  GREEN
            )

        self.play(ShowCreation(f[0]))

        for i in range(0, size - 1):
            self.play(ReplacementTransform(f[i], f[i + 1]))
