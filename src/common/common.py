from manim import * 
from pathlib import Path
from manim import ImageMobject

# This creates a path relative to common.py itself

import manimpango

def layout()->[mobject.types.image_mobject.ImageMobject, mobject.text.text_mobject.Text]:
    ASSET_DIR = Path(__file__).parent.parent / "assets"
    background = ImageMobject(ASSET_DIR / "images" / "blackboard.png").set_opacity(.8)
    manimpango.register_font(str(ASSET_DIR / "fonts" / "nyala_regular.ttf"))
    background.scale_to_fit_width(config.frame_width)
    background.scale_to_fit_height(config.frame_height)
    background.set_z_index(-10)  # Keep behind everything
    bg_text = Text("@BK_BROOK", fill_opacity=0.025).scale(3)
    bg_text.set_z_index(-9)  # Keep behind everything
    return background, bg_text 