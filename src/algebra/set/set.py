

from manim import * 
import manimpango
from common.common import layout

class Introduction(Scene):
    def construct(self):
        SCALE_FACTOR_PER_FONT_POINT= 0.5
        DEFAULT_FONT_SIZE = 20
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
        # _set_builder_notation = MathTex(r"E = \{ 2n : n \in \mathbb{Z} \}").next_to(underline, DOWN, buff=0.2).scale(.5)
        # _set_builder_notation_alt = MathTex(r"E = \{ n \in \mathbb{Z} : n\text{ is even} \}").next_to(_set_builder_notation, DOWN, buff=0.2).scale(.5)
        # _set_builder_expression_rule =  MathTex(r"X = \{ expression : rule \}").scale(.5) ኣገላልፃ: ሕጊ
        # self.play(Write(_set_builder_notation), run_time=1)
        # self.wait(2)
        # self.play(Write(_set_builder_notation_alt), run_time=1)
        # self.wait(2)

        # Common number line
        number_line_1 = NumberLine(x_range=[-3, 4, 1],include_numbers=False,stroke_width=2, color=GREY_B)
        number_line_2 = number_line_1.copy().shift(DOWN)
        number_line_3 = number_line_2.copy().shift(DOWN)
        number_line_4 = number_line_3.copy().shift(DOWN)
        number_line_5 = number_line_4.copy().shift(DOWN)
        number_line_6 = number_line_5.copy().shift(DOWN)
        number_line_7 = number_line_6.copy().shift(DOWN)
        number_line_8 = number_line_7.copy().shift(DOWN)

        
    
        number_line_1.add_tip(tip_shape=StealthTip, tip_length=0.2) 
        number_line_1.add_tip(tip_shape=StealthTip, tip_length=0.2, at_start=True)
        number_line_2.add_tip(tip_shape=StealthTip, tip_length=0.2) 
        number_line_2.add_tip(tip_shape=StealthTip, tip_length=0.2, at_start=True)
        number_line_3.add_tip(tip_shape=StealthTip, tip_length=0.2) 
        number_line_3.add_tip(tip_shape=StealthTip, tip_length=0.2, at_start=True)
        number_line_4.add_tip(tip_shape=StealthTip, tip_length=0.2) 
        number_line_4.add_tip(tip_shape=StealthTip, tip_length=0.2, at_start=True)
        number_line_5.add_tip(tip=StealthTip(fill_color=BLUE, stroke_color=BLUE, length=0.2, stroke_width=4,)) 
        number_line_5.add_tip(tip_shape=StealthTip, tip_length=0.2, at_start=True)
        number_line_6.add_tip(tip= StealthTip(fill_color=BLUE, stroke_color=BLUE, length=0.2, stroke_width=4,)) 
        number_line_6.add_tip(tip_shape=StealthTip, tip_length=0.2, at_start=True)
        number_line_7.add_tip(tip_shape=StealthTip, tip_length=0.2) 
        number_line_7.add_tip(tip= StealthTip(fill_color=BLUE, stroke_color=BLUE, length=0.2, stroke_width=4,), at_start=True)
        number_line_8.add_tip(tip_shape=StealthTip, tip_length=0.2) 
        number_line_8.add_tip(tip= StealthTip(fill_color=BLUE, stroke_color=BLUE, length=0.2, stroke_width=4,), at_start=True)

        set_builder_1 =  MathTex(r"[a,b] = \{ x \in \mathbb{Z} : a \leq x \leq b \}").next_to(number_line_1, LEFT*3, buff=0.5)
        set_builder_2 =  MathTex(r"(a,b) = \{ x \in \mathbb{Z} : a < x < b \}").next_to(number_line_2, LEFT*3, buff=0.5)
        set_builder_3 =  MathTex(r"(a,b] = \{ x \in \mathbb{Z} : a < x \leq b \}").next_to(number_line_3, LEFT*3, buff=0.5)
        set_builder_4 =  MathTex(r"[a,b) = \{ x \in \mathbb{Z} : a \leq x < b \}").next_to(number_line_4, LEFT*3, buff=0.5)
        set_builder_5 =  MathTex(r"(a,\infty) = \{ x \in \mathbb{Z} : a < x \}").next_to(number_line_5, LEFT*3, buff=0.5)
        set_builder_6 =  MathTex(r"[a,\infty) = \{ x \in \mathbb{Z} : a \leq x \}").next_to(number_line_6, LEFT*3, buff=0.5)
        set_builder_7 =  MathTex(r"(-\infty,b) = \{ x \in \mathbb{Z} :  x < b \}").next_to(number_line_7, LEFT*3, buff=0.5)
        set_builder_8 =  MathTex(r"(-\infty,b] = \{ x \in \mathbb{Z} :  x \leq b \}").next_to(number_line_8, LEFT*3, buff=0.5)


        # Positions for a and b
        a_val = -1
        b_val = 2

        # ----- Top: closed interval [a, b] -----
        # Segment between a and b
        segment_1 = Line(number_line_1.n2p(a_val-.1), number_line_1.n2p(b_val-.1), stroke_width=6, color=BLUE )
        segment_2 = Line(number_line_2.n2p(a_val + .1),  number_line_2.n2p(b_val - .1), stroke_width=6, color=BLUE )
        segment_3 = Line(number_line_3.n2p(a_val + .1),  number_line_3.n2p(b_val -.1), stroke_width=6, color=BLUE )
        segment_4 = Line(number_line_4.n2p(a_val + .1),  number_line_4.n2p(b_val -.1), stroke_width=6, color=BLUE )
        segment_5 = Line(number_line_5.n2p(a_val + .1),  number_line_5.n2p(4), stroke_width=6, color=BLUE )
        segment_6 = Line(number_line_6.n2p(a_val + .1),  number_line_6.n2p(4), stroke_width=6, color=BLUE )
        segment_7 = Line(number_line_7.n2p(-3),  number_line_7.n2p(b_val -.1), stroke_width=6, color=BLUE )
        segment_8 = Line(number_line_8.n2p(-3),  number_line_8.n2p(b_val -.1), stroke_width=6, color=BLUE )

        # Filled dots at a and b
        dot_a_1 = Dot(number_line_1.n2p(a_val), radius=0.14, color=BLUE)
        dot_b_1 = Dot(number_line_1.n2p(b_val), radius=0.14, color=BLUE)
        dot_a_1.set_z_index(number_line_1.z_index + 1)
        dot_b_1.set_z_index(number_line_1.z_index + 1)
        # Labels a, b
        label_a_1 = MathTex("a").next_to(dot_a_1, UP, buff=0.2)
        label_b_1 = MathTex("b").next_to(dot_b_1, UP, buff=0.2)

        # Open circles: use small circles with no fill
        circle_a_open_2 = Circle(radius=0.11, stroke_color=BLUE, stroke_width=3,fill_opacity=0).move_to(number_line_2.n2p(a_val)).set_z_index(number_line_2.z_index + 1)

        circle_b_open_2 = circle_a_open_2.copy().move_to(number_line_2.n2p(b_val)).set_z_index(number_line_2.z_index + 1)

        label_a_2 = MathTex("a").next_to(circle_a_open_2, UP, buff=0.2)
        label_b_2 = MathTex("b").next_to(circle_b_open_2, UP, buff=0.2)

        circle_a_open_3 = circle_a_open_2.copy().move_to(number_line_3.n2p(a_val))
        dot_b_3 = Dot(number_line_3.n2p(b_val), radius=0.14, color=BLUE).set_z_index(number_line_3.z_index + 1)

        label_a_3 = MathTex("a").next_to(circle_a_open_3, UP, buff=0.2)
        label_b_3 = MathTex("b").next_to(dot_b_3, UP, buff=0.2)

        
        dot_a_4 = Dot(number_line_4.n2p(a_val), radius=0.14, color=BLUE).set_z_index(number_line_4.z_index + 1)
        circle_b_open_4 = circle_b_open_2.copy().move_to(number_line_4.n2p(b_val))

        label_a_4 = MathTex("a").next_to(dot_a_4, UP, buff=0.2)
        label_b_4 = MathTex("b").next_to(circle_b_open_4, UP, buff=0.2)

        circle_a_open_5 = circle_a_open_2.copy().move_to(number_line_5.n2p(a_val))
        label_a_5 = MathTex("a").next_to(circle_a_open_5, UP, buff=0.2)

        dot_a_6 = Dot(number_line_6.n2p(a_val), radius=0.14, color=BLUE).set_z_index(number_line_6.z_index + 1)
        label_a_6 = MathTex("a").next_to(dot_a_6, UP, buff=0.2)

        circle_b_open_7 = circle_b_open_2.copy().move_to(number_line_7.n2p(b_val))
        label_b_7 = MathTex("b").next_to(circle_b_open_7, UP, buff=0.2)

        dot_b_8 = Dot(number_line_8.n2p(b_val), radius=0.14, color=BLUE).set_z_index(number_line_8.z_index + 1)
        label_b_8 = MathTex("b").next_to(dot_b_8, UP, buff=0.2)

        vgroup = VGroup(
            dot_a_1,label_a_1,
            dot_b_1,label_b_1,
            number_line_1,set_builder_1, segment_1,
            number_line_2, set_builder_2,segment_2,
            number_line_3, set_builder_3,segment_3,
            number_line_4, set_builder_4,segment_4,
            number_line_5, set_builder_5,segment_5,
            number_line_6, set_builder_6,segment_6,
            number_line_7, set_builder_7,segment_7,
            number_line_8, set_builder_8,segment_8,            
            circle_a_open_2, label_a_2, circle_b_open_2, label_b_2,
            circle_a_open_3,label_a_3, dot_b_3,label_b_3,
            dot_a_4,label_a_4, circle_b_open_4,label_b_4,
            circle_a_open_5,label_a_5,
            dot_a_6, label_a_6,
            circle_b_open_7,label_b_7,
            dot_b_8, label_b_8

            ).scale(.5).next_to(underline, DOWN)
        # Add everything
        self.add(vgroup)

        self.wait()


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
# manim -ql -p --disable_caching set.py Introduction
# manim -ql -p set.py Introduction

