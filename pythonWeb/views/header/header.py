import reflex as rx
from pythonWeb.componentes.link_icon import link_icon
from pythonWeb.componentes.info_text import info_text
import pythonWeb.styles.styles as styles
import pythonWeb.styles.colors as colors
def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(src="avatar.jpg",
                      fallback="BR",
                      size="9",
                      radius="full",
                      color_scheme="yellow",
                      variant="solid",
                      high_contrast=False,
                      padding=styles.Size.MEDIUM,
                      border="6px solid ",
                      border_color=colors.Color.PRIMARY),
            rx.vstack(
                rx.text("BRAIS MOURE", size="7", font_weight="700"),
                rx.text("@moredev", size="6", margin_top="0px"),
                rx.hstack(
                    link_icon("twitter", "https://twitter.com"),
                    link_icon("twitch", "https://twitch.com"),
                    link_icon("gitlab", "https://twitch.com"),
                    link_icon("github", "https://github.com"),
                    link_icon("linkedin", "https://linkedin.com"),
                    padding_top="20px",
                    column_gap=styles.Spacer.LARGE,
                ),
                row_gap="0px",
            ),
            align_items="center",
            width="100%",
            justify_content=["center","center","start","start","start"],
            flex_direction=["column", "column", "row", "row", "row"],
        ),
        rx.flex(
            info_text("+14", "años de experiencia"),
            rx.spacer(),
            info_text("+100", "aplicaciones creadas"),
            rx.spacer(),
            info_text("+2M", "seguidores en las redes"),
            width="100%",
            padding_y="40px",
            #flex_direction=["column", "column", "row", "row", "row"],

        ),
        rx.text('Soy Mecánico y Constructor de software desde hace mas de 12 años. Actualmente trabajo como freelance full-stack developer iOS y Android. Además, creo contenido formativo sobre programación en redes. Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!'),
        align="start",
        padding="40px",
        max_width="90%"
    )
