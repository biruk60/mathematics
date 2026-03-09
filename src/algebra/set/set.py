from manim import * 
import manimpango
from common.common import layout

class Introduction(Scene):
    def construct(self):
        background, bg_text = layout()
        # self.add(background)
        # self.add(bg_text) 
        self.add(background)  
        self.add(bg_text)   
        # Title
        title = Text("መእተዊ / Introduction", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)

        # t = MathTex(r"\int_a^b", "f'(x)", "dx"," =", " f(b)","-", "f(a)").next_to(underline, DOWN*2, buff=0.5)
        # ch = MathTex(r"\{...,-4,-3,-2,-1,0,1,2,3,4,...\}").next_to(t, DOWN*2, buff=0.5)
        # ex = MathTex(r"\Large f(x)=\int_{-\infty}^x e^{-t^2}dt").next_to(ch, DOWN, buff=.5)()
        # A =  MathTex(r"\{","2","4","6","8","\}").next_to(underline, DOWN*2, buff=0.5)
        _set = Text("set")
        _elements= Text("elements") 
        _set_A = Text("A")      
        _set_a =  MathTex(r"\{2,4,6,8\}")
        _set_b =  MathTex(r"\{4,2,8,6\}")
        _set_c = MathTex(r"\{2,4,5,7\}")
        _equal = MathTex(r" = ")
        _not_equal = MathTex(r" \neq ")
        _element_of = MathTex(r"\in")
        _not_element_of = MathTex(r"\notin")
        _set_of_natural_numbers = MathTex(r"\mathbb{N} = \{1,2,3,4,5,6,7,8,...\}") 
        _natural_number =  MathTex(r"\mathbb{N}")
        _set_of_integers = MathTex(r"\mathbb{Z} = \{...,-4,-3,-2,-1,0,1,2,3,4,...\}")
        _integer = MathTex(r"\mathbb{Z}")
        _rational_number = MathTex(r"\mathbb{Q}")
        _real_number = MathTex(r"\mathbb{R}")
        _complex_number = MathTex(r"\mathbb{C}")
        _infinite_set = MathTex(r"\{","...",",-4,-3,-2,-1,0,1,2,3,4,", "...","\}")
        _set_of_bools = MathTex(r"B = \{T,F\}")
        _set_of_vowels = MathTex(r"V = \{a,e,i,o,u\}")
        _set_of_xy_coordinates = MathTex(r"\{(0,0),(1,0),(0,1),(1,1)\}")
        _set_of_sets = MathTex(r"S = \{1, \{1, 2\}, \{3, 4\} \}")
        _set_of_matrix = MathTex(
            r"S = \left\{ "
            r"\begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}, "
            r"\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, "
            r"\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} "
            r"\right\}"
        )
        _cardinality= Text("|x|")
        _cardinality_of_v = Text("|V| = 5")
        _cardinality_of_m = Text("|M| = 3")
        _empty_set = MathTex(r"\emptyset")
        empty_set_braces = MathTex(r"\{ \}")
        _cardinality_of_empty = MathTex(r"|\emptyset| = 0")
        set_with_empty = MathTex(r"\{ \emptyset \}")
        # self.play(Write(set_with_empty), run_time=1)
        _set_builder_notation = MathTex(r"E = \{ 2n : n \in \mathbb{Z} \}").next_to(underline, DOWN, buff=0.2)
        _set_builder_notation_alt = MathTex(r"E = \{ n \in \mathbb{Z} : n\text{ is even} \}").next_to(_set_builder_notation, DOWN, buff=0.2)
        _set_builder_expression_rule =  MathTex(r"X = \{ expression : rule \}")
        self.play(Write(_set_builder_notation), run_time=1)
        self.wait(2)
        self.play(Write(_set_builder_notation_alt), run_time=1)
        self.wait(2)
        '''
        
        num_list = [MathTex(n) for n in ["2", "4", "6", "8"]]
        
        # 2. Group them and arrange with a buffer (space)
        # buff=1.0 provides a generous space between elements
        numbers = VGroup(*num_list).arrange(RIGHT, buff=1.0)
        box = SurroundingRectangle(numbers, color=YELLOW, 
                                          fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.1
                                          ,stroke_width= 2, buff=MED_LARGE_BUFF)

        # 3. Animate them
        self.play(Create(box))
        self.play(Write(numbers))
        self.wait(2)
        self.play(FadeOut(box), FadeOut(numbers))
        self.wait(2)
        self.add(_equal)
        outer_box = RoundedRectangle(width=5, height=3,fill_opacity=0.05, corner_radius=0.1, fill_color=ORANGE,
                                          stroke_width= 2, color=YELLOW)
        
        box_left = Square(side_length=1.5, color=RED)
        box_right = Square(side_length=2, color=GREEN).next_to(box_left, RIGHT, buff=0.4)
        box_deep = Square(side_length=1.5, color=BLUE).move_to(box_right.get_center())
        box_deeper = Square(side_length=0.5, color=PURPLE).move_to(box_deep.get_center())
        # Group and position boxes to the right of the equal sign
        boxes_group = VGroup(box_left, box_right, box_deep, box_deeper).move_to(outer_box.get_center())
        box_viz = VGroup(outer_box, boxes_group).next_to(_equal, RIGHT, buff=0.4)

        # 3. Define the Set Stages (using MathTex)
        # We use r'...' for LaTeX strings
        sets = [
            MathTex(r"A", r"=", r"\{ \}"),
            MathTex(r"A", r"=", r"\{ \{ \} \}"),
            MathTex(r"A", r"=", r"\{ \{ \}, \{ \} \}"),
            MathTex(r"A", r"=", r"\{ \{ \}, \{ \{ \} \} \}"),
            MathTex(r"A", r"=", r"\{ \{ \}, \{ \{ \{ \} \} \} \}") # Deepest stage
        ]

        # Initialize the first set position
        for s in sets:
            s.next_to(_equal, LEFT, buff=0.4)

        current_set = sets[0]

        # 4. Animation Sequence
        # Step 1: Outer Box
        self.play(Create(outer_box), Write(current_set))
        self.wait(0.5)

        # Step 2: Left Inner Box
        self.play(
            Create(box_left),
            Transform(current_set, sets[1].next_to(_equal, LEFT, buff=0.4))
        )
        self.wait(0.5)

        # Step 3: Right Inner Box
        self.play(
            Create(box_right),
            Transform(current_set, sets[2].next_to(_equal, LEFT, buff=0.4))
        )
        self.wait(0.5)

        # Step 4: Deep Inner Box
        self.play(
            Create(box_deep),
            Transform(current_set, sets[3].next_to(_equal, LEFT, buff=0.4))
        )
        self.wait(0.5)
        self.play(
            Create(box_deeper),
            Transform(current_set, sets[4].next_to(_equal, LEFT, buff=0.4))
        )
        self.wait(2)
'''
# manim -ql -p --disable_caching set.py Formula
# manim -ql -p  set.py Introduction