class CartesianProduct(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)  
        self.add(bg_text)   
        # Title
        title = Text("ብዝሒት ካርቴዥያን / Cartesian Product", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        # 2. Build the Product Grid (A x B)
        _order_pair_defintion_title= MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")
        _order_pair_defintion_1 = MarkupText("ስርዓት ዘለዎ ጽምዲ (ordered pair)፣ ኣብ ሓጹር ተዓጽዩ ብኮማ ዝተፈልየ፣ ናይ xን yን ዝተብሃሉ ክልተ ነገራት ዝርዝር እዩ። ምልክቱ ድማ፣ <span font_family='Sans' fgcolor='ORANGE'>(x, y)</span> እዩ።",font_size=30, color=WHITE, font="Nyala")
        _order_pair_definition = VGroup(_order_pair_defintion_title, _order_pair_defintion_1).scale(.5).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).shift(LEFT*1)
        
        _order_pair_defintion_box = SurroundingRectangle(_order_pair_definition, color=YELLOW, buff=0.4, fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2, stroke_width=1)
        self.add(_order_pair_defintion_title,
                _order_pair_defintion_1,
                _order_pair_defintion_box)
        self.wait(4)
        self.play(FadeOut(_order_pair_definition),FadeOut(_order_pair_defintion_box))
        self.wait(2)
        _example_1 = MathTex("(1, 2)")
        _example_2 = MathTex("(2, 1)")
        _not_equal = MathTex(r" \neq ", color=RED)
        _example = VGroup(_example_1, _not_equal, _example_2).arrange(RIGHT, buff=.2)
        numberplane = NumberPlane()
        dot = Dot(ORIGIN)
        _dot_1 = Dot(point=[1., 2., 0.], radius=.12, color=YELLOW)
        _dot_2 = Dot(point=[2., 1., 0.],radius=.12, color=RED)       
        _text_dot_1 = Text('(1, 2)').next_to(_dot_1.get_end(), RIGHT)
        _text_dot_2 = Text('(2, 1)').next_to(_dot_2.get_end(), RIGHT)
        _plane = VGroup(numberplane, dot,_dot_1,_dot_2, _text_dot_1, _text_dot_2).scale(.5)

        _order_pair = VGroup(_example, _plane).arrange(RIGHT, buff=.5).next_to(underline, DOWN*3, buff=0.2).scale(.5)
        self.play(Write(_example_1))
        self.wait()
        self.play(Write(_example_2))
        self.wait()
        self.play(Write(_not_equal))
        self.wait()
        self.play(FadeIn(numberplane), FadeIn(dot))
        self.wait()
        self.play(FadeIn(_dot_1))
        self.wait()
        self.play(FadeIn(_dot_2))
        self.wait()
        _example_copy_1 = _example_1.copy()
        _example_copy_2 = _example_2.copy()
        self.play(FadeTransform(_example_copy_1,_text_dot_1))
        self.wait()
        self.play(FadeTransform(_example_copy_2,_text_dot_2))
        self.wait(2)
        self.play(ShrinkToCenter(_order_pair))
        self.wait(2)
        
        _cartesian_product_defintion_title= MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")
        _cartesian_product_defintion_1 = MarkupText("ምልክቱ A X B ዝኾነ ናይ Aን Bን ዝተብሃሉ ክልተ ስብስባት Cartesian Product፣ በዚ መልክዕ ይግለፅ።",font_size=30, color=WHITE, font="Nyala")
        _cartesian_product_defintion_2 = MathTex(r"A \times B = \{(a,b): a \in A, b \in B \}")
        _cartesian_product_definition = VGroup(_cartesian_product_defintion_title, _cartesian_product_defintion_1, _cartesian_product_defintion_2).scale(.5).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).shift(LEFT*1)
        
        _cartesian_product_defintion_box = SurroundingRectangle(_cartesian_product_definition, color=YELLOW, buff=0.4, fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2, stroke_width=1)
        self.add(_cartesian_product_defintion_title,
                _cartesian_product_defintion_1,
                _cartesian_product_defintion_2,
                _cartesian_product_defintion_box)
        self.wait(4)
        self.play(FadeOut( _cartesian_product_definition),FadeOut( _cartesian_product_defintion_box))
        self.wait(2)
        grid_content = VGroup(
            MathTex("(k,r)", "(\\ell,r)", "(m,r)", color=PURPLE),
            MathTex("(k,q)", "(\\ell,q)", "(m,q)", color=PURPLE)
        ).arrange(DOWN, buff=1.0)
        
        # Manually align columns for row 2 to match row 1
        for i in range(3):
            grid_content[1][i].align_to(grid_content[0][i], LEFT)
        
        box_ab = RoundedRectangle(
            height=grid_content.height + 0.8, 
            width=grid_content.width + 1.0, 
            corner_radius=0.3,stroke_width= 2
        ).move_to(grid_content)
        label_ab = MathTex("A \\times B").next_to(box_ab, RIGHT, aligned_edge=UP, buff=0.2)
        product_section = VGroup(box_ab, grid_content, label_ab)

        # 3. Build Set B (Vertical)
        elements_b = VGroup(MathTex("r", color=RED), MathTex("q", color=RED)).arrange(DOWN, buff=1.0)
        elements_b.next_to(box_ab, LEFT, buff=1.2).align_to(grid_content, UP)

        
        box_b = RoundedRectangle(height=elements_b.height + 0.8, width=0.8, corner_radius=0.4, stroke_width= 2, fill_color=PURPLE).move_to(elements_b)
        label_b = MathTex("B").next_to(box_b, LEFT, aligned_edge=UP, buff=0.2)
        set_b_section = VGroup(box_b, elements_b, label_b)

        # 4. Build Set A (Horizontal)
        elements_a = VGroup(MathTex("k" ,color=BLUE), MathTex("\\ell",color=BLUE), MathTex("m",color=BLUE)).arrange(RIGHT, buff=1.5)
        elements_a.next_to(box_ab, DOWN, buff=1.0).align_to(grid_content, LEFT)
        
        box_a = RoundedRectangle(height=0.8, width=elements_a.width + 1.2, corner_radius=0.4, stroke_width= 2, fill_color=BLUE).move_to(elements_a)
        label_a = MathTex("A").next_to(box_a, RIGHT, buff=0.2)
        set_a_section = VGroup(box_a, elements_a, label_a)

        # 5. Group, Scale, and Position
        diagram = VGroup(product_section, set_b_section, set_a_section)
        diagram.scale(0.5) # Scale entire diagram to 0.5
        diagram.next_to(underline, DOWN, buff=1.0) # Position under title       

        # 6. Animation        
        _sets = [
            MathTex(r"A \times B", r"=", r"\{ \}"),
            MathTex(r"A \times B", r"=", r"\{ (k, r) \}"),
            MathTex(r"A \times B", r"=", r"\{ (k, r),(\ell, r)\}"),
            MathTex(r"A \times B", r"=", r"\{ (k, r),(\ell, r),(m, r) \}"),
            MathTex(r"A \times B", r"=", r"\{ (k, r),(\ell, r),(m, r),(k, q) \}"),
            MathTex(r"A \times B", r"=", r"\{ (k, r),(\ell, r),(m, r),(k, q),(\ell, q) \}"),
            MathTex(r"A \times B", r"=", r"\{ (k, r),(\ell, r),(m, r),(k, q),(\ell, q), (m, q)\}")           
        ]

        # Initialize the first set position 
        for s in _sets:
            s.scale(.5).next_to(diagram, DOWN, buff=0.4)

        current_set = _sets[0]
	
        self.play(FadeIn(set_b_section, shift=DOWN), run_time=2)
        self.play(FadeIn(set_a_section, shift=DOWN), run_time=2)
        self.play(FadeIn(box_ab),FadeIn(label_ab), FadeIn(current_set), run_time=2)
        self.wait(2)
        x = 1
        for i, row_char in enumerate(elements_b):      # r, then q
            for j, col_char in enumerate(elements_a):  # k, then l, then m
                
                # Target coordinate in your grid_content
                target = grid_content[i][j]
                
                # Create temporary copies to transform so the originals stay (or disappear)
                self.play(
                    ReplacementTransform(col_char.copy(), target), # Transform 'k' to '(' or 'k'
                    ReplacementTransform(row_char.copy(), target), # Transform 'r' to 'r' or ')'
                    Transform(current_set, _sets[x].next_to(diagram, DOWN, buff=0.4)),
                    run_time=1
                )
                x = x + 1
                self.wait(.5)
        
        self.wait(2)
        _sets_cardinality = MathTex(r'|A \times B| = |A|.|B|').next_to(current_set, DOWN*2, buff=0.2).scale(.5)
        self.play(Write(_sets_cardinality))
        self.wait(2)
        self.play(FadeOut(diagram), FadeOut(current_set),FadeOut(_sets_cardinality) )
        self.wait(2)
        _cartesian_notation_RR = MathTex(r"\mathbb{R} \times \mathbb{R} = \{ (x, y) : x, y \in \mathbb{R} \}")
        _cartesian_notation_RN = MathTex(r"\mathbb{R} \times \mathbb{N} = \{ (x, y) : x \in \mathbb{R}, y \in \mathbb{N} \}")
        _cartesian_notation_NN = MathTex(r"\mathbb{N} \times \mathbb{N} = \{ (x, y) : x, y \in \mathbb{N} \}")

        plane_fill = Rectangle(
            width=8, height=6, 
            fill_color=LIGHT_PINK, 
            fill_opacity=0.3, 
            stroke_width=0
        )

        # 2. Create the double-headed axes
        # We use DoubleArrow to get tips on both ends
        x_axis = DoubleArrow(
            start=LEFT * 4.5, end=RIGHT * 4.5, 
            buff=0, color=WHITE, stroke_width=2
        )
        y_axis = DoubleArrow(
            start=DOWN * 3.5, end=UP * 3.5, 
            buff=0, color=WHITE, stroke_width=2
        )

        # 3. Create the labels
        x_label = MathTex("x", color=WHITE).next_to(x_axis.get_end(), RIGHT, buff=0.1)
        y_label = MathTex("y", color=WHITE).next_to(y_axis.get_end(), UP, buff=0.1)
        
        # The set notation label in the bottom right (4th quadrant)
        inner_label = MathTex(r"\mathbb{R} \times \mathbb{R}", color=WHITE).scale(0.8)
        inner_label.move_to(RIGHT * 1.8 + DOWN * 1.2)

        # 4. Add everything to the scene
        # We add the fill first so it stays behind the lines and text
        # 3. Create the Diagram VGroup (the "body")
        diagram_body = VGroup(plane_fill, x_axis, y_axis, x_label, y_label, inner_label)

        # 4. Combine Title and Body into one Master VGroup
        # We arrange them vertically with the title on top
        full_rr = VGroup(_cartesian_notation_RR, diagram_body).arrange(DOWN, buff=0.8)
        
        # Center the whole thing on screen
        full_rr.move_to(LEFT*4).scale(.35)
        self.play(FadeIn(full_rr))
        self.wait(2)

        # Fade out the entire group at once as requested
        # self.play(FadeOut(full_group))
        # self.wait(1)

        lines = VGroup(*[
            # We add 'UP * y' to both the start and end points to space them out
            Line(LEFT * 3.5 + UP * y, RIGHT * 3.5 + UP * y, stroke_width=2, color=PINK)
            for y in np.arange(0.5, 3.5, 0.5)
        ])

        # 3. Create the Axes (DoubleArrow)
        x_axis = DoubleArrow(LEFT * 4.5, RIGHT * 4.5, color=WHITE, stroke_width=2, buff=0)
        y_axis = DoubleArrow(DOWN * 3.5, UP * 3.5, color=WHITE, stroke_width=2, buff=0)
        
        # Position the lines relative to the x-axis
        lines.next_to(x_axis, UP, buff=0.5)

        # 4. Labels
        x_label = MathTex("x").next_to(x_axis.get_end(), RIGHT, buff=0.1)
        y_label = MathTex("y").next_to(y_axis.get_end(), UP, buff=0.1)
        
        # Label for the specific set (bottom right)
        graph_label = MathTex(r"\mathbb{R} \times \mathbb{N}").scale(0.8)
        graph_label.move_to(RIGHT * 2 + DOWN * 0.8)

        # 5. Group the Graph elements
        graph_body = VGroup(lines, x_axis, y_axis, x_label, y_label, graph_label)

        # 6. Final Master VGroup: Title + Graph
        full_rn = VGroup(_cartesian_notation_RN, graph_body).arrange(DOWN, buff=1.0)
        full_rn.next_to(full_rr, RIGHT, buff=.2).shift(LEFT*2).scale(.35)

        # --- ANIMATION ---
        self.play(Write(_cartesian_notation_RN))
        self.wait(0.5)
        
        # Animate lines appearing one by one to emphasize the "Discrete" nature of N
        self.play(Create(x_axis), Create(y_axis), Write(x_label), Write(y_label))
        self.play(AnimationGroup(*[Create(l) for l in lines], lag_ratio=0.2))
        self.play(Write(graph_label))
        
        self.wait(2)
        
        # Fade out everything at once
        # self.play(FadeOut(full_rn))

        dots = VGroup()
        for x in np.arange(0.5, 3.5, 0.5):
            for y in np.arange(0.5, 3.5, 0.5):
                dots.add(Dot(point=[x, y, 0], radius=0.06, color=PINK))

        # 3. Create the Axes (DoubleArrow)
        # Origin is at [0,0,0], dots start at 0.5
        x_axis = DoubleArrow(LEFT * 4.5, RIGHT * 4.5, color=WHITE, stroke_width=2, buff=0)
        y_axis = DoubleArrow(DOWN * 3.5, UP * 3.5, color=WHITE, stroke_width=2, buff=0)

        # 4. Labels
        x_label = MathTex("x").next_to(x_axis.get_end(), RIGHT, buff=0.1)
        y_label = MathTex("y").next_to(y_axis.get_end(), UP, buff=0.1)
        
        # Label for the specific set (bottom right area of the first quadrant)
        graph_label = MathTex(r"\mathbb{N} \times \mathbb{N}").scale(0.8)
        graph_label.move_to(RIGHT * 2 + DOWN * 0.8)

        # 5. Group the Graph elements
        # Note: we group the axes, dots, and labels together
        graph_body = VGroup(x_axis, y_axis, dots, x_label, y_label, graph_label)

        # 6. Final Master VGroup: Title + Graph
        full_nn = VGroup(_cartesian_notation_NN, graph_body).arrange(DOWN, buff=0.8)
        full_nn.next_to(full_rn, RIGHT, buff=.2).shift(LEFT*2).scale(.35)

        # --- ANIMATION ---
        self.play(Write(_cartesian_notation_NN))
        self.wait(0.5)

        # Draw axes
        self.play(Create(x_axis), Create(y_axis), Write(x_label), Write(y_label))
        
        # Animate dots appearing in order (by column)
        self.play(LaggedStartMap(FadeIn, dots, shift=UP*0.2, scale=0.5, lag_ratio=0.05))
        
        self.play(Write(graph_label))
        self.wait(2)

        # Fade out the entire VGroup at once
        self.play(FadeOut(full_nn), FadeOut(full_rn), FadeOut(full_rr))
        self.wait()

        _cartesian_notation_RNZ = MathTex(
            r"\mathbb{R} \times \mathbb{N} \times \mathbb{Z} = \{ (x, y, z) : x \in \mathbb{R}, y \in \mathbb{N}, z \in \mathbb{Z} \}"
        ).scale(.5)
        _cartesian_product_n = MathTex(
            r"A_1 \times A_2 \times \cdots \times A_n = \{ (x_1, x_2, \dots, x_n) : x_i \in A_i \text{ for each } i = 1, 2, \dots, n \}"
        ).scale(.5)
        _cartesian_notation_An = MathTex(
            r"A^n = A \times A \times \cdots \times A = \{ (x_1, x_2, \dots, x_n) : x_1, x_2, \dots, x_n \in A \}"
        ).scale(.5)
        _matrix_set_M = MathTex(
            r"M = \left\{ \begin{bmatrix} u & v & w \\ x & y & z \end{bmatrix} : u, v, w, x, y, z \in \mathbb{R} \right\}"
        ).next_to(underline, DOWN, buff=.5).scale(.5)

        _r6_notation = MathTex(
            r"\mathbb{R}^6 = \{ (u, v, w, x, y, z) : u, v, w, x, y, z \in \mathbb{R} \}"
        ).next_to(_matrix_set_M, DOWN, buff=.2).scale(.5)
        _M_not_r6 = MathTex(r"M \neq \mathbb{R}^6").next_to(_r6_notation, DOWN, buff=.2).scale(.5)
        self.play(Write(_cartesian_notation_RNZ))
        self.wait(2)
        self.play(Unwrite(_cartesian_notation_RNZ))
        self.wait(2)

        self.play(Write(_cartesian_product_n))
        self.wait(2)
        self.play(Unwrite(_cartesian_product_n))
        self.wait(2)

        self.play(Write(_cartesian_notation_An))
        self.wait(2)
        self.play(Unwrite(_cartesian_notation_An))
        self.wait(2)

        self.play(Write(_matrix_set_M))
        self.wait(1)
        self.play(Write(_r6_notation))
        self.wait(1)
        self.play(Write(_M_not_r6))
        self.wait(1)
        self.play(Unwrite(_cartesian_notation_An))
        self.wait(2)
    
