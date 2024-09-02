import reflex as rx
from pythonWeb.styles.colors import TextColor

def link_icon(icono: str, url: str) -> rx.Component:
    return rx.link(
        rx.icon( 
            icono, 
            size=30, 
            color=TextColor.BODY,
        ),
        href=url,
        is_external=True,
    )
