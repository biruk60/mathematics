
from manim import * 


from common.common import layout, add_shadow

class OutroScene(Scene):
    def construct(self):
       
        background, bg_text = layout()
        self.add(background)
        self.add(bg_text)
        
        self.wait()   
             
        # Texts
        share_text = add_shadow(Text("Share.", font_size=44, color="#054114").shift(3*LEFT))
        like_text = add_shadow(Text("Like.", font_size=44, color="#0B0B46").next_to(share_text, 1.5*RIGHT))
        subscribe_text = add_shadow(Text("Subscribe.", font_size=44, color='#EDC001').next_to(like_text, 1.5*RIGHT)).shift(UP*.05)
        
        bell = SVGMobject("../assets/svgs/bell.svg").scale(0.2)
        bell.set_color('#EDC001')  
        bell.next_to(subscribe_text, UP*.7, buff=0.1)
        
        bell_shadow = add_shadow(bell)

        like = SVGMobject("../assets/svgs/like.svg").scale(0.2)
        like.set_color('#0B0B46')  
        like.next_to(like_text, UP*.7, buff=0.1)
        
        like_shadow = add_shadow(like)

        share = SVGMobject("../assets/svgs/share.svg").scale(0.2)
        share.set_color('#054114')  
        share.next_to(share_text, UP*.7, buff=0.1)
        
        share_shadow = add_shadow(share, color=BLACK, opacity=0.1, shift=(0.025,-0.025,0))
        
        v_share = VGroup(share_text,  share_shadow)
        v_like = VGroup(like_text, like_shadow)
        v_subscribe = VGroup(subscribe_text, bell_shadow)

        buff=0.3
        self.play(FadeIn(share_text), FadeIn(like_text), FadeIn(subscribe_text), 
                  FadeIn(bell_shadow), FadeIn(like_shadow),FadeIn(share_shadow), run_time=1)
        # self.add_sound("assets/sounds/Outro/share_like_subscribe.mp3")
        self.play(Circumscribe(v_share, Circle, color='#054114', buff=buff), run_time=.3)
        self.play(Circumscribe(v_share, Circle, True,color='#054114', buff=buff), run_time=.3)
        self.wait()
        self.play(Circumscribe(v_like, Rectangle, color="#0B0B46", buff=buff), run_time=.35)
        self.play(Circumscribe(v_like, Rectangle, True,color='#0B0B46', buff=buff), run_time=.2)
        self.wait()
        self.play(Circumscribe(v_subscribe, Circle, color='#EDC001', buff=buff), run_time=.5)
        self.play(Circumscribe(v_subscribe, Circle, True,color='#EDC001', buff=buff), run_time=.5)
        final_group = VGroup(v_share, v_like, v_subscribe)
        self.play(ShrinkToCenter(final_group), run_time=1)   
        self.wait(1)
        # manim -ql -p --disable_caching  -o outro_video.mp4 .\outro.py OutroScene