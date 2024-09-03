from enum import Enum
import reflex as rx
from .colors import Color, TextColor
from .fonts import Font, FontWeight
#Constantes
MAX_WIDTH = "900px"


STYLEFONTS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    "/css/styles.css",
]

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
     "font_family":Font.DEFAULT,
     "font_weight":FontWeight.MEDIUM,
     "font_size":Size.MEDIUM,
    rx.button:{
        "width":"99%",
        "height":"100%",
        "cursor":"pointer",
        "display":"flex",
        "color":TextColor.HEADER,
        "padding_y":Spacer.EXTRA_LARGE,
        "padding_x": Spacer.EXTRA_LARGE,
        "border_radius":Size.LARGE,
        "background-color":Color.CONTENT,
        "text_align" : "start",
        "white_space": "normal",
        "justify_content":"start",
        "transition":".3s ease-in-out",
        "_hover":{
            "background_color":Color.SECONDARY,
        },
    },
    rx.link:{
        "text_decoration": "none",
        "color": Color.SECONDARY,
        "_hover":{
            "color": "red !important",
        },
    },
}

section_tittle_style=dict(
   font_size = Size.EXTRA_LARGE,
   font_family=Font.TITLE,
   font_weight=FontWeight.BOLD,
   padding_top=Size.DEFAULT,
   color=TextColor.HEADER,
   padding_bottom=Spacer.SMALL,
   border_bottom_color=TextColor.HEADER,
   border_bottom="4px solid",
   margin_bottom= Spacer.SMALL,
)
tittle_style=dict(
   font_size = Size.EXTRA_LARGE,
   padding_top=Size.DEFAULT,
   color=TextColor.BODY,
   font_family=Font.TITLE,
   font_weight=FontWeight.BOLD,
)

button_icon_style = dict(
    font_size = Size.LARGE,
    stroke=Color.ICON,
    width=Size.LARGE,
    height=Size.LARGE,
)

button_tittle_style = dict(
    font_size = Size.LARGE,
    color=TextColor.BODY,
    font_family=Font.TITLE,
    font_weight=FontWeight.EXTRABOLD,
)

button_body_style = dict(
    font_size = Size.MEDIUM,
    color=TextColor.BODY,
    font_family=Font.DEFAULT,
    font_weight=FontWeight.LIGHT,
)