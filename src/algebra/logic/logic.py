from manim import * 
import manimpango
from common.common import layout

class Introduction(Scene):
    def construct(self):
        
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)        
               
        # Title
        title = Text("መእተዊ / Introduction", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        line_start = -600 
        line_end = 2100
        
        logos_greek = Text("λόγος", color=WHITE)
        equals = Text("≡", color=WHITE)
        logos_tigrigna = Text("ርትዒ / መጎት", color=WHITE, font="Nyala")
        logos = VGroup(logos_greek, equals, logos_tigrigna)
        logos.arrange(RIGHT, buff=0.1)
        line = NumberLine(
            x_range=[line_start, line_end, 100],
            unit_size=.5,
            length=12,
            color=BLUE,
            include_numbers=False,
        )
        
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

        brain = SVGMobject("../../assets/svgs/brain.svg").scale(.6)
        brain.set_color(WHITE)
        discussion = SVGMobject("../../assets/svgs/debate.svg" , color=WHITE)
        discussion.set_color(WHITE)
        think = SVGMobject("../../assets/svgs/science_think.svg", color=WHITE)
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
                
        self.play( Succession(
        *[
            AnimationGroup(
                Indicate(throb, color=RED, scale_factor=1.1),                
                run_time=1
            ) 
            for _ in range(3)
        ]
    )  )
    
        self.wait()
        self.play(FadeOut(brain), FadeOut(starting_group), run_time=.5)
        self.wait()
 # manim -ql -p --disable_caching  logic.py Introduction

class Statement(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)  
        title = Text("ሓሳብ / Proposition", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)
        self.add(title)
        self.add(underline)

        statement_definition_title = MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")       
        statement_definition_1 = MarkupText("ሓሳብ (proposition)፣ ዝኾነ ትርጉም ዘለዎ፣ ንፁርን ዘየሻሚን ሓረግ እዩ።",font_size=30, color=WHITE, font="Nyala")
        statement_definition_2 = MarkupText("እቲ ሓረግ፣ ወይ ሓቂ ወይ ሓሶት ክኾን ይኽእል እዪ። ኣብ ሓደ እዋን ግን፣",font_size=30, color=WHITE, font="Nyala")
        statement_definition_3 = MarkupText("ሓቂን ሓሶትን ክኾን ኣይኽእልን።",font_size=30, color=WHITE, font="Nyala")
        statement_definition = VGroup(statement_definition_title, statement_definition_1, statement_definition_2, statement_definition_3).scale(.7).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).shift(LEFT*1)
        
        statement_box = SurroundingRectangle(statement_definition, color=YELLOW, buff=0.4, fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2, stroke_width=1)
        self.add(statement_definition_title,
                  statement_definition_1,
                  statement_definition_2,
                  statement_definition_3,statement_box)
        self.wait(2)
        
        self.play(FadeOut(statement_definition), FadeOut(statement_box))
        self.wait(2)
        font_size =28
        first_sentence = MarkupText("1. እዙይ ሕብሪ ፃዕዳ እዩ።", font_size=font_size, font="Nyala")
        second_sentence = MarkupText("2. ጠጠው በል!", font_size=font_size, font="Nyala")
        third_sentence = MarkupText("3. ፈጣሪ ይሓግዝካ!", font_size=font_size, font="Nyala")
        fourth_sentence = MarkupText("4. ናበይ ትኸይድ ኣለኻ?", font_size=font_size, font="Nyala")

        BulletedList = VGroup(first_sentence, second_sentence, third_sentence, fourth_sentence)
        BulletedList.arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(underline, DOWN, buff=0.5)
        self.play(Write(first_sentence))
        self.wait() 
        self.play(Write(second_sentence))
        self.wait()
        self.play(Write(third_sentence))
        self.wait()
        self.play(Write(fourth_sentence))
        self.wait(2)

        box_one = SurroundingRectangle(first_sentence, color=YELLOW, buff=.1, stroke_width=1)        
        self.play(Create(box_one))
        self.wait(2)

        self.play(FadeOut(BulletedList), FadeOut(box_one))
        self.wait(2)     
       

        open_statement_definition_title = MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")       
        open_statement_definition_1 = MarkupText("ኽፉት ሓሳብ(open proposition)፣ ሓደ ወይ ልዕሊ ሓደ ተለዋወጥቲ ወይ ተውላጠ-ስማት ዝሓዘ ሓረግ ኮይኑ፣",font_size=30, color=WHITE, font="Nyala")
        open_statement_definition_2 = MarkupText("ሕድ ሕድ ተለዋዋጢ ወይ ተውላጠ-ስም ብፍሉይ ዋጋ ወይ ብውልቀ-ሰብ ምስ ዝትካእ፣ ሓሳብ ይኸውን።",font_size=30, color=WHITE, font="Nyala")
        
        open_statement_definition = VGroup(open_statement_definition_title, open_statement_definition_1, 
                                           open_statement_definition_2 ).scale(.7).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).shift(LEFT*1)
        
        open_statement_box = SurroundingRectangle(open_statement_definition, color=YELLOW, buff=0.4, fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2, stroke_width=1)
        self.add(open_statement_definition_title,
                  open_statement_definition_1,
                  open_statement_definition_2,                 
                  open_statement_box)
        self.wait(1)
        self.play(FadeOut(open_statement_definition), FadeOut(open_statement_box))
        self.wait(1)
        
        x = MarkupText(
            "ሀ",
            font_size=30, font="Nyala"
        )
        x_rest = MarkupText(
            "- 3 = 6",
            font_size=30, font="Nyala"
        )  

        he = MarkupText(
            "እሱ",
            font_size=30, font="Nyala"
        )
        he_rest = MarkupText(
            "መምህር እዩ።",
            font_size=30, font="Nyala"
        )              
       
        x_statement = VGroup(x, x_rest).arrange(RIGHT, buff=0.1)
        he_statement = VGroup(he, he_rest).arrange(RIGHT, buff=0.1)
        variables = VGroup(x_statement, he_statement).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(underline, DOWN, buff=0.5)
        self.play(Write(x_statement))
        self.wait()
        self.play(Write(he_statement))
        self.wait(2)

        x_box = SurroundingRectangle(x, color=RED, buff=0.05, stroke_width= 1)        
        self.play(Create(x_box))
        self.wait(2)
        he_box = SurroundingRectangle(he, color=RED, buff=0.05,  stroke_width= 1)        
        self.play(Create(he_box))
        self.wait(2)
        self.play(FadeOut(variables), FadeOut(x_box), FadeOut(he_box))
        self.wait(2)      


class Propositions(Scene):
    def construct(self):        
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)        
               
        # Title
        title = Text("ዓይነታት ሓሳባት / Types of Propositions ", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
       
        simple_statement_definition_title = MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")       
        simple_statement_definition_1 = MarkupText("simple proposition (ቐሊል ሓሳብ) ከም <span fgcolor='YELLOW'>and (ከምኡ እውን)</span> ፡ <span fgcolor='YELLOW'>or (ወይ)</span> ፡ <span fgcolor='YELLOW'>not (ኣይኰነን)</span>፡ ወዘተ...",font_size=30, color=WHITE, font="Nyala")
        simple_statement_definition_2 = MarkupText("ዝኣመሰሉ ጠመርቲ ቃላት ዘይብሉ፣ ሓደ ሓሳብ ዘመሓላልፍ ሓረግ እዩ።",font_size=30, color=WHITE, font="Nyala")        
        simple_statement_definition = VGroup(simple_statement_definition_title, simple_statement_definition_1, simple_statement_definition_2).scale(.5).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).shift(LEFT*1)
        
        simple_box = SurroundingRectangle(simple_statement_definition, color=YELLOW, buff=0.4, 
                                          fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2
                                          ,stroke_width= 1)
        self.add(simple_statement_definition_title,
                  simple_statement_definition_1,
                  simple_statement_definition_2,
                  simple_box)
        self.wait(2)
        
        first_statement = MarkupText(
            "ሀ. መቐለ ርእሰ ከተማ ትግራይ እያ።",
            font_size=30, font="Nyala"
        )
        second_statement = MarkupText(
            "ለ. ወለደ ኣብርሃ ንጉስ፣ ብሉፅ ፖለቲከኛ ትግራይ እዩ።",
            font_size=30, font="Nyala"
        )  
        
        simple_sentences = VGroup(first_statement, second_statement).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(simple_statement_definition, DOWN*2, buff=0.5).scale(.5)    
        self.play(FadeIn(first_statement))
        self.wait(2)

        self.play(FadeIn(second_statement))
        self.wait(2)   
        self.play(FadeOut(simple_sentences), FadeOut(simple_statement_definition), FadeOut(simple_box))   
        self.wait(2)

        
        compound_statement_definition_title = MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")       
        compound_statement_definition_1 = MarkupText("ክልተ ወይ ልዕሊኡ ቀለልቲ ሓሳባት ብመልክዕ ሓደ ሓረግ እንትግለፁ፣ compound (ውሁድ) ሓሳብ ይፈጥሩ።",font_size=30, color=WHITE, font="Nyala")
        compound_statement_definition = VGroup(compound_statement_definition_title, compound_statement_definition_1).scale(.5).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).shift(LEFT*1)
        
        compound_box = SurroundingRectangle(compound_statement_definition, color=YELLOW, buff=0.4, 
                                            fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2,
                                             stroke_width= 1)
        self.add(compound_statement_definition_title,
                  compound_statement_definition_1,                  
                  compound_box)
        self.wait(2)
        self.wait(2)
        text_a = MarkupText("ሀ. ", font_size=30, font="Nyala")
        text_b = MarkupText("ለ. ", font_size=30, font="Nyala")
        third_statement_1 = MarkupText("√1 = 1", font_size=30)
        third_statement_2 = MarkupText(
            " ከምኡውን",
            font_size=30, font="Nyala"
        )
        third_statement_3 = MarkupText(
            " <span font_family='Sans' font_size='30'>3 &lt; 4</span> እዩ።",
            font_size=30, font="Nyala"
        )
        fourth_statement_1 = MarkupText(
            "ድሕሪ ሰሉስ ዘሎ መዓልቲ ረቡዕ",
            font_size=30, font="Nyala"
        ) 
        fourth_statement_2 = MarkupText(
            " ወይ",
            font_size=30, font="Nyala"
        )  
        fourth_statement_3 = MarkupText(
            " 2 + 2 = 4 እዩ።",
            font_size=30, font="Nyala"
        )   
        third_statement =VGroup(text_a, third_statement_1, third_statement_2, third_statement_3).arrange(RIGHT)
        fourth_statement =VGroup(text_b, fourth_statement_1, fourth_statement_2, fourth_statement_3).arrange(RIGHT)
        compound_sentences = VGroup(third_statement, fourth_statement).arrange(DOWN*2, aligned_edge=LEFT, buff=0.5).scale(.5).next_to(compound_statement_definition, DOWN*2, buff=0.5)      
        self.play(FadeIn(text_a),FadeIn(third_statement_1), FadeIn(third_statement_2), FadeIn(third_statement_3))
        self.wait(2)
       
        underline_third_statement_1 = Line(LEFT*third_statement_1.width/2, RIGHT*third_statement_1.width/2, stroke_width=1, color=YELLOW)
        underline_third_statement_1.next_to(third_statement_1, DOWN, buff=0.1)
        self.play(FadeIn(underline_third_statement_1))
        self.wait(2)
       
        underline_third_statement_3 = Line(LEFT*third_statement_3.width/2, RIGHT*third_statement_3.width/2, stroke_width=1, color=ORANGE)
        underline_third_statement_3.next_to(third_statement_3, UP, buff=0.1)
        self.play(Create(underline_third_statement_3))
        self.wait(2)
       
        third_box = SurroundingRectangle(third_statement_2, color=RED, buff=.05, stroke_width= 1)        
        self.play(Create(third_box))
        
        self.wait(2)
        self.play(FadeIn(text_b),FadeIn(fourth_statement_1), FadeIn(fourth_statement_2), FadeIn(fourth_statement_3))
        self.wait(2) 
        
        underline_fourth_statement_1 = Line(LEFT*fourth_statement_1.width/2, RIGHT*fourth_statement_1.width/2, stroke_width=1, color=YELLOW)
        underline_fourth_statement_1.next_to(fourth_statement_1, DOWN, buff=0.1)
        self.play(Create(underline_fourth_statement_1))
        self.wait(2)
       
        underline_fourth_statement_3 = Line(LEFT*fourth_statement_3.width/2, RIGHT*fourth_statement_3.width/2, stroke_width=1, color=ORANGE)
        underline_fourth_statement_3.next_to(fourth_statement_3, UP, buff=0.1)
        self.play(Create(underline_fourth_statement_3))
        self.wait(2)
                
        fourth_box = SurroundingRectangle(fourth_statement_2, color=RED, buff=.05, stroke_width= 1)        
        self.play(Create(fourth_box))
        self.wait(2)
        self.play(FadeOut(compound_sentences), FadeOut(compound_statement_definition), 
                  FadeOut(compound_box), FadeOut(third_box), 
                  FadeOut(fourth_box), FadeOut(underline_third_statement_1), 
                  FadeOut(underline_third_statement_3), 
                  FadeOut(underline_fourth_statement_1), FadeOut(underline_fourth_statement_3))
        self.wait(2)
        n_propositions = MarkupText("n" , font_size=30)
        two_n = MathTex(r"2^n", font_size=30)
        imply = MarkupText(" → " , font_size=30)
        logical_possibilities = VGroup(n_propositions, imply, two_n)
        logical_possibilities.arrange(RIGHT, buff=0.5).next_to(underline, DOWN, buff=0.5)
        self.play(Write(n_propositions))
        self.wait() 
        self.play(Write(imply),Write(two_n))
        self.wait()
        example_one = MathTex(r"p, q: p \land q = 2^2 = 4", font_size=30)
        example_two = MathTex(r"p, q, r: (p \land q) \land r = 2^3 = 8", font_size=30)
        example= VGroup(example_one, example_two).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(logical_possibilities, DOWN, buff=0.5)
        self.play(Write(example_one))
        self.wait() 
        self.play(Write(example_two))
        self.wait()
        self.play(FadeOut(example), FadeOut(logical_possibilities))
        self.wait(2)
# manim -ql -p --disable_caching logic.py Propositions

