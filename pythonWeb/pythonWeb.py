import reflex as rx
from pythonWeb.componentes.navbar import navbar
from pythonWeb.componentes.footer import footer
from pythonWeb.views.header.header import header
from pythonWeb.views.links.links import links

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
       # rx.box(
            navbar(),
            header(),
            rx.text('Soy ingeniero de software y actualmente trabajo como freelance full-stack developer iOS y Android. Además, creo contenido formativo sobre programación en redes. Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!'),
            links(),
            footer(),
            border="1px solid red",
            display="flex",
            flex_direction="column",
            align_items="center",
            gap="20px",

      #  ),
        #border="1px solid green"
    )


app = rx.App()
app.add_page(index)
app._compile()