from manim import *

class bif(GraphScene):
    def construct(self):
       #configuring graph scene
        self.x_min = 2.4
        self.y_min = 0
        self.x_max = 4
        self.y_max = 1
        self.axes_color = BLUE
        self.setup_axes()
        #compute
        r = 2.4
        xn = 0.60
        xnext = r*xn * (1-xn);
        xn = xnext
        while(r<4):
            #first letting the result settle after 100 iterations
            for i in range(100):
                if(xnext == 0):
                    break;
                xnext = r * xn * (1-xn)
                xn = xnext
            #now the settled points are plotted
            for i in range(1000):
                dot = Dot([r,xn,0], radius= 0.008)
                dot.move_to(self.coords_to_point(r,xn))
                xnext = r * xn *(1-xn)
                xn = xnext
               # print(xn)
                self.play(ShowCreation(dot),run_time = 0.01,rate_function = linear) 
            r = r + 0.001
            #print("next")
        
        self.wait(3)
        #make larger
        #animate

