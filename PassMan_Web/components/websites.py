import reflex as rx
from PassMan_Web.styles.styles import Color


def websites(websites) -> rx.Component:
    return rx.flex(
        rx.foreach(
            websites,
            lambda j: one_website(j[0],j[1],j[2],j[3],j[4],j[5]),
        ),
        flex_wrap="wrap",
        spacing="1",
        width="100%",
    )


def one_website(website: str,username:str,gmail:str,password:str,image:str, url:str) -> rx.Component:
    return rx.card(
        rx.flex(
            rx.inset(
                rx.box(
                    rx.image(
                        src=image,
                        height="100%",
                        width="100%",
                    ),
                    height="10em",
                    width="10em", 
                    margin_right="4em"                       
                ),
                side="left",
                pr="current",
            ),
            rx.vstack(
                rx.box(
                    rx.text(website, size="5",font_weight="bold"),
                    rx.text(username),
                    rx.text(gmail),
                    rx.text(password, type="password"),
                    color=Color.BLACK.value,
                    width="20em",
                    padding_y="1em",
                    height="15em"),
            ),
            direction="row",
            width="100%",
        ),
        _hover={"background_color": Color.GRAY2.value},
        margin_top="2em",
        margin_left="2em",
        width="36em",
        height="10em",
        radius="full",
        background_color=Color.LILAC2.value,
        on_click=rx.redirect(url, external=True),
    )
