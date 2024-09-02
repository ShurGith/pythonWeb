from enum import Enum
import reflex as rx
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
    rx.button:{
        "width":"100%",
        "height":"100%",
        "cursor":"pointer",
        "display":"block",
        "padding_y":Spacer.EXTRA_LARGE,
        "padding_x": Spacer.EXTRA_LARGE,
        "border_radius":Size.LARGE,
    },
    rx.link:{
        "text_decoration": "none",
        "color": "red",
        "_hover":{
            "color": "red",
        },
    },
}

tittle_style=dict(
   size="6",
   width="100%",
   padding_top=Size.DEFAULT,
)

button_tittle_style = dict(
    font_size = Size.LARGE.value,
    color="#000",
    font_weight="700"
)

button_body_style = dict(
    font_size = Size.MEDIUM.value
)