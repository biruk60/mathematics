from manim import *

class LikeTermsScene(Scene):
    def construct(self):
        # Colors / sizes
        header_color = RED_E
        text_color = BLACK

        # --- Header banner ---
        header_text = Text(
            "To add like terms, add their numerical coefficients.",
            color=WHITE,
            font_size=26,
            weight=BOLD,
        )
        header_box = Rectangle(
            width=header_text.width + 0.6,
            height=header_text.height + 0.4,
            fill_color=header_color,
            fill_opacity=1.0,
            stroke_width=0,
        )
        header_group = VGroup(header_box, header_text).arrange()
        header_group.to_edge(UP, buff=0.6)

        # --- "For example," ---
        for_example = Text("For example,", font_size=26, color=text_color)
        for_example.next_to(header_group, DOWN, aligned_edge=LEFT, buff=0.6)

        # Left examples (numeric and ay^2)
        ex1 = MathTex("5(2)", "+", "3(2)", "=", "8(2)", font_size=34)
        ex1.next_to(for_example, DOWN, aligned_edge=LEFT, buff=0.6)

        # Braces over 5(2) + 3(2)
        brace1_left = Brace(ex1[0:3], UP, buff=0.12)
        brace1_left_text = brace1_left.get_text("")  # empty label, just the brace

        # Second left example: 3ay^2 + 2ay^2 + 5ay^2 = 10ay^2
        ex2 = MathTex(
            "3ay^{2}", "+", "2ay^{2}", "+", "5ay^{2}", "=", "10ay^{2}",
            font_size=34
        )
        ex2.next_to(ex1, DOWN, aligned_edge=LEFT, buff=0.9)

        brace2_left = Brace(ex2[0:5], UP, buff=0.12)
        brace2_left_text = brace2_left.get_text("")

        # Small "and" between the two columns
        and_text = Text("and", font_size=26, color=text_color)
        and_text.next_to(ex2, RIGHT, buff=0.4)

        # Right examples (x and xy)
        ex3 = MathTex("2x", "+", "3x", "=", "5x", font_size=34)
        ex3.to_edge(RIGHT, buff=1.2)
        ex3.align_to(ex1, UP)

        brace1_right = Brace(ex3[0:3], UP, buff=0.12)
        brace1_right_text = brace1_right.get_text("")

        ex4 = MathTex("xy", "+", "xy", "=", "2xy", font_size=34)
        ex4.align_to(ex3, LEFT)
        ex4.next_to(ex3, DOWN, buff=0.9)

        brace2_right = Brace(ex4[0:3], UP, buff=0.12)
        brace2_right_text = brace2_right.get_text("")

        # Collect all mobjects
        all_mobjects = VGroup(
            header_group,
            for_example,
            ex1, brace1_left, brace1_left_text,
            ex2, brace2_left, brace2_left_text,
            and_text,
            ex3, brace1_right, brace1_right_text,
            ex4, brace2_right, brace2_right_text,
        )

        # Optional: scale to fit if needed
        all_mobjects.scale(0.9)
        self.add(all_mobjects)