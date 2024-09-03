import reflex as rx
from pythonWeb.styles.styles import Size as Size
from pythonWeb.styles.colors import Color as Color
from pythonWeb.styles.fonts import Font, FontWeight


def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.image(src="/logo.svg"),
            rx.flex(
                rx.text("moure", color=Color.PRIMARY),
                rx.text("dev",  color=Color.SECONDARY),
                font_family=Font.LOGO,
                font_size=Size.LARGE,
                font_weight=FontWeight.LIGHT
            ),
            justify="center",
            align_items="center",
        ),
        position="sticky",
        top="0px",
        background="rgba(64, 125, 199, 0.4)",
        box_shadow="0 4px 30px #6496311a",
        backdrop_filter="blur(5px)",
        padding_y=Size.DEFAULT_BIG,
        padding_x=Size.EXTRA_LARGE,
        z_index= 999,
    )