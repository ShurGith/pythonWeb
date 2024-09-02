import reflex as rx
import datetime
from pythonWeb.styles.styles import Size, Spacer as Size, Spacer


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="/favicon.ico", width="50px", height="auto", margin_bottom=Spacer.SMALL),
        rx.link(f"© 2014-{datetime.date.today().year} MoureDev by Brais Moure v4.", 
        href= "htpps://mouredev.com", 
        is_external = True,
        ),
        rx.text("\n BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD."),
        justify="center",
        align="center",
        margin_y=Size.EXTRA_LARGE,
        font_size=Size.MEDIUM,
        gap=Spacer.SMALL
    )