class Connectives(Scene):
    def construct(self):        
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)        
               
        # Title
        title = Text("መጥመርቲ / Connectives", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        font_size =28
        negation = MarkupText("1. ኣንፃር / Negation", font_size=font_size, font="Nyala")
        conjunction = MarkupText("2. መስተፃምር / Conjunction", font_size=font_size, font="Nyala")
        disjunction = MarkupText("3. ፍልያ / Disjunction", font_size=font_size, font="Nyala")
        implication = MarkupText("4. ዝተኣመተ / Implication", font_size=font_size, font="Nyala")
        biImplication = MarkupText("5. ድርብ ዝተኣመተ / Bi-implication", font_size=font_size, font="Nyala")

        BulletedList = VGroup(negation, conjunction, disjunction, implication, biImplication)
        BulletedList.arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(underline, DOWN, buff=0.5)
        self.play(Write(negation))
        self.wait() 
        self.play(Write(conjunction))
        self.wait()
        self.play(Write(disjunction))
        self.wait()
        self.play(Write(implication))
        self.wait(2)
        self.play(Write(biImplication))
        self.wait(2)
        self.play(FadeOut(BulletedList))
        self.wait(2)
# manim -ql -p --disable_caching logic.py Connectives


class Negation(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)        
               
        # Title
        title = Text("ኣንፃር / Negation", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        
        negation_definition_title = MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")
       
        negation_definition_1 = MarkupText("p ዝባሃል ሓሳብ እንተልዩ፣ <span fgcolor='ORANGE'>¬p</span> ናይ p ኣንፃር ምልክት እዩ።",font_size=30, color=WHITE, font="Nyala")
        negation_definition_2 = MarkupText("'p ኣይኾነን እዩ' ዝብል ሓሳብ ኢልና ንገልፆ።",font_size=30, color=WHITE, font="Nyala")
        
        negation_definition = VGroup(negation_definition_title, negation_definition_1, negation_definition_2).scale(.7).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).shift(LEFT*1)
        
        box = SurroundingRectangle(negation_definition, color=YELLOW, buff=0.4, 
                                          fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2
                                          ,stroke_width= 1)
        self.add(negation_definition_title,
                  negation_definition_1,
                  negation_definition_2,
                  box)
        self.wait(2)
        font_size =28
        ex_one = MarkupText("P = እቲ ቤተ መፃሕፍቲ ሕዚ ኽፉት እዩ።", font_size=font_size, font="Nyala")
        ex_one_not = MarkupText("¬P = እቲ ቤተ መፃሕፍቲ ሕዚ ኽፉት ኣይኾነን እዩ።", font_size=font_size, font="Nyala")
        ex = VGroup(ex_one, ex_one_not)
        ex.arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(negation_definition, DOWN*2, buff=0.5)

        self.play(FadeIn(ex_one))
        self.wait(1) 
        self.play(FadeIn(ex_one_not))
        self.wait(1)
        self.play(FadeOut(ex), FadeOut(negation_definition), FadeOut(box))
        self.wait(1)
        # Table content
        headers = ["p", "¬p"]
        table_data = [
            ["T", "F"],
            ["F", "T"],            
        ]

        # Create table object without MathTex
        table = Table(
            table_data,
            col_labels=[Text(h) for h in headers],  # Use Text here
            include_outer_lines=False,
        )            
        table.scale(.7).center()
        # Get each column as a VGroup
        first_col = VGroup(table.get_columns()[0], table.get_col_labels()[0])
        second_col = VGroup(table.get_columns()[1], table.get_col_labels()[1])
        # Add to scene
        
        # Hide all columns initially
        for col in [first_col, second_col]:
            col.set_opacity(0)
        
        self.add(table)
        self.play(first_col[1].animate.set_opacity(1))
        self.wait(0.3)
        self.play(second_col[1].animate.set_opacity(1))
        self.wait(0.3)
    
        for cell in first_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)
            
        self.wait(1)
        
        for cell in second_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)
            
        self.wait(1) 
        self.play(table.animate.set_opacity(0)) 
        self.wait(1)

# manim -ql -p --disable_caching logic.py Negation

class Conjunction(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)        
               
        # Title
        title = Text("መስተፃምር / Conjunction", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        self.wait(2)
        conjunction_definition_title = MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")
       
        conjunction_definition_1 = MarkupText("pን qን ዝባሃሉ ክልተ ሓሳባት እንተልዮም፣ pን qን ክልቲኦም ሓቂ እንተኾይኖም ጥራሕ እዩ፣ ",font_size=30, color=WHITE, font="Nyala")
        conjunction_definition_2 = MarkupText("ናይ pን qን መስተፃምር / conjunction ሓቂ ዝኾን።",font_size=30, color=WHITE, font="Nyala")
        conjunction_definition_3 = MarkupText("ምልክቱ ድማ፣ <span font_family='Sans' fgcolor='ORANGE'>p ∧ q</span> እዩ።",font_size=30, color=WHITE, font="Nyala")
        conjunction_definition = VGroup(conjunction_definition_title, conjunction_definition_1, conjunction_definition_2, conjunction_definition_3).scale(.5).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).shift(LEFT*1)
        
        box = SurroundingRectangle(conjunction_definition, color=YELLOW, buff=0.4, fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2, stroke_width=1)
        self.add(conjunction_definition_title,
                  conjunction_definition_1,
                  conjunction_definition_2,
                  conjunction_definition_3,box)
        self.wait()
       
        self.play(FadeOut(conjunction_definition),FadeOut(box))
        self.wait()
        # Table content
        headers = ["p", "q", "p ∧ q"]
        table_data = [
            ["T", "T", "T"],
            ["T", "F", "F"],
            ["F", "T", "F"],
            ["F", "F", "F"],          
        ]

        # Create table object without MathTex
        table = Table(
            table_data,
            col_labels=[Text(h) for h in headers],  # Use Text here
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        )            
        table.scale(.5).next_to(underline, DOWN, buff=0.5).center()
        # Get each column as a VGroup
        first_col = VGroup(table.get_columns()[0], table.get_col_labels()[0])
        second_col = VGroup(table.get_columns()[1], table.get_col_labels()[1])
        third_col = VGroup(table.get_columns()[2], table.get_col_labels()[2])
        # Add to scene
        
        # Hide all columns initially
        for col in [first_col, second_col,third_col]:
            col.set_opacity(0)
        
        self.add(table)
        self.play(first_col[1].animate.set_opacity(1))
        self.wait(.5)
        self.play(second_col[1].animate.set_opacity(1))
        self.wait(.5)
        self.play(third_col[1].animate.set_opacity(1))
        self.wait(.5)
    
        for cell in first_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(.5)
        
        for cell in second_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(.5) 

        for cell in third_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(.5)

        self.play(table.animate.set_opacity(0)) 
        self.wait(2)

# manim -ql -p --disable_caching logic.py Conjunction

class Disjunction(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)        
               
        # Title
        title = Text("ፍልያ / Disjunction", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        self.wait(2)
        disjunction_definition_title = MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")        
        disjunction_definition_1 = MarkupText("pን qን ዝባሃሉ ክልተ ሓሳባት እንተልዮም፣ pን qን ክልቲኦም ሓሶት እንተኾይኖም ጥራሕ እዩ፣ ",font_size=30, color=WHITE, font="Nyala")
        disjunction_definition_2 = MarkupText("ናይ pን qን ፍልያ / disjunction ሓሶት ዝኾን።",font_size=30, color=WHITE, font="Nyala")
        disjunction_definition_3 = MarkupText("ምልክቱ ድማ፣ <span font_family='Sans' fgcolor='ORANGE'>p ∨ q</span> እዩ።",font_size=30, color=WHITE, font="Nyala")
        disjunction_definition = VGroup(disjunction_definition_title, disjunction_definition_1, disjunction_definition_2, disjunction_definition_3).scale(.5).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).shift(LEFT*1)
        
        box = SurroundingRectangle(disjunction_definition, color=YELLOW, buff=0.4, fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2, stroke_width=1)
        self.add(disjunction_definition_title,
                  disjunction_definition_1,
                  disjunction_definition_2,
                  disjunction_definition_3,box)
        self.wait(2)
       
        self.play(FadeOut(disjunction_definition),FadeOut(box))
        self.wait(2)
        # Table content
        headers = ["p", "q", "p ∨ q"]
        table_data = [
            ["T", "T", "T"],
            ["T", "F", "T"],
            ["F", "T", "T"],
            ["F", "F", "F"],          
        ]

        # Create table object without MathTex
        table = Table(
            table_data,
            col_labels=[Text(h) for h in headers],  # Use Text here
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        )            
        table.scale(.5).next_to(underline, DOWN, buff=0.5).center()
        # Get each column as a VGroup
        first_col = VGroup(table.get_columns()[0], table.get_col_labels()[0])
        second_col = VGroup(table.get_columns()[1], table.get_col_labels()[1])
        third_col = VGroup(table.get_columns()[2], table.get_col_labels()[2])
        # Add to scene
        
        # Hide all columns initially
        for col in [first_col, second_col,third_col]:
            col.set_opacity(0)
        
        self.add(table)
        self.play(first_col[1].animate.set_opacity(1))
        self.wait()
        self.play(second_col[1].animate.set_opacity(1))
        self.wait()
        self.play(third_col[1].animate.set_opacity(1))
        self.wait()
    
        for cell in first_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait()
        
        for cell in second_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait() 

        for cell in third_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait()

        self.play(table.animate.set_opacity(0)) 
        self.wait(2)

# manim -ql -p --disable_caching logic.py Disjunction


class Implication(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)        
               
        # Title
        title = Text("ዝተኣመተ / Implication", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        self.wait(2)
        implication_definition_title = MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")       
        implication_definition_1 = MarkupText("pን qን ዝባሃሉ ክልተ ሓሳባት እንተልዮም፣ p ሓቂ ን q ሓሶት ን እንተኾይኖም ጥራሕ እዩ፣ ",font_size=30, color=WHITE, font="Nyala")
        implication_definition_2 = MarkupText("ናይ pን qን ዝተኣመተ / Implication ሓሶት ዝኾን።",font_size=30, color=WHITE, font="Nyala")
        implication_definition_3 = MarkupText("ምልክቱ ድማ፣ <span font_family='Sans' fgcolor='ORANGE'>p → q</span> እዩ።",font_size=30, color=WHITE, font="Nyala")
        implication_definition = VGroup(implication_definition_title, implication_definition_1, implication_definition_2, implication_definition_3).scale(.5).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).shift(LEFT*1)
        
        box = SurroundingRectangle(implication_definition, color=YELLOW, buff=0.4, fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2, stroke_width=1)
        self.add(implication_definition_title,
                  implication_definition_1,
                  implication_definition_2,
                  implication_definition_3,box)
        self.wait(2)
       
        self.play(FadeOut(implication_definition),FadeOut(box))
        self.wait(2)
        # Table content
        headers = ["p", "q", "p → q"]
        table_data = [
            ["T", "T", "T"],
            ["T", "F", "F"],
            ["F", "T", "T"],
            ["F", "F", "T"],          
        ]

        # Create table object without MathTex
        table = Table(
            table_data,
            col_labels=[Text(h) for h in headers],  # Use Text here
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        )            
        table.scale(.5).next_to(underline, DOWN, buff=0.5).center()
        # Get each column as a VGroup
        first_col = VGroup(table.get_columns()[0], table.get_col_labels()[0])
        second_col = VGroup(table.get_columns()[1], table.get_col_labels()[1])
        third_col = VGroup(table.get_columns()[2], table.get_col_labels()[2])
        # Add to scene
        
        # Hide all columns initially
        for col in [first_col, second_col,third_col]:
            col.set_opacity(0)
        
        self.add(table)
        self.play(first_col[1].animate.set_opacity(1))
        self.wait()
        self.play(second_col[1].animate.set_opacity(1))
        self.wait()
        self.play(third_col[1].animate.set_opacity(1))
        self.wait()
    
        for cell in first_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(.5)
        
        for cell in second_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(.5) 

        for cell in third_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(.5)

        self.play(table.animate.set_opacity(0)) 
        self.wait(1)
        implication_explanation = MarkupText("p → q",font_size=30, color=WHITE)
        antecedent = MarkupText("<span font_family='Sans'>p =</span> ቅድመ ፍጻመ <span font_family='Sans'>/ antecedent</span>",font_size=30, color=WHITE, font="Nyala")
        consequent = MarkupText("<span font_family='Sans'>q =</span> ዝስዕብ <span font_family='Sans'>/ consequent</span>",font_size=30, color=WHITE, font="Nyala")
        antecedent_consequent = VGroup(implication_explanation,antecedent, consequent)
        antecedent_consequent.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(implication_explanation), run_time=.5)
        self.wait(.5)
        self.play(Write(antecedent), run_time=.5)
        self.wait(.5)
        self.play(Write(consequent), run_time=.5)
        self.wait(.5)
        self.play(FadeOut(antecedent_consequent), run_time=.5)

        example_line_one = Text("p = 2 < -2",font_size=30, color=WHITE)
        example_line_two = Text("p = 4 > 1",font_size=30, color=WHITE)
        example_line_three = Text("p → q  ≡ T",font_size=30, color=WHITE)

        example = VGroup(example_line_one,example_line_two, example_line_three)
        example.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(example_line_one), run_time=.5)
        self.wait(.5)
        self.play(Write(example_line_two), run_time=.5)
        self.wait(.5)
        self.play(Write(example_line_three), run_time=.5)
        self.wait(.5)
        self.play(FadeOut(example), run_time=.5)

             
        note_implication = MarkupText("p → q",font_size=30, color=WHITE)
        note_converse = MarkupText("q → p = Converse ",font_size=30, color=WHITE)
        note_inverse = MarkupText("¬p → ¬q = Inverse",font_size=30, color=WHITE)
        note_contrapositive = MarkupText("¬q → ¬p = Contrapositive ",font_size=30, color=WHITE)
        note_definition = VGroup(note_implication, note_converse, note_inverse,note_contrapositive )

        note_definition.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(note_implication), run_time=.5)
        self.wait(.5)
        self.play(Write(note_converse), run_time=.5)
        self.wait(.5)
        self.play(Write(note_inverse), run_time=.5)
        self.wait(.5)
        self.play(Write(note_contrapositive), run_time=.5)
        self.wait(.5)
        self.play(FadeOut(note_definition))
        self.wait(2)

# manim -ql -p --disable_caching logic.py Implication

class BiImplication(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)        
               
        # Title
        title = Text("ድርብ ዝተኣመተ / Bi-Implication", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        self.wait(2)
        biImplication_definition_title = MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")       
        biImplication_definition_1 = MarkupText("pን qን ዝባሃሉ ክልተ ሓሳባት እንተልዮም፣ pን qን ክልቲኦም ሓቂ እንተኾይኖም ወይ ክልቲኦም ሓሶት እንተኾይኖም ጥራሕ እዩ፣ ",font_size=30, color=WHITE, font="Nyala")
        biImplication_definition_2 = MarkupText("ናይ pን qን ድርብ ዝተኣመተ / bi-implication ሓቂ ዝኾን።",font_size=30, color=WHITE, font="Nyala")
        biImplication_definition_3 = MarkupText("ምልክቱ ድማ፣ <span font_family='Sans' fgcolor='ORANGE'>p ↔ q</span> እዩ።",font_size=30, color=WHITE, font="Nyala")
        biImplication_definition = VGroup(biImplication_definition_title, biImplication_definition_1, biImplication_definition_2, biImplication_definition_3).scale(.5).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).shift(LEFT*1)
        
        box = SurroundingRectangle(biImplication_definition, color=YELLOW, buff=0.4, fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2, stroke_width=1)
        self.add(biImplication_definition_title,
                  biImplication_definition_1,
                  biImplication_definition_2,
                  biImplication_definition_3,box)
        self.wait(1)
       
        self.play(FadeOut(biImplication_definition),FadeOut(box))
        self.wait(1)
        # Table content
        headers = ["p", "q", "p ↔ q"]
        table_data = [
            ["T", "T", "T"],
            ["T", "F", "F"],
            ["F", "T", "F"],
            ["F", "F", "T"],          
        ]

        # Create table object without MathTex
        table = Table(
            table_data,
            col_labels=[Text(h) for h in headers],  # Use Text here
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        )            
        table.scale(.5).next_to(underline, DOWN, buff=0.5).center()
        # Get each column as a VGroup
        first_col = VGroup(table.get_columns()[0], table.get_col_labels()[0])
        second_col = VGroup(table.get_columns()[1], table.get_col_labels()[1])
        third_col = VGroup(table.get_columns()[2], table.get_col_labels()[2])
        # Add to scene
        
        # Hide all columns initially
        for col in [first_col, second_col,third_col]:
            col.set_opacity(0)
        
        self.add(table)
        self.play(first_col[1].animate.set_opacity(1))
        self.wait()
        self.play(second_col[1].animate.set_opacity(1))
        self.wait()
        self.play(third_col[1].animate.set_opacity(1))
        self.wait()
    
        for cell in first_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(.5)
        
        for cell in second_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(.5) 

        for cell in third_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(.5)

        self.play(table.animate.set_opacity(0)) 
        self.wait(1)

# manim -ql -p --disable_caching logic.py BiImplication

