import reflex as rx
from pythonWeb.styles.styles import Size
from pythonWeb.styles.colors import Color, TextColor


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            as_="span",
            font_weight="bold",
            color=Color.PRIMARY
        ),
        f" {body}",
        font_size=Size.MEDIUM,
        color=TextColor.BODY
    )