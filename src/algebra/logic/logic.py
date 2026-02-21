from manim import * 
import manimpango
from common.common import layout

class Introduction(Scene):
    def construct(self):
        
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)        
               
        # Title
        title = Text("መእተዊ", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
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
        self.wait(3)
 # manim -ql -p --disable_caching logic.py Introduction

class Statement(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)  
        title = Text("ሓረግ", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)
        self.add(title)
        self.add(underline)
        font_size =28
        first_sentence = MarkupText("1. እዙይ ሕብሪ ፃዕዳ እዩ።", font_size=font_size, font="Nyala")
        second_sentence = MarkupText("2. በይዛኻ እንዶ ተማላኣኒ!?", font_size=font_size, font="Nyala")
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

        box_one = SurroundingRectangle(first_sentence, color=YELLOW, buff=.1)        
        self.play(Create(box_one))
        self.wait(2)

        self.play(FadeOut(BulletedList), FadeOut(box_one))
        self.wait(2)

        

        statement_definition = '''መብርሂ: 
        proposition (ሓሳብ)፣ ዝኾነ ትርጉም ዘለዎ፣ ንፁርን ዘየሻሚን ሓረግ እዩ።
        እቲ ሓረግ፣ ወይ ሓቂ ወይ ሓሶት ክኾን ይኽእል እዪ። 
        ኣብ ሓደ እዋን ግን ክልቲኡ (ወይ ሓቂ ወይ ሓሶት) ክኾን ኣይኽእልን።'''
        statement = Code(
                code_string=statement_definition,
                tab_width=4,
                formatter_style="vim",
                 add_line_numbers=False,
                background="rectangle",                
                background_config={"stroke_color": MAROON, "stroke_width": 2, "fill_color": ORANGE, "fill_opacity": 0.05},
                paragraph_config={"font": "Nyala"},
            ).next_to(underline, DOWN, buff=0.5).shift(LEFT *2)
        self.play(Create(statement))
        self.wait(2)
        self.play(FadeOut(statement))
        self.wait(2)
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

        x_box = SurroundingRectangle(x, color=YELLOW, buff=.1)        
        self.play(Create(x_box))
        self.wait(2)
        he_box = SurroundingRectangle(he, color=YELLOW, buff=.1)        
        self.play(Create(he_box))
        self.wait(2)
        self.play(FadeOut(variables), FadeOut(x_box), FadeOut(he_box))
        self.wait(2)
        open_statement_definition = '''መብርሂ: 
        open proposition (ክፉት ሓሳብ)፣ 
        ሓደ ወይ ልዕሊ ሓደ ተለዋዋጢ ወይ ተውላጠ-ስማት ዝሓዘ ሓረግ ኮይኑ፣
        ነፍሲ ወከፍ ተለዋዋጢ ወይ ተውላጠ-ስማት 
        ብፍሉይ ዋጋ ወይ ውልቀ-ሰብ ምስ ዝትካእ ሓሳብ ይኸውን።'''
        open_statement = Code(
                code_string=open_statement_definition,
                tab_width=4,
                formatter_style="vim",
                 add_line_numbers=False,
                background="rectangle",                
                background_config={"stroke_color": YELLOW, "stroke_width": 2, "fill_color": ORANGE, "fill_opacity": 0.05},
                paragraph_config={"font": "Nyala"},
            ).next_to(underline, DOWN, buff=0.5).shift(LEFT *2)
        self.play(Create(open_statement))
        self.wait(2)

        
# manim -ql -p --disable_caching logic.py Statement


class Propositions(Scene):
    def construct(self):        
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)        
               
        # Title
        title = Text("ዓይነታት ሓሳባት", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
       
        simple_statement_definition_title = MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")       
        simple_statement_definition_1 = MarkupText("simple proposition (ቐሊል ሓሳብ) ከም <span fgcolor='YELLOW'>and (ከምኡ እውን)</span> ፡ <span fgcolor='YELLOW'>or (ወይ)</span> ፡ <span fgcolor='YELLOW'>not (ኣይኰነን)</span>፡ ወዘተ...",font_size=30, color=WHITE, font="Nyala")
        simple_statement_definition_2 = MarkupText("ዝኣመሰሉ ጠመርቲ ቃላት ዘይብሉ፣ ሓደ ሓሳብ ዘመሓላልፍ ሓረግ እዩ።",font_size=30, color=WHITE, font="Nyala")        
        simple_statement_definition = VGroup(simple_statement_definition_title, simple_statement_definition_1, simple_statement_definition_2).scale(.5).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).shift(LEFT*1)
        
        simple_box = SurroundingRectangle(simple_statement_definition, color=YELLOW, buff=0.4, fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2)
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
        
        compound_box = SurroundingRectangle(compound_statement_definition, color=YELLOW, buff=0.4, fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2)
        self.add(compound_statement_definition_title,
                  compound_statement_definition_1,                  
                  compound_box)
        self.wait(2)
        self.wait(2)
        third_statement_1 = MarkupText(
            "ሀ. ናይ 1 ርብዒ ሱር 1 ኮይኑ",
            font_size=30, font="Nyala"
        )
        third_statement_2 = MarkupText(
            " ኮይኑ ከምኡ",
            font_size=30, font="Nyala"
        )
        third_statement_3 = MarkupText(
            " ሰለስተ ካብ ኣርባዕተ ዝነኣሰ እዩ።",
            font_size=30, font="Nyala"
        )
        fourth_statement_1 = MarkupText(
            "ለ. ድሕሪ ሰሉስ ዘሎ መዓልቲ ረቡዕ",
            font_size=30, font="Nyala"
        ) 
        fourth_statement_2 = MarkupText(
            " ወይ",
            font_size=30, font="Nyala"
        )  
        fourth_statement_3 = MarkupText(
            " ክልተ ክድመር ክልተ ኣርባዕተ እዩ።",
            font_size=30, font="Nyala"
        )   
        third_statement =VGroup(third_statement_1, third_statement_2, third_statement_3).arrange(RIGHT)
        fourth_statement =VGroup(fourth_statement_1, fourth_statement_2, fourth_statement_3).arrange(RIGHT)
        compound_sentences = VGroup(third_statement, fourth_statement).arrange(DOWN*4, aligned_edge=LEFT, buff=0.5).scale(.5).next_to(compound_statement_definition, DOWN*3, buff=0.5)      
        self.play(FadeIn(third_statement_1), FadeIn(third_statement_2), FadeIn(third_statement_3))
        self.wait(2)
        br1 = BraceText(third_statement_1, "1", label_constructor=Text, font_size =20,  brace_config={
                
                "stroke_width": 0.25
            },           
        buff=0.05  ).set_color(ORANGE).set_stroke(width=.5)
        self.add(br1)
        self.wait(2)
        br2 = BraceText(third_statement_3, "2", brace_direction=UP , label_constructor=Text, font_size =20,  brace_config={
                
                "stroke_width": 0.25
            },           
        buff=0.05).set_color(ORANGE)
        self.add(br2)
        self.wait(2)
        third_box = SurroundingRectangle(third_statement_2, color=YELLOW, buff=.1)        
        self.play(Create(third_box))
        self.wait(2)
        self.play(FadeIn(fourth_statement_1), FadeIn(fourth_statement_2), FadeIn(fourth_statement_3))
        self.wait(2) 
        
        br3 = BraceText(fourth_statement_1, "1", label_constructor=Text, font_size =20,  brace_config={
                
                "stroke_width": 0.25
            },           
        buff=0.05).set_color(ORANGE).set_stroke(width=.5)
        self.add(br3)
        self.wait(2)
        br4 = BraceText(fourth_statement_3, "2", brace_direction=UP, label_constructor=Text, font_size =20,  brace_config={
                
                "stroke_width": 0.25
            },           
        buff=0.05).set_color(ORANGE)
        self.add(br4)
        self.wait(2)
        fourth_box = SurroundingRectangle(fourth_statement_2, color=YELLOW, buff=.1)        
        self.play(Create(fourth_box))
        self.wait(2)
