import reflex as rx
import pythonWeb.constants as const
from pythonWeb.componentes.navbar import navbar
from pythonWeb.componentes.footer import footer
from pythonWeb.views.header.header import header
from pythonWeb.views.links.links import links
import pythonWeb.styles.styles as styles

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
                navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                align="center",
                padding=styles.Spacer.LARGE,
                max_width=styles.MAX_WIDTH,
                width="100%",
            ),
        ),
        footer(),
    )

app = rx.App(
    stylesheets=styles.STYLEFONTS,
    style=styles.BASE_STYLE
)
app.add_page(index,
             title="MoreDev | Te enseño programación y desarrollo de software"),
app._compile()