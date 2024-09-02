import reflex as rx
import pythonWeb.styles.styles as styles

def title(text: str)->rx.Component:
   return rx.heading(
        text,
        size="8",
        #text_decoration="underline",
        padding_bottom="8px",
        padding_right="40px",
        border_bottom="6px solid black",
        width="max-content",
        style=styles.tittle_style,
    )