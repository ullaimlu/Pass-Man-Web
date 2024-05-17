import reflex as rx
from PassMan_Web.styles.styles import Color

def my_space_tittle(tab:str) -> rx.Component:
    return rx.box(
        rx.text(tab,size="6", weight="bold"),
        border_radius="3em",
        width="80em",
        height="4em",
        background_color=Color.LILAC.value,
        padding_x="2em",
        padding_y="1em",
        margin_top="4em"
    )
    
def my_space(tab:str, content:rx.Component) -> rx.Component:
    return rx.scroll_area(
        content,
        border_radius="1em",
        width="80em",
        height="44em",
        margin_top="0.5em",
        background_color=Color.LILAC.value,
    )
