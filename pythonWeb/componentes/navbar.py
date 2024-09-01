import reflex as rx

def navbar() -> rx.Component:
    return rx.vstack(
        rx.text(
            "mouredev",
            height="40px", color="#ffffff", font_size="1.5em", font_weight="700",cursor="pointer"
        ),
        position="sticky",
        background="#083762",
        padding_x="16px",
        padding_y="8px",
        z_index= 999,
    )