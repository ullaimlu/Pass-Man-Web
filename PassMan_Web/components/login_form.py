import reflex as rx
from PassMan_Web.styles.colors import *

def login_form() -> rx.Component:
    return rx.center(
        rx.flex(
            rx.form(
                rx.center(
                    rx.text("Sign in",
                        color= Color.WHITET.value,
                        font_size="3em",
                        font_weight="bold"), 
                    width="100%"),
                rx.text("Email",
                    margin_top="1em",
                    color= Color.WHITET.value,
                    margin_left="0.5em",
                    font_size="1em",
                    font_weight="bold"), 
                rx.input(
                    name="email",
                    border= "none",
                    border_top= "1px",
                    background= Color.LILAC2.value,
                    height="3em"),
                rx.text("Password",
                    margin_top="1em",
                    color= Color.WHITET.value,
                    margin_left="0.5em",
                    font_size="1em",
                    font_weight="bold"), 
                rx.input(
                    name="pass",
                    border= "none",
                    border_top= "1px",
                    background= Color.LILAC2.value,
                    height="3em"),
                rx.center(
                    rx.text("¿Forgot your password?",
                        margin_top="1em",
                        color= Color.WHITET.value,
                        margin_left="0.5em",
                        text_decoration="underline white",
                        font_size="1em",
                        font_weight="bold"), 
                ),
                
                rx.flex(
                    rx.button(
                        "Sign In",
                        _hover={"background_color": Color.GRAY.value},
                        background_color=Color.LILAC.value,
                        color=Color.BLACK.value,
                        padding_x= "3em",
                        padding_y= "2em",
                        margin_left="2.5em",
                        border_radius="3em",
                        margin_top= "1em",
                        text_align="left", 
                    ),
                    rx.button(
                        "Sign In with Google",
                        _hover={"background_color": Color.GRAY.value},
                        background_color=Color.LILAC.value,
                        color=Color.BLACK.value,
                        padding_x= "3em",
                        padding_y= "2em",
                        border_radius="3em",
                        margin_top= "1em",
                        text_align="left", 
                    ),
                    spacing="2"
                
                ),
                rx.center(
                    rx.text("¿You don't have an account yet?",
                        rx.chakra.span(" Sign Up",text_decoration="underline white"),
                        margin_top="1em",
                        color= Color.WHITET.value,
                        margin_left="0.5em",  
                        font_size="1em",
                        font_weight="bold"), 
                ),
                width= "100%",
                margin_top= "9em"
            ),
            rx.image(src="/logog.png", width="30%", margin_top="20%"),
            width="40em",
            margin="0",
            height="100%",
            align="center",
            spacing="8"
        ),
        width="100%"
    )

def sign_up_form() -> rx.Component:
    return rx.center(
        rx.flex(
            rx.form(
                rx.center(
                    rx.text("Sign up",
                        color= Color.WHITET.value,
                        font_size="3em",
                        font_weight="bold"), 
                    width="100%"),
                rx.text("Email",
                    margin_top="1em",
                    color= Color.WHITET.value,
                    margin_left="0.5em",
                    font_size="1em",
                    font_weight="bold"), 
                rx.input(
                    name="email",
                    border= "none",
                    border_top= "1px",
                    background= Color.LILAC2.value,
                    height="3em"),
                rx.text("Name",
                    margin_top="1em",
                    color= Color.WHITET.value,
                    margin_left="0.5em",
                    font_size="1em",
                    font_weight="bold"), 
                rx.input(
                    name="name",
                    border= "none",
                    border_top= "1px",
                    background= Color.LILAC2.value,
                    height="3em"),
                rx.text("Create Password",
                    margin_top="1em",
                    color= Color.WHITET.value,
                    margin_left="0.5em",
                    font_size="1em",
                    font_weight="bold"), 
                rx.input(
                    name="pass",
                    border= "none",
                    border_top= "1px",
                    background= Color.LILAC2.value,
                    height="3em"),
                rx.text("Confirm Password",
                    margin_top="1em",
                    color= Color.WHITET.value,
                    margin_left="0.5em",
                    font_size="1em",
                    font_weight="bold"), 
                rx.input(
                    name="pass",
                    border= "none",
                    border_top= "1px",
                    background= Color.LILAC2.value,
                    height="3em"),
                
                rx.flex(
                    rx.button(
                        "Create Account",
                        _hover={"background_color": Color.GRAY.value},
                        background_color=Color.LILAC.value,
                        color=Color.BLACK.value,
                        padding_x= "3em",
                        padding_y= "2em",
                        margin_left="2.5em",
                        border_radius="3em",
                        margin_top= "1em",
                        text_align="left", 
                    ),
                    rx.button(
                        "Sign Up with Google",
                        _hover={"background_color": Color.GRAY.value},
                        background_color=Color.LILAC.value,
                        color=Color.BLACK.value,
                        padding_x= "3em",
                        padding_y= "2em",
                        border_radius="3em",
                        margin_top= "1em",
                        text_align="left", 
                    ),
                    spacing="2"
                
                ),
                rx.center(
                    rx.text("¿You already have an account?",
                        rx.chakra.span(" Sign In",text_decoration="underline white"),
                        margin_top="1em",
                        color= Color.WHITET.value,
                        margin_left="0.5em",  
                        font_size="1em",
                        font_weight="bold"), 
                ),
                width= "100%",
                margin_top= "6em"
            ),
            rx.image(src="/logog.png", width="30%", margin_top="20%"),
            width="40em",
            margin="0",
            height="100%",
            align="center",
            spacing="8"
        ),
        width="100%"
    )