class TautologyAndContradiction(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)        
               
        # Title
        title = Text("ህውላለ ወ ግርጭት / Tautology and Contradiction", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        self.wait(2)
        tautology_definition_title = MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")
       
        tautology_definition_1 = MarkupText("ሓቅነት ዝተደረኸሎም ቀለልቲ ሓሳባት ብዝየገደስ፣ ሓደ ውህድ ሓሳብ ኩሉ ሻዕ ሓቂ እንተኾይኑ፣",font_size=30, color=WHITE, font="Nyala")
        tautology_definition_2 = MarkupText("እዙይ ሓሳብ ህውላለ / tautology ይባሃል። ምልክቱ ድማ፣ <span font_family='Sans' fgcolor='ORANGE'>t</span> እዩ።",font_size=30, color=WHITE, font="Nyala")
        tautology_definition = VGroup(tautology_definition_title, tautology_definition_1, tautology_definition_2).scale(.5).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).shift(LEFT*1)
        
        tautology_box = SurroundingRectangle(tautology_definition, color=YELLOW, buff=0.4, fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2, stroke_width=1)
        self.add(tautology_definition_title,
                  tautology_definition_1,
                  tautology_definition_2,
                  tautology_box)
        self.wait(2)
       
        self.play(FadeOut(tautology_definition),FadeOut(tautology_box))
        self.wait(2)
        # Table content
        tautology_headers = ["p", "¬p", "p ∨ ¬p"]
        tautology_table_data = [
            ["T", "F", "T"],
            ["F", "T", "T"],
                     
        ]

        # Create table object without MathTex
        tautology_table = Table(
            tautology_table_data,
            col_labels=[Text(h) for h in tautology_headers],  # Use Text here
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        )            
        tautology_table.scale(.5).next_to(underline, DOWN, buff=0.5).center()
        # Get each column as a VGroup
        tautology_first_col = VGroup(tautology_table.get_columns()[0], tautology_table.get_col_labels()[0])
        tautology_second_col = VGroup(tautology_table.get_columns()[1], tautology_table.get_col_labels()[1])
        tautology_third_col = VGroup(tautology_table.get_columns()[2], tautology_table.get_col_labels()[2])
        # Add to scene
        
        # Hide all columns initially
        for col in [tautology_first_col, tautology_second_col,tautology_third_col]:
            col.set_opacity(0)
        
        self.add(tautology_table)
        self.play(tautology_first_col[1].animate.set_opacity(1))
        self.wait(1)
        self.play(tautology_second_col[1].animate.set_opacity(1))
        self.wait(1)
        self.play(tautology_third_col[1].animate.set_opacity(1))
        self.wait(1)
    
        for cell in tautology_first_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(2)
        
        for cell in tautology_second_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(2) 

        for cell in tautology_third_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(2)

        self.play(tautology_table.animate.set_opacity(0)) 
        self.wait(2)
        
        self.play(FadeOut(tautology_table))
        self.wait(2)
        contradiction_definition_title = MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")
       
        contradiction_definition_1 = MarkupText("ሓቅነት ዝተደረኸሎም ቀለልቲ ሓሳባት ብዝየገደስ፣ ሓደ ውህድ ሓሳብ ኩሉ ሻዕ ሓሶት እንተኾይኑ፣ ",font_size=30, color=WHITE, font="Nyala")
        contradiction_definition_2 = MarkupText("እዙይ ሓሳብ ግርጭት / contradiction ይባሃል። ምልክቱ ድማ፣ <span font_family='Sans' fgcolor='ORANGE'>c</span> እዩ።",font_size=30, color=WHITE, font="Nyala")
        contradiction_definition = VGroup(contradiction_definition_title, contradiction_definition_1, contradiction_definition_2).scale(.5).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).shift(LEFT*1)
        
        contradiction_box = SurroundingRectangle(contradiction_definition, color=YELLOW, buff=0.4, fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2, stroke_width=1)
        self.add(contradiction_definition_title,
                  contradiction_definition_1,
                  contradiction_definition_2,
                  contradiction_box)
        self.wait(2)
       
        self.play(FadeOut(contradiction_definition),FadeOut(contradiction_box))
        self.wait(2)
        # Table content
        contradiction_headers = ["p", "¬p", "p ∧ ¬p"]
        contradiction_table_data = [
            ["T", "F", "F"],
            ["F", "T", "F"],
                     
        ]
      
        # Create table object without MathTex
        contradiction_table = Table(
            contradiction_table_data,
            col_labels=[Text(h) for h in contradiction_headers],  # Use Text here
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        )            
        contradiction_table.scale(.5).next_to(underline, DOWN, buff=0.5).center()
        # Get each column as a VGroup
        contradiction_first_col = VGroup(contradiction_table.get_columns()[0], contradiction_table.get_col_labels()[0])
        contradiction_second_col = VGroup(contradiction_table.get_columns()[1], contradiction_table.get_col_labels()[1])
        contradiction_third_col = VGroup(contradiction_table.get_columns()[2], contradiction_table.get_col_labels()[2])
        # Add to scene
        
        # Hide all columns initially
        for col in [contradiction_first_col, contradiction_second_col,contradiction_third_col]:
            col.set_opacity(0)
        
        self.add(contradiction_table)
        self.play(contradiction_first_col[1].animate.set_opacity(1))
        self.wait(1)
        self.play(contradiction_second_col[1].animate.set_opacity(1))
        self.wait(1)
        self.play(contradiction_third_col[1].animate.set_opacity(1))
        self.wait(1)
    
        for cell in contradiction_first_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(2)
        
        for cell in contradiction_second_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(2) 

        for cell in contradiction_third_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(2)

        self.play(contradiction_table.animate.set_opacity(0)) 
        self.wait(2)


# manim -ql -p --disable_caching logic.py TautologyAndContradiction

