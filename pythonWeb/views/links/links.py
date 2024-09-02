import reflex as rx
from pythonWeb.componentes.link_button import link_button
from pythonWeb.componentes.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("twitch","Twich", "Mi canal de esto", "https://twitch.tv/mourdev" ),
        link_button("youtube","Youtube", "Libero volutpat sed cras ornare arcu dui. Sed viverra ipsum nunc aliquet bibendum.","https://youtube.com/mourdev"),
        link_button("atom","Youtube Secundario", "Consequat interdum varius sit amet mattis vulputate. Nunc aliquet bibendum enim facilisis ","https://twitch.tv/mourdev"),
        link_button("instagram","Instagram","Pellentesque sit amet porttitor eget. Sit amet purus gravida quis blandit turpis.", "https://instagram.com/mourdev"),
        link_button("chrome","Discord", "At quis risus sed vulputate odio. Nulla at volutpat diam ut venenatis.","https://discord.gg/mourdev"),

        title("Códigos"),
        link_button("codesandbox","Codesandbox", "Mi canal de esto", "https://twitch.tv/mourdev" ),
        link_button("codepen","Codepen", "Libero volutpat sed cras ornare arcu dui. Sed viverra ipsum nunc aliquet bibendum.","https://youtube.com/mourdev"),
        link_button("trello","Trello", "Consequat interdum varius sit amet mattis vulputate. Nunc aliquet bibendum enim facilisis ","https://twitch.tv/mourdev"),
        link_button("linkedin","Linkedin","Pellentesque sit amet porttitor eget. Sit amet purus gravida quis blandit turpis.", "https://instagram.com/mourdev"),
        link_button("facebook","Fcebook", "At quis risus sed vulputate odio. Nulla at volutpat diam ut venenatis.","https://discord.gg/mourdev"),
    )