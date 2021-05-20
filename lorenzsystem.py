from manim import *
class strange2(GraphScene):
    def construct(self):
        self.graph_origin = ORIGIN
        self.x_max = 50
        self.x_min = -50
        self.y_max = 50
        self.y_min = -50
        self.x_axis_config = {"include_ticks": False}
        self.y_axis_config = {"include_ticks": False}
        self.setup_axis(animate = True)

        #system variables
        ro = 28
        sigma = 10
        beta  = 8/3
        x =1
        y =1 
        z =1
        dt = 0.01
        path = VMobjec(stroke_width = 2)
        dot = Dot([x,y,0])
        dot.move_to(self.coords_to_point(x,y))
        path.set_points_as_corners([dot.get_center(),dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.set_points_as_corners([dot.get_center(), dot.get_center()])

        path.add_updater(previous_path)
        self.add(path,dot)
        path.set_color_by_gradient(RED,BLUE,GREEN)

        for i in range(1500):
            dx = sigma * (y-x) * dt
            dy = (x*(ro-z) -y)*dt
            dz =(x*y - beta * z) * dt
            x = x +dx
            y = y +dy
            z = z +dz
            self.play(dot.animate.move_to(self.coords_to_point(x,y)), run_time = 0.001, rate_function = linear)

        self.wait(3)

