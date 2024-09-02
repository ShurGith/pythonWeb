import reflex as rx
from pythonWeb.styles.styles import Size as Size

def navbar() -> rx.Component:
    return rx.hstack(
        rx.avatar(src="/logo.svg", fallback="JJ", size="4"),
        rx.text(
            "mouredev",
            height="40px", color="#ffffff", font_size="1.5em", font_weight="700",cursor="pointer"
        ),
        position="sticky",
        top="0px",
        background="lightgray",
        padding_y=Size.DEFAULT_BIG,
        padding_x=Size.EXTRA_LARGE,
        z_index= 999,
    )