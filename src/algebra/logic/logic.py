from manim import * 

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
        title = Text("ምሉእ-ሓሳብ", font_size=40, color=WHITE, font="Nyala").scale(0.9).to_edge(UP)
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
        proposition (ወይ መግለጺ)፣ ዝኾነ ትርጉም ዘለዎ፣ ንፁርን ዘየሻሚን ሓረግ እዩ።
        እቲ ሓረግ፣ ወይ ሓቂ ወይ ሓሶት ክኾን ይኽእል እዪ። 
        ኣብ ሓደ እዋን ግን ክልቲኡ (ወይ ሓቂ ወይ ሓሶት) ክኾን ኣይኽእልን።'''
        statement = Code(
                code_string=statement_definition,
                tab_width=4,
                formatter_style="vim",
                 add_line_numbers=False,
                background="rectangle",                
                background_config={"stroke_color": MAROON, "stroke_width": 2, "fill_color": GREEN, "fill_opacity": 0.025},
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

        x_box = SurroundingRectangle(x, color=MAROON, buff=.1)        
        self.play(Create(x_box))
        self.wait(2)
        he_box = SurroundingRectangle(he, color=MAROON, buff=.1)        
        self.play(Create(he_box))
        self.wait(2)
        self.play(FadeOut(variables), FadeOut(x_box), FadeOut(he_box))
        self.wait(2)
        open_statement_definition = '''መብርሂ: 
        open proposition (ወይ ክፉት-መግለጺ)፣ 
        ሓደ ወይ ልዕሊ ሓደ ተለዋዋጢ ወይ ተውላጠ-ስማት ዝሓዘ ሓረግ ኮይኑ፣
        ነፍሲ ወከፍ ተለዋዋጢ ወይ ተውላጠ-ስማት 
        ብፍሉይ ዋጋ ወይ ውልቀ-ሰብ ምስ ዝትካእ መግለጺ ይኸውን።'''
        open_statement = Code(
                code_string=open_statement_definition,
                tab_width=4,
                formatter_style="vim",
                 add_line_numbers=False,
                background="rectangle",                
                background_config={"stroke_color": MAROON, "stroke_width": 2, "fill_color": GREEN, "fill_opacity": 0.025},
                paragraph_config={"font": "Nyala"},
            ).next_to(underline, DOWN, buff=0.5).shift(LEFT *2)
        self.play(Create(open_statement))
        self.wait(2)

class Negation(Scene):
    def construct(self):
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)  
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
        table.center()
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

class SetColumnColorsExample(Scene):
    def construct(self):
        table = Table(
            [["T", "F"],
            ["F","T"]],
            # row_labels=[Text("R1"), Text("R2")],
            col_cdlabels=[Text("P"), Text("¬P")]
        ).set_column_colors([BLUE], [GREEN],[YELLOW])
        
        col1 = SurroundingRectangle(table.get_columns()[0])
        col2 = SurroundingRectangle(table.get_columns()[1])
        row1 = SurroundingRectangle(table.get_rows()[1])
        row2 = SurroundingRectangle(table.get_rows()[2])
        cell1 = SurroundingRectangle(table.get_cell((1,1)), color=RED)
        cell1_content = SurroundingRectangle(table.get_entries((2, 1)), color=BLUE)
        cell2_content = SurroundingRectangle(table.get_entries((3, 1)), color=BLUE)
        self.play(Create(table), run_time=1)
        self.wait() 
        # self.play(chama.animate.set_opacity(1), run_time=1)
        self.play(Create(col1), run_time=1)
        self.wait() 
        # highlight = table.get_cells((2,1), color=GREEN, fill_opacity=.75)
        # table.add_to_back(highlight)
        self.play(Create(cell1), run_time=1)
        self.wait() 
        self.play(Create(cell1_content), run_time=1)
        self.wait()
        self.play(ReplacementTransform(cell1_content, cell2_content), run_time=1)
        self.wait()
        self.play(FadeOut(cell2_content), ReplacementTransform(col1, col2), run_time=1)
        self.wait()
        # self.play(ReplacementTransform(col1, col2), run_time=1)
        # self.wait()
        self.play(FadeOut(col2), run_time=1)
        self.wait()
        self.play(Create(row1), run_time=1)
        self.wait()
        self.play(ReplacementTransform(row1, row2), run_time=1)
        self.wait()
        