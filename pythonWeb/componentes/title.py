import reflex as rx
import pythonWeb.styles.styles as styles

def title(text: str)->rx.Component:
   return rx.heading(
        text,
        #size="8",
        style=styles.section_tittle_style,
    )