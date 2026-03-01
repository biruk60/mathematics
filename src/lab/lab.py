from manim import * 
import manimpango

from common.common import layout, add_shadow

# manim -ql -p -o lab_video.mp4 .\lab.py SpinningTriangle
  
    

class SpinningTriangle(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text) 
        # background = ImageMobject("../assets/images/blackboard.png").set_opacity(.8)
        cog = SVGMobject("../assets/svgs/thinking.svg")
        self.play(            
            Rotate(cog, angle=2*PI, rate_func=linear , run_time=10),
            )

class RotateGear(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text) 
        # 1. Load the SVG
        # Replace 'head_gear.svg' with your file path
        # Use config to color, or let it use SVG colors
        thinking_head = SVGMobject("../assets/svgs/brain.svg")
        
        gear1 = thinking_head[0] # Your specific gear object
        gear2 = thinking_head[1]
        
        self.add(thinking_head)
        
        # This rotates the gear around its OWN center
        # self.play(
        #     Rotate(
        #         gear,
        #         angle=2*PI,
        #         about_point=gear.get_center(), # CRITICAL: Keeps it from moving
        #         rate_func=linear,
        #         run_time=5
        #     )
        # )
        self.play( Succession(
        *[
            AnimationGroup(
                Indicate(gear1, color=RED, scale_factor=1.1),
                Indicate(gear2, color=RED, scale_factor=1.1),
                run_time=1
            ) 
            for _ in range(6)
        ]
    )  )

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
        
class EquivalenceScene(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)
        title = Text("Logical Equivalence", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        self.wait(1)
        font_size =20

       
        # Negation of t and c:  ¬t ≡ c
        tandc_title = Text("Negation of t and c: ¬t ≡ c", font_size=font_size + 8)
        tandc_underline = Line(LEFT*tandc_title.width/2, RIGHT*tandc_title.width/2, stroke_width=1, color=WHITE)
        tandc_underline.next_to(tandc_title, DOWN, buff=0.2)        	

        # tandc_bullet_underline = Line(LEFT*tandc.width/2, RIGHT*tandc.width/2, stroke_width=1, color=YELLOW)
        # tandc_bullet_underline.next_to(tandc, DOWN, buff=0.1)
        tandc_table = Table(
            [["T", "F", "F"]           ],           
            col_labels=[Text("t"), Text("c"), Text("¬t")],
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        ).scale(0.7).next_to(tandc_underline, DOWN*2, buff=0.5)

        tandc_group = VGroup(tandc_title, tandc_underline, tandc_table)
        tandc_group.arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(underline, DOWN, buff=0.25).scale(0.6).shift(2*RIGHT)
       
        # self.add(tandc_title, tandc_underline, tandc_bullet_underline)
        self.add(tandc_title, tandc_underline)
       
        self.wait(.5)
        self.play(FadeIn(tandc_table), run_time=.5)
        self.wait(.5)
		
        # "p ∨ q
        tandc_row1_col0_content = SurroundingRectangle(tandc_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        tandc_row1_col1_content = SurroundingRectangle(tandc_table.get_entries((2, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(tandc_row1_col0_content), run_time=.5)
        self.play(Create(tandc_row1_col1_content),run_time=.5)
        
        self.wait(.5)
        self.play(FadeOut(tandc_row1_col0_content), FadeOut(tandc_row1_col1_content), run_time=.5)
        self.wait(.5)
		
        
		
        tandc_col0 = SurroundingRectangle(tandc_table.get_columns()[1][1:], color=RED, buff=0.05, fill_color=ORANGE, fill_opacity=0.075, stroke_width= 1)
        tandc_col2 = SurroundingRectangle(tandc_table.get_columns()[2][1:], color=RED, buff=0.05, fill_color=ORANGE, fill_opacity=0.075,  stroke_width= 1)
        self.add(tandc_col0, tandc_col2)
        self.wait(.5)
        # self.play(FadeOut(tandc_group), FadeOut(tandc_col3), FadeOut(tandc_col4),  FadeOut(tandc_bullet_underline), run_time=.5)
        self.play(FadeOut(tandc_group), FadeOut(tandc_col0), FadeOut(tandc_col2), run_time=.5)
        self.wait(1)


        # manim -ql -p  .\lab.py EquivalenceScene
