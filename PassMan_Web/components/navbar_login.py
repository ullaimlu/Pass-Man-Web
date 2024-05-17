import reflex as rx
from PassMan_Web.styles.colors import *

def navbar_login() ->rx.Component:
    return rx.hstack(
        rx.text("Pass",
            color= Color.WHITET.value,
            margin_left="0.6em",
            font_size="3em",
            font_weight="bold",
            margin_top= "0.2em",), 
        rx.text("Man", 
            color=Color.GRAY.value,
            font_size="3em",
            font_weight="bold",
            margin_top= "0.2em",),
        rx.spacer(),
        rx.button(
            "Sign Up",
            _hover={"background_color": Color.GRAY.value},
            background_color=Color.LILAC.value,
            color=Color.BLACK.value,
            padding_x= "3em",
            padding_y= "2em",
            border_radius="3em",
            margin_top= "1.1em",
            text_align="left",
            on_click= rx.redirect("/sign-up")
        ),
        width="98%",
    )

def navbar_sign_up() ->rx.Component:
    return rx.hstack(
        rx.text("Pass",
            color= Color.WHITET.value,
            margin_left="0.6em",
            font_size="3em",
            font_weight="bold",
            margin_top= "0.2em",), 
        rx.text("Man", 
            color=Color.GRAY.value,
            font_size="3em",
            font_weight="bold",
            margin_top= "0.2em",),
        rx.spacer(),
        rx.button(
            "Sign In",
            _hover={"background_color": Color.GRAY.value},
            background_color=Color.LILAC.value,
            color=Color.BLACK.value,
            padding_x= "3em",
            padding_y= "2em",
            border_radius="3em",
            margin_top= "1.1em",
            text_align="left",
            on_click= rx.redirect("../")
        ),
        width="98%",
    )