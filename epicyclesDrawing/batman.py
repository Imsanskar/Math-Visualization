from manim import *
import cmath
import random
from utility import *

class expo(GraphScene):

   def construct(self):
        self.graph_origin = ORIGIN
        self.x_max = 3
        self.x_min = -3
        self.y_max = 3
        self.y_min = -3
        self.x_axis_config = {"include_ticks": False}
        self.y_axis_config = {"include_ticks": False}
        self.axes_color = "#000000"
        self.x_axis_label = ''
        self.y_axis_label = ''
        self.setup_axes(animate = True)
        points = functionPoints('chels.txt')
        #print(points)

        coefficients = dft(points)

        def fValues(t,coeffs):
            onep = 0
            for n in range(len(coeffs)):
                #onep += (coeffs[n][0] + coeffs[n][1]*1j) * cmath.exp(1j*(n-len(coeffs)/2)*t)
                #onep += (coeffs[n][0] + coeffs[n][1]) *
                singleCircle = 0
                singleCircle = (coefficients[n]) * cmath.exp(1j*(n)*t)
                onep += singleCircle


            return onep
        t=0
        dt = (cmath.pi * 2)/len(coefficients)
        temp = fValues(t,coefficients)
        x = temp.real
        y = temp.imag
        t+=dt
       # #print(x,y)
       # print(expo1,expo2,expo3)
       # print(coeff1,coeff2,coeff3)

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

        for i in range(len(coefficients)):
            #temp = expoFunc(t,expo1,expo2,expo3,coeff1,coeff2,coeff3)
            temp = fValues(t,coefficients)
            x = temp.real
            y = temp.imag
            print(x,y)
            t +=dt 
            self.play(dot.animate.move_to(self.coords_to_point(x,y)), run_time = 0.01, rate_function = linear)
