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
        self.x_axis_label = ''
        self.y_axis_label = ''
        self.x_axis_config = {"include_ticks": False}
        self.y_axis_config = {"include_ticks": False}
        self.axes_color = '#000000'
        self.setup_axes(animate = True)

        def expoFunc(t,expo1,expo2,expo3,coeff1,coeff2,coeff3):
            return coeff1 * cmath.exp(1j*t*expo1) + coeff2 * cmath.exp(1j*t*expo2) + coeff3 * cmath.exp(1j*t*expo3)

        #for random value of exponents and coefficients for general exponential sums
        #repeat the whole process any number of times to generate that many random 
        for j in range(200):
            random.seed()
            expo1 = random.randrange(-30.0,30.0, 1)
            expo2 = random.randrange(-30.0,30.0, 1)
            expo3 = random.randrange(-30.0, 30.0, 1)
        #
            coeff1 = (random.randrange(-100.0,100.0,1) + random.randrange(-100.0,100.0,1)*1j)/100
            coeff2 = (random.randrange(-100.0,100.0,1) + random.randrange(-100.0,100.0,1)*1j)/100
            coeff3 = (random.randrange(-100.0,100.0,1) + random.randrange(-100.0,100.0,1)*1j)/100

            print(expo1,expo2,expo3)
            print(coeff1,coeff2,coeff3)

            path = VMobject()
            path.set_color_by_gradient(RED)
            points = []
            t=0
            for i in range(1000):
                temp = expoFunc(t,expo1,expo2,expo3,coeff1,coeff2,coeff3)
                x = temp.real
                y = temp.imag
                t += 0.01
                points.append([x,y])
            #print(points)

            path.set_points_smoothly([*[self.coords_to_point(i[0],i[1]) for i in points]])
            self.add(path)
            self.wait(0.5)
            self.remove(path)



