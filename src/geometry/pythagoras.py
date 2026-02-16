from manim import * 

# import sys
# from pathlib import Path

# # This finds the 'src' directory relative to this file
# src_path = Path(__file__).resolve().parent.parent
# sys.path.append(str(src_path))

from common.common import layout

class PythagorasScene(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)
        
        self.wait()        
        # Title
        title = Text("መርትዖ ናይ ፓይታጎረስ ቲአረም", font_size=30, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)
        self.play(Write(title), run_time=1)
        self.play(Create(underline), run_time=1)           # "In this lesson, we’re going to explore..."
        self.wait(10)
      
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
        vequation_one = VGroup(eq_square_a, eq_plus,eq_square_b,eq_equal, eq_square_c ).scale(.5)
        vequation_one.arrange(RIGHT, buff=0.1)
        vgtriangle = VGroup(triangle, square_a, square_b, square_c, right_angle, label_90, label_a, label_b, label_c, filled_triangle, filled_square_a, filled_square_b, filled_square_c,).scale(.35)
        
        vgtriangle.move_to(ORIGIN).shift(LEFT*5).shift(UP*1.5)
        vequation_one.move_to(vgtriangle).shift(RIGHT*4).shift(UP*1)

        eq_big_square = MarkupText(
            "(ሀ + ለ)²",
            font_size=30, font="Nyala"
        )
        eq_equal_two = MarkupText(
            "=",
            font_size=30, font="Nyala"
        )
        
        eq_small_square = MarkupText(
            "ሐ²",
            font_size=30, font="Nyala"
        )
        eq_plus_two = MarkupText(
            "+",
            font_size=30, font="Nyala"
        )
        eq_four_triangles = MarkupText(
            "4(ሀለ/2)",
            font_size=30, font="Nyala"
        )
        vequation_two = VGroup(eq_big_square, eq_equal_two,eq_small_square,eq_plus_two, eq_four_triangles ).scale(.5)
        vequation_two.arrange(RIGHT, buff=0.1)
        vequation_two.move_to(vequation_one).shift(DOWN)
        self.play(Create(triangle), run_time=1)
        self.wait(1)
        self.play(Write(label_a), Write(label_b), Write(label_c), run_time=1)
        self.wait(1)
        self.play(Create(right_angle), run_time=1)
        self.wait(1)
        self.play(Write(label_90), run_time=1)
        self.wait(5)
        self.play(Create(square_c), run_time=1)
        self.wait(3)
        self.play(Create(square_a))
        self.wait()
        self.play(Create(square_b))
        self.wait(2)
        
        square_a.set_fill(RED, opacity=0.1)
        square_b.set_fill(YELLOW, opacity=0.1)
        square_c.set_fill(GREEN, opacity=0.1)
        self.play(Create(eq_plus), Create(eq_equal),  FadeTransform(filled_square_a, eq_square_a, stretch=True)
                  ,FadeTransform(filled_square_b, eq_square_b, stretch=True)
                  ,FadeTransform(filled_square_c, eq_square_c, stretch=True))
        self.wait(8)
        self.play(Create(filled_triangle), run_time=1)
        triangle.set_fill(BLUE, opacity=0.5)

        
        # Triangles
        tri_blue = Polygon(
            [0, 0, 0], [b, 0, 0], [0, a, 0],
            stroke_width=1, color=WHITE
        ).set_fill(BLUE, opacity=0.5)

       
        tri_yellow = Polygon(
            [b+a, 0, 0], [b, 0, 0], [b+a, b, 0],
            stroke_width=1, color=WHITE
        ).set_fill(BLUE, opacity=0.5)

        tri_green = Polygon(
            [0, a, 0], [a, b+a, 0], [0, b+a, 0],
            stroke_width=1, color=WHITE
        ).set_fill(BLUE, opacity=0.5)

        tri_red = Polygon(
            [b+a, b+a, 0], [a+b, b, 0], [a, a+b, 0],
            
            stroke_width=1, color=WHITE
        ).set_fill(BLUE, opacity=0.5)

        tri_blue_shade = Polygon(
            [0, 0, 0], [b, 0, 0], [0, a, 0],
            stroke_width=1, color=WHITE
        ).set_fill(RED, opacity=0.5)
      
        tri_yellow_shade = Polygon(
            [b+a, 0, 0], [b, 0, 0], [b+a, b, 0],
            stroke_width=1, color=WHITE
        ).set_fill(RED, opacity=0.5)

        tri_green_shade = Polygon(
            [0, a, 0], [a, b+a, 0], [0, b+a, 0],
            stroke_width=1, color=WHITE
        ).set_fill(RED, opacity=0.5)

        tri_red_shade = Polygon(
            [b+a, b+a, 0], [a+b, b, 0], [a, a+b, 0],            
            stroke_width=1, color=WHITE
        ).set_fill(RED, opacity=0.5)

        # FIXED: Proper side midpoints + direction + buff
        label_blue_a = MarkupText("ሀ", font_size=30, font="Nyala").next_to(
            Line(tri_blue.points[0], tri_blue.points[2]).get_center(),  # side a (vertical)
            LEFT * 7.5, buff=0.15
        ).shift(UP)

        label_blue_b = MarkupText("ለ", font_size=30, font="Nyala").next_to(
            Line(tri_blue.points[0], tri_blue.points[1]).get_center(),  # side b (horizontal)  
            DOWN *.3, buff=0.5
        ).shift(RIGHT * .5)
        label_blue_c = MarkupText("ሐ", font_size=30, font="Nyala").next_to(
            Line(tri_blue.points[1], tri_blue.points[2]).get_center(),  # hypotenuse
            UR*2, buff=0.6
        ).shift(LEFT*1.2)

        label_yellow_a = MarkupText("ሀ", font_size=30, font="Nyala").next_to(
            Line(tri_yellow.points[0], tri_yellow.points[2]).get_center(),  # side a (vertical)
            LEFT *3, buff=0.15
        ).shift(DOWN *.2)

        label_yellow_b = MarkupText("ለ", font_size=30, font="Nyala").next_to(
            Line(tri_yellow.points[0], tri_yellow.points[1]).get_center(),  # side b (horizontal)  
            UP*2, buff=0.5
        ).shift(RIGHT * .5)
        label_yellow_c = MarkupText("ሐ", font_size=30, font="Nyala").next_to(
            Line(tri_yellow.points[1], tri_yellow.points[2]).get_center(),  # hypotenuse
            UR*2.5, buff=0.6
        ).shift(LEFT*1.8)

        label_green_a = MarkupText("ሀ", font_size=30, font="Nyala").next_to(
            Line(tri_green.points[0], tri_green.points[2]).get_center(),  # side a (vertical)
             buff=0.15
        ).shift(UP*2.2)

        label_green_b = MarkupText("ለ", font_size=30, font="Nyala").next_to(
            Line(tri_green.points[0], tri_green.points[1]).get_center(),  # side b (horizontal)  
            UP*2, buff=0.5
        ).shift(LEFT *.5)
        label_green_c = MarkupText("ሐ", font_size=30, font="Nyala").next_to(
            Line(tri_green.points[1], tri_green.points[2]).get_center(),  # hypotenuse
            buff=0.6
        ).shift(LEFT*.5)

        label_red_a = MarkupText("ሀ", font_size=30, font="Nyala").next_to(
            Line(tri_red.points[0], tri_red.points[2]).get_center(),  # side a (vertical)
             buff=0.15
        )

        label_red_b = MarkupText("ለ", font_size=30, font="Nyala").next_to(
            Line(tri_red.points[0], tri_red.points[1]).get_center(),  # side b (horizontal)  
            UP, buff=0.5
        ).shift(LEFT*1.2)
        label_red_c = MarkupText("ሐ", font_size=30, font="Nyala").next_to(
            Line(tri_red.points[1], tri_red.points[2]).get_center(),  # hypotenuse
           DOWN*.4, buff=0.6
        ).shift(LEFT*1.7)

        p1 = [0,0,0]
        p2 = [a+b,0,0]
        p3 = [a+b,a+b,0]
        brace1 = BraceBetweenPoints(p1, p2, stroke_width=.5).set_color(YELLOW).shift(0.2 * DOWN)
        brace2 = BraceBetweenPoints(p2, p3, stroke_width=.5).set_color(YELLOW).shift(0.2 * RIGHT)

        inner_square = Polygon(
        [b, 0, 0],           # Bottom-right of tri_blue  
        [b+a, b, 0],         # Top-left of tri_yellow
        [a, b+a, 0],         # Top-right of tri_green
        [0, a, 0],           # Bottom-left of tri_red
        stroke_width=1, 
        color=WHITE
    ).set_fill(GREEN, opacity=0.1)

        # 1. Group the triangles together
        all_triangles = VGroup(tri_blue, tri_yellow, tri_green, tri_red, tri_blue_shade, tri_yellow_shade, tri_green_shade, tri_red_shade, 
                               label_blue_a, label_blue_b, label_blue_c, label_yellow_a, label_yellow_b, label_yellow_c,
                               label_green_a, label_green_b, label_green_c, label_red_a, label_red_b, label_red_c, brace1, brace2, inner_square ).scale(.35)
        
       
        all_triangles.next_to(vgtriangle, DOWN, buff=0.4).shift(RIGHT*.4)
        
        self.wait(2) 
        self.play(
            FadeTransform(filled_triangle, tri_blue, stretch=True),
            Write(label_blue_a), Write(label_blue_b), Write(label_blue_c),
            run_time=1
        )
        
        self.wait(1)
                            # time to explain a,b,c, hypotenuse
        self.play(Create(tri_yellow), run_time=3)
        self.play(Write(label_yellow_a), Write(label_yellow_b), Write(label_yellow_c), run_time=1)
        self.play(Create(tri_green), run_time=3)
        self.play(Write(label_green_a), Write(label_green_b), Write(label_green_c), run_time=1)
        self.play(Create(tri_red), run_time=3)
        self.play(Write(label_red_a), Write(label_red_b), Write(label_red_c), run_time=1)
        self.wait(12)

        self.play(Create(brace1), run_time=1)
        self.play(Create(brace2), run_time=1)
        self.wait(7)
        self.play(FadeTransform(brace1, eq_big_square, stretch=True),FadeTransform(brace2, eq_big_square, stretch=True), run_time=1 ) 
        self.wait(1)       
        self.play(Create(eq_equal_two) , run_time=1 ) 
        self.wait()
        self.play(FadeIn(inner_square))
        self.wait(1)
        self.play(FadeTransform(inner_square, eq_small_square, stretch=True), run_time=1) 
        self.wait(1)
        self.play(FadeIn(tri_blue_shade),FadeIn(tri_yellow_shade),FadeIn(tri_green_shade),FadeIn(tri_red_shade), run_time=1)
        self.wait(1)
        self.play(Create(eq_plus_two), FadeTransform(tri_blue_shade, eq_four_triangles, stretch=True), FadeTransform(tri_yellow_shade, eq_four_triangles, stretch=True), 
                  FadeTransform(tri_green_shade, eq_four_triangles, stretch=True), FadeTransform(tri_red_shade, eq_four_triangles, stretch=True) , run_time=1 )
        
        self.wait(10)

        eq_step_three = MarkupText(
            "(ሀ + ለ)(ሀ + ለ) = ሐ² + (2)(2)(ሀለ)/(2)",
            font_size=30, font="Nyala"
        ).scale(.5)

        eq_step_four = MarkupText(
            "ሀ² + 2ለሀ + ለ² = ሐ² + 2ሀለ",
            font_size=30, font="Nyala"
        ).scale(.5)
        
        eq_step_five = MarkupText(
            "ሀ² + 2ለሀ -2ለሀ + ለ² = ሐ² + 2ሀለ - 2ለሀ",
            font_size=30, font="Nyala" 
        ).scale(.5)
        eq_step_six = MarkupText(
            "ሀ² + ለ² = ሐ²",
            font_size=30, font="Nyala" 
        ).scale(.5)
                
        eq_step_three.move_to(vequation_two).shift(DOWN*.5)
        
        eq_step_four.move_to(eq_step_three).shift(DOWN*.5)
        
        eq_step_five.move_to(eq_step_four).shift(DOWN*.5)
        
        eq_step_six.move_to(eq_step_five).shift(DOWN*.5)
        self.play(Create(eq_step_three), run_time=1)
        self.wait(3)
        self.play(Create(eq_step_four), run_time=1)
        self.wait(3)
        self.play(Create(eq_step_five), run_time=1)
        self.wait(4)
        self.play(Create(eq_step_six), run_time=1)
        self.wait(1)
        box_one = SurroundingRectangle(vequation_one, color=YELLOW, buff=.1)
        box_two = SurroundingRectangle(eq_step_six, color=YELLOW, buff=.1)
        self.add(box_one, box_two)
        self.wait(5)
    
       

# manim -ql -p -o pythagoras_video.mp4 .\pythagoras.py PythagorasScene