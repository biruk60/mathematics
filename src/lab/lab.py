from manim import * 

from common.common import layout

class MovingFrameBox(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text) 
        
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(
            Create(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()

class TriangleScene(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)        
               
        # Title
        title = Text("መርትዖ ናይ ፓይታጎረስ ቲአረም", font_size=30, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        # Side values
        a, b = 2, 3
        c = (a**2 + b**2) ** 0.5
        side = a + b
       
         # Create triangle
        triangle = Polygon(
            [0, 0, 0], [b, 0, 0], [0, a, 0],
            stroke_width=1, color=WHITE
        )
       
        filled_triangle = Polygon(
            [0, 0, 0], [b, 0, 0], [0, a, 0],
            stroke_width=1, color=WHITE
        ).set_fill(BLUE, opacity=0.3)
        # Create squares on each side
        square_a = Square(side_length=a, color=RED, stroke_width=1).next_to(Line(triangle.points[0], triangle.points[2]).get_center(), UP*2, buff=0).shift(LEFT*2)
        filled_square_a = Square(side_length=a, color=RED, stroke_width=1).set_fill(RED, opacity=0.1).next_to(Line(triangle.points[0], triangle.points[2]).get_center(), UP*2, buff=0).shift(LEFT*2)
        square_b = Square(side_length=b, color=YELLOW, stroke_width=1).next_to( Line(triangle.points[0], triangle.points[1]).get_center(), DOWN *1.5, buff=0).shift(RIGHT)
        filled_square_b = Square(side_length=b, color=YELLOW, stroke_width=1).set_fill(YELLOW, opacity=0.1).next_to( Line(triangle.points[0], triangle.points[1]).get_center(), DOWN *1.5, buff=0).shift(RIGHT)
        
        # Square on hypotenuse is rotated
        angle = np.arctan(a / b)
        square_c = Square(side_length=c, color=GREEN, stroke_width=1).rotate(-angle).next_to(Line(triangle.points[1], triangle.points[2]).get_center(),UR).shift(LEFT*1.77).shift(DOWN*.27)
        filled_square_c = Square(side_length=c, color=GREEN, stroke_width=1).set_fill(GREEN, opacity=0.1).rotate(-angle).next_to(Line(triangle.points[1], triangle.points[2]).get_center(),UR).shift(LEFT*1.77).shift(DOWN*.27)
        # Labels
        label_a = MarkupText("ሀ", font_size=30, font="Nyala").next_to(
            Line(triangle.points[0], triangle.points[2]).get_center(),  # side a (vertical)
            LEFT * 7.5, buff=0.15
        ).shift(UP)

        label_b = MarkupText("ለ", font_size=30, font="Nyala").next_to(
            Line(triangle.points[0], triangle.points[1]).get_center(),  # side b (horizontal)  
            DOWN *.3, buff=0.5
        ).shift(RIGHT * .5)
        label_c = MarkupText("ሐ", font_size=30, font="Nyala").next_to(
            Line(triangle.points[1], triangle.points[2]).get_center(),  # hypotenuse
            UR*2, buff=0.6
        ).shift(LEFT*1.2)

       
        right_angle = RightAngle(Line([0, 0, 0],[0, a, 0]), Line([0, 0, 0], [b, 0, 0]), length=0.5, quadrant=(1,1), stroke_width=1)        
        label_90 = MarkupText("90°",font_size=30, font="Nyala").next_to(right_angle, UR, buff=0.1)

        eq_square_a = MarkupText(
            "ሀ²",
            font_size=30, font="Nyala"
        )
        eq_plus = MarkupText(
            "+",
            font_size=30, font="Nyala"
        )
        eq_square_b = MarkupText(
            "ለ²",
            font_size=30, font="Nyala"
        )
        eq_equal = MarkupText(
            "=",
            font_size=30, font="Nyala"
        )
        eq_square_c = MarkupText(
            "ሐ²",
            font_size=30, font="Nyala"
        )
        vequation_one = VGroup(eq_square_a, eq_plus,eq_square_b,eq_equal, eq_square_c).scale(.6)
        vequation_one.arrange(RIGHT, buff=0.1)
        vgtriangle = VGroup(triangle, filled_triangle, square_a, square_b, square_c, right_angle, label_90, label_a, label_b, label_c).scale(.60)
        
        vgtriangle.move_to(ORIGIN)
        vequation_one.move_to(vgtriangle).shift(DOWN*3)
        self.add(triangle, filled_triangle)
        
        self.add(label_a, label_b, label_c)
        
        self.add(right_angle)
        
        self.add(label_90)
        
        self.add(square_c)
        
        self.add(square_a)
        
        self.add(square_b)
        
        self.add(vequation_one)
        