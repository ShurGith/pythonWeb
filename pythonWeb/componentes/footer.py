import reflex as rx
import datetime
def footer() -> rx.Component:
    return rx.hstack(
        rx.image(src="/favicon.ico", width="20px", height="auto"),
        rx.text(f"© 2014-{datetime.date.today().year} "),
        rx.link("MoureDev by Brais Moure v4.", href= "htpps://mouredev.com", is_external = True),
        rx.text("\n BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD."),
        justify="center",
        align="center",
    )