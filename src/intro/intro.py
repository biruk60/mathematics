from manim import * 
import manimpango

def layout()->[mobject.types.image_mobject.ImageMobject, mobject.text.text_mobject.Text]:
    background = ImageMobject("assets/images/blackboard.png").set_opacity(.8)
    manimpango.register_font("assets/fonts/nyala_regular.ttf")
    background.scale_to_fit_width(config.frame_width)
    background.scale_to_fit_height(config.frame_height)
    background.set_z_index(-10)  # Keep behind everything
    bg_text = Text("@BK_BROOK", fill_opacity=0.025).scale(3)
    bg_text.set_z_index(-9)  # Keep behind everything
    return background, bg_text 

class IntroScene(ThreeDScene):
    def construct(self):
        
        background, bg_text = layout()
        self.add_fixed_in_frame_mobjects(background)
        self.add_fixed_in_frame_mobjects(bg_text)
        
        self.wait()
        # Texts
        share_text = Text("ሒሳብ", font_size=36, color='#52B2BF', font="Nyala").shift(3*LEFT)
        like_text = Text("ምስ", font_size=36, color='#708238', font="Nyala").next_to(share_text, 1.5*RIGHT)
        subscribe_text = Text("ብሩኽ", font_size=36, color='#EDC001', font="Nyala").next_to(like_text, 1.5*RIGHT)
        buff=0.3
        
        self.play(FadeIn(share_text), FadeIn(like_text), FadeIn(subscribe_text), run_time=1)
        # self.add_sound("assets/sounds/Outro/share_like_subscribe.mp3")
        self.play(Circumscribe(share_text, Circle, color='#52B2BF', buff=buff), run_time=.3)
        self.play(Circumscribe(share_text, Circle, True,color='#52B2BF', buff=buff), run_time=.3)
        self.wait()
        self.play(Circumscribe(like_text, Rectangle, color='#708238', buff=buff), run_time=.35)
        self.play(Circumscribe(like_text, Rectangle, True,color='#708238', buff=buff), run_time=.2)
        self.wait()
        self.play(Circumscribe(subscribe_text, Circle, color='#EDC001', buff=buff), run_time=.5)
        self.play(Circumscribe(subscribe_text, Circle, True,color='#EDC001', buff=buff), run_time=.5)
        final_group = VGroup(share_text, like_text, subscribe_text)
        self.play(ShrinkToCenter(final_group), run_time=1)   
        self.wait(1)     
        
        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            x_length=8,
            y_length=6,
            z_length=6,           
            axis_config={'tip_shape': StealthTip } 
        )
                
        graph = axes.plot(lambda x: x ** 2, x_range=[-2, 2, 1], color=BLUE)
        rects = axes.get_riemann_rectangles(
                                graph,
                                x_range=[-2, 2],
                                dx=0.08,
                                color=BLUE
                                
                            )

        graph2 = axes.plot_parametric_curve(
            lambda t: np.array([np.cos(t), np.sin(t), t]),
            t_range=[-2 * PI, 2 * PI],
            color='#EDC001',
        )
        self.play(GrowFromPoint(axes, ORIGIN),runt_time=.5)
        self.play(Create(graph), run_time=.5)
        # self.play(FadeIn(axes, runt_time=1), FadeIn(graph, run_time=2))
        self.wait(.5)

        ##THE CAMERA IS AUTO SET TO PHI = 0 and THETA = -90

        self.move_camera(phi=60 * DEGREES)
        self.wait(.5)
        self.move_camera(theta=-45 * DEGREES)

        self.begin_ambient_camera_rotation(
            rate=PI / 10, about="theta"
        )  # Rotates at a rate of radians per second
        self.wait(.5)
        self.play(Create(rects), run_time=3)
        self.play(Create(graph2))
        self.wait(.5)
        self.stop_ambient_camera_rotation()

        self.wait(.5)
        self.begin_ambient_camera_rotation(
            rate=PI / 10, about="phi"
        )  # Rotates at a rate of radians per second
        self.wait(.5) 
        self.stop_ambient_camera_rotation()
        self.wait(.5)
        what = VGroup(axes, graph, graph2, rects)
        self.play(ShrinkToCenter(what))
        self.wait(1.5)       

        
        # manim -ql -p --disable_caching  -o intro_video.mp4 .\intro.py IntroScene