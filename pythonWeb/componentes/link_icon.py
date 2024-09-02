import reflex as rx
import pythonWeb.styles.styles as styles

def link_icon(icono: str, url: str) -> rx.Component:
    return rx.link(
        rx.icon( icono, size=30, color="black" ),
        href=url,
        is_external=True,
    )
