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
                # Distributive law: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)
        distributive_title = Text("Distributive laws: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r) ", font_size=font_size + 8)
        distributive_underline = Line(LEFT*distributive_title.width/2, RIGHT*distributive_title.width/2, stroke_width=1, color=WHITE)
        distributive_underline.next_to(distributive_title, DOWN, buff=0.2)        	

        # distributive_bullet_underline = Line(LEFT*distributive.width/2, RIGHT*distributive.width/2, stroke_width=1, color=YELLOW)
        # distributive_bullet_underline.next_to(distributive, DOWN, buff=0.1)
        #  distributive_headers = ["p","q","r", "p ∨ q","p ∧ q", "(p ∧ r)", "p ∧ (q ∨ r)", "(p ∧ q) ∨ (p ∧ r)"]
        distributive_table = Table(
            [["T", "T", "T", "T", "T", "T", "T", "T"],
            ["T", "T", "F", "T", "T", "F", "T", "T"],
            ["T", "F", "T", "T", "F", "T", "T", "T"],
            ["T", "F", "F", "F", "F", "F", "F", "F"],
            ["F", "T", "T", "T", "F", "F", "F", "F"],
            ["F", "T", "F", "T", "F", "F", "F", "F"],
            ["F", "F", "T", "T", "F", "F", "F", "F"],
            ["F", "F", "F", "F", "F", "F", "F", "F"]],           
            col_labels=[Text("P"), Text("q"), Text("r"),Text("p ∨ q"), Text("p ∧ q"), Text("p ∧ r"), Text("p ∧ (q ∨ r)"), Text("(p ∧ q) ∨ (p ∧ r)")],
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        ).scale(0.5).next_to(distributive_underline, DOWN, buff=0.5)

        distributive_group = VGroup(distributive_title, distributive_underline, distributive_table)
        distributive_group.arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(underline, DOWN, buff=0.25).scale(0.6).shift(2*RIGHT)
       
        # self.add(distributive_title, distributive_underline, distributive_bullet_underline)
        self.add(distributive_title, distributive_underline)
       
        self.wait(1)
        self.play(FadeIn(distributive_table), run_time=1)
        self.wait(1)

        # p ∨ q

        distributive_row1_col0_content = SurroundingRectangle(distributive_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col1_content = SurroundingRectangle(distributive_table.get_entries((2, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col3_content = SurroundingRectangle(distributive_table.get_entries((2, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row1_col0_content), run_time=1)
        self.play(Create(distributive_row1_col1_content),run_time=1)        
        self.play(Create(distributive_row1_col3_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row1_col0_content), FadeOut(distributive_row1_col1_content), FadeOut(distributive_row1_col3_content), run_time=1)
        self.wait(1)

        distributive_row2_col0_content = SurroundingRectangle(distributive_table.get_entries((3, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row2_col1_content = SurroundingRectangle(distributive_table.get_entries((3, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row2_col3_content = SurroundingRectangle(distributive_table.get_entries((3, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row2_col0_content), run_time=1)
        self.play(Create(distributive_row2_col1_content),run_time=1)        
        self.play(Create(distributive_row2_col3_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row2_col0_content), FadeOut(distributive_row2_col1_content),FadeOut(distributive_row2_col3_content), run_time=1)
        self.wait(1)

        distributive_row3_col0_content = SurroundingRectangle(distributive_table.get_entries((4, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row3_col1_content = SurroundingRectangle(distributive_table.get_entries((4, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row3_col3_content = SurroundingRectangle(distributive_table.get_entries((4, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row3_col0_content), run_time=1)
        self.play(Create(distributive_row3_col1_content),run_time=1)        
        self.play(Create(distributive_row3_col3_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row3_col0_content), FadeOut(distributive_row3_col1_content), FadeOut(distributive_row3_col3_content), run_time=1)
        self.wait(1)

        distributive_row4_col0_content = SurroundingRectangle(distributive_table.get_entries((5, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row4_col1_content = SurroundingRectangle(distributive_table.get_entries((5, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row4_col3_content = SurroundingRectangle(distributive_table.get_entries((5, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row4_col0_content), run_time=1)
        self.play(Create(distributive_row4_col1_content),run_time=1)        
        self.play(Create(distributive_row4_col3_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row4_col0_content), FadeOut(distributive_row4_col1_content), FadeOut(distributive_row4_col3_content), run_time=1)        
        self.wait(1)

        distributive_row5_col0_content = SurroundingRectangle(distributive_table.get_entries((6, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row5_col1_content = SurroundingRectangle(distributive_table.get_entries((6, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row5_col3_content = SurroundingRectangle(distributive_table.get_entries((6, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row5_col0_content), run_time=1)
        self.play(Create(distributive_row5_col1_content),run_time=1)        
        self.play(Create(distributive_row5_col3_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row5_col0_content), FadeOut(distributive_row5_col1_content), FadeOut(distributive_row5_col3_content), run_time=1)
        self.wait(1)

        distributive_row6_col0_content = SurroundingRectangle(distributive_table.get_entries((7, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row6_col1_content = SurroundingRectangle(distributive_table.get_entries((7, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row6_col3_content = SurroundingRectangle(distributive_table.get_entries((7, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row6_col0_content), run_time=1)
        self.play(Create(distributive_row6_col1_content),run_time=1)       
        self.play(Create(distributive_row6_col3_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row6_col0_content), FadeOut(distributive_row6_col1_content), FadeOut(distributive_row6_col3_content), run_time=1)
        self.wait(1)

        distributive_row7_col0_content = SurroundingRectangle(distributive_table.get_entries((8, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row7_col1_content = SurroundingRectangle(distributive_table.get_entries((8, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row7_col3_content = SurroundingRectangle(distributive_table.get_entries((8, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row7_col0_content), run_time=1)
        self.play(Create(distributive_row7_col1_content),run_time=1)       
        self.play(Create(distributive_row7_col3_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row7_col0_content), FadeOut(distributive_row7_col1_content), FadeOut(distributive_row7_col3_content), run_time=1)
        self.wait(1)

        distributive_row8_col0_content = SurroundingRectangle(distributive_table.get_entries((9, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row8_col1_content = SurroundingRectangle(distributive_table.get_entries((9, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row8_col3_content = SurroundingRectangle(distributive_table.get_entries((9, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row8_col0_content), run_time=1)
        self.play(Create(distributive_row8_col1_content),run_time=1)        
        self.play(Create(distributive_row8_col3_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row8_col0_content), FadeOut(distributive_row8_col1_content), FadeOut(distributive_row8_col3_content), run_time=1)
        self.wait(1)

        # p ∧ q
        distributive_row1_col0_content = SurroundingRectangle(distributive_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col1_content = SurroundingRectangle(distributive_table.get_entries((2, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col3_content = SurroundingRectangle(distributive_table.get_entries((2, 5)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row1_col0_content), run_time=1)
        self.play(Create(distributive_row1_col1_content),run_time=1)        
        self.play(Create(distributive_row1_col3_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row1_col0_content), FadeOut(distributive_row1_col1_content), FadeOut(distributive_row1_col3_content), run_time=1)
        self.wait(1)

        distributive_row2_col0_content = SurroundingRectangle(distributive_table.get_entries((3, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row2_col1_content = SurroundingRectangle(distributive_table.get_entries((3, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row2_col3_content = SurroundingRectangle(distributive_table.get_entries((3, 5)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row2_col0_content), run_time=1)
        self.play(Create(distributive_row2_col1_content),run_time=1)        
        self.play(Create(distributive_row2_col3_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row2_col0_content), FadeOut(distributive_row2_col1_content),FadeOut(distributive_row2_col3_content), run_time=1)
        self.wait(1)

        distributive_row3_col0_content = SurroundingRectangle(distributive_table.get_entries((4, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row3_col1_content = SurroundingRectangle(distributive_table.get_entries((4, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row3_col3_content = SurroundingRectangle(distributive_table.get_entries((4, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row3_col0_content), run_time=1)
        self.play(Create(distributive_row3_col1_content),run_time=1)        
        self.play(Create(distributive_row3_col3_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row3_col0_content), FadeOut(distributive_row3_col1_content), FadeOut(distributive_row3_col3_content), run_time=1)
        self.wait(1)

        distributive_row4_col0_content = SurroundingRectangle(distributive_table.get_entries((5, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row4_col1_content = SurroundingRectangle(distributive_table.get_entries((5, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row4_col3_content = SurroundingRectangle(distributive_table.get_entries((5, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row4_col0_content), run_time=1)
        self.play(Create(distributive_row4_col1_content),run_time=1)        
        self.play(Create(distributive_row4_col3_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row4_col0_content), FadeOut(distributive_row4_col1_content), FadeOut(distributive_row4_col3_content), run_time=1)        
        self.wait(1)

        distributive_row5_col0_content = SurroundingRectangle(distributive_table.get_entries((6, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row5_col1_content = SurroundingRectangle(distributive_table.get_entries((6, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row5_col3_content = SurroundingRectangle(distributive_table.get_entries((6, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row5_col0_content), run_time=1)
        self.play(Create(distributive_row5_col1_content),run_time=1)        
        self.play(Create(distributive_row5_col3_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row5_col0_content), FadeOut(distributive_row5_col1_content), FadeOut(distributive_row5_col3_content), run_time=1)
        self.wait(1)

        distributive_row6_col0_content = SurroundingRectangle(distributive_table.get_entries((7, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row6_col1_content = SurroundingRectangle(distributive_table.get_entries((7, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row6_col3_content = SurroundingRectangle(distributive_table.get_entries((7, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row6_col0_content), run_time=1)
        self.play(Create(distributive_row6_col1_content),run_time=1)       
        self.play(Create(distributive_row6_col3_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row6_col0_content), FadeOut(distributive_row6_col1_content), FadeOut(distributive_row6_col3_content), run_time=1)
        self.wait(1)

        distributive_row7_col0_content = SurroundingRectangle(distributive_table.get_entries((8, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row7_col1_content = SurroundingRectangle(distributive_table.get_entries((8, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row7_col3_content = SurroundingRectangle(distributive_table.get_entries((8, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row7_col0_content), run_time=1)
        self.play(Create(distributive_row7_col1_content),run_time=1)       
        self.play(Create(distributive_row7_col3_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row7_col0_content), FadeOut(distributive_row7_col1_content), FadeOut(distributive_row7_col3_content), run_time=1)
        self.wait(1)

        distributive_row8_col0_content = SurroundingRectangle(distributive_table.get_entries((9, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row8_col1_content = SurroundingRectangle(distributive_table.get_entries((9, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row8_col3_content = SurroundingRectangle(distributive_table.get_entries((9, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row8_col0_content), run_time=1)
        self.play(Create(distributive_row8_col1_content),run_time=1)        
        self.play(Create(distributive_row8_col3_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row8_col0_content), FadeOut(distributive_row8_col1_content), FadeOut(distributive_row8_col3_content), run_time=1)
        self.wait(1)

        # p ∧ r
        distributive_row1_col2_content = SurroundingRectangle(distributive_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col3_content = SurroundingRectangle(distributive_table.get_entries((2, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col5_content = SurroundingRectangle(distributive_table.get_entries((2, 6)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row1_col2_content), run_time=1)
        self.play(Create(distributive_row1_col3_content),run_time=1)        
        self.play(Create(distributive_row1_col5_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row1_col2_content), FadeOut(distributive_row1_col3_content), FadeOut(distributive_row1_col5_content), run_time=1)
        self.wait(1)

        distributive_row2_col2_content = SurroundingRectangle(distributive_table.get_entries((3, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row2_col3_content = SurroundingRectangle(distributive_table.get_entries((3, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row2_col5_content = SurroundingRectangle(distributive_table.get_entries((3, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row2_col2_content), run_time=1)
        self.play(Create(distributive_row2_col3_content),run_time=1)        
        self.play(Create(distributive_row2_col5_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row2_col2_content), FadeOut(distributive_row2_col3_content),FadeOut(distributive_row2_col5_content), run_time=1)
        self.wait(1)

        distributive_row3_col2_content = SurroundingRectangle(distributive_table.get_entries((4, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row3_col3_content = SurroundingRectangle(distributive_table.get_entries((4, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row3_col5_content = SurroundingRectangle(distributive_table.get_entries((4, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row3_col2_content), run_time=1)
        self.play(Create(distributive_row3_col3_content),run_time=1)        
        self.play(Create(distributive_row3_col5_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row3_col2_content), FadeOut(distributive_row3_col3_content), FadeOut(distributive_row3_col5_content), run_time=1)
        self.wait(1)

        distributive_row4_col2_content = SurroundingRectangle(distributive_table.get_entries((5, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row4_col3_content = SurroundingRectangle(distributive_table.get_entries((5, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row4_col5_content = SurroundingRectangle(distributive_table.get_entries((5, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row4_col2_content), run_time=1)
        self.play(Create(distributive_row4_col3_content),run_time=1)        
        self.play(Create(distributive_row4_col5_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row4_col2_content), FadeOut(distributive_row4_col3_content), FadeOut(distributive_row4_col5_content), run_time=1)        
        self.wait(1)

        distributive_row5_col2_content = SurroundingRectangle(distributive_table.get_entries((6, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row5_col3_content = SurroundingRectangle(distributive_table.get_entries((6, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row5_col5_content = SurroundingRectangle(distributive_table.get_entries((6, 6)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row5_col2_content), run_time=1)
        self.play(Create(distributive_row5_col3_content),run_time=1)        
        self.play(Create(distributive_row5_col5_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row5_col2_content), FadeOut(distributive_row5_col3_content), FadeOut(distributive_row5_col5_content), run_time=1)
        self.wait(1)

        distributive_row6_col2_content = SurroundingRectangle(distributive_table.get_entries((7, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row6_col3_content = SurroundingRectangle(distributive_table.get_entries((7, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row6_col5_content = SurroundingRectangle(distributive_table.get_entries((7, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row6_col2_content), run_time=1)
        self.play(Create(distributive_row6_col3_content),run_time=1)       
        self.play(Create(distributive_row6_col5_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row6_col2_content), FadeOut(distributive_row6_col3_content), FadeOut(distributive_row6_col5_content), run_time=1)
        self.wait(1)

        distributive_row7_col2_content = SurroundingRectangle(distributive_table.get_entries((8, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row7_col3_content = SurroundingRectangle(distributive_table.get_entries((8, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row7_col5_content = SurroundingRectangle(distributive_table.get_entries((8, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row7_col2_content), run_time=1)
        self.play(Create(distributive_row7_col3_content),run_time=1)       
        self.play(Create(distributive_row7_col5_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row7_col2_content), FadeOut(distributive_row7_col3_content), FadeOut(distributive_row7_col5_content), run_time=1)
        self.wait(1)

        distributive_row8_col2_content = SurroundingRectangle(distributive_table.get_entries((9, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row8_col3_content = SurroundingRectangle(distributive_table.get_entries((9, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row8_col5_content = SurroundingRectangle(distributive_table.get_entries((9, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row8_col2_content), run_time=1)
        self.play(Create(distributive_row8_col3_content),run_time=1)        
        self.play(Create(distributive_row8_col5_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row8_col2_content), FadeOut(distributive_row8_col3_content), FadeOut(distributive_row8_col5_content), run_time=1)
        self.wait(1)

         # p ∧ (q ∨ r)
        distributive_row1_col4_content = SurroundingRectangle(distributive_table.get_entries((2, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col3_content = SurroundingRectangle(distributive_table.get_entries((2, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col6_content = SurroundingRectangle(distributive_table.get_entries((2, 6)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row1_col4_content), run_time=1)
        self.play(Create(distributive_row1_col3_content),run_time=1)        
        self.play(Create(distributive_row1_col6_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row1_col4_content), FadeOut(distributive_row1_col3_content), FadeOut(distributive_row1_col6_content), run_time=1)
        self.wait(1)

        distributive_row2_col4_content = SurroundingRectangle(distributive_table.get_entries((3, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row2_col3_content = SurroundingRectangle(distributive_table.get_entries((3, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row2_col6_content = SurroundingRectangle(distributive_table.get_entries((3, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row2_col4_content), run_time=1)
        self.play(Create(distributive_row2_col3_content),run_time=1)        
        self.play(Create(distributive_row2_col6_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row2_col4_content), FadeOut(distributive_row2_col3_content),FadeOut(distributive_row2_col6_content), run_time=1)
        self.wait(1)

        distributive_row3_col4_content = SurroundingRectangle(distributive_table.get_entries((4, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row3_col3_content = SurroundingRectangle(distributive_table.get_entries((4, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row3_col6_content = SurroundingRectangle(distributive_table.get_entries((4, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row3_col4_content), run_time=1)
        self.play(Create(distributive_row3_col3_content),run_time=1)        
        self.play(Create(distributive_row3_col6_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row3_col4_content), FadeOut(distributive_row3_col3_content), FadeOut(distributive_row3_col6_content), run_time=1)
        self.wait(1)

        distributive_row4_col4_content = SurroundingRectangle(distributive_table.get_entries((5, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row4_col3_content = SurroundingRectangle(distributive_table.get_entries((5, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row4_col6_content = SurroundingRectangle(distributive_table.get_entries((5, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row4_col4_content), run_time=1)
        self.play(Create(distributive_row4_col3_content),run_time=1)        
        self.play(Create(distributive_row4_col6_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row4_col4_content), FadeOut(distributive_row4_col3_content), FadeOut(distributive_row4_col6_content), run_time=1)        
        self.wait(1)

        distributive_row5_col4_content = SurroundingRectangle(distributive_table.get_entries((6, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row5_col3_content = SurroundingRectangle(distributive_table.get_entries((6, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row5_col6_content = SurroundingRectangle(distributive_table.get_entries((6, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row5_col4_content), run_time=1)
        self.play(Create(distributive_row5_col3_content),run_time=1)        
        self.play(Create(distributive_row5_col6_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row5_col4_content), FadeOut(distributive_row5_col3_content), FadeOut(distributive_row5_col6_content), run_time=1)
        self.wait(1)

        distributive_row6_col4_content = SurroundingRectangle(distributive_table.get_entries((7, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row6_col3_content = SurroundingRectangle(distributive_table.get_entries((7, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row6_col6_content = SurroundingRectangle(distributive_table.get_entries((7, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row6_col4_content), run_time=1)
        self.play(Create(distributive_row6_col3_content),run_time=1)       
        self.play(Create(distributive_row6_col6_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row6_col4_content), FadeOut(distributive_row6_col3_content), FadeOut(distributive_row6_col6_content), run_time=1)
        self.wait(1)

        distributive_row7_col4_content = SurroundingRectangle(distributive_table.get_entries((8, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row7_col3_content = SurroundingRectangle(distributive_table.get_entries((8, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row7_col6_content = SurroundingRectangle(distributive_table.get_entries((8, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row7_col4_content), run_time=1)
        self.play(Create(distributive_row7_col3_content),run_time=1)       
        self.play(Create(distributive_row7_col6_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row7_col4_content), FadeOut(distributive_row7_col3_content), FadeOut(distributive_row7_col6_content), run_time=1)
        self.wait(1)

        distributive_row8_col4_content = SurroundingRectangle(distributive_table.get_entries((9, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row8_col3_content = SurroundingRectangle(distributive_table.get_entries((9, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row8_col6_content = SurroundingRectangle(distributive_table.get_entries((9, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row8_col4_content), run_time=1)
        self.play(Create(distributive_row8_col3_content),run_time=1)        
        self.play(Create(distributive_row8_col6_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row8_col4_content), FadeOut(distributive_row8_col3_content), FadeOut(distributive_row8_col6_content), run_time=1)
        self.wait(1)

        # (p ∧ q) ∨ (p ∧ r)

        distributive_row1_col1_content = SurroundingRectangle(distributive_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col5_content = SurroundingRectangle(distributive_table.get_entries((2, 5)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col7_content = SurroundingRectangle(distributive_table.get_entries((2, 7)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row1_col1_content), run_time=1)
        self.play(Create(distributive_row1_col5_content),run_time=1)        
        self.play(Create(distributive_row1_col7_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row1_col1_content), FadeOut(distributive_row1_col5_content), FadeOut(distributive_row1_col7_content), run_time=1)
        self.wait(1)

        distributive_row2_col1_content = SurroundingRectangle(distributive_table.get_entries((3, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row2_col5_content = SurroundingRectangle(distributive_table.get_entries((3, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row2_col7_content = SurroundingRectangle(distributive_table.get_entries((3, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row2_col1_content), run_time=1)
        self.play(Create(distributive_row2_col5_content),run_time=1)        
        self.play(Create(distributive_row2_col7_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row2_col1_content), FadeOut(distributive_row2_col5_content),FadeOut(distributive_row2_col7_content), run_time=1)
        self.wait(1)

        distributive_row3_col1_content = SurroundingRectangle(distributive_table.get_entries((4, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row3_col5_content = SurroundingRectangle(distributive_table.get_entries((4, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row3_col7_content = SurroundingRectangle(distributive_table.get_entries((4, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row3_col1_content), run_time=1)
        self.play(Create(distributive_row3_col5_content),run_time=1)        
        self.play(Create(distributive_row3_col7_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row3_col1_content), FadeOut(distributive_row3_col5_content), FadeOut(distributive_row3_col7_content), run_time=1)
        self.wait(1)

        distributive_row4_col1_content = SurroundingRectangle(distributive_table.get_entries((5, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row4_col5_content = SurroundingRectangle(distributive_table.get_entries((5, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row4_col7_content = SurroundingRectangle(distributive_table.get_entries((5, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row4_col1_content), run_time=1)
        self.play(Create(distributive_row4_col5_content),run_time=1)        
        self.play(Create(distributive_row4_col7_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row4_col1_content), FadeOut(distributive_row4_col5_content), FadeOut(distributive_row4_col7_content), run_time=1)        
        self.wait(1)

        distributive_row5_col1_content = SurroundingRectangle(distributive_table.get_entries((6, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row5_col5_content = SurroundingRectangle(distributive_table.get_entries((6, 5)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row5_col7_content = SurroundingRectangle(distributive_table.get_entries((6, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row5_col1_content), run_time=1)
        self.play(Create(distributive_row5_col5_content),run_time=1)        
        self.play(Create(distributive_row5_col7_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row5_col1_content), FadeOut(distributive_row5_col5_content), FadeOut(distributive_row5_col7_content), run_time=1)
        self.wait(1)

        distributive_row6_col1_content = SurroundingRectangle(distributive_table.get_entries((7, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row6_col5_content = SurroundingRectangle(distributive_table.get_entries((7, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row6_col7_content = SurroundingRectangle(distributive_table.get_entries((7, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row6_col1_content), run_time=1)
        self.play(Create(distributive_row6_col5_content),run_time=1)       
        self.play(Create(distributive_row6_col7_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row6_col1_content), FadeOut(distributive_row6_col5_content), FadeOut(distributive_row6_col7_content), run_time=1)
        self.wait(1)

        distributive_row7_col1_content = SurroundingRectangle(distributive_table.get_entries((8, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row7_col5_content = SurroundingRectangle(distributive_table.get_entries((8, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row7_col7_content = SurroundingRectangle(distributive_table.get_entries((8, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row7_col1_content), run_time=1)
        self.play(Create(distributive_row7_col5_content),run_time=1)       
        self.play(Create(distributive_row7_col7_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row7_col1_content), FadeOut(distributive_row7_col5_content), FadeOut(distributive_row7_col7_content), run_time=1)
        self.wait(1)

        distributive_row8_col1_content = SurroundingRectangle(distributive_table.get_entries((9, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row8_col5_content = SurroundingRectangle(distributive_table.get_entries((9, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row8_col7_content = SurroundingRectangle(distributive_table.get_entries((9, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row8_col1_content), run_time=1)
        self.play(Create(distributive_row8_col5_content),run_time=1)        
        self.play(Create(distributive_row8_col7_content) ,run_time=1)
        self.wait(1)
        self.play(FadeOut(distributive_row8_col1_content), FadeOut(distributive_row8_col5_content), FadeOut(distributive_row8_col7_content), run_time=1)
        self.wait(1)

        
        
        distributive_col6 = SurroundingRectangle(distributive_table.get_columns()[6][1:], color=RED, buff=0.05, 
                                             stroke_width= 1)
        distributive_col7 = SurroundingRectangle(distributive_table.get_columns()[7][1:], color=RED, buff=0.05, 
                                             stroke_width= 1)
        self.add(distributive_col6, distributive_col7)
        self.wait(1)
        # self.play(FadeOut(distributive_group), FadeOut(distributive_col6), FadeOut(distributive_col7),  FadeOut(distributive_bullet_underline), run_time=1)
        self.play(FadeOut(distributive_group), FadeOut(distributive_col6), FadeOut(distributive_col7), run_time=1)
        self.wait(2)
        
      
        # manim -ql -p  .\lab.py EquivalenceScene
