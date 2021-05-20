from manimlib import *

def seriesSum(x, size):
    sum = 1
    for i in range(1, size):
        sum += math.pow(-1, i) * math.pow(x, i * 2) / math.factorial(i * 2)
    return sum

class TaylorSeries(Scene):
    def construct(self):
        axes = Axes(
            x_range = (-5 * math.pi, 5 * math.pi + 0.1), 
            y_range = (-1, 2),
        )
        #axes.add_coordinate_labels()

        self.play(Write(axes), lag_ratio = 0.01)

        cos_graph = axes.get_graph(
            lambda x: math.cos(x),
            color = GREEN,
        )
        cos_graph.set_stroke(width = 5)

        self.play(
            ShowCreation(cos_graph),
        )

        self.wait()

        size = 25
        series = [0] * size
        for i in range(size):
            series[i] = axes.get_graph(
                lambda x: seriesSum(x, i),
                color =  RED
            )

        self.play(ShowCreation(series[0]))

        for i in range(0, size - 1):
            self.play(ReplacementTransform(series[i], series[i + 1]))