# manim -ql -p --disable_caching logic.py Propositions

class Connectives(Scene):
    def construct(self):        
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)        
               
        # Title
        title = Text("መጥመርቲ", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        font_size =28
        negation = MarkupText("1. Negation", font_size=font_size)
        conjunction = MarkupText("2. Conjunction", font_size=font_size)
        disjunction = MarkupText("3. Disjunction", font_size=font_size)
        implication = MarkupText("4. Implication", font_size=font_size)
        biImplication = MarkupText("5. Bi-implication", font_size=font_size)

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
        title = Text("Negation", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        
        negation_definition_title = MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")
       
        negation_definition_1 = MarkupText("p ዝባሃል ሓሳብ እንተልዩ፣ <span fgcolor='{ORANGE}'>¬p</span> ናይ p ምኽሓድ ምልክት እዩ።",font_size=30, color=WHITE, font="Nyala")
        negation_definition_2 = MarkupText("'p ኣይኾነን እዩ' ብዝብል ሓሳብ ኢልና ንገልፆ።",font_size=30, color=WHITE, font="Nyala")
        
        disjunction_definition = VGroup(negation_definition_title, negation_definition_1, negation_definition_2).scale(.7).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).shift(LEFT*1)
        
        box = SurroundingRectangle(disjunction_definition, color=YELLOW, buff=0.4, fill_color=ORANGE, fill_opacity=0.05, corner_radius=0.2)
        self.add(negation_definition_title,
                  negation_definition_1,
                  negation_definition_2,
                  box)
        self.wait(2)
        font_size =28
        ex_one = MarkupText("P = እቲ ቤተ መፃሕፍቲ ሕዚ ኽፉት እዩ።", font_size=font_size, font="Nyala")
        ex_one_not = MarkupText("¬P = እቲ ቤተ መፃሕፍቲ ሕዚ ኽፉት ኣይኾነን እዩ።", font_size=font_size, font="Nyala")
        ex = VGroup(ex_one, ex_one_not)
        ex.arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(disjunction_definition, DOWN, buff=0.5)

        self.play(FadeIn(ex_one))
        self.wait(2) 
        self.play(FadeIn(ex_one_not))
        self.wait(2)
        self.play(FadeOut(ex), FadeOut(disjunction_definition), FadeOut(box))
        self.wait(2)
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
            
        self.wait(2) 
        self.play(table.animate.set_opacity(0)) 
        self.wait(2)

# manim -ql -p --disable_caching logic.py Negation

class Disjunction(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)        
               
        # Title
        title = Text("Disjunction", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
        underline = Line(LEFT*title.width/2, RIGHT*title.width/2, stroke_width=4, color=WHITE)
        underline.next_to(title, DOWN, buff=0.2)

        self.add(title)
        self.add(underline)
        disjunction_definition_title = MarkupText("<span underline='low' underline_color='#FFFF00'>መብርሂ:</span>",font_size=40, color=WHITE, font="Nyala")
       
        disjunction_definition_1 = MarkupText("pን qን ዝባሃሉ ክልተ ሓሳባት እንተልዮም፣ ናይ pን qን disjunction፣",font_size=30, color=WHITE, font="Nyala")
        disjunction_definition_2 = MarkupText("ወይ p ሓቂ እንተኾይኑ ወይ q ሓቂ እንተኾይኑ ወይ pን qን ክልቲኦም ሓቂ እንተኾይኖም፣ <span font_family='Sans' fgcolor='{ORANGE}'>p ∨ q</span> ሓቂ እዩ ብይብል።",font_size=30, color=WHITE, font="Nyala")
        disjunction_definition_3 = MarkupText("ምልክቱ ድማ፣ <span font_family='Sans' fgcolor='{ORANGE}'>p ∨ q</span> እዩ።",font_size=30, color=WHITE, font="Nyala")
        disjunction_definition = VGroup(disjunction_definition_title, disjunction_definition_1, disjunction_definition_2, disjunction_definition_3).scale(.7).arrange(DOWN, aligned_edge=LEFT).next_to(underline, DOWN*2, buff=0.5).shift(LEFT*1)
        
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
        )            
        table.scale(.7).next_to(underline, DOWN, buff=0.5).center()
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
        self.wait(1)
        self.play(second_col[1].animate.set_opacity(1))
        self.wait(1)
        self.play(third_col[1].animate.set_opacity(1))
        self.wait(1)
    
        for cell in first_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(2)
        
        for cell in second_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(2) 

        for cell in third_col[0]:
            self.play(cell.animate.set_opacity(1))
            self.wait(0.3)            
        self.wait(2)

        self.play(table.animate.set_opacity(0)) 
        self.wait(2)

# manim -ql -p --disable_caching logic.py Disjunction
