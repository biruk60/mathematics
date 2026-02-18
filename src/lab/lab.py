from manim import * 

from common.common import layout

class CivilizationTimeline(Scene):
    def construct(self):
        # 1. Timeline Configuration
        # We start the math range earlier (-12000) than the first milestone (-10000)
        # to create visual room for the arrow tip.
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)        
               
        # Title
        title = Text("ምዕባለ ስነ-መጐት", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        line_start = -600 
        line_end = 2100
        
        logos_greek = Text("λόγος", color=WHITE)
        equals = Text("≡", color=WHITE)
        logos_tigrigna = Text("ርትዒ / መጎት", color=WHITE, font="Nyala")
        logos = VGroup(logos_greek, equals, logos_tigrigna).next_to(underline, DOWN, buff=.2).scale(.6)
        logos.arrange(RIGHT, buff=0.1)
        line = NumberLine(
            x_range=[line_start, line_end, 100],
            unit_size=.5,
            length=12,
            color=BLUE,
            include_numbers=False,
        ).next_to(logos, DOWN*4, buff=.2)
        
        # Add arrows to both ends
        line.add_tip(tip_shape=StealthTip, tip_length=0.2) 
        line.add_tip(tip_shape=StealthTip, tip_length=0.2, at_start=True) 
        
       
        
        # Milestones (Year, Label, Position)
        milestones = [
            (-384, "ኣርስቶትል", "384-322 <b>ዓ.ዓ</b>", UP),
            (1646, "ላይብነትዝ", "1646-1716 <b>ዓ.ም</b>", DOWN),
            (1815, "ቡል", "1815-1864 <b>ዓ.ም</b>", UP)
        ]
        
        self.play(Write(logos_greek))
        self.wait()
        self.play(Write(equals), Write(logos_tigrigna))
        self.wait()
        self.play(ShrinkToCenter(logos))
        self.play(FadeIn(line))
        self.wait(1)

        all_elements = []
        # 2. Animate Milestones
        for year, name, date_str, direction in milestones:
            # Place dot at the birth year
            dot = Dot(color=YELLOW).move_to(line.n2p(year))
            
            # Name label
            label = MarkupText(name, font_size=26,font="Nyala")
            label.next_to(dot, direction, buff=0.3)
                
            # Date range label
            date_label = MarkupText(date_str, font_size=20, color=RED,font="Nyala")
            date_label.next_to(label, direction, buff=0.1)

            self.play(
                FadeIn(dot, scale=0.5), 
                Write(label), 
                FadeIn(date_label, shift=direction*0.2),
                run_time=1
            )
            all_elements.extend([dot, label, date_label])
            self.wait(1)

        self.wait(1)
        self.play(FadeOut(line),  FadeOut(*all_elements))
        self.wait(1)

        brain = SVGMobject("../assets/svgs/brain.svg").scale(.6)
        brain.set_color(WHITE)
        discussion = SVGMobject("../assets/svgs/debate.svg" , color=WHITE)
        discussion.set_color(WHITE)
        think = SVGMobject("../assets/svgs/science_think.svg", color=WHITE)
        think.set_color(WHITE)

        starting_group = VGroup(think, discussion).scale(.6)
        starting_group.arrange(RIGHT, buff=2)
        self.add(think)
        self.wait()
        self.add(discussion)
        self.wait()
        self.play(Transform(starting_group, brain), run_time=1)
        self.wait()
        throb = brain[0] # Your specific gear object
        # gear2 = thinking_head[1]
        
        
        self.play( Succession(
        *[
            AnimationGroup(
                Indicate(throb, color=RED, scale_factor=1.1),
                # Indicate(gear2, color=RED, scale_factor=1.1),
                run_time=1
            ) 
            for _ in range(3)
        ]
    )  )
        self.wait(3)
 # manim -ql -p -o lab.mp4 lab.py CivilizationTimeLine
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
        