# manim -qk -p set.py CartesianProduct

class Subset(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)  
        self.add(bg_text)   
        # Title
        title = Text("ንኡስ ስብስብ / Subset", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        _subset_defintion_title= MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")
        _subset_defintion_1 = MarkupText("Aን Bን ስብስባት እዮም ንበል። ሕድ ሕድ ባእታ ናይ A ባእታ ናይ B እውን እንተኾይኑ፣ ስብስብ A ንኡስ ስብስብ ናይ B እዩ ንብል።",font_size=30, color=WHITE, font="Nyala")
        _subset_defintion_2_1 = MathTex(r"A \subseteq B", color=ORANGE)
        _subset_defintion_2_2 = MarkupText(" ብዝብል ድማ ነዚ ንገልፆ።",font_size=30, color=WHITE, font="Nyala")
        _subset_defintion_2 = VGroup(_subset_defintion_2_1, _subset_defintion_2_2).arrange(RIGHT)
        _subset_definition_3 = MarkupText("ኹሎም ባእታታት ናይ A፣ ናይ B ባእታታት እውን እንተዘይኾይኖም፣ ብኻልእ ኣባህላ፣ ዋላ ሓደ ናይ A ባእታ ናይ B ባእታ እንተዘይኾኑ፣ ስብስብ A ናይ ስብስብ B ንኡስ ስብስብ ኣይኾነን።",font_size=30, color=WHITE, font="Nyala")
        _subset_defintion_4_1 = MathTex(r"A \not\subseteq B", color=ORANGE)
        _subset_defintion_4_2 = MarkupText(" ብዝብል ድማ ነዚ ንገልፆ።",font_size=30, color=WHITE, font="Nyala")
        _subset_defintion_4 = VGroup(_subset_defintion_4_1, _subset_defintion_4_2).arrange(RIGHT)
        _subset_definition = VGroup(_subset_defintion_title, _subset_defintion_1, _subset_defintion_2, _subset_definition_3, _subset_defintion_4).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).scale(.5)
        
        _subset_defintion_box = SurroundingRectangle(_subset_definition, color=YELLOW, buff=0.4, fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2, stroke_width=1)
        self.add(_subset_defintion_title,
                _subset_defintion_1,
                _subset_defintion_2,
                _subset_definition_3,
                _subset_defintion_4,
                _subset_defintion_box)
        self.wait(4)
        self.play(FadeOut( _subset_definition),FadeOut( _subset_defintion_box))
        self.wait(2)

        lines = [
            r"\{2, 3, 7\} \subseteq \{2, 3, 4, 5, 6, 7\}",
            r"\{2, 3, 7\} \not\subseteq \{2, 4, 5, 6, 7\}",
            r"\{2, 3, 7\} \subseteq \{2, 3, 7\}",
            r"\{(x, \sin(x)) : x \in \mathbb{R}\} \subseteq \mathbb{R}^2",
            r"\{1, 3, 5, 7, 11, 13, 17, \dots\} \subseteq \mathbb{N}",
            r"\mathbb{N} \subseteq \mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R}"
        ]

        # 2. Put them in a VGroup and arrange them
        # We align to the LEFT to match your image
        subset_group = VGroup(*[
            MathTex(line, font_size=36) for line in lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(underline, DOWN, buff=.1).scale(.5)

        # 3. Display them one by one
        for item in subset_group:
            self.play(Write(item), run_time=1)
            self.wait(0.5)

        self.wait(2)
        
        # Now you can fade the whole thing out easily
        self.play(FadeOut(subset_group))
        _empty_set_rule = MathTex(r"\forall A, \emptyset \subseteq A").scale(.5)
        self.play(Write(_empty_set_rule), run_time=1)

        # Specifically for itself
        _empty_set_self = MathTex(r"\emptyset \subseteq \emptyset").next_to(_empty_set_rule, DOWN, buff=.2).scale(.5)
        self.play(Write(_empty_set_self), run_time=1)
        self.wait()
        self.play(FadeOut(_empty_set_rule),FadeOut(_empty_set_self), run_time=1)
        self.wait()
        # 1. Configuration
        elements = ["a", "b", "c"]
        depth = len(elements)
        h_spacing = 4.5
        v_spacing = 5.5
        gap_size = 0.45  # The size of the physical gap for the text
        all_elements = VGroup()

        def get_set_label(subset):
            if not subset: return "\\{ \\}"
            return "\\{ " + ", ".join(subset) + " \\}"

        # Helper to draw a line with a physical hole in the middle
        def draw_broken_line(start, end, label_text):
            mid = (start + end) / 2
            unit_vec = (end - start) / np.linalg.norm(end - start)
            
            # Segment 1: From start to just before the center
            line1 = Line(start, mid - unit_vec * gap_size, stroke_width=1)
            # Segment 2: From just after the center to the end
            line2 = Line(mid + unit_vec * gap_size, end, stroke_width=1)
            
            label = Text(label_text, font_size=20).move_to(mid)
            return VGroup(line1, line2, label)

        # 2. Recursive function to build the tree
        def create_tree(current_set, level, x, y):
            if level > depth:
                leaf = MathTex(get_set_label(current_set), font_size=32)
                leaf.move_to([x, y, 0])
                all_elements.add(leaf)
                return

            next_x = x + h_spacing
            offset = v_spacing / (2 ** level)
            y_up, y_down = y + offset, y - offset

            # --- Create Broken Diagonal Lines ---
            # We calculate the start/end points for the lines
            start_pt = np.array([x + 0.5, y, 0])
            end_up = np.array([next_x - 0.7, y_up, 0])
            end_down = np.array([next_x - 0.7, y_down, 0])

            no_branch = draw_broken_line(start_pt, end_up, "No")
            yes_branch = draw_broken_line(start_pt, end_down, "Yes")

            # --- Vertical Dotted Line ---
            # Connects the "No" and "Yes" text labels
            dotted_line = DashedLine(
                no_branch[2].get_bottom() + DOWN * 0.1, 
                yes_branch[2].get_top() + UP * 0.1,
                color=GRAY_B, stroke_width=1, dash_length=0.1
            )

            # Node Label
            node_label = MathTex(get_set_label(current_set), font_size=32, color=GRAY_A)
            node_label.move_to([x, y, 0])
            
            all_elements.add(no_branch, yes_branch, dotted_line, node_label)

            # Recurse
            create_tree(current_set, level + 1, next_x, y_up)
            create_tree(current_set + [elements[level-1]], level + 1, next_x, y_down)

        # 3. Headers (Elevated)
        headers = VGroup().next_to(underline, DOWN*1.5, buff=.25)
        header_y_pos = 7.0 
        for i, char in enumerate(elements):
            header_x = -4 + (i * h_spacing) + (h_spacing / 2)
            h_text = MathTex(f"\\text{{Insert }}{char}?", font_size=30)
            h_text.move_to([header_x, header_y_pos, 0])
            arrow = Arrow(h_text.get_bottom(), h_text.get_bottom() + DOWN * 1, buff=0.1, stroke_width=2)
            headers.add(h_text, arrow)
        all_elements.add(headers)

        # 4. Generate, Scale, and Center
        create_tree([], 1, -4, 0)
        all_elements.scale(0.45)
        all_elements.move_to(ORIGIN).shift(DOWN*.25)
        _powerset_list = MathTex(
            r"\{\}, \{c\}, \{b\}, \{b, c\}, \{a\}, \{a, c\}, \{a, b\} \text{ and } \{a, b, c\}."
        ).next_to(all_elements, DOWN*.5, buff=.1).scale(.5)
        # 5. Animation
        self.play(FadeIn(all_elements, lag_ratio=0.05), Write(_powerset_list), run_time=2)
        # self.add(all_elements)
        self.wait(2)
        self.play(FadeOut(all_elements), FadeOut(_powerset_list))
        self.wait(2)

        _set_cardinality = MathTex(r'|A| = n').scale(.5)
        _number_of_subsets = MathTex(r" \implies 2^n").next_to(_set_cardinality, RIGHT).scale(.5)
        self.play(Write(_set_cardinality), run_time=.5)
        self.wait()
        self.play(Write(_number_of_subsets), run_time=.5)
        self.wait()
        self.play(FadeOut(_set_cardinality), FadeOut(_number_of_subsets))
        self.wait(2)

        _subset_notation = MathTex(r"A \subseteq B")
        _not_subset = MathTex(r"A \not\subseteq B")
        _power_set = MathTex(r"\mathcal{P}(A)")
        _power_set_cardinality = MathTex(r"|\mathcal{P}(A)| = 2^{|A|}")

# manim -ql -p  set.py Subset



class SetDifference(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)  
        self.add(bg_text)   
        # Title
        title = Text("Difference", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        # 1. Setup Axes
        axes_one = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 6, 1],
            axis_config={"include_tip": True}
        ).add_coordinates()

        axes_two = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 6, 1],
            axis_config={"include_tip": True}
        ).add_coordinates()

        # 2. Define the Parabola (Set B: y = x^2)
        parabola = axes_one.plot(lambda x: x**2, color=BLUE, stroke_width=4)
        line_color = ORANGE
        line = axes_two.plot(lambda x: x + 1, color=line_color, stroke_width=4)
        # 3. Calculate intersection points for B - A
        # Intersection occurs at x^2 = x + 1
        x1 = (1 + np.sqrt(5)) / 2
        x2 = (1 - np.sqrt(5)) / 2
        
        # Create the "Holes" (Open circles)
        # We use Dot with fill_opacity=0 to make it hollow
        holea1 = Dot(
            point=axes_one.c2p(x1, x1**2), 
            radius=0.1, 
            fill_color=BLACK,      # Matches background to "cut" the line
            fill_opacity=1,        # Must be solid to hide the line underneath
            stroke_width=2,        # The thickness of the hole's ring
            stroke_color=BLUE      # Matches the graph color
        )
        
        holea2 = Dot(
            point=axes_one.c2p(x2, x2**2), 
            radius=0.1, 
            fill_color=BLACK, 
            fill_opacity=1, 
            stroke_width=2, 
            stroke_color=BLUE
        )

        holeb1 = Dot(
            point=axes_two.c2p(x1, x1**2), 
            radius=0.1, 
            fill_color=BLACK,      # Matches background to "cut" the line
            fill_opacity=1,        # Must be solid to hide the line underneath
            stroke_width=2,        # The thickness of the hole's ring
            stroke_color=ORANGE      # Matches the graph color
        )
        
        holeb2 = Dot(
            point=axes_two.c2p(x2, x2**2), 
            radius=0.1, 
            fill_color=BLACK, 
            fill_opacity=1, 
            stroke_width=2, 
            stroke_color=ORANGE
        )

        axes_three = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 6, 1],
            axis_config={"include_tip": True}
        ).add_coordinates()

        # 2. Calculate the intersection coordinates (x^2 = x + 1)
        # These are the Golden Ratio points
        phi = (1 + np.sqrt(5)) / 2
        psi = (1 - np.sqrt(5)) / 2
        
        # Define the points in the coordinate system
        # Point 1: (~1.618, ~2.618)
        # Point 2: (~-0.618, ~0.382)
        p1 = axes_three.c2p(phi, phi**2)
        p2 = axes_three.c2p(psi, psi**2)

        # 3. Create the Intersection Set (Solid Dots)
        dot1 = Dot(point=p1, color=RED, radius=0.12)
        dot2 = Dot(point=p2, color=RED, radius=0.12)
        
        # 4. Labels
        # A cap B label
        
    

        # 4. Labels
        # Positioning the label near the upper hole
        label1 = MathTex("B - A").next_to(holea1, RIGHT, buff=0.3)
        label2 = MathTex("A - B").next_to(holeb1, RIGHT, buff=0.3)
        label3 = MathTex("A \\cap B", color=WHITE).scale(1.2).next_to(dot1, RIGHT, buff=0.3)
        

        vgroup= VGroup(axes_one, parabola, holea1, holea2, label1).scale(.25).next_to(underline, DOWN).to_edge(LEFT)
        line_vgroup = VGroup(axes_two,line, holeb1, holeb2, label2).scale(.25).next_to(vgroup, RIGHT, buff=.5)
        n_vgroup = VGroup(axes_three, dot1, dot2, label3).scale(.25).next_to(line_vgroup, RIGHT, buff=.5)
        
        # 5. Animation Sequence
        self.add(vgroup)
        self.add(line_vgroup)
        self.add(n_vgroup)
        self.wait(2)

        lines = [
            r"1. \quad A \cup B = \{a, b, c, d, e, f\}",
            r"2. \quad A \cap B = \{d, e\}",
            r"3. \quad A - B = \{a, b, c\}",
            r"4. \quad B - A = \{f\}",
            r"5. \quad (A - B) \cup (B - A) = \{a, b, c, f\}",
            r"6. \quad A \cup C = \{a, b, c, d, e, 1, 2, 3\}",
            r"7. \quad A \cap C = \emptyset",
            r"8. \quad A - C = \{a, b, c, d, e\}",
            r"9. \quad (A \cap C) \cup (A - C) = \{a, b, c, d, e\}",
            r"10. \quad (A \cap B) \times B = \{(d, d), (d, e), (d, f), (e, d), (e, e), (e, f)\}",
            r"11. \quad (A \times C) \cap (B \times C) = \{(d, 1), (d, 2), (d, 3), (e, 1), (e, 2), (e, 3)\}"
        ]

        # Convert strings to MathTex objects and group them
        set_list = VGroup(*[
            MathTex(line, font_size=32) for line in lines
        ])

        # Arrange them vertically, aligned to the left edge
        set_list.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        # Center the whole group on the screen
        set_list.move_to(ORIGIN)

        # Animation: Write them line by line
        self.play(Write(set_list, run_time=5, lag_ratio=0.5))
        self.wait(2)

        _complement_notation = MathTex(r"\overline{A} = U - A.")

        