class Equivalence(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)        
               
        # Title
        title = Text("ስነ-መጐታዊ መዓርነት / Logical Equivalence", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        self.wait(2)
        equivalence_definition_title = MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")
       
        equivalence_definition_1 = MarkupText("ክልተ ሓደ ዓይነት ባእታ ሓሳብ ዘጠቓልሉ ሓሳባት ተመሳሳሊ ናይ ሓቂ ሰደቓታት እንተሃልይዎም፣ ስነ-መጐታዊ ማዕረ እዮም ይበሃል።",font_size=30, color=WHITE, font="Nyala")
        equivalence_definition_2 = MarkupText("ናይ እዙይ ስነ-መጐታዊ መዓርነት ምልክት ድማ <span font_family='Sans' fgcolor='ORANGE'>≡</span> እዩ።",font_size=30, color=WHITE, font="Nyala")
        
        equivalence_definition = VGroup(equivalence_definition_title, equivalence_definition_1, equivalence_definition_2).scale(.5).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).shift(LEFT*1)
        
        box = SurroundingRectangle(equivalence_definition, color=YELLOW, buff=0.4, fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2, stroke_width=1)
        self.add(equivalence_definition_title,
                 equivalence_definition_1,
                  equivalence_definition_2,
                 box)
        self.wait(2)       
        self.play(FadeOut(equivalence_definition),FadeOut(box))
        self.wait(2)
        font_size =20
        commutative = Text("1. Commutative law: p ∧ q  ≡ q ∧ p", font_size=font_size)
        associative = Text("2. Associative law: (p ∧ q) ∧ r ≡ p ∧ (q ∧ r)", font_size=font_size)
        distributive = Text("3. Distributive law: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)", font_size=font_size)
        identity = Text("4. Identity law: p ∧ t ≡ p", font_size=font_size)
        negation = Text("5. Negation law: p ∧ ¬p ≡ c", font_size=font_size)
        doubleNegation = Text("6. Double Negation law: ¬(¬p) ≡ p ", font_size=font_size)
        idempotent = Text("7. Idempotent law:  p ∧ p ≡ p", font_size=font_size)
        deMorgan = Text("8. De Morgan's law: ¬(p ∧ q) ≡ ¬p ∨ ¬q", font_size=font_size)
        universal = Text("9. Universal bound law: p ∨ t ≡ t", font_size=font_size)
        absorption = Text("10. Absorption law: p ∧ (p ∨ q) ≡ p", font_size=font_size)
        tandc = Text("11. Negations of t and c:  ¬t ≡ c", font_size=font_size)

        BulletedList = VGroup(commutative, associative, distributive, identity, negation, doubleNegation,
                               idempotent, deMorgan, universal, absorption, tandc)
        BulletedList.arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(underline, DOWN, buff=0.25)
        
        BulletedList.generate_target()        
        BulletedList.target.shift(4.5*LEFT).scale(0.6)
        self.play(FadeIn(commutative))
        self.wait(2) 
        self.play(FadeIn(associative))
        self.wait(2)
        self.play(FadeIn(distributive))
        self.wait(2)
        self.play(FadeIn(identity))
        self.wait(2)
        self.play(FadeIn(negation))
        self.wait(2)
        self.play(FadeIn(doubleNegation))
        self.wait(2)
        self.play(FadeIn(idempotent))
        self.wait(2)
        self.play(FadeIn(deMorgan))
        self.wait(2)
        self.play(FadeIn(universal))
        self.wait(2)
        self.play(FadeIn(absorption))
        self.wait(2)
        self.play(FadeIn(tandc))
        self.wait(2)   
       
        box = SurroundingRectangle(BulletedList.target, color=YELLOW, buff=0.4, fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2, stroke_width=1)        
       
        box.add_updater(lambda b: b.become(
            SurroundingRectangle(
                BulletedList,
                color=YELLOW,
                buff=0.4,
                fill_color=ORANGE,
                fill_opacity=0.05,
                corner_radius=0.2,
                stroke_width=1
            )
        ))

        self.add(box)
        self.play(
            MoveToTarget(BulletedList),
            run_time=1
        )

        box.remove_updater(box.updaters[0])
        self.wait(1)
        HORIZONTAL_OFFSET =  RIGHT
        '''
        # Commutative law: p ∧ q  ≡ q ∧ p
        commutative_title = Text("Commutative law: p ∧ q  ≡ q ∧ p", font_size=font_size + 8)
        commutative_underline = Line(LEFT*commutative_title.width/2, RIGHT*commutative_title.width/2, stroke_width=1, color=WHITE)
        commutative_underline.next_to(commutative_title, DOWN, buff=0.2)        	

        commutative_bullet_underline = Line(LEFT*commutative.width/2, RIGHT*commutative.width/2, stroke_width=1, color=YELLOW)
        commutative_bullet_underline.next_to(commutative, DOWN, buff=0.1)
        commutative_table = Table(
            [ ["T", "T", "T", "T"],
            ["T", "F", "F", "F"],
            ["F", "T", "F", "F"],
            ["F", "F", "F", "F"]],           
            col_labels=[Text("P"), Text("q"), Text("p ∧ q"), Text("q ∧ p")],
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        ).scale(0.5).next_to(commutative_underline, DOWN*1.5, buff=0.5)

        commutative_group = VGroup(commutative_title, commutative_underline, commutative_table)
        commutative_group.arrange(DOWN, aligned_edge=LEFT, buff=0.20).scale(0.6).next_to(box, RIGHT*3) 
        commutative_group.align_to(box, UP)
         
          # or any vector             
       
        self.add(commutative_title, commutative_underline, commutative_bullet_underline)
       
        self.wait(.5)
        self.play(FadeIn(commutative_table), run_time=.5)
        self.wait(.5)
       
        commutative_row1_col0_content = SurroundingRectangle(commutative_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        commutative_row1_col1_content = SurroundingRectangle(commutative_table.get_entries((2, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        commutative_row1_col2_content = SurroundingRectangle(commutative_table.get_entries((2, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        commutative_row1_col3_content = SurroundingRectangle(commutative_table.get_entries((2, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        self.play(Create(commutative_row1_col0_content), run_time=.5)
        self.play(Create(commutative_row1_col1_content),run_time=.5)
        self.play(Create(commutative_row1_col2_content), run_time=.5)
        self.play( Create(commutative_row1_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(commutative_row1_col0_content), FadeOut(commutative_row1_col1_content),
                          FadeOut(commutative_row1_col2_content), FadeOut(commutative_row1_col3_content), run_time=.5)
        self.wait(.5)
        commutative_row2_col0_content = SurroundingRectangle(commutative_table.get_entries((3, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        commutative_row2_col1_content = SurroundingRectangle(commutative_table.get_entries((3, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        commutative_row2_col2_content = SurroundingRectangle(commutative_table.get_entries((3, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        commutative_row2_col3_content = SurroundingRectangle(commutative_table.get_entries((3, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(commutative_row2_col0_content), run_time=.5)
        self.play(Create(commutative_row2_col1_content),run_time=.5)
        self.play(Create(commutative_row2_col2_content), run_time=.5)
        self.play( Create(commutative_row2_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(commutative_row2_col0_content), FadeOut(commutative_row2_col1_content),
                          FadeOut(commutative_row2_col2_content), FadeOut(commutative_row2_col3_content), run_time=.5)
        self.wait(.5)

        commutative_row3_col0_content = SurroundingRectangle(commutative_table.get_entries((4, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        commutative_row3_col1_content = SurroundingRectangle(commutative_table.get_entries((4, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        commutative_row3_col2_content = SurroundingRectangle(commutative_table.get_entries((4, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        commutative_row3_col3_content = SurroundingRectangle(commutative_table.get_entries((4, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(commutative_row3_col0_content), run_time=.5)
        self.play(Create(commutative_row3_col1_content),run_time=.5)
        self.play(Create(commutative_row3_col2_content), run_time=.5)
        self.play( Create(commutative_row3_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(commutative_row3_col0_content), FadeOut(commutative_row3_col1_content),
                          FadeOut(commutative_row3_col2_content), FadeOut(commutative_row3_col3_content), run_time=.5)
        self.wait(.5)

        commutative_row4_col0_content = SurroundingRectangle(commutative_table.get_entries((5, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        commutative_row4_col1_content = SurroundingRectangle(commutative_table.get_entries((5, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        commutative_row4_col2_content = SurroundingRectangle(commutative_table.get_entries((5, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        commutative_row4_col3_content = SurroundingRectangle(commutative_table.get_entries((5, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(commutative_row4_col0_content), run_time=.5)
        self.play(Create(commutative_row4_col1_content),run_time=.5)
        self.play(Create(commutative_row4_col2_content), run_time=.5)
        self.play( Create(commutative_row4_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(commutative_row4_col0_content), FadeOut(commutative_row4_col1_content),
                          FadeOut(commutative_row4_col2_content), FadeOut(commutative_row4_col3_content), run_time=.5)
        self.wait(.5)
        commutative_col3 = SurroundingRectangle(commutative_table.get_columns()[2][1:], color=RED, buff=0.05,fill_color=ORANGE, fill_opacity=0.075, stroke_width= 1)
        commutative_col4 = SurroundingRectangle(commutative_table.get_columns()[3][1:], color=RED, buff=0.05, fill_color=ORANGE, fill_opacity=0.075, stroke_width= 1)
        self.add(commutative_col3, commutative_col4)
        self.wait(.5)
        self.play(FadeOut(commutative_group), FadeOut(commutative_col3), FadeOut(commutative_col4),  FadeOut(commutative_bullet_underline), run_time=.5)
        self.wait(1)
         
              
		# Associative law: (p ∧ q) ∧ r ≡ p ∧ (q ∧ r)
        associative_title = Text("Associative laws: (p ∧ q) ∧ r ≡ p ∧ (q ∧ r)", font_size=font_size + 8)
        associative_underline = Line(LEFT*associative_title.width/2, RIGHT*associative_title.width/2, stroke_width=1, color=WHITE)
        associative_underline.next_to(associative_title, DOWN, buff=0.2)        	

        associative_bullet_underline = Line(LEFT*associative.width/2, RIGHT*associative.width/2, stroke_width=1, color=YELLOW)
        associative_bullet_underline.next_to(associative, DOWN, buff=0.1)
        # associative_headers = ["p", "q","r", "p ∧ q","q ∧ r", "(p ∧ q) ∧ r", "p ∧ (q ∧ r)"]
        associative_table = Table(
            [["T", "T", "T", "T", "T", "T", "T"],
            ["T", "T", "F", "T", "F", "F", "F"],
            ["T", "F", "T", "F", "F", "F", "F"],
            ["T", "F", "F", "F", "F", "F", "F"],
			["F", "T", "T", "F", "T", "F", "F"],
            ["F", "T", "F", "F", "F", "F", "F"],
            ["F", "F", "T", "F", "F", "F", "F"],
            ["F", "F", "F", "F", "F", "F", "F"]],           
            col_labels=[Text("P"), Text("q"), Text("r"), Text("p ∧ q"), Text("q ∧ r"), Text("(p ∧ q) ∧ r"), Text("p ∧ (q ∧ r)")],
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        ).scale(0.5).next_to(associative_underline, DOWN*1.5, buff=0.5)

        associative_group = VGroup(associative_title, associative_underline, associative_table)
        associative_group.arrange(DOWN, aligned_edge=LEFT, buff=0.20).scale(0.6).next_to(box, RIGHT*3) 
        associative_group.align_to(box, UP)     
        self.add(associative_title, associative_underline, associative_bullet_underline)
        # self.add(associative_title, associative_underline)
       
        self.wait(.5)
        self.play(FadeIn(associative_table), run_time=.5)
        self.wait(.5)
        # p ∧ q
        associative_row1_col0_content = SurroundingRectangle(associative_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row1_col1_content = SurroundingRectangle(associative_table.get_entries((2, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row1_col3_content = SurroundingRectangle(associative_table.get_entries((2, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(associative_row1_col0_content), run_time=.5)
        self.play(Create(associative_row1_col1_content),run_time=.5)        
        self.play(Create(associative_row1_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row1_col0_content), FadeOut(associative_row1_col1_content), FadeOut(associative_row1_col3_content), run_time=.5)
        self.wait(.5)

        associative_row2_col0_content = SurroundingRectangle(associative_table.get_entries((3, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row2_col1_content = SurroundingRectangle(associative_table.get_entries((3, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row2_col3_content = SurroundingRectangle(associative_table.get_entries((3, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(associative_row2_col0_content), run_time=.5)
        self.play(Create(associative_row2_col1_content),run_time=.5)        
        self.play(Create(associative_row2_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row2_col0_content), FadeOut(associative_row2_col1_content),FadeOut(associative_row2_col3_content), run_time=.5)
        self.wait(.5)

        associative_row3_col0_content = SurroundingRectangle(associative_table.get_entries((4, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row3_col1_content = SurroundingRectangle(associative_table.get_entries((4, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        associative_row3_col3_content = SurroundingRectangle(associative_table.get_entries((4, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row3_col0_content), run_time=.5)
        self.play(Create(associative_row3_col1_content),run_time=.5)        
        self.play(Create(associative_row3_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row3_col0_content), FadeOut(associative_row3_col1_content), FadeOut(associative_row3_col3_content), run_time=.5)
        self.wait(.5)

        associative_row4_col0_content = SurroundingRectangle(associative_table.get_entries((5, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row4_col1_content = SurroundingRectangle(associative_table.get_entries((5, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        associative_row4_col3_content = SurroundingRectangle(associative_table.get_entries((5, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row4_col0_content), run_time=.5)
        self.play(Create(associative_row4_col1_content),run_time=.5)        
        self.play(Create(associative_row4_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row4_col0_content), FadeOut(associative_row4_col1_content), FadeOut(associative_row4_col3_content), run_time=.5)        
        self.wait(.5)

        associative_row5_col0_content = SurroundingRectangle(associative_table.get_entries((6, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row5_col1_content = SurroundingRectangle(associative_table.get_entries((6, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        associative_row5_col3_content = SurroundingRectangle(associative_table.get_entries((6, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row5_col0_content), run_time=.5)
        self.play(Create(associative_row5_col1_content),run_time=.5)        
        self.play(Create(associative_row5_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row5_col0_content), FadeOut(associative_row5_col1_content), FadeOut(associative_row5_col3_content), run_time=.5)
        self.wait(.5)

        associative_row6_col0_content = SurroundingRectangle(associative_table.get_entries((7, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row6_col1_content = SurroundingRectangle(associative_table.get_entries((7, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        associative_row6_col3_content = SurroundingRectangle(associative_table.get_entries((7, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row6_col0_content), run_time=.5)
        self.play(Create(associative_row6_col1_content),run_time=.5)       
        self.play(Create(associative_row6_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row6_col0_content), FadeOut(associative_row6_col1_content), FadeOut(associative_row6_col3_content), run_time=.5)
        self.wait(.5)

        associative_row7_col0_content = SurroundingRectangle(associative_table.get_entries((8, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row7_col1_content = SurroundingRectangle(associative_table.get_entries((8, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        associative_row7_col3_content = SurroundingRectangle(associative_table.get_entries((8, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row7_col0_content), run_time=.5)
        self.play(Create(associative_row7_col1_content),run_time=.5)       
        self.play(Create(associative_row7_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row7_col0_content), FadeOut(associative_row7_col1_content), FadeOut(associative_row7_col3_content), run_time=.5)
        self.wait(.5)

        associative_row8_col0_content = SurroundingRectangle(associative_table.get_entries((9, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row8_col1_content = SurroundingRectangle(associative_table.get_entries((9, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        associative_row8_col3_content = SurroundingRectangle(associative_table.get_entries((9, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row8_col0_content), run_time=.5)
        self.play(Create(associative_row8_col1_content),run_time=.5)        
        self.play(Create(associative_row8_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row8_col0_content), FadeOut(associative_row8_col1_content), FadeOut(associative_row8_col3_content), run_time=.5)
        self.wait(.5)

        # q ∧ r
        associative_row1_col2_content = SurroundingRectangle(associative_table.get_entries((2, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row1_col3_content = SurroundingRectangle(associative_table.get_entries((2, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row1_col5_content = SurroundingRectangle(associative_table.get_entries((2, 5)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(associative_row1_col2_content), run_time=.5)
        self.play(Create(associative_row1_col3_content),run_time=.5)        
        self.play(Create(associative_row1_col5_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row1_col2_content), FadeOut(associative_row1_col3_content), FadeOut(associative_row1_col5_content), run_time=.5)
        self.wait(.5)

        associative_row2_col2_content = SurroundingRectangle(associative_table.get_entries((3, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row2_col3_content = SurroundingRectangle(associative_table.get_entries((3, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row2_col5_content = SurroundingRectangle(associative_table.get_entries((3, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1) 
        self.play(Create(associative_row2_col2_content), run_time=.5)
        self.play(Create(associative_row2_col3_content),run_time=.5)        
        self.play(Create(associative_row2_col5_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row2_col2_content), FadeOut(associative_row2_col3_content),FadeOut(associative_row2_col5_content), run_time=.5)
        self.wait(.5)

        associative_row3_col2_content = SurroundingRectangle(associative_table.get_entries((4, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row3_col3_content = SurroundingRectangle(associative_table.get_entries((4, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        associative_row3_col5_content = SurroundingRectangle(associative_table.get_entries((4, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row3_col2_content), run_time=.5)
        self.play(Create(associative_row3_col3_content),run_time=.5)        
        self.play(Create(associative_row3_col5_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row3_col2_content), FadeOut(associative_row3_col3_content), FadeOut(associative_row3_col5_content), run_time=.5)
        self.wait(.5)

        associative_row4_col2_content = SurroundingRectangle(associative_table.get_entries((5, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row4_col3_content = SurroundingRectangle(associative_table.get_entries((5, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        associative_row4_col5_content = SurroundingRectangle(associative_table.get_entries((5, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row4_col2_content), run_time=.5)
        self.play(Create(associative_row4_col3_content),run_time=.5)        
        self.play(Create(associative_row4_col5_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row4_col2_content), FadeOut(associative_row4_col3_content), FadeOut(associative_row4_col5_content), run_time=.5)        
        self.wait(.5)

        associative_row5_col2_content = SurroundingRectangle(associative_table.get_entries((6, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row5_col3_content = SurroundingRectangle(associative_table.get_entries((6, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        associative_row5_col5_content = SurroundingRectangle(associative_table.get_entries((6, 5)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row5_col2_content), run_time=.5)
        self.play(Create(associative_row5_col3_content),run_time=.5)        
        self.play(Create(associative_row5_col5_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row5_col2_content), FadeOut(associative_row5_col3_content), FadeOut(associative_row5_col5_content), run_time=.5)
        self.wait(.5)

        associative_row6_col2_content = SurroundingRectangle(associative_table.get_entries((7, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row6_col3_content = SurroundingRectangle(associative_table.get_entries((7, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        associative_row6_col5_content = SurroundingRectangle(associative_table.get_entries((7, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row6_col2_content), run_time=.5)
        self.play(Create(associative_row6_col3_content),run_time=.5)       
        self.play(Create(associative_row6_col5_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row6_col2_content), FadeOut(associative_row6_col3_content), FadeOut(associative_row6_col5_content), run_time=.5)
        self.wait(.5)

        associative_row7_col2_content = SurroundingRectangle(associative_table.get_entries((8, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row7_col3_content = SurroundingRectangle(associative_table.get_entries((8, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        associative_row7_col5_content = SurroundingRectangle(associative_table.get_entries((8, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row7_col2_content), run_time=.5)
        self.play(Create(associative_row7_col3_content),run_time=.5)       
        self.play(Create(associative_row7_col5_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row7_col2_content), FadeOut(associative_row7_col3_content), FadeOut(associative_row7_col5_content), run_time=.5)
        self.wait(.5)

        associative_row8_col2_content = SurroundingRectangle(associative_table.get_entries((9, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row8_col3_content = SurroundingRectangle(associative_table.get_entries((9, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        associative_row8_col5_content = SurroundingRectangle(associative_table.get_entries((9, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row8_col2_content), run_time=.5)
        self.play(Create(associative_row8_col3_content),run_time=.5)        
        self.play(Create(associative_row8_col5_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row8_col2_content), FadeOut(associative_row8_col3_content), FadeOut(associative_row8_col5_content), run_time=.5)
        self.wait(.5)

         # (p ∧ q) ∧ r
        associative_row1_col4_content = SurroundingRectangle(associative_table.get_entries((2, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row1_col3_content = SurroundingRectangle(associative_table.get_entries((2, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row1_col6_content = SurroundingRectangle(associative_table.get_entries((2, 6)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(associative_row1_col4_content), run_time=.5)
        self.play(Create(associative_row1_col3_content),run_time=.5)        
        self.play(Create(associative_row1_col6_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row1_col4_content), FadeOut(associative_row1_col3_content), FadeOut(associative_row1_col6_content), run_time=.5)
        self.wait(.5)

        associative_row2_col4_content = SurroundingRectangle(associative_table.get_entries((3, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row2_col3_content = SurroundingRectangle(associative_table.get_entries((3, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row2_col6_content = SurroundingRectangle(associative_table.get_entries((3, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1) 
        self.play(Create(associative_row2_col4_content), run_time=.5)
        self.play(Create(associative_row2_col3_content),run_time=.5)        
        self.play(Create(associative_row2_col6_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row2_col4_content), FadeOut(associative_row2_col3_content),FadeOut(associative_row2_col6_content), run_time=.5)
        self.wait(.5)

        associative_row3_col4_content = SurroundingRectangle(associative_table.get_entries((4, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row3_col3_content = SurroundingRectangle(associative_table.get_entries((4, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        associative_row3_col6_content = SurroundingRectangle(associative_table.get_entries((4, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row3_col4_content), run_time=.5)
        self.play(Create(associative_row3_col3_content),run_time=.5)        
        self.play(Create(associative_row3_col6_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row3_col4_content), FadeOut(associative_row3_col3_content), FadeOut(associative_row3_col6_content), run_time=.5)
        self.wait(.5)

        associative_row4_col4_content = SurroundingRectangle(associative_table.get_entries((5, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row4_col3_content = SurroundingRectangle(associative_table.get_entries((5, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        associative_row4_col6_content = SurroundingRectangle(associative_table.get_entries((5, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row4_col4_content), run_time=.5)
        self.play(Create(associative_row4_col3_content),run_time=.5)        
        self.play(Create(associative_row4_col6_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row4_col4_content), FadeOut(associative_row4_col3_content), FadeOut(associative_row4_col6_content), run_time=.5)        
        self.wait(.5)

        associative_row5_col4_content = SurroundingRectangle(associative_table.get_entries((6, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row5_col3_content = SurroundingRectangle(associative_table.get_entries((6, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        associative_row5_col6_content = SurroundingRectangle(associative_table.get_entries((6, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row5_col4_content), run_time=.5)
        self.play(Create(associative_row5_col3_content),run_time=.5)        
        self.play(Create(associative_row5_col6_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row5_col4_content), FadeOut(associative_row5_col3_content), FadeOut(associative_row5_col6_content), run_time=.5)
        self.wait(.5)

        associative_row6_col4_content = SurroundingRectangle(associative_table.get_entries((7, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row6_col3_content = SurroundingRectangle(associative_table.get_entries((7, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        associative_row6_col6_content = SurroundingRectangle(associative_table.get_entries((7, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row6_col4_content), run_time=.5)
        self.play(Create(associative_row6_col3_content),run_time=.5)       
        self.play(Create(associative_row6_col6_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row6_col4_content), FadeOut(associative_row6_col3_content), FadeOut(associative_row6_col6_content), run_time=.5)
        self.wait(.5)

        associative_row7_col4_content = SurroundingRectangle(associative_table.get_entries((8, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row7_col3_content = SurroundingRectangle(associative_table.get_entries((8, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        associative_row7_col6_content = SurroundingRectangle(associative_table.get_entries((8, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row7_col4_content), run_time=.5)
        self.play(Create(associative_row7_col3_content),run_time=.5)       
        self.play(Create(associative_row7_col6_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row7_col4_content), FadeOut(associative_row7_col3_content), FadeOut(associative_row7_col6_content), run_time=.5)
        self.wait(.5)

        associative_row8_col4_content = SurroundingRectangle(associative_table.get_entries((9, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row8_col3_content = SurroundingRectangle(associative_table.get_entries((9, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        associative_row8_col6_content = SurroundingRectangle(associative_table.get_entries((9, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row8_col4_content), run_time=.5)
        self.play(Create(associative_row8_col3_content),run_time=.5)        
        self.play(Create(associative_row8_col6_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row8_col4_content), FadeOut(associative_row8_col3_content), FadeOut(associative_row8_col6_content), run_time=.5)
        self.wait(.5)

        # p ∧ (q ∧ r)

        associative_row1_col1_content = SurroundingRectangle(associative_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row1_col5_content = SurroundingRectangle(associative_table.get_entries((2, 5)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row1_col7_content = SurroundingRectangle(associative_table.get_entries((2, 7)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(associative_row1_col1_content), run_time=.5)
        self.play(Create(associative_row1_col5_content),run_time=.5)        
        self.play(Create(associative_row1_col7_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row1_col1_content), FadeOut(associative_row1_col5_content), FadeOut(associative_row1_col7_content), run_time=.5)
        self.wait(.5)

        associative_row2_col1_content = SurroundingRectangle(associative_table.get_entries((3, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row2_col5_content = SurroundingRectangle(associative_table.get_entries((3, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row2_col7_content = SurroundingRectangle(associative_table.get_entries((3, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1) 
        self.play(Create(associative_row2_col1_content), run_time=.5)
        self.play(Create(associative_row2_col5_content),run_time=.5)        
        self.play(Create(associative_row2_col7_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row2_col1_content), FadeOut(associative_row2_col5_content),FadeOut(associative_row2_col7_content), run_time=.5)
        self.wait(.5)

        associative_row3_col1_content = SurroundingRectangle(associative_table.get_entries((4, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row3_col5_content = SurroundingRectangle(associative_table.get_entries((4, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        associative_row3_col7_content = SurroundingRectangle(associative_table.get_entries((4, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row3_col1_content), run_time=.5)
        self.play(Create(associative_row3_col5_content),run_time=.5)        
        self.play(Create(associative_row3_col7_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row3_col1_content), FadeOut(associative_row3_col5_content), FadeOut(associative_row3_col7_content), run_time=.5)
        self.wait(.5)

        associative_row4_col1_content = SurroundingRectangle(associative_table.get_entries((5, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        associative_row4_col5_content = SurroundingRectangle(associative_table.get_entries((5, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        associative_row4_col7_content = SurroundingRectangle(associative_table.get_entries((5, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row4_col1_content), run_time=.5)
        self.play(Create(associative_row4_col5_content),run_time=.5)        
        self.play(Create(associative_row4_col7_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row4_col1_content), FadeOut(associative_row4_col5_content), FadeOut(associative_row4_col7_content), run_time=.5)        
        self.wait(.5)

        associative_row5_col1_content = SurroundingRectangle(associative_table.get_entries((6, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row5_col5_content = SurroundingRectangle(associative_table.get_entries((6, 5)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        associative_row5_col7_content = SurroundingRectangle(associative_table.get_entries((6, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row5_col1_content), run_time=.5)
        self.play(Create(associative_row5_col5_content),run_time=.5)        
        self.play(Create(associative_row5_col7_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row5_col1_content), FadeOut(associative_row5_col5_content), FadeOut(associative_row5_col7_content), run_time=.5)
        self.wait(.5)

        associative_row6_col1_content = SurroundingRectangle(associative_table.get_entries((7, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row6_col5_content = SurroundingRectangle(associative_table.get_entries((7, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        associative_row6_col7_content = SurroundingRectangle(associative_table.get_entries((7, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row6_col1_content), run_time=.5)
        self.play(Create(associative_row6_col5_content),run_time=.5)       
        self.play(Create(associative_row6_col7_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row6_col1_content), FadeOut(associative_row6_col5_content), FadeOut(associative_row6_col7_content), run_time=.5)
        self.wait(.5)

        associative_row7_col1_content = SurroundingRectangle(associative_table.get_entries((8, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row7_col5_content = SurroundingRectangle(associative_table.get_entries((8, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        associative_row7_col7_content = SurroundingRectangle(associative_table.get_entries((8, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row7_col1_content), run_time=.5)
        self.play(Create(associative_row7_col5_content),run_time=.5)       
        self.play(Create(associative_row7_col7_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row7_col1_content), FadeOut(associative_row7_col5_content), FadeOut(associative_row7_col7_content), run_time=.5)
        self.wait(.5)

        associative_row8_col1_content = SurroundingRectangle(associative_table.get_entries((9, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        associative_row8_col5_content = SurroundingRectangle(associative_table.get_entries((9, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        associative_row8_col7_content = SurroundingRectangle(associative_table.get_entries((9, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(associative_row8_col1_content), run_time=.5)
        self.play(Create(associative_row8_col5_content),run_time=.5)        
        self.play(Create(associative_row8_col7_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(associative_row8_col1_content), FadeOut(associative_row8_col5_content), FadeOut(associative_row8_col7_content), run_time=.5)
        self.wait(.5)
        
        associative_col5 = SurroundingRectangle(associative_table.get_columns()[5][1:], color=RED, buff=0.05,fill_color=ORANGE, fill_opacity=0.075,   stroke_width= 1)
        associative_col6 = SurroundingRectangle(associative_table.get_columns()[6][1:], color=RED, buff=0.05,fill_color=ORANGE, fill_opacity=0.075,   stroke_width= 1)
        self.add(associative_col5, associative_col6)
        self.wait(.5)
        self.play(FadeOut(associative_group), FadeOut(associative_col5), FadeOut(associative_col6),  FadeOut(associative_bullet_underline), run_time=.5)
        
        self.wait(1)

          

        # Distributive law: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)
        distributive_title = Text("Distributive laws: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r) ", font_size=font_size + 8)
        distributive_underline = Line(LEFT*distributive_title.width/2, RIGHT*distributive_title.width/2, stroke_width=1, color=WHITE)
        distributive_underline.next_to(distributive_title, DOWN, buff=0.2)        	

        distributive_bullet_underline = Line(LEFT*distributive.width/2, RIGHT*distributive.width/2, stroke_width=1, color=YELLOW)
        distributive_bullet_underline.next_to(distributive, DOWN, buff=0.1)
        distributive_headers = ["p","q","r", "q ∨ r","p ∧ q", "(p ∧ r)", "p ∧ (q ∨ r)", "(p ∧ q) ∨ (p ∧ r)"]
        distributive_table = Table(
            [["T", "T", "T", "T", "T", "T", "T", "T"],
            ["T", "T", "F", "T", "T", "F", "T", "T"],
            ["T", "F", "T", "T", "F", "T", "T", "T"],
            ["T", "F", "F", "F", "F", "F", "F", "F"],
            ["F", "T", "T", "T", "F", "F", "F", "F"],
            ["F", "T", "F", "T", "F", "F", "F", "F"],
            ["F", "F", "T", "T", "F", "F", "F", "F"],
            ["F", "F", "F", "F", "F", "F", "F", "F"]],           
            col_labels=[Text("P"), Text("q"), Text("r"),Text("q ∨ r"), Text("p ∧ q"), Text("p ∧ r"), Text("p ∧ (q ∨ r)"), Text("(p ∧ q) ∨ (p ∧ r)")],
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        ).scale(0.5).next_to(distributive_underline, DOWN, buff=0.5)

        distributive_group = VGroup(distributive_title, distributive_underline, distributive_table)
        distributive_group.arrange(DOWN, aligned_edge=LEFT, buff=0.20).scale(0.6).next_to(box, RIGHT*3) 
        distributive_group.align_to(box, UP) 
       
        self.add(distributive_title, distributive_underline, distributive_bullet_underline)        
       
        self.wait(.5)
        self.play(FadeIn(distributive_table), run_time=.5)
        self.wait(.5)

        # q ∨ r

        distributive_row1_col0_content = SurroundingRectangle(distributive_table.get_entries((2, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col1_content = SurroundingRectangle(distributive_table.get_entries((2, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col3_content = SurroundingRectangle(distributive_table.get_entries((2, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row1_col0_content), run_time=.5)
        self.play(Create(distributive_row1_col1_content),run_time=.5)        
        self.play(Create(distributive_row1_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row1_col0_content), FadeOut(distributive_row1_col1_content), FadeOut(distributive_row1_col3_content), run_time=.5)
        self.wait(.5)

        distributive_row2_col0_content = SurroundingRectangle(distributive_table.get_entries((3, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row2_col1_content = SurroundingRectangle(distributive_table.get_entries((3, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row2_col3_content = SurroundingRectangle(distributive_table.get_entries((3, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row2_col0_content), run_time=.5)
        self.play(Create(distributive_row2_col1_content),run_time=.5)        
        self.play(Create(distributive_row2_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row2_col0_content), FadeOut(distributive_row2_col1_content),FadeOut(distributive_row2_col3_content), run_time=.5)
        self.wait(.5)

        distributive_row3_col0_content = SurroundingRectangle(distributive_table.get_entries((4, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row3_col1_content = SurroundingRectangle(distributive_table.get_entries((4, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row3_col3_content = SurroundingRectangle(distributive_table.get_entries((4, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row3_col0_content), run_time=.5)
        self.play(Create(distributive_row3_col1_content),run_time=.5)        
        self.play(Create(distributive_row3_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row3_col0_content), FadeOut(distributive_row3_col1_content), FadeOut(distributive_row3_col3_content), run_time=.5)
        self.wait(.5)

        distributive_row4_col0_content = SurroundingRectangle(distributive_table.get_entries((5, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row4_col1_content = SurroundingRectangle(distributive_table.get_entries((5, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row4_col3_content = SurroundingRectangle(distributive_table.get_entries((5, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row4_col0_content), run_time=.5)
        self.play(Create(distributive_row4_col1_content),run_time=.5)        
        self.play(Create(distributive_row4_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row4_col0_content), FadeOut(distributive_row4_col1_content), FadeOut(distributive_row4_col3_content), run_time=.5)        
        self.wait(.5)

        distributive_row5_col0_content = SurroundingRectangle(distributive_table.get_entries((6, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row5_col1_content = SurroundingRectangle(distributive_table.get_entries((6, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row5_col3_content = SurroundingRectangle(distributive_table.get_entries((6, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row5_col0_content), run_time=.5)
        self.play(Create(distributive_row5_col1_content),run_time=.5)        
        self.play(Create(distributive_row5_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row5_col0_content), FadeOut(distributive_row5_col1_content), FadeOut(distributive_row5_col3_content), run_time=.5)
        self.wait(.5)

        distributive_row6_col0_content = SurroundingRectangle(distributive_table.get_entries((7, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row6_col1_content = SurroundingRectangle(distributive_table.get_entries((7, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row6_col3_content = SurroundingRectangle(distributive_table.get_entries((7, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row6_col0_content), run_time=.5)
        self.play(Create(distributive_row6_col1_content),run_time=.5)       
        self.play(Create(distributive_row6_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row6_col0_content), FadeOut(distributive_row6_col1_content), FadeOut(distributive_row6_col3_content), run_time=.5)
        self.wait(.5)

        distributive_row7_col0_content = SurroundingRectangle(distributive_table.get_entries((8, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row7_col1_content = SurroundingRectangle(distributive_table.get_entries((8, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row7_col3_content = SurroundingRectangle(distributive_table.get_entries((8, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row7_col0_content), run_time=.5)
        self.play(Create(distributive_row7_col1_content),run_time=.5)       
        self.play(Create(distributive_row7_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row7_col0_content), FadeOut(distributive_row7_col1_content), FadeOut(distributive_row7_col3_content), run_time=.5)
        self.wait(.5)

        distributive_row8_col0_content = SurroundingRectangle(distributive_table.get_entries((9, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row8_col1_content = SurroundingRectangle(distributive_table.get_entries((9, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row8_col3_content = SurroundingRectangle(distributive_table.get_entries((9, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row8_col0_content), run_time=.5)
        self.play(Create(distributive_row8_col1_content),run_time=.5)        
        self.play(Create(distributive_row8_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row8_col0_content), FadeOut(distributive_row8_col1_content), FadeOut(distributive_row8_col3_content), run_time=.5)
        self.wait(.5)

        # p ∧ q
        distributive_row1_col0_content = SurroundingRectangle(distributive_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col1_content = SurroundingRectangle(distributive_table.get_entries((2, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col3_content = SurroundingRectangle(distributive_table.get_entries((2, 5)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row1_col0_content), run_time=.5)
        self.play(Create(distributive_row1_col1_content),run_time=.5)        
        self.play(Create(distributive_row1_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row1_col0_content), FadeOut(distributive_row1_col1_content), FadeOut(distributive_row1_col3_content), run_time=.5)
        self.wait(.5)

        distributive_row2_col0_content = SurroundingRectangle(distributive_table.get_entries((3, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row2_col1_content = SurroundingRectangle(distributive_table.get_entries((3, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row2_col3_content = SurroundingRectangle(distributive_table.get_entries((3, 5)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row2_col0_content), run_time=.5)
        self.play(Create(distributive_row2_col1_content),run_time=.5)        
        self.play(Create(distributive_row2_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row2_col0_content), FadeOut(distributive_row2_col1_content),FadeOut(distributive_row2_col3_content), run_time=.5)
        self.wait(.5)

        distributive_row3_col0_content = SurroundingRectangle(distributive_table.get_entries((4, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row3_col1_content = SurroundingRectangle(distributive_table.get_entries((4, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row3_col3_content = SurroundingRectangle(distributive_table.get_entries((4, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row3_col0_content), run_time=.5)
        self.play(Create(distributive_row3_col1_content),run_time=.5)        
        self.play(Create(distributive_row3_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row3_col0_content), FadeOut(distributive_row3_col1_content), FadeOut(distributive_row3_col3_content), run_time=.5)
        self.wait(.5)

        distributive_row4_col0_content = SurroundingRectangle(distributive_table.get_entries((5, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row4_col1_content = SurroundingRectangle(distributive_table.get_entries((5, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row4_col3_content = SurroundingRectangle(distributive_table.get_entries((5, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row4_col0_content), run_time=.5)
        self.play(Create(distributive_row4_col1_content),run_time=.5)        
        self.play(Create(distributive_row4_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row4_col0_content), FadeOut(distributive_row4_col1_content), FadeOut(distributive_row4_col3_content), run_time=.5)        
        self.wait(.5)

        distributive_row5_col0_content = SurroundingRectangle(distributive_table.get_entries((6, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row5_col1_content = SurroundingRectangle(distributive_table.get_entries((6, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row5_col3_content = SurroundingRectangle(distributive_table.get_entries((6, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row5_col0_content), run_time=.5)
        self.play(Create(distributive_row5_col1_content),run_time=.5)        
        self.play(Create(distributive_row5_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row5_col0_content), FadeOut(distributive_row5_col1_content), FadeOut(distributive_row5_col3_content), run_time=.5)
        self.wait(.5)

        distributive_row6_col0_content = SurroundingRectangle(distributive_table.get_entries((7, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row6_col1_content = SurroundingRectangle(distributive_table.get_entries((7, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row6_col3_content = SurroundingRectangle(distributive_table.get_entries((7, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row6_col0_content), run_time=.5)
        self.play(Create(distributive_row6_col1_content),run_time=.5)       
        self.play(Create(distributive_row6_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row6_col0_content), FadeOut(distributive_row6_col1_content), FadeOut(distributive_row6_col3_content), run_time=.5)
        self.wait(.5)

        distributive_row7_col0_content = SurroundingRectangle(distributive_table.get_entries((8, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row7_col1_content = SurroundingRectangle(distributive_table.get_entries((8, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row7_col3_content = SurroundingRectangle(distributive_table.get_entries((8, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row7_col0_content), run_time=.5)
        self.play(Create(distributive_row7_col1_content),run_time=.5)       
        self.play(Create(distributive_row7_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row7_col0_content), FadeOut(distributive_row7_col1_content), FadeOut(distributive_row7_col3_content), run_time=.5)
        self.wait(.5)

        distributive_row8_col0_content = SurroundingRectangle(distributive_table.get_entries((9, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row8_col1_content = SurroundingRectangle(distributive_table.get_entries((9, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row8_col3_content = SurroundingRectangle(distributive_table.get_entries((9, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row8_col0_content), run_time=.5)
        self.play(Create(distributive_row8_col1_content),run_time=.5)        
        self.play(Create(distributive_row8_col3_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row8_col0_content), FadeOut(distributive_row8_col1_content), FadeOut(distributive_row8_col3_content), run_time=.5)
        self.wait(.5)

        # p ∧ r
        distributive_row1_col2_content = SurroundingRectangle(distributive_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col3_content = SurroundingRectangle(distributive_table.get_entries((2, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col5_content = SurroundingRectangle(distributive_table.get_entries((2, 6)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row1_col2_content), run_time=.5)
        self.play(Create(distributive_row1_col3_content),run_time=.5)        
        self.play(Create(distributive_row1_col5_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row1_col2_content), FadeOut(distributive_row1_col3_content), FadeOut(distributive_row1_col5_content), run_time=.5)
        self.wait(.5)

        distributive_row2_col2_content = SurroundingRectangle(distributive_table.get_entries((3, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row2_col3_content = SurroundingRectangle(distributive_table.get_entries((3, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row2_col5_content = SurroundingRectangle(distributive_table.get_entries((3, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row2_col2_content), run_time=.5)
        self.play(Create(distributive_row2_col3_content),run_time=.5)        
        self.play(Create(distributive_row2_col5_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row2_col2_content), FadeOut(distributive_row2_col3_content),FadeOut(distributive_row2_col5_content), run_time=.5)
        self.wait(.5)

        distributive_row3_col2_content = SurroundingRectangle(distributive_table.get_entries((4, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row3_col3_content = SurroundingRectangle(distributive_table.get_entries((4, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row3_col5_content = SurroundingRectangle(distributive_table.get_entries((4, 6)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row3_col2_content), run_time=.5)
        self.play(Create(distributive_row3_col3_content),run_time=.5)        
        self.play(Create(distributive_row3_col5_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row3_col2_content), FadeOut(distributive_row3_col3_content), FadeOut(distributive_row3_col5_content), run_time=.5)
        self.wait(.5)

        distributive_row4_col2_content = SurroundingRectangle(distributive_table.get_entries((5, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row4_col3_content = SurroundingRectangle(distributive_table.get_entries((5, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row4_col5_content = SurroundingRectangle(distributive_table.get_entries((5, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row4_col2_content), run_time=.5)
        self.play(Create(distributive_row4_col3_content),run_time=.5)        
        self.play(Create(distributive_row4_col5_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row4_col2_content), FadeOut(distributive_row4_col3_content), FadeOut(distributive_row4_col5_content), run_time=.5)        
        self.wait(.5)

        distributive_row5_col2_content = SurroundingRectangle(distributive_table.get_entries((6, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row5_col3_content = SurroundingRectangle(distributive_table.get_entries((6, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row5_col5_content = SurroundingRectangle(distributive_table.get_entries((6, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row5_col2_content), run_time=.5)
        self.play(Create(distributive_row5_col3_content),run_time=.5)        
        self.play(Create(distributive_row5_col5_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row5_col2_content), FadeOut(distributive_row5_col3_content), FadeOut(distributive_row5_col5_content), run_time=.5)
        self.wait(.5)

        distributive_row6_col2_content = SurroundingRectangle(distributive_table.get_entries((7, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row6_col3_content = SurroundingRectangle(distributive_table.get_entries((7, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row6_col5_content = SurroundingRectangle(distributive_table.get_entries((7, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row6_col2_content), run_time=.5)
        self.play(Create(distributive_row6_col3_content),run_time=.5)       
        self.play(Create(distributive_row6_col5_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row6_col2_content), FadeOut(distributive_row6_col3_content), FadeOut(distributive_row6_col5_content), run_time=.5)
        self.wait(.5)

        distributive_row7_col2_content = SurroundingRectangle(distributive_table.get_entries((8, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row7_col3_content = SurroundingRectangle(distributive_table.get_entries((8, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row7_col5_content = SurroundingRectangle(distributive_table.get_entries((8, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row7_col2_content), run_time=.5)
        self.play(Create(distributive_row7_col3_content),run_time=.5)       
        self.play(Create(distributive_row7_col5_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row7_col2_content), FadeOut(distributive_row7_col3_content), FadeOut(distributive_row7_col5_content), run_time=.5)
        self.wait(.5)

        distributive_row8_col2_content = SurroundingRectangle(distributive_table.get_entries((9, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row8_col3_content = SurroundingRectangle(distributive_table.get_entries((9, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row8_col5_content = SurroundingRectangle(distributive_table.get_entries((9, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row8_col2_content), run_time=.5)
        self.play(Create(distributive_row8_col3_content),run_time=.5)        
        self.play(Create(distributive_row8_col5_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row8_col2_content), FadeOut(distributive_row8_col3_content), FadeOut(distributive_row8_col5_content), run_time=.5)
        self.wait(.5)

         # p ∧ (q ∨ r)
        distributive_row1_col4_content = SurroundingRectangle(distributive_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col3_content = SurroundingRectangle(distributive_table.get_entries((2, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col6_content = SurroundingRectangle(distributive_table.get_entries((2, 7)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row1_col4_content), run_time=.5)
        self.play(Create(distributive_row1_col3_content),run_time=.5)        
        self.play(Create(distributive_row1_col6_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row1_col4_content), FadeOut(distributive_row1_col3_content), FadeOut(distributive_row1_col6_content), run_time=.5)
        self.wait(.5)

        distributive_row2_col4_content = SurroundingRectangle(distributive_table.get_entries((3, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row2_col3_content = SurroundingRectangle(distributive_table.get_entries((3, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row2_col6_content = SurroundingRectangle(distributive_table.get_entries((3, 7)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row2_col4_content), run_time=.5)
        self.play(Create(distributive_row2_col3_content),run_time=.5)        
        self.play(Create(distributive_row2_col6_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row2_col4_content), FadeOut(distributive_row2_col3_content),FadeOut(distributive_row2_col6_content), run_time=.5)
        self.wait(.5)

        distributive_row3_col4_content = SurroundingRectangle(distributive_table.get_entries((4, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row3_col3_content = SurroundingRectangle(distributive_table.get_entries((4, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row3_col6_content = SurroundingRectangle(distributive_table.get_entries((4, 7)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row3_col4_content), run_time=.5)
        self.play(Create(distributive_row3_col3_content),run_time=.5)        
        self.play(Create(distributive_row3_col6_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row3_col4_content), FadeOut(distributive_row3_col3_content), FadeOut(distributive_row3_col6_content), run_time=.5)
        self.wait(.5)

        distributive_row4_col4_content = SurroundingRectangle(distributive_table.get_entries((5, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row4_col3_content = SurroundingRectangle(distributive_table.get_entries((5, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row4_col6_content = SurroundingRectangle(distributive_table.get_entries((5, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row4_col4_content), run_time=.5)
        self.play(Create(distributive_row4_col3_content),run_time=.5)        
        self.play(Create(distributive_row4_col6_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row4_col4_content), FadeOut(distributive_row4_col3_content), FadeOut(distributive_row4_col6_content), run_time=.5)        
        self.wait(.5)

        distributive_row5_col4_content = SurroundingRectangle(distributive_table.get_entries((6, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row5_col3_content = SurroundingRectangle(distributive_table.get_entries((6, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row5_col6_content = SurroundingRectangle(distributive_table.get_entries((6, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row5_col4_content), run_time=.5)
        self.play(Create(distributive_row5_col3_content),run_time=.5)        
        self.play(Create(distributive_row5_col6_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row5_col4_content), FadeOut(distributive_row5_col3_content), FadeOut(distributive_row5_col6_content), run_time=.5)
        self.wait(.5)

        distributive_row6_col4_content = SurroundingRectangle(distributive_table.get_entries((7, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row6_col3_content = SurroundingRectangle(distributive_table.get_entries((7, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row6_col6_content = SurroundingRectangle(distributive_table.get_entries((7, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row6_col4_content), run_time=.5)
        self.play(Create(distributive_row6_col3_content),run_time=.5)       
        self.play(Create(distributive_row6_col6_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row6_col4_content), FadeOut(distributive_row6_col3_content), FadeOut(distributive_row6_col6_content), run_time=.5)
        self.wait(.5)

        distributive_row7_col4_content = SurroundingRectangle(distributive_table.get_entries((8, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row7_col3_content = SurroundingRectangle(distributive_table.get_entries((8, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row7_col6_content = SurroundingRectangle(distributive_table.get_entries((8, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row7_col4_content), run_time=.5)
        self.play(Create(distributive_row7_col3_content),run_time=.5)       
        self.play(Create(distributive_row7_col6_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row7_col4_content), FadeOut(distributive_row7_col3_content), FadeOut(distributive_row7_col6_content), run_time=.5)
        self.wait(.5)

        distributive_row8_col4_content = SurroundingRectangle(distributive_table.get_entries((9, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row8_col3_content = SurroundingRectangle(distributive_table.get_entries((9, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row8_col6_content = SurroundingRectangle(distributive_table.get_entries((9, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row8_col4_content), run_time=.5)
        self.play(Create(distributive_row8_col3_content),run_time=.5)        
        self.play(Create(distributive_row8_col6_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row8_col4_content), FadeOut(distributive_row8_col3_content), FadeOut(distributive_row8_col6_content), run_time=.5)
        self.wait(.5)

        # (p ∧ q) ∨ (p ∧ r)

        distributive_row1_col1_content = SurroundingRectangle(distributive_table.get_entries((2, 5)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col5_content = SurroundingRectangle(distributive_table.get_entries((2, 6)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row1_col7_content = SurroundingRectangle(distributive_table.get_entries((2, 8)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row1_col1_content), run_time=.5)
        self.play(Create(distributive_row1_col5_content),run_time=.5)        
        self.play(Create(distributive_row1_col7_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row1_col1_content), FadeOut(distributive_row1_col5_content), FadeOut(distributive_row1_col7_content), run_time=.5)
        self.wait(.5)

        distributive_row2_col1_content = SurroundingRectangle(distributive_table.get_entries((3, 5)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        distributive_row2_col5_content = SurroundingRectangle(distributive_table.get_entries((3, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row2_col7_content = SurroundingRectangle(distributive_table.get_entries((3, 8)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1) 
        self.play(Create(distributive_row2_col1_content), run_time=.5)
        self.play(Create(distributive_row2_col5_content),run_time=.5)        
        self.play(Create(distributive_row2_col7_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row2_col1_content), FadeOut(distributive_row2_col5_content),FadeOut(distributive_row2_col7_content), run_time=.5)
        self.wait(.5)

        distributive_row3_col1_content = SurroundingRectangle(distributive_table.get_entries((4, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row3_col5_content = SurroundingRectangle(distributive_table.get_entries((4, 6)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)        
        distributive_row3_col7_content = SurroundingRectangle(distributive_table.get_entries((4, 8)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row3_col1_content), run_time=.5)
        self.play(Create(distributive_row3_col5_content),run_time=.5)        
        self.play(Create(distributive_row3_col7_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row3_col1_content), FadeOut(distributive_row3_col5_content), FadeOut(distributive_row3_col7_content), run_time=.5)
        self.wait(.5)

        distributive_row4_col1_content = SurroundingRectangle(distributive_table.get_entries((5, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row4_col5_content = SurroundingRectangle(distributive_table.get_entries((5, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row4_col7_content = SurroundingRectangle(distributive_table.get_entries((5, 8)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row4_col1_content), run_time=.5)
        self.play(Create(distributive_row4_col5_content),run_time=.5)        
        self.play(Create(distributive_row4_col7_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row4_col1_content), FadeOut(distributive_row4_col5_content), FadeOut(distributive_row4_col7_content), run_time=.5)        
        self.wait(.5)

        distributive_row5_col1_content = SurroundingRectangle(distributive_table.get_entries((6, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row5_col5_content = SurroundingRectangle(distributive_table.get_entries((6, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row5_col7_content = SurroundingRectangle(distributive_table.get_entries((6, 8)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row5_col1_content), run_time=.5)
        self.play(Create(distributive_row5_col5_content),run_time=.5)        
        self.play(Create(distributive_row5_col7_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row5_col1_content), FadeOut(distributive_row5_col5_content), FadeOut(distributive_row5_col7_content), run_time=.5)
        self.wait(.5)

        distributive_row6_col1_content = SurroundingRectangle(distributive_table.get_entries((7, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row6_col5_content = SurroundingRectangle(distributive_table.get_entries((7, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row6_col7_content = SurroundingRectangle(distributive_table.get_entries((7, 8)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row6_col1_content), run_time=.5)
        self.play(Create(distributive_row6_col5_content),run_time=.5)       
        self.play(Create(distributive_row6_col7_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row6_col1_content), FadeOut(distributive_row6_col5_content), FadeOut(distributive_row6_col7_content), run_time=.5)
        self.wait(.5)

        distributive_row7_col1_content = SurroundingRectangle(distributive_table.get_entries((8, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row7_col5_content = SurroundingRectangle(distributive_table.get_entries((8, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row7_col7_content = SurroundingRectangle(distributive_table.get_entries((8, 8)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row7_col1_content), run_time=.5)
        self.play(Create(distributive_row7_col5_content),run_time=.5)       
        self.play(Create(distributive_row7_col7_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row7_col1_content), FadeOut(distributive_row7_col5_content), FadeOut(distributive_row7_col7_content), run_time=.5)
        self.wait(.5)

        distributive_row8_col1_content = SurroundingRectangle(distributive_table.get_entries((9, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        distributive_row8_col5_content = SurroundingRectangle(distributive_table.get_entries((9, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)        
        distributive_row8_col7_content = SurroundingRectangle(distributive_table.get_entries((9, 8)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(distributive_row8_col1_content), run_time=.5)
        self.play(Create(distributive_row8_col5_content),run_time=.5)  
        self.play(Create(distributive_row8_col7_content) ,run_time=.5)
        self.wait(.5)
        self.play(FadeOut(distributive_row8_col1_content), FadeOut(distributive_row8_col5_content), FadeOut(distributive_row8_col7_content), run_time=.5)
        self.wait(.5)        
        
        distributive_col6 = SurroundingRectangle(distributive_table.get_columns()[6][1:], color=RED, buff=0.05,fill_color=ORANGE, fill_opacity=0.075, stroke_width= 1)
        distributive_col7 = SurroundingRectangle(distributive_table.get_columns()[7][1:], color=RED, buff=0.05,fill_color=ORANGE, fill_opacity=0.075,  stroke_width= 1)
        self.add(distributive_col6, distributive_col7)
        self.wait(1)
        self.play(FadeOut(distributive_group), FadeOut(distributive_col6), FadeOut(distributive_col7),  FadeOut(distributive_bullet_underline), run_time=.5)        
        self.wait(1)
    
        # Identity laws: p ∧ t ≡ p
        identity_title = Text("Identity law: p ∧ t ≡ p", font_size=font_size + 8)
        identity_underline = Line(LEFT*identity_title.width/2, RIGHT*identity_title.width/2, stroke_width=1, color=WHITE)
        identity_underline.next_to(identity_title, DOWN, buff=0.2)        	

        identity_bullet_underline = Line(LEFT*identity.width/2, RIGHT*identity.width/2, stroke_width=1, color=YELLOW)
        identity_bullet_underline.next_to(identity, DOWN, buff=0.1)
        identity_table = Table(
            [["T", "T", "T"],
            ["F", "T", "F"]],           
            col_labels=[Text("P"), Text("t"), Text("p ∧ t")],
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        ).scale(0.5).next_to(identity_underline, DOWN*2, buff=0.5)

        identity_group = VGroup(identity_title, identity_underline, identity_table)
        identity_group.arrange(DOWN, aligned_edge=LEFT, buff=0.20).scale(0.6).next_to(box, RIGHT*3) 
        identity_group.align_to(box, UP)
       
        self.add(identity_title, identity_underline, identity_bullet_underline)        
       
        self.wait(.5)
        self.play(FadeIn(identity_table), run_time=1)
        self.wait(.5)
       
        identity_row1_col0_content = SurroundingRectangle(identity_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        identity_row1_col1_content = SurroundingRectangle(identity_table.get_entries((2, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        identity_row1_col2_content = SurroundingRectangle(identity_table.get_entries((2, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(identity_row1_col0_content), run_time=.5)
        self.play(Create(identity_row1_col1_content),run_time=.5)
        self.play(Create(identity_row1_col2_content),run_time=.5)
        
        self.wait(.5)
        self.play(FadeOut(identity_row1_col0_content), FadeOut(identity_row1_col1_content),FadeOut(identity_row1_col2_content), run_time=.5)
        self.wait(.5)

        identity_row2_col0_content = SurroundingRectangle(identity_table.get_entries((3, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        identity_row2_col1_content = SurroundingRectangle(identity_table.get_entries((3, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        identity_row2_col2_content = SurroundingRectangle(identity_table.get_entries((3, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(identity_row2_col0_content), run_time=.5)
        self.play(Create(identity_row2_col1_content),run_time=.5)
        self.play(Create(identity_row2_col2_content),run_time=.5)
       
        self.wait(.5)
        self.play(FadeOut(identity_row2_col0_content), FadeOut(identity_row2_col1_content),FadeOut(identity_row2_col2_content),  run_time=.5)
        self.wait(.5)
        
        identity_col1 = SurroundingRectangle(identity_table.get_columns()[0][1:], color=RED, buff=0.05,fill_color=ORANGE, fill_opacity=0.075, stroke_width= 1)
        identity_col3 = SurroundingRectangle(identity_table.get_columns()[2][1:], color=RED, buff=0.05,fill_color=ORANGE, fill_opacity=0.075, stroke_width= 1)
        self.add(identity_col1, identity_col3)
        self.wait(.5)
        self.play(FadeOut(identity_group), FadeOut(identity_col1), FadeOut(identity_col3), FadeOut(identity_bullet_underline), run_time=1)       
        self.wait(1)

        # Negation laws: p ∧ ¬p ≡ c
        negation_title = Text("Negation law: p ∧ ¬p ≡ c", font_size=font_size + 8)
        negation_underline = Line(LEFT*negation_title.width/2, RIGHT*negation_title.width/2, stroke_width=1, color=WHITE)
        negation_underline.next_to(negation_title, DOWN, buff=0.2)        	

        negation_bullet_underline = Line(LEFT*negation.width/2, RIGHT*negation.width/2, stroke_width=1, color=YELLOW)
        negation_bullet_underline.next_to(negation, DOWN, buff=0.1)
        negation_table = Table(
            [["T", "F", "F", "F"],
            ["F", "T", "F", "F"]],           
            col_labels=[Text("P"),Text("¬p"), Text("c"), Text("p ∧ ¬p")],
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        ).scale(0.5).next_to(negation_underline, DOWN*2, buff=0.5)

        negation_group = VGroup(negation_title, negation_underline, negation_table)
        negation_group.arrange(DOWN, aligned_edge=LEFT, buff=0.20).scale(0.6).next_to(box, RIGHT*3) 
        negation_group.align_to(box, UP)
       
        self.add(negation_title, negation_underline, negation_bullet_underline)        
       
        self.wait(.5)
        self.play(FadeIn(negation_table), run_time=1)
        self.wait(.5)
       
        negation_row1_col0_content = SurroundingRectangle(negation_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        negation_row1_col1_content = SurroundingRectangle(negation_table.get_entries((2, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        negation_row1_col3_content = SurroundingRectangle(negation_table.get_entries((2, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(negation_row1_col0_content), run_time=.5)
        self.play(Create(negation_row1_col1_content),run_time=.5)
        self.play(Create(negation_row1_col3_content),run_time=.5)
        
        self.wait(.5)
        self.play(FadeOut(negation_row1_col0_content), FadeOut(negation_row1_col1_content),FadeOut(negation_row1_col3_content), run_time=.5)
        self.wait(.5)

        negation_row2_col0_content = SurroundingRectangle(negation_table.get_entries((3, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        negation_row2_col1_content = SurroundingRectangle(negation_table.get_entries((3, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        negation_row2_col3_content = SurroundingRectangle(negation_table.get_entries((3, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(negation_row2_col0_content), run_time=.5)
        self.play(Create(negation_row2_col1_content),run_time=.5)
        self.play(Create(negation_row2_col3_content),run_time=.5)
       
        self.wait(.5)
        self.play(FadeOut(negation_row2_col0_content), FadeOut(negation_row2_col1_content),FadeOut(negation_row2_col3_content),  run_time=.5)
        self.wait(.5)

        
        negation_col3 = SurroundingRectangle(negation_table.get_columns()[2][1:], color=RED, buff=0.05,fill_color=ORANGE, fill_opacity=0.075, stroke_width= 1)
        negation_col4 = SurroundingRectangle(negation_table.get_columns()[3][1:], color=RED, buff=0.05,fill_color=ORANGE, fill_opacity=0.075, stroke_width= 1)
        self.add(negation_col3, negation_col4)
        self.wait(.5)
        self.play(FadeOut(negation_group), FadeOut(negation_col3), FadeOut(negation_col4),  FadeOut(negation_bullet_underline), run_time=1)        
        self.wait(1)

        # Double Negation laws: ¬(¬p) ≡ p 
        doubleNegation_title = Text("Double Negation law: ¬(¬p) ≡ p ", font_size=font_size + 8)
        doubleNegation_underline = Line(LEFT*doubleNegation_title.width/2, RIGHT*doubleNegation_title.width/2, stroke_width=1, color=WHITE)
        doubleNegation_underline.next_to(doubleNegation_title, DOWN, buff=0.2)        	

        doubleNegation_bullet_underline = Line(LEFT*doubleNegation.width/2, RIGHT*doubleNegation.width/2, stroke_width=1, color=YELLOW)
        doubleNegation_bullet_underline.next_to(doubleNegation, DOWN, buff=0.1)
        doubleNegation_table = Table(
            [["T", "F", "T"],
            ["F", "T", "F"]],           
            col_labels=[Text("P"),Text("¬p"), Text("¬(¬p)")],
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        ).scale(0.5).next_to(doubleNegation_underline, DOWN*2, buff=0.5)

        doubleNegation_group = VGroup(doubleNegation_title,doubleNegation_underline,doubleNegation_table)
        doubleNegation_group.arrange(DOWN, aligned_edge=LEFT, buff=0.20).scale(0.6).next_to(box, RIGHT*3) 
        doubleNegation_group.align_to(box, UP)
       
        self.add(doubleNegation_title,doubleNegation_underline,doubleNegation_bullet_underline)
        
       
        self.wait(.5)
        self.play(FadeIn(doubleNegation_table), run_time=1)
        self.wait(.5)
       
        doubleNegation_row1_col0_content = SurroundingRectangle(doubleNegation_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        doubleNegation_row1_col1_content = SurroundingRectangle(doubleNegation_table.get_entries((2, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        doubleNegation_row1_col2_content = SurroundingRectangle(doubleNegation_table.get_entries((2, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(doubleNegation_row1_col0_content), run_time=.5)
        self.play(Create(doubleNegation_row1_col1_content),run_time=.5)
        self.play(Create(doubleNegation_row1_col2_content),run_time=.5)
        
        self.wait(.5)
        self.play(FadeOut(doubleNegation_row1_col0_content), FadeOut(doubleNegation_row1_col1_content),FadeOut(doubleNegation_row1_col2_content), run_time=.5)
        self.wait(.5)

        doubleNegation_row2_col0_content = SurroundingRectangle(doubleNegation_table.get_entries((3, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        doubleNegation_row2_col1_content = SurroundingRectangle(doubleNegation_table.get_entries((3, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        doubleNegation_row2_col2_content = SurroundingRectangle(doubleNegation_table.get_entries((3, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(doubleNegation_row2_col0_content), run_time=.5)
        self.play(Create(doubleNegation_row2_col1_content),run_time=.5)
        self.play(Create(doubleNegation_row2_col2_content),run_time=.5)
       
        self.wait(.5)
        self.play(FadeOut(doubleNegation_row2_col0_content), FadeOut(doubleNegation_row2_col1_content),FadeOut(doubleNegation_row2_col2_content),  run_time=.5)
        self.wait(.5)

        
        doubleNegation_col1 = SurroundingRectangle(doubleNegation_table.get_columns()[0][1:], color=RED, buff=0.05,fill_color=ORANGE, fill_opacity=0.075,  stroke_width= 1)
        doubleNegation_col3 = SurroundingRectangle(doubleNegation_table.get_columns()[2][1:], color=RED, buff=0.05,fill_color=ORANGE, fill_opacity=0.075,  stroke_width= 1)
        self.add(doubleNegation_col1,doubleNegation_col3)
        self.wait(.5)
        self.play(FadeOut(doubleNegation_group), FadeOut(doubleNegation_col1), FadeOut(doubleNegation_col3), FadeOut(doubleNegation_bullet_underline), run_time=1)        
        self.wait(1)

        # Idempotent laws: p ∧ p ≡ p 
        idempotent_title = Text("Idempotent law: p ∧ p ≡ p", font_size=font_size + 8)
        idempotent_underline = Line(LEFT*idempotent_title.width/2, RIGHT*idempotent_title.width/2, stroke_width=1, color=WHITE)
        idempotent_underline.next_to(idempotent_title, DOWN, buff=0.2)        	

        idempotent_bullet_underline = Line(LEFT*idempotent.width/2, RIGHT*idempotent.width/2, stroke_width=1, color=YELLOW)
        idempotent_bullet_underline.next_to(idempotent, DOWN, buff=0.1)
        idempotent_table = Table(
            [["T", "T"],
            ["F", "F"]],           
            col_labels=[Text("P"),Text("p ∧ p")],
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        ).scale(0.5).next_to(idempotent_underline, DOWN*2, buff=0.5)

        idempotent_group = VGroup(idempotent_title, idempotent_underline, idempotent_table)
        idempotent_group.arrange(DOWN, aligned_edge=LEFT, buff=0.20).scale(0.6).next_to(box, RIGHT*3) 
        idempotent_group.align_to(box, UP)
       
        self.add(idempotent_title, idempotent_underline, idempotent_bullet_underline)        
       
        self.wait(.5)
        self.play(FadeIn(idempotent_table), run_time=1)
        self.wait(.5)
       
        idempotent_row1_col0_content = SurroundingRectangle(idempotent_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        idempotent_row1_col1_content = SurroundingRectangle(idempotent_table.get_entries((2, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        
        
        self.play(Create(idempotent_row1_col0_content), run_time=.5)
        self.play(Create(idempotent_row1_col1_content),run_time=.5)
        
        
        self.wait(.5)
        self.play(FadeOut(idempotent_row1_col0_content), FadeOut(idempotent_row1_col1_content), run_time=.5)
        self.wait(.5)

        idempotent_row2_col0_content = SurroundingRectangle(idempotent_table.get_entries((3, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        idempotent_row2_col1_content = SurroundingRectangle(idempotent_table.get_entries((3, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        
        
        self.play(Create(idempotent_row2_col0_content), run_time=.5)
        self.play(Create(idempotent_row2_col1_content),run_time=.5)
        
       
        self.wait(.5)
        self.play(FadeOut(idempotent_row2_col0_content), FadeOut(idempotent_row2_col1_content),  run_time=.5)
        self.wait(.5)

        
        idempotent_col1 = SurroundingRectangle(idempotent_table.get_columns()[0][1:], color=RED, buff=0.05,fill_color=ORANGE, fill_opacity=0.075, stroke_width= 1)
        idempotent_col2 = SurroundingRectangle(idempotent_table.get_columns()[1][1:], color=RED, buff=0.05,fill_color=ORANGE, fill_opacity=0.075,  stroke_width= 1)
        self.add(idempotent_col1, idempotent_col2)
        self.wait(.5)
        self.play(FadeOut(idempotent_group), FadeOut(idempotent_col1), FadeOut(idempotent_col2),  FadeOut(idempotent_bullet_underline), run_time=1)
        
        self.wait(1)

         # De Morgan's law: p ∧ q  ≡ q ∧ p
        deMorgan_title = Text("De Morgan's law:  ¬(p ∧ q) ≡ ¬p ∨ ¬q ", font_size=font_size + 8)
        deMorgan_underline = Line(LEFT*deMorgan_title.width/2, RIGHT*deMorgan_title.width/2, stroke_width=1, color=WHITE)
        deMorgan_underline.next_to(deMorgan_title, DOWN, buff=0.2)        	

        deMorgan_bullet_underline = Line(LEFT*deMorgan.width/2, RIGHT*deMorgan.width/2, stroke_width=1, color=YELLOW)
        deMorgan_bullet_underline.next_to(deMorgan, DOWN, buff=0.1)
        deMorgan_table = Table(
            [ ["T", "T", "F", "F", "T", "F", "F"],
            ["T", "F", "F", "T", "F", "T", "T"],
            ["F", "T", "T", "F", "F", "T", "T"],
            ["F", "F", "T", "T", "F", "T", "T"]],           
            col_labels=[Text("P"), Text("q"), Text("¬P"), Text("¬q"), Text("p ∧ q"), Text("¬(p ∧ q)"), Text("¬p ∨ ¬q")],
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        ).scale(0.5).next_to(deMorgan_underline, DOWN*2, buff=0.5)

        deMorgan_group = VGroup(deMorgan_title, deMorgan_underline, deMorgan_table)
        deMorgan_group.arrange(DOWN, aligned_edge=LEFT, buff=0.20).scale(0.6).next_to(box, RIGHT*3) 
        deMorgan_group.align_to(box, UP)
       
        self.add(deMorgan_title, deMorgan_underline, deMorgan_bullet_underline)
        
       
        self.wait(2)
        self.play(FadeIn(deMorgan_table), run_time=1)
        self.wait(1)

        # p ∧ q 
        deMorgan_row1_col0_content = SurroundingRectangle(deMorgan_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        deMorgan_row1_col1_content = SurroundingRectangle(deMorgan_table.get_entries((2, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        deMorgan_row1_col4_content = SurroundingRectangle(deMorgan_table.get_entries((2, 5)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(deMorgan_row1_col0_content), run_time=.5)
        self.play(Create(deMorgan_row1_col1_content),run_time=.5)
        self.play(Create(deMorgan_row1_col4_content), run_time=.5)
        
        self.wait(.5)
        self.play(FadeOut(deMorgan_row1_col0_content), FadeOut(deMorgan_row1_col1_content), FadeOut(deMorgan_row1_col4_content),  run_time=.5)
        self.wait(.5)
        deMorgan_row2_col0_content = SurroundingRectangle(deMorgan_table.get_entries((3, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        deMorgan_row2_col1_content = SurroundingRectangle(deMorgan_table.get_entries((3, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        deMorgan_row2_col4_content = SurroundingRectangle(deMorgan_table.get_entries((3, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(deMorgan_row2_col0_content), run_time=.5)
        self.play(Create(deMorgan_row2_col1_content),run_time=.5)
        self.play(Create(deMorgan_row2_col4_content), run_time=.5)
        
        self.wait(.5)
        self.play(FadeOut(deMorgan_row2_col0_content), FadeOut(deMorgan_row2_col1_content), FadeOut(deMorgan_row2_col4_content),  run_time=.5)
        self.wait(.5)

        deMorgan_row3_col0_content = SurroundingRectangle(deMorgan_table.get_entries((4, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        deMorgan_row3_col1_content = SurroundingRectangle(deMorgan_table.get_entries((4, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        deMorgan_row3_col4_content = SurroundingRectangle(deMorgan_table.get_entries((4, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
       
        self.play(Create(deMorgan_row3_col0_content), run_time=.5)
        self.play(Create(deMorgan_row3_col1_content),run_time=.5)
        self.play(Create(deMorgan_row3_col4_content), run_time=.5)
        
        self.wait(.5)
        self.play(FadeOut(deMorgan_row3_col0_content), FadeOut(deMorgan_row3_col1_content), FadeOut(deMorgan_row3_col4_content),  run_time=.5)
        self.wait(.5)

        deMorgan_row4_col0_content = SurroundingRectangle(deMorgan_table.get_entries((5, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        deMorgan_row4_col1_content = SurroundingRectangle(deMorgan_table.get_entries((5, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        deMorgan_row4_col4_content = SurroundingRectangle(deMorgan_table.get_entries((5, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(deMorgan_row4_col0_content), run_time=.5)
        self.play(Create(deMorgan_row4_col1_content),run_time=.5)
        self.play(Create(deMorgan_row4_col4_content), run_time=.5)
        
        self.wait(.5)
        self.play(FadeOut(deMorgan_row4_col0_content), FadeOut(deMorgan_row4_col1_content), FadeOut(deMorgan_row4_col4_content),  run_time=.5)
        self.wait(.5)
        
        # ¬(p ∧ q)
        deMorgan_row1_col4_content = SurroundingRectangle(deMorgan_table.get_entries((2, 5)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        deMorgan_row1_col5_content = SurroundingRectangle(deMorgan_table.get_entries((2, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        self.play(Create(deMorgan_row1_col4_content), run_time=.5)
        self.play(Create(deMorgan_row1_col5_content),run_time=.5)        
        self.wait(.5)
        self.play(FadeOut(deMorgan_row1_col4_content), FadeOut(deMorgan_row1_col5_content), run_time=.5)
        self.wait(.5)

        
        deMorgan_row2_col4_content = SurroundingRectangle(deMorgan_table.get_entries((3, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        deMorgan_row2_col5_content = SurroundingRectangle(deMorgan_table.get_entries((3, 6)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        self.play(Create(deMorgan_row2_col4_content), run_time=.5)
        self.play(Create(deMorgan_row2_col5_content),run_time=.5)        
        self.wait(.5)
        self.play(FadeOut(deMorgan_row2_col4_content), FadeOut(deMorgan_row2_col5_content),  run_time=.5)
        self.wait(.5)

        
        deMorgan_row3_col4_content = SurroundingRectangle(deMorgan_table.get_entries((4, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        deMorgan_row3_col5_content = SurroundingRectangle(deMorgan_table.get_entries((4, 6)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        self.play(Create(deMorgan_row3_col4_content), run_time=.5)
        self.play(Create(deMorgan_row3_col5_content),run_time=.5)        
        self.wait(.5)
        self.play(FadeOut(deMorgan_row3_col4_content), FadeOut(deMorgan_row3_col5_content),  run_time=.5)
        self.wait(.5)

        deMorgan_row4_col4_content = SurroundingRectangle(deMorgan_table.get_entries((5, 5)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        deMorgan_row4_col5_content = SurroundingRectangle(deMorgan_table.get_entries((5, 6)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(deMorgan_row4_col4_content), run_time=.5)
        self.play(Create(deMorgan_row4_col5_content),run_time=.5)        
        self.wait(.5)
        self.play(FadeOut(deMorgan_row4_col4_content), FadeOut(deMorgan_row4_col5_content), run_time=.5)
        self.wait(.5)

        # ¬p ∨ ¬q
        deMorgan_row1_col3_content = SurroundingRectangle(deMorgan_table.get_entries((2, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        deMorgan_row1_col4_content = SurroundingRectangle(deMorgan_table.get_entries((2, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        deMorgan_row1_col7_content = SurroundingRectangle(deMorgan_table.get_entries((2, 7)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)       
        self.play(Create(deMorgan_row1_col3_content), run_time=.5)
        self.play(Create(deMorgan_row1_col4_content),run_time=.5)
        self.play(Create(deMorgan_row1_col7_content), run_time=.5)
        
        self.wait(.5)
        self.play(FadeOut(deMorgan_row1_col3_content), FadeOut(deMorgan_row1_col4_content),  FadeOut(deMorgan_row1_col7_content),  run_time=.5)
        self.wait(.5)

        deMorgan_row2_col3_content = SurroundingRectangle(deMorgan_table.get_entries((3, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        deMorgan_row2_col4_content = SurroundingRectangle(deMorgan_table.get_entries((3, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        deMorgan_row2_col7_content = SurroundingRectangle(deMorgan_table.get_entries((3, 7)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
       
        self.play(Create(deMorgan_row2_col3_content), run_time=.5)
        self.play(Create(deMorgan_row2_col4_content),run_time=.5)
        self.play(Create(deMorgan_row2_col7_content), run_time=.5)
        
        self.wait(.5)
        self.play(FadeOut(deMorgan_row2_col3_content), FadeOut(deMorgan_row2_col4_content), FadeOut(deMorgan_row2_col7_content),  run_time=.5)
        self.wait(.5)

        deMorgan_row3_col3_content = SurroundingRectangle(deMorgan_table.get_entries((4, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        deMorgan_row3_col4_content = SurroundingRectangle(deMorgan_table.get_entries((4, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        deMorgan_row3_col7_content = SurroundingRectangle(deMorgan_table.get_entries((4, 7)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(deMorgan_row3_col3_content), run_time=.5)
        self.play(Create(deMorgan_row3_col4_content),run_time=.5)
        self.play(Create(deMorgan_row3_col7_content), run_time=.5)
        
        self.wait(.5)
        self.play(FadeOut(deMorgan_row3_col3_content), FadeOut(deMorgan_row3_col4_content), FadeOut(deMorgan_row3_col7_content),  run_time=.5)
        self.wait(.5)

        deMorgan_row4_col3_content = SurroundingRectangle(deMorgan_table.get_entries((5, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        deMorgan_row4_col4_content = SurroundingRectangle(deMorgan_table.get_entries((5, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        deMorgan_row4_col7_content = SurroundingRectangle(deMorgan_table.get_entries((5, 7)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(deMorgan_row4_col3_content), run_time=.5)
        self.play(Create(deMorgan_row4_col4_content),run_time=.5)
        self.play(Create(deMorgan_row4_col7_content), run_time=.5)
       
        self.wait(.5)
        self.play(FadeOut(deMorgan_row4_col3_content), FadeOut(deMorgan_row4_col4_content), FadeOut(deMorgan_row4_col7_content),  run_time=.5)
        self.wait(.5)

        deMorgan_col6 = SurroundingRectangle(deMorgan_table.get_columns()[5][1:], color=RED, buff=0.05, fill_color=ORANGE, fill_opacity=0.075,stroke_width= 1)
        deMorgan_col7 = SurroundingRectangle(deMorgan_table.get_columns()[6][1:], color=RED, buff=0.05, fill_color=ORANGE, fill_opacity=0.075,stroke_width= 1)
        self.add(deMorgan_col6, deMorgan_col7)
        self.wait(.5)
        self.play(FadeOut(deMorgan_group), FadeOut(deMorgan_col6), FadeOut(deMorgan_col7),  FadeOut(deMorgan_bullet_underline), run_time=1)
        
        self.wait(1)

        # Universal bound law: p ∨ t ≡ t
        universal_title = Text("Universal bound law: p ∨ t ≡ t", font_size=font_size + 8)
        universal_underline = Line(LEFT*universal_title.width/2, RIGHT*universal_title.width/2, stroke_width=1, color=WHITE)
        universal_underline.next_to(universal_title, DOWN, buff=0.2)        	

        universal_bullet_underline = Line(LEFT*universal.width/2, RIGHT*universal.width/2, stroke_width=1, color=YELLOW)
        universal_bullet_underline.next_to(universal, DOWN, buff=0.1)
        universal_table = Table(
            [["T", "T", "T"],
            ["F", "T", "T"]],           
            col_labels=[Text("P"), Text("t"), Text("p ∨ t")],
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        ).scale(0.7).next_to(universal_underline, DOWN*2, buff=0.5)

        universal_group = VGroup(universal_title, universal_underline, universal_table)
        universal_group.arrange(DOWN, aligned_edge=LEFT, buff=0.20).scale(0.6).next_to(box, RIGHT*3) 
        universal_group.align_to(box, UP)
       
        self.add(universal_title, universal_underline, universal_bullet_underline)
        
       
        self.wait(.5)
        self.play(FadeIn(universal_table), run_time=1)
        self.wait(.5)
       
        universal_row1_col0_content = SurroundingRectangle(universal_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        universal_row1_col1_content = SurroundingRectangle(universal_table.get_entries((2, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        universal_row1_col2_content = SurroundingRectangle(universal_table.get_entries((2, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(universal_row1_col0_content), run_time=.5)
        self.play(Create(universal_row1_col1_content),run_time=.5)
        self.play(Create(universal_row1_col2_content),run_time=.5)
        
        self.wait(.5)
        self.play(FadeOut(universal_row1_col0_content), FadeOut(universal_row1_col1_content),FadeOut(universal_row1_col2_content), run_time=.5)
        self.wait(.5)

        universal_row2_col0_content = SurroundingRectangle(universal_table.get_entries((3, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        universal_row2_col1_content = SurroundingRectangle(universal_table.get_entries((3, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        universal_row2_col2_content = SurroundingRectangle(universal_table.get_entries((3, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(universal_row2_col0_content), run_time=.5)
        self.play(Create(universal_row2_col1_content),run_time=.5)
        self.play(Create(universal_row2_col2_content),run_time=.5)
       
        self.wait(.5)
        self.play(FadeOut(universal_row2_col0_content), FadeOut(universal_row2_col1_content),FadeOut(universal_row2_col2_content),  run_time=.5)
        self.wait(.5)
        
        universal_col1 = SurroundingRectangle(universal_table.get_columns()[1][1:], color=RED, buff=0.05, fill_color=ORANGE, fill_opacity=0.075,  stroke_width= 1)
        universal_col3 = SurroundingRectangle(universal_table.get_columns()[2][1:], color=RED, buff=0.05, fill_color=ORANGE, fill_opacity=0.075,  stroke_width= 1)
        self.add(universal_col1, universal_col3)
        self.wait(.5)
        self.play(FadeOut(universal_group), FadeOut(universal_col1), FadeOut(universal_col3),  FadeOut(universal_bullet_underline), run_time=1)
        
        self.wait(1)

        # Absorption law: p ∧ (p ∨ q) ≡ p
        absorption_title = Text("Absorption law:p ∧ (p ∨ q) ≡ p", font_size=font_size + 8)
        absorption_underline = Line(LEFT*absorption_title.width/2, RIGHT*absorption_title.width/2, stroke_width=1, color=WHITE)
        absorption_underline.next_to(absorption_title, DOWN, buff=0.2)        	

        absorption_bullet_underline = Line(LEFT*absorption.width/2, RIGHT*absorption.width/2, stroke_width=1, color=YELLOW)
        absorption_bullet_underline.next_to(absorption, DOWN, buff=0.1)
        absorption_table = Table(
            [["T", "T", "T", "T"],
            ["T", "F", "T", "T"],
            ["F", "T", "T", "F"],
            ["F", "F", "F", "F"]],           
            col_labels=[Text("P"), Text("q"), Text("p ∨ q"), Text("p ∧ (p ∨ q)")],
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        ).scale(0.7).next_to(absorption_underline, DOWN*2, buff=0.5)

        absorption_group = VGroup(absorption_title, absorption_underline, absorption_table)
        absorption_group.arrange(DOWN, aligned_edge=LEFT, buff=0.20).scale(0.6).next_to(box, RIGHT*3) 
        absorption_group.align_to(box, UP)
       
        self.add(absorption_title, absorption_underline, absorption_bullet_underline)
        
       
        self.wait(.5)
        self.play(FadeIn(absorption_table), run_time=.5)
        self.wait(.5)
		
        # "p ∨ q
        absorption_row1_col0_content = SurroundingRectangle(absorption_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        absorption_row1_col1_content = SurroundingRectangle(absorption_table.get_entries((2, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        absorption_row1_col2_content = SurroundingRectangle(absorption_table.get_entries((2, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(absorption_row1_col0_content), run_time=.5)
        self.play(Create(absorption_row1_col1_content),run_time=.5)
        self.play(Create(absorption_row1_col2_content), run_time=.5)
       
        self.wait(.5)
        self.play(FadeOut(absorption_row1_col0_content), FadeOut(absorption_row1_col1_content),FadeOut(absorption_row1_col2_content), run_time=.5)
        self.wait(.5)
		
        absorption_row2_col0_content = SurroundingRectangle(absorption_table.get_entries((3, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        absorption_row2_col1_content = SurroundingRectangle(absorption_table.get_entries((3, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        absorption_row2_col2_content = SurroundingRectangle(absorption_table.get_entries((3, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
       
        self.play(Create(absorption_row2_col0_content), run_time=.5)
        self.play(Create(absorption_row2_col1_content),run_time=.5)
        self.play(Create(absorption_row2_col2_content), run_time=.5)
        
        self.wait(.5)
        self.play(FadeOut(absorption_row2_col0_content), FadeOut(absorption_row2_col1_content),FadeOut(absorption_row2_col2_content),  run_time=.5)
        self.wait(.5)

        absorption_row3_col0_content = SurroundingRectangle(absorption_table.get_entries((4, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        absorption_row3_col1_content = SurroundingRectangle(absorption_table.get_entries((4, 2)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        absorption_row3_col2_content = SurroundingRectangle(absorption_table.get_entries((4, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
       
        self.play(Create(absorption_row3_col0_content), run_time=.5)
        self.play(Create(absorption_row3_col1_content),run_time=.5)
        self.play(Create(absorption_row3_col2_content), run_time=.5)
        
        self.wait(.5)
        self.play(FadeOut(absorption_row3_col0_content), FadeOut(absorption_row3_col1_content), FadeOut(absorption_row3_col2_content),  run_time=.5)
        self.wait(.5)

        absorption_row4_col0_content = SurroundingRectangle(absorption_table.get_entries((5, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        absorption_row4_col1_content = SurroundingRectangle(absorption_table.get_entries((5, 2)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        absorption_row4_col2_content = SurroundingRectangle(absorption_table.get_entries((5, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(absorption_row4_col0_content), run_time=.5)
        self.play(Create(absorption_row4_col1_content),run_time=.5)
        self.play(Create(absorption_row4_col2_content), run_time=.5)
      
        self.wait(.5)
        self.play(FadeOut(absorption_row4_col0_content), FadeOut(absorption_row4_col1_content), FadeOut(absorption_row4_col2_content),  run_time=.5)
        self.wait(.5)
		
		# p ∧ (p ∨ q)
        absorption_row1_col0_content = SurroundingRectangle(absorption_table.get_entries((2, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        absorption_row1_col2_content = SurroundingRectangle(absorption_table.get_entries((2, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        absorption_row1_col3_content = SurroundingRectangle(absorption_table.get_entries((2, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(absorption_row1_col0_content), run_time=.5)
        self.play(Create(absorption_row1_col2_content),run_time=.5)
        self.play(Create(absorption_row1_col3_content), run_time=.5)
       
        self.wait(.5)
        self.play(FadeOut(absorption_row1_col0_content), FadeOut(absorption_row1_col2_content),FadeOut(absorption_row1_col3_content), run_time=.5)
        self.wait(.5)
		
        absorption_row2_col0_content = SurroundingRectangle(absorption_table.get_entries((3, 1)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        absorption_row2_col2_content = SurroundingRectangle(absorption_table.get_entries((3, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        absorption_row2_col3_content = SurroundingRectangle(absorption_table.get_entries((3, 4)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
       
        self.play(Create(absorption_row2_col0_content), run_time=.5)
        self.play(Create(absorption_row2_col2_content),run_time=.5)
        self.play(Create(absorption_row2_col3_content), run_time=.5)
        
        self.wait(.5)
        self.play(FadeOut(absorption_row2_col0_content), FadeOut(absorption_row2_col2_content),FadeOut(absorption_row2_col3_content),  run_time=.5)
        self.wait(.5)

        absorption_row3_col0_content = SurroundingRectangle(absorption_table.get_entries((4, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        absorption_row3_col2_content = SurroundingRectangle(absorption_table.get_entries((4, 3)),buff=0.05,  color=GREEN, corner_radius=0.02, stroke_width=1)
        absorption_row3_col3_content = SurroundingRectangle(absorption_table.get_entries((4, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
       
        self.play(Create(absorption_row3_col0_content), run_time=.5)
        self.play(Create(absorption_row3_col2_content),run_time=.5)
        self.play(Create(absorption_row3_col3_content), run_time=.5)
        
        self.wait(.5)
        self.play(FadeOut(absorption_row3_col0_content), FadeOut(absorption_row3_col2_content), FadeOut(absorption_row3_col3_content),  run_time=.5)
        self.wait(.5)

        absorption_row4_col0_content = SurroundingRectangle(absorption_table.get_entries((5, 1)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        absorption_row4_col2_content = SurroundingRectangle(absorption_table.get_entries((5, 3)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        absorption_row4_col3_content = SurroundingRectangle(absorption_table.get_entries((5, 4)),buff=0.05,  color=RED, corner_radius=0.02, stroke_width=1)
        
        self.play(Create(absorption_row4_col0_content), run_time=.5)
        self.play(Create(absorption_row4_col2_content),run_time=.5)
        self.play(Create(absorption_row4_col3_content), run_time=.5)
      
        self.wait(.5)
        self.play(FadeOut(absorption_row4_col0_content), FadeOut(absorption_row4_col2_content), FadeOut(absorption_row4_col3_content),  run_time=.5)
        self.wait(.5)
		
        absorption_col0 = SurroundingRectangle(absorption_table.get_columns()[0][1:], color=RED, buff=0.05, fill_color=ORANGE, fill_opacity=0.075,
                                             stroke_width= 1)
        absorption_col3 = SurroundingRectangle(absorption_table.get_columns()[3][1:], color=RED, buff=0.05, fill_color=ORANGE, fill_opacity=0.075,
                                             stroke_width= 1)
        self.add(absorption_col0, absorption_col3)
        self.wait(.5)
        self.play(FadeOut(absorption_group), FadeOut(absorption_col0), FadeOut(absorption_col3),  FadeOut(absorption_bullet_underline), run_time=.5)
        
        self.wait(1)

        # Negation of t and c:  ¬t ≡ c
        tandc_title = Text("Negation of t and c: ¬t ≡ c", font_size=font_size + 8)
        tandc_underline = Line(LEFT*tandc_title.width/2, RIGHT*tandc_title.width/2, stroke_width=1, color=WHITE)
        tandc_underline.next_to(tandc_title, DOWN, buff=0.2)        	

        tandc_bullet_underline = Line(LEFT*tandc.width/2, RIGHT*tandc.width/2, stroke_width=1, color=YELLOW)
        tandc_bullet_underline.next_to(tandc, DOWN, buff=0.1)
        tandc_table = Table(
            [["T", "F", "F"]           ],           
            col_labels=[Text("t"), Text("c"), Text("¬t")],
            include_outer_lines=False,
            line_config={"stroke_width": 1},
        ).scale(0.7).next_to(tandc_underline, DOWN*2, buff=0.5)

        tandc_group = VGroup(tandc_title, tandc_underline, tandc_table)
        tandc_group.arrange(DOWN, aligned_edge=LEFT, buff=0.20).scale(0.6).next_to(box, RIGHT*3) 
        tandc_group.align_to(box, UP)
       
        self.add(tandc_title, tandc_underline, tandc_bullet_underline)
        
       
        self.wait(.5)
        self.play(FadeIn(tandc_table), run_time=.5)
        self.wait(.5)
		
        # ¬t
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
        self.play(FadeOut(tandc_group), FadeOut(tandc_col0), FadeOut(tandc_col2),  FadeOut(tandc_bullet_underline), run_time=.5)
        
        self.wait(1)
''' 
 
# manim -ql -p --disable_caching logic.py Equivalence
# manim -ql -p logic.py Equivalence
