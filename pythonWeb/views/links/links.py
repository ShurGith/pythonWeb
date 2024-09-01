import reflex as rx
from pythonWeb.componentes.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twich", "https://twitch.tv/mourdev"),
        link_button("Youtube", "https://youtube.com/mourdev"),
        link_button("Youtube Secundario", "https://twitch.tv/mourdev"),
        link_button("Instagram", "https://instagram.com/mourdev"),
        link_button("Discord", "https://discord.gg/mourdev"),
    )