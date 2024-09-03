import reflex as rx
from pythonWeb.styles.styles import Size
from pythonWeb.styles.colors import Color, TextColor
from pythonWeb.styles.fonts  import Font, FontWeight


def info_text(azul: str, texto: str) -> rx.Component:
    return rx.hstack(
        rx.text(
            azul,
            font_weight=FontWeight.EXTRABOLD,
            font_family = Font.DEFAULT,
            color=Color.PRIMARY,
        ),
        rx.text(
            texto,
            font_size=Size.MEDIUM,
            font_weight=FontWeight.LIGHT,
            font_family = Font.DEFAULT,
            color=TextColor.BODY,
        ),
        gap="3px",
        white_space="normal",
        align_items=["start","start","center","center","center"],
        flex_direction=["column", "column", "row", "row", "row"],
    )