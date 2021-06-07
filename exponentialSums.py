from manim import *
import cmath
import random

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

        def expoFunc(t,expo1,expo2,expo3,coeff1,coeff2,coeff3):
            return coeff1 * cmath.exp(1j*t*expo1) + coeff2 * cmath.exp(1j*t*expo2) + coeff3 * cmath.exp(1j*t*expo3)

        t=0
        #for random value of exponents and coefficients for general exponential sums
        random.seed()
        expo1 = random.randrange(-30.0,30.0, 1)
        expo2 = random.randrange(-30.0,30.0, 1)
        expo3 = random.randrange(-30.0, 30.0, 1)
        #
        coeff1 = (random.randrange(-100.0,100.0,1) + random.randrange(-100.0,100.0,1)*1j)/100
        coeff2 = (random.randrange(-100.0,100.0,1) + random.randrange(-100.0,100.0,1)*1j)/100
        coeff3 = (random.randrange(-100.0,100.0,1) + random.randrange(-100.0,100.0,1)*1j)/100
        temp = expoFunc(t,expo1,expo2,expo3,coeff1,coeff2,coeff3)
        x = temp.real
        y = temp.imag
        t+=0.01
        #print(x,y)
        print(expo1,expo2,expo3)
        print(coeff1,coeff2,coeff3)

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

        for i in range(300):
            temp = expoFunc(t,expo1,expo2,expo3,coeff1,coeff2,coeff3)
            x = temp.real
            y = temp.imag
            t += 0.01
            self.play(dot.animate.move_to(self.coords_to_point(x,y)), run_time = 0.01, rate_function = linear)



