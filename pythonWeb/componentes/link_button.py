import reflex as rx
import pythonWeb.styles.styles as styles

def link_button(icono: str, title: str, body: str, url: str) -> rx.Component:
    return  rx.link(
        rx.button(
            rx.hstack(
                rx.icon( icono, style=styles.button_icon_style),#size=40 ),
                rx.vstack(
                  rx.text(title, style=styles.button_tittle_style),
                  rx.text(body, style=styles.button_body_style),
                ),
                align="center",
                gap=styles.Spacer.EXTRA_LARGE
            ),
            href=url,
            is_external = True,
        ),
        width="100%",
    )