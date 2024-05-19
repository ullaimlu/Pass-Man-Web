import reflex as rx
from PassMan_Web.components import *
from PassMan_Web.styles.colors import *
#from database.pipelines import CoursePipeline

content=[["Facebook","ullaimlu","ullaimlu@gmail.com","*******","/websites/facebook.png","https://facebook.com"],["Instagram","ullaimlu","ullaimlu@gmail.com","******","/websites/instagram.png","https://instagram.com"]]
class WebsState(rx.State):
    websites: list[list[str]]= content



def principal_in(tab: str, content=WebsState.websites) -> rx.Component:
    #content= courses(content)
    content=websites(content)
    return rx.hstack(
        sidebar(),
        rx.vstack(
            rx.button(rx.icon("log_out", size=15),
                "Log Out",
                on_click=SignInState.log_out,
                _hover={"background_color": Color.GRAY.value},
                background_color=Color.LILAC.value,
                color=Color.BLACK.value,
                padding_y= "0.5em",
                border_radius="3em",
                margin_top="1em",
                margin_left="84em",
                width="8em"),
            my_space_tittle(tab),
            my_space(tab, content),
            width="100%"
        )
    )

    
        