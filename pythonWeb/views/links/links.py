import reflex as rx
import pythonWeb.constants as const
from pythonWeb.componentes.link_button import link_button
from pythonWeb.componentes.title import title
import pythonWeb.styles.styles as styles
#from pythonWeb.styles.styles import Spacer as Spacer

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("twitch","Twich", "Mi canal de esto", const.TWITCH_URL  ),
        link_button("youtube","Youtube", "Libero volutpat sed cras ornare arcu dui. Sed viverra ipsum nunc aliquet bibendum.",const.YOUTUBE_URL),
        link_button("atom","Youtube Secundario", "Consequat interdum varius sit amet mattis vulputate. Nunc aliquet bibendum enim facilisis ",const.YOUTUBE_SECONDARY_URL),
        link_button("instagram","Instagram","Pellentesque sit amet porttitor eget. Sit amet purus gravida quis blandit turpis.", "https://instagram.com/mourdev"),
        link_button("chrome","Discord", "At quis risus sed vulputate odio. Nulla at volutpat diam ut venenatis.",const.DISCORD_URL),

        title("Recursos y Más"),
        link_button("codesandbox","Codesandbox", "Mi canal de esto", const.YOUTUBE_SECONDARY_URL ),
        link_button("codepen","Codepen", "Libero volutpat sed cras ornare arcu dui. Sed viverra ipsum nunc aliquet bibendum.",const.YOUTUBE_URL),
        link_button("trello","Trello", "Consequat interdum varius sit amet mattis vulputate. Nunc aliquet bibendum enim facilisis ",const.YOUTUBE_SECONDARY_URL),
        link_button("linkedin","Linkedin","Pellentesque sit amet porttitor eget.", "https://instagram.com/mourdev"),
        link_button("facebook","Fcebook", "At quis risus sed vulputate odio. Nulla at volutpat diam ut venenatis.","https://discord.gg/mourdev"),

        title("Contacto"),
        link_button("speech","Contacto", "Mi canal∑ de esto", const.YOUTUBE_SECONDARY_URL ),
        link_button("phone","Telefono", "Libero volutpat sed cras ornare arcu dui. Sed viverra ipsum nunc aliquet bibendum.",const.YOUTUBE_URL),
        link_button("mail","Email", "Consequat interdum varius sit amet mattis vulputate. Nunc aliquet bibendum enim facilisis ",const.YOUTUBE_SECONDARY_URL),

        spacing=styles.Size.DEFAULT.value
    )