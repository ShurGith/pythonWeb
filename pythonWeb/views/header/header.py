import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
         rx.flex(
            rx.avatar(src="/logo.svg", fallback="JJ", size="4"),
            rx.text("Reflex User", weight="bold", size="4"),
            rx.text("@reflexuser", color_scheme="gray"),
            rx.button(
                "Edit Profile",
                color_scheme="indigo",
                variant="solid",
            ),
            direction="column",
            spacing="1",
        ),
        align="center"
    )