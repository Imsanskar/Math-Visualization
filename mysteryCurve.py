from manim import *
import cmath

class expo(GraphScene):

   def construct(self):
        self.graph_origin = ORIGIN
        self.x_max = 3
        self.x_min = -3
        self.y_max = 3
        self.y_min = -3
        self.x_axis_config = {"include_ticks": False}
        self.y_axis_config = {"include_ticks": False}
        self.setup_axes(animate = True)

        def mysteryFunc(t):
            return cmath.exp(1j*t) + 1/2* cmath.exp(6*1j*t) + 1j/3 * cmath.exp((-14*1j*t))

        t=0
        temp = mysteryFunc(t)
        x = temp.real
        y = temp.imag
        t+=0.01
        #print(x,y)
        dot = Dot([x,y,0])
        dot.move_to(self.coords_to_point(x,y))
        path = VMobject(color= BLUE)
        path.set_points_as_corners([dot.get_center(),dot.get_center()])
        path.set_color_by_gradient(RED)
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path,dot)

        for i in range(1000):
            x = mysteryFunc(t).real
            y = mysteryFunc(t).imag
            t += 0.01
            self.play(dot.animate.move_to(self.coords_to_point(x,y)), run_time = 0.01, rate_function = linear)



