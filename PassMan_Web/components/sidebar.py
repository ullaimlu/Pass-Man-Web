import reflex as rx
from PassMan_Web.styles.styles import Color
from PassMan_Web.components.sidebar_button import *
from PassMan_Web.components.passman_assistant import *


def sidebar() -> rx.Component:
    return rx.box(
            rx.vstack(
            rx.hstack(
                rx.text("Pass",
                    color= Color.WHITET.value,
                    font_size="3em",
                    font_weight="bold"), 
                rx.text("Man", 
                    color=Color.GRAY.value,
                    font_size="3em",
                    font_weight="bold"),  
            ),
                
            sidebar_button1("New","plus"),
            sidebar_button2("My Websites","globe","../../user/courses/1"),
            rx.spacer(),
            passman_assistant(),
            height="100%",
            z_index="5",
            padding_x="2em",
            padding_y="1em",
            align_items="left",
        ),
        width="25.5em",
        height="54.3em",
    )