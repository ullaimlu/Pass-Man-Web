import reflex as rx
from PassMan_Web.styles.styles import Color

def passman_assistant() -> rx.Component:
    return rx.hstack(
        rx.image(src="/logog.png", width="3em"),
        rx.box(
            rx.text("Do you have any question?",size="2"),
            border_radius="32em",
            background_color=Color.GRAY.value,
            width="9em",
            padding_x="1em",
            margin_top="1.2em"
        )
    )