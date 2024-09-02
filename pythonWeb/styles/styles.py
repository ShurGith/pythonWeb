from enum import Enum
import reflex as rx
from .colors import Color, TextColor
#Constantes
MAX_WIDTH = "900px"


#Tamaños
class Spacer(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.9em"
    DEFAULT = "1em"
    LARGE = "2em"
    EXTRA_LARGE = "3em"

class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    DEFAULT_BIG = "1.3em"
    LARGE = "2em"
    EXTRA_LARGE = "3em"

#Styles
BASE_STYLE = {
    "background-color": Color.BACKGROUND,
    "color":TextColor.BODY,
    rx.button:{
        "width":"100%",
        "height":"100%",
        "cursor":"pointer",
        "display":"block",
        "color":TextColor.HEADER,
        "padding_y":Spacer.EXTRA_LARGE,
        "padding_x": Spacer.EXTRA_LARGE,
        "border_radius":Size.LARGE,
        "background-color":Color.CONTENT,
        "transition":".3s ease-in-out",
        "_hover":{
            "background_color":Color.SECONDARY,
        },
    },
    rx.link:{
        "text_decoration": "none",
        "_hover":{
            "color": "red",
        },
    },
}

section_tittle_style=dict(
   font_size = Size.LARGE,
   padding_top=Size.DEFAULT,
   color=TextColor.HEADER,
   padding_bottom=Spacer.SMALL,
   border_bottom_color=TextColor.HEADER, 
   border_bottom="4px solid",
   margin_bottom= Spacer.SMALL,
)
tittle_style=dict(
   size="6",
   width="100%",
   padding_top=Size.DEFAULT,
   color=TextColor.BODY,
)

button_icon_style = dict(
    font_size = Size.LARGE,
    stroke=Color.ICON,
    width=Size.LARGE,
    height=Size.LARGE,
)

button_tittle_style = dict(
    font_size = Size.LARGE,
    color=TextColor.HEADER,
    font_weight="700"
)

button_body_style = dict(
    font_size = Size.MEDIUM
)