# manim -ql -p  set.py SetDifference




class VennDiagram(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)  
        self.add(bg_text)   
        # Title
        title = Text("Difference", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        # 1. Define the Circles
        # Standard layout: C at top, A bottom-left, B bottom-right
        
        circle_a = Circle(radius=2, color=WHITE).shift(LEFT * 1.1 + DOWN * 0.7)
        circle_b = Circle(radius=2, color=WHITE).shift(RIGHT * 1.1 + DOWN * 0.7)
        circle_c = Circle(radius=2, color=WHITE).shift(UP * 1.1)

        # 2. Define the Labels
        label_a = MathTex("A").next_to(circle_a, LEFT + DOWN, buff=0.2)
        label_b = MathTex("B").next_to(circle_b, RIGHT + DOWN, buff=0.2)
        label_c = MathTex("C").next_to(circle_c, UP, buff=0.2)
        
        operation_text = MathTex("(A \\cup B) \\setminus C").to_edge(UP, buff=1)

        # 3. Create the Shaded Region
        # (A Union B) Difference C
        union_ab = Union(circle_a, circle_b)
        shaded_region = Difference(union_ab, circle_c)
        shaded_region.set_fill(BLUE, opacity=0.6)
        shaded_region.set_stroke(width=0)
        vgroupall = VGroup(circle_a, circle_b, circle_c, label_a, 
        label_b, label_c, union_ab, shaded_region)
        vgroupall.next_to(underline, DOWN, buff=0.2).scale(.5)
        # 4. Animation Sequence
        self.play(Write(operation_text))
        self.play(
            Create(circle_a), 
            Create(circle_b), 
            Create(circle_c),
            run_time=2
        )
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(0.5)

        # Show the "Union" first (optional, for clarity)
        # self.play(union_ab.animate.set_fill(BLUE, opacity=0.2)) 
        
        # Final highlight of the set operation
        self.play(FadeIn(shaded_region))
        self.play(shaded_region.animate.set_fill(BLUE, opacity=0.8))
        

        # Circle C at top, A bottom-left, B bottom-right
        c_a = Circle(radius=1.8, color=WHITE).shift(LEFT * 1 + DOWN * 0.6)
        c_b = Circle(radius=1.8, color=WHITE).shift(RIGHT * 1 + DOWN * 0.6)
        c_c = Circle(radius=1.8, color=WHITE).shift(UP * 0.8)
        
        circles = VGroup(c_a, c_b, c_c)
        labels = VGroup(
            MathTex("A").next_to(c_a, LEFT+DOWN, buff=0.1),
            MathTex("B").next_to(c_b, RIGHT+DOWN, buff=0.1),
            MathTex("C").next_to(c_c, UP, buff=0.1)
        )

        # --- 2. FIRST OPERATION: (A U B) ∩ C ---
        title1 = MathTex("(A \\cup B) \\cap C").to_edge(UP)
        
        # Logic: Combine A and B, then find where that union overlaps with C
        union_ab = Union(c_a, c_b)
        shaded1 = Intersection(union_ab, c_c, fill_opacity=0.6, fill_color=YELLOW, stroke_width=0)

        self.play(Write(title1), Create(circles), Write(labels))
        self.play(FadeIn(shaded1))
        self.wait(2)
        
        # Transition to next diagram
        self.play(FadeOut(shaded1), FadeOut(title1))

        # --- 3. SECOND OPERATION: A U (B ∩ C) ---
        title2 = MathTex("A \\cup (B \\cap C)").to_edge(UP)
        
        # Logic: Find the overlap of B and C, then combine that whole area with all of A
        inter_bc = Intersection(c_b, c_c)
        shaded2 = Union(c_a, inter_bc, fill_opacity=0.6, fill_color=PINK, stroke_width=0)

        self.play(Write(title2))
        self.play(FadeIn(shaded2))
        self.wait(3)
        self.wait(3)
# manim -qk -p set.py VennDiagram

class Indexes(ThreeDScene):
    def construct(self):
        # 1. Setup Axes
        axes = ThreeDAxes(
            x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-3, 3, 1],
            x_length=5, y_length=5, z_length=4,
            axis_config={"include_tip": True}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")

        # --- LEFT IMAGE: SINGLE VERTICAL PLANE ---
        # Horizontal Plane (xy-plane)
        xy_plane = Rectangle(width=6, height=6, stroke_width=1, stroke_color=WHITE)
        xy_plane.set_fill(WHITE, opacity=0.1)

        # Vertical Plane (angled)
        # We create a rectangle and rotate it to stand vertically
        v_plane = Rectangle(width=6, height=4, stroke_width=2, stroke_color=LIGHT_PINK)
        v_plane.set_fill(LIGHT_PINK, opacity=0.6)
        v_plane.rotate(90*DEGREES, axis=RIGHT) # Make it vertical
        v_plane.rotate(45*DEGREES, axis=OUT)   # Angle it across the xy-plane

        # Points and Labels
        point_coord = axes.c2p(-2, 1, 0)
        dot = Dot3D(point=point_coord, color=RED)
        dot_label = MathTex("(-2, 1, 0)", font_size=24).next_to(dot, DOWN+LEFT, buff=0.1)
        plane_label = MathTex("P_{(1,2)}", font_size=30).move_to(axes.c2p(-1.5, 1, 2))

        left_group = VGroup(xy_plane, v_plane, axes, labels, dot, dot_label, plane_label).scale(.5)
        left_group.shift(LEFT * 3.5)

        # --- RIGHT IMAGE: PENCIL OF PLANES ---
        axes2 = axes.copy().shift(RIGHT * 3.5)
        
        # Horizontal base
        horiz_base = xy_plane.copy().move_to(axes2.get_center())
        
        # Create multiple vertical planes rotated around the Z-axis
        pencil = VGroup()
        colors = [YELLOW, PINK, LIGHT_BROWN, WHITE]
        for i in range(4):
            p = Rectangle(width=5, height=4, stroke_width=1, stroke_color=WHITE)
            p.set_fill(colors[i % len(colors)], opacity=0.4)
            p.rotate(90*DEGREES, axis=RIGHT) # Vertical
            p.rotate(i * 45 * DEGREES, axis=OUT) # Rotate around Z
            pencil.add(p)
        
        right_group = VGroup(horiz_base, pencil, axes2).shift(RIGHT * 3.5).scale(.5)

        # --- ANIMATION ---
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        # Show Left Diagram
        # self.play(Create(axes), FadeIn(xy_plane))
        # self.play(FadeIn(v_plane), Create(dot), Write(dot_label), Write(plane_label))
        # self.wait(1)
        self.add(left_group, right_group)
        self.wait(1)

        # Show Right Diagram
        # self.play(FadeIn(right_group))
        # self.begin_ambient_camera_rotation(rate=0.1, about="theta") # Slowly rotate to show 3D depth
        # self.move_camera(
        #     theta=-45 * DEGREES + 2 * PI, 
        #     run_time=8, 
        #     rate_func=linear
        # )
        tilted_axis = [1, 1, 1] 
        self.play(
            Rotate(left_group, angle=2*PI, axis=tilted_axis,  about_point=left_group.get_center()),
            Rotate(right_group, angle=2*PI, axis=tilted_axis, about_point=right_group.get_center()),
            run_time=6,
            rate_func=linear
        )
        self.wait(4)
        _union_general = MathTex(
            r"A_1 \cup A_2 \cup A_3 \cup \cdots \cup A_n = \{x : x \in A_i \text{ for at least one set } A_i, \text{ for } 1 \leq i \leq n\},"
        )
        _intersection_general = MathTex(
            r"A_1 \cap A_2 \cap A_3 \cap \cdots \cap A_n = \{x : x \in A_i \text{ for every set } A_i, \text{ for } 1 \leq i \leq n\},"
        )  
        _summation_notation = MathTex(
    r"\sum_{i=1}^{n} a_i = a_1 + a_2 + a_3 + \cdots + a_n."
)
        _infinite_sum = MathTex(
    r"\sum_{i=1}^{\infty} a_i = a_1 + a_2 + a_3 + \cdots + a_i + \cdots"
)
        _indexed_notations = MathTex(
    r"\bigcup_{i=1}^{n} A_i = A_1 \cup A_2 \cup A_3 \cup \cdots \cup A_n",
    r"\text{ and }",
    r"\bigcap_{i=1}^{n} A_i = A_1 \cap A_2 \cap A_3 \cap \cdots \cap A_n"
)
        
        # 1. Row 1: Infinite Union
        row1 = MathTex(
            r"\bigcup_{i=1}^{\infty} A_i = A_1 \cup A_2 \cup A_3 \cup \cdots = \{x : x \in A_i \text{ for at least one set } A_i \text{ with } 1 \leq i \}.",
            font_size=28
        )

        # 2. Row 2: Infinite Intersection
        row2 = MathTex(
            r"\bigcap_{i=1}^{\infty} A_i = A_1 \cap A_2 \cap A_3 \cap \cdots = \{x : x \in A_i \text{ for every set } A_i \text{ with } 1 \leq i \}.",
            font_size=28
        )

        # 3. Create the Vertical Group and Align
        definitions = VGroup(row1, row2).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        # 4. Create the surrounding box (just like the image)
        box = SurroundingRectangle(definitions, color=WHITE, buff=0.4, stroke_width=1)
        
        # Combine into one master group
        full_display = VGroup(definitions, box).move_to(ORIGIN)

        # --- ANIMATION ---
        self.play(Write(row1), run_time=2)
        self.play(Write(row2), run_time=2)
        self.play(Create(box))
        self.wait(3)
# manim -ql -p set.py Indexes

class Test(ThreeDScene):
    def construct(self):
        text = Text("Hello")
        _text_two = Text("Salut").next_to(text, RIGHT*2, buff=.2)
        self.play(Write(text))
        # self.wait()
        # self.play(Unwrite(text))
        # self.wait()
        # self.play(FadeIn(text))
        self.wait(2)
        _text_copy = text.copy()
        self.play(FadeTransform(_text_copy, _text_two, stretch=True))
        self.wait(3)

# manim -ql -p set.py Test


