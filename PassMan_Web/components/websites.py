import reflex as rx
from PassMan_Web.styles.styles import Color
from selenium_folder.selenium_login import *


class SeleniumHandle(rx.State):
    selenium_id: int=0
    user: str=""
    password:str =""
    def handle_selenium(self, user, password, selenium_id):
        self.user=user
        self.password=password
        self.selenium_id=selenium_id
        selenium_login(self.user, self.password, self.selenium_id)

def websites(websites) -> rx.Component:
    return rx.flex(
        rx.foreach(
            websites,
            lambda j: one_website(j[0],j[1],j[2],j[4],j[3]),
        ),
        flex_wrap="wrap",
        spacing="1",
        width="100%",
    )


def one_website(website: str,username:str,password:str,image:str, sid:str) -> rx.Component:
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
                    rx.text("{hidden}"),
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
        on_click=SeleniumHandle.handle_selenium(username, password, sid),